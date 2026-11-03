/* Drill engine core: pure logic, no DOM. Used by the drill page and by the simulations in Node. */
(function (root) {
  "use strict";
  var H18 = 18 * 3600 * 1000;
  var clamp = function (x, a, b) { return Math.max(a, Math.min(b, x)); };
  var LET = "ABCDEF";

  function make(cfg) {
    var Q = cfg.Q, byId = {}, rng = cfg.rng || Math.random, HR = {};
    (cfg.highRoi || []).forEach(function (t) { HR[t] = 1; });
    Q.forEach(function (q) { byId[q.id] = q; });
    function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(rng() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
    function rec(S, id) { return S.q[id] || null; }
    function starred(S, id) { var s = S.stars && S.stars[id]; return !!(s && s.s); }
    function isHR(S, q) { return starred(S, q.id) || !!q.lp || !!HR[q.t]; }
    function status(S, q) {
      var r = S.q[q.id];
      if (!r || !r.n) return "new";
      if (r.last !== "r" || r.g) return "shaky";
      return r.rs >= (q.ty === "tf" ? 3 : 2) ? "solid" : "right";
    }
    function missed(S, q) { var r = S.q[q.id]; return !!(r && r.n && (r.last === "w" || r.g)); }
    function restNeeded(S, q, n) {
      var r = S.q[q.id]; if (!r || !r.n) return 0;
      if (r.ms >= 2) return clamp(0.10 * n, 6, 25);
      if (r.last === "w" || r.g) return clamp(0.25 * n, 10, 60);
      var base = clamp(0.70 * n, 12, 300);
      if (status(S, q) === "solid") base *= 1.5;
      if (isHR(S, q)) base = clamp(0.40 * base, 8, 120);
      return base;
    }
    function ready(S, q, n, now) {
      var r = S.q[q.id]; if (!r || !r.n) return true;
      if (now - r.t >= H18) return true;
      return (S.ans - r.c) >= restNeeded(S, q, n);
    }
    function prevBlocked(S, q) {
      if (!S.prev || S.prev.indexOf(q.id) < 0) return false;
      var r = S.q[q.id];
      return !(isHR(S, q) || (r && r.ms >= 2));
    }
    function fmt(q) { return q.ty === "cloze" ? "blanks" : q.ty; }

    /* greedy interleave: never the same topic twice in a row, avoid the same format 3 times */
    function interleave(list) {
      var rest = list.slice(), out = [];
      while (rest.length) {
        var lt = out.length ? out[out.length - 1].t : null;
        var f1 = out.length ? fmt(out[out.length - 1]) : null, f2 = out.length > 1 ? fmt(out[out.length - 2]) : null;
        var pick = -1, i;
        for (i = 0; i < rest.length; i++) if (rest[i].t !== lt && !(f1 && f1 === f2 && fmt(rest[i]) === f1)) { pick = i; break; }
        if (pick < 0) for (i = 0; i < rest.length; i++) if (rest[i].t !== lt) { pick = i; break; }
        if (pick < 0) pick = 0;
        out.push(rest.splice(pick, 1)[0]);
      }
      return out;
    }
    /* keep rough order but split same-topic neighbours */
    function spread(list) {
      var a = list.slice();
      for (var i = 1; i < a.length; i++) {
        if (a[i].t === a[i - 1].t) {
          for (var j = i + 1; j < a.length; j++) if (a[j].t !== a[i - 1].t && (i + 1 >= a.length || a[j].t !== (a[i + 1] || {}).t || true)) { var x = a[i]; a[i] = a[j]; a[j] = x; break; }
        }
      }
      return a;
    }
    /* never 3 identical true/false answers in a row (among the true/false questions): re-deal the T/F slots */
    function fixTF(list) {
      var a = list.slice(), slots = [];
      a.forEach(function (q, i) { if (q.ty === "tf") slots.push(i); });
      if (slots.length < 3) return a;
      function topicOK(arr, i) { var q = arr[i]; return !((arr[i - 1] && arr[i - 1].t === q.t) || (arr[i + 1] && arr[i + 1].t === q.t)); }
      for (var attempt = 0; attempt < 30; attempt++) {
        var pool = slots.map(function (i) { return a[i]; }), out = [];
        if (attempt) pool = shuffle(pool);
        while (pool.length) {
          var want = (out.length >= 2 && out[out.length - 1].c === out[out.length - 2].c) ? 1 - out[out.length - 1].c : null, pick = 0;
          if (want === null) { var ct = 0; pool.forEach(function (x) { if (x.c === 0) ct++; }); var cf = pool.length - ct; if (ct !== cf) want = ct > cf ? 0 : 1; }
          if (want !== null) { var f = -1; for (var k = 0; k < pool.length; k++) if (pool[k].c === want) { f = k; break; } if (f >= 0) pick = f; }
          out.push(pool.splice(pick, 1)[0]);
        }
        var b = a.slice(); slots.forEach(function (idx, n) { b[idx] = out[n]; });
        var ok = true;
        for (var n = 2; n < out.length; n++) if (out[n].c === out[n - 1].c && out[n].c === out[n - 2].c) ok = false;
        slots.forEach(function (idx) { if (!topicOK(b, idx)) ok = false; });
        if (ok || attempt === 29) { if (ok || attempt === 29) return b; }
      }
      return a;
    }
    /* keep true/false answers dealable without 3 identical in a row: majority <= 2 * (minority + 1) */
    function balanceTF(list, pool) {
      var a = list.slice(), used = {}; a.forEach(function (q) { used[q.id] = 1; });
      for (var guard = 0; guard < 200; guard++) {
        var T = 0, F = 0; a.forEach(function (q) { if (q.ty === "tf") (q.c === 0 ? T++ : F++); });
        var maj = T >= F ? 0 : 1, M = Math.max(T, F), m = Math.min(T, F);
        if (M <= 2 * (m + 1)) break;
        var idx = -1; for (var i = a.length - 1; i >= 0; i--) if (a[i].ty === "tf" && a[i].c === maj) { idx = i; break; }
        var rep = null;
        for (var k = 0; k < pool.length; k++) { var q = pool[k]; if (!used[q.id] && q.ty !== "tf") { rep = q; break; } }
        if (!rep) for (var k2 = 0; k2 < pool.length; k2++) { var q2 = pool[k2]; if (!used[q2.id] && q2.ty === "tf" && q2.c !== maj) { rep = q2; break; } }
        if (rep) { used[rep.id] = 1; a[idx] = rep; } else a.splice(idx, 1);
      }
      return a;
    }
    function finish(list, pool) { return fixTF(interleave(pool ? balanceTF(list, shuffle(pool)) : list)); }

    /* ---------- limited session ---------- */
    function buildLimited(S, pool, N, now) {
      var n = pool.length, note = "";
      var elig = pool.filter(function (q) { return ready(S, q, n, now) && !prevBlocked(S, q); });
      var A = shuffle(elig.filter(function (q) { return missed(S, q); })).sort(function (a, b) {
        return ((S.q[b.id].ms >= 2) - (S.q[a.id].ms >= 2));
      });
      var B = shuffle(elig.filter(function (q) { var r = S.q[q.id]; return r && r.n && !missed(S, q); })).sort(function (a, b) { return (isHR(S, b) ? 1 : 0) - (isHR(S, a) ? 1 : 0); });
      var C = shuffle(elig.filter(function (q) { var r = S.q[q.id]; return !r || !r.n; })).sort(function (a, b) { return (isHR(S, b) ? 1 : 0) - (isHR(S, a) ? 1 : 0); });
      var chosen = [], used = {};
      function take(arr, cap) { for (var i = 0; i < arr.length && chosen.length < N && cap > 0; i++) if (!used[arr[i].id]) { used[arr[i].id] = 1; chosen.push(arr[i]); cap--; } }
      take(A, Math.floor(N * 0.25));
      take(B, Math.floor(N * 0.20));
      take(C, N);
      take(A.concat(B), N);
      if (chosen.length < N) {
        var recent = pool.filter(function (q) { return !used[q.id]; }).sort(function (a, b) { return (S.q[a.id] ? S.q[a.id].t : 0) - (S.q[b.id] ? S.q[b.id].t : 0); });
        if (recent.length) note = "Not enough rested questions, so some recently answered ones are included, longest ago first.";
        take(recent, N);
      }
      return { list: finish(shuffle(chosen), pool), note: note };
    }

    /* ---------- topic level from saved answers ---------- */
    function topicStats(S, topics) {
      var o = {};
      topics.forEach(function (t) { o[t] = { n: 0, ok: 0 }; });
      Q.forEach(function (q) { var r = S.q[q.id]; if (r && r.n && o[q.t]) { o[q.t].n += r.n; o[q.t].ok += r.ok || 0; } });
      return o;
    }
    function level(p) { return p >= 80 ? "Strong" : p >= 60 ? "Okay" : "Weak"; }

    /* ---------- pre-test ---------- */
    function buildPretest(S, topics) {
      var per = topics.length > 10 ? 2 : 3, picks = {};
      topics.forEach(function (t) {
        var c = shuffle(Q.filter(function (q) { return q.t === t && !q.lp; })), sel = [], fs = {};
        c.forEach(function (q) { if (sel.length < per && !fs[fmt(q)]) { fs[fmt(q)] = 1; sel.push(q); } });
        c.forEach(function (q) { if (sel.length < per && sel.indexOf(q) < 0) sel.push(q); });
        picks[t] = sel;
      });
      var order = topics.slice().sort(function (a, b) {
        var ha = HR[a] ? 1 : 0, hb = HR[b] ? 1 : 0; if (ha !== hb) return hb - ha;
        var sa = picks[a].some(function (q) { return starred(S, q.id); }) ? 1 : 0, sb = picks[b].some(function (q) { return starred(S, q.id); }) ? 1 : 0;
        return sb - sa;
      });
      var out = [];
      for (var r = 0; r < per; r++) order.forEach(function (t) { if (picks[t][r]) out.push(picks[t][r]); });
      /* round robin never repeats a topic back to back unless a topic ends a round and starts the next */
      for (var i = 1; i < out.length; i++) if (out[i].t === out[i - 1].t) { for (var j = i + 1; j < out.length; j++) if (out[j].t !== out[i - 1].t) { var x = out[i]; out[i] = out[j]; out[j] = x; break; } }
      return fixTF(balanceTF(out, Q.filter(function (q) { return !q.lp; })));
    }

    /* ---------- last pass ---------- */
    function buildLastPass(S, pool, onlyWeak) {
      var rank = { shaky: 0, "new": 1, right: 2, solid: 3 };
      var lp = shuffle(pool.filter(function (q) { return q.lp; })).sort(function (a, b) { return rank[status(S, a)] - rank[status(S, b)]; });
      if (onlyWeak) lp = balanceTF(lp.slice(0, onlyWeak), lp.slice(onlyWeak));
      return fixTF(spread(lp));
    }

    /* ---------- timed mixed plan ---------- */
    function buildTimed(S, pool, minutes, now) {
      var avg = (S.avg && S.avg.c >= 5) ? S.avg.s / S.avg.c : 45;
      var N = Math.max(5, Math.floor(minutes * 60 / avg));
      var topics = {}; pool.forEach(function (q) { topics[q.t] = 1; }); topics = Object.keys(topics);
      var st = topicStats(S, topics);
      var scored = topics.map(function (t) { return { t: t, p: st[t].n ? 100 * st[t].ok / st[t].n : 50, n: st[t].n }; }).sort(function (a, b) { return a.p - b.p; });
      var weakT = scored.slice(0, Math.max(1, Math.ceil(topics.length / 3))).map(function (x) { return x.t; });
      var n = pool.length, used = {}, out = [], mix = { weak: 0, review: 0, fresh: 0 };
      var elig = pool.filter(function (q) { return ready(S, q, n, now) && !prevBlocked(S, q); });
      function take(arr, cap, key) { for (var i = 0; i < arr.length && cap > 0 && out.length < N; i++) if (!used[arr[i].id]) { used[arr[i].id] = 1; out.push(arr[i]); mix[key]++; cap--; } }
      var wN = Math.round(N * 0.5), rN = Math.round(N * 0.3), fN = N - wN - rN;
      var weakPool = shuffle(elig.filter(function (q) { return weakT.indexOf(q.t) >= 0; })).sort(function (a, b) { return (missed(S, b) ? 1 : 0) - (missed(S, a) ? 1 : 0); });
      take(weakPool, wN, "weak");
      var review = shuffle(elig.filter(function (q) { var r = S.q[q.id]; return r && r.n; }));
      take(review.filter(function (q) { return missed(S, q); }), rN, "review");
      take(review.filter(function (q) { return !missed(S, q); }), rN - mix.review, "review");
      var fresh = shuffle(elig.filter(function (q) { var r = S.q[q.id]; return !r || !r.n || status(S, q) === "right"; }));
      take(fresh, fN, "fresh");
      /* top up from anything left so the plan reaches its size */
      take(shuffle(elig), N - out.length, "fresh");
      if (out.length < N) take(shuffle(pool.filter(function (q) { return !used[q.id]; })), N - out.length, "fresh");
      out = balanceTF(out, shuffle(pool)); return { list: finish(shuffle(out)), mix: mix, weak: weakT, N: out.length };
    }

    /* ---------- endless ---------- */
    function nextEndless(S, pool, now, last) {
      var n = pool.length;
      var c = pool.filter(function (q) { return ready(S, q, n, now) && !prevBlocked(S, q) && (!last || q.t !== last.t || pool.length < 2); });
      if (!c.length) c = pool.slice().sort(function (a, b) { return (S.q[a.id] ? S.q[a.id].t : 0) - (S.q[b.id] ? S.q[b.id].t : 0); }).slice(0, 8);
      var w = c.map(function (q) { var r = S.q[q.id], x = 1; if (r && r.n && missed(S, q)) x = r.ms >= 2 ? 5 : 3; else if (!r || !r.n) x = 1.5; if (isHR(S, q)) x *= 1.5; return x; });
      var tot = w.reduce(function (a, b) { return a + b; }, 0), r = rng() * tot;
      for (var i = 0; i < c.length; i++) { r -= w[i]; if (r <= 0) return c[i]; }
      return c[c.length - 1];
    }

    /* ---------- where the right answer goes ---------- */
    function pickLetterIndex(S, nOpts, prevCorrect, lastPos) {
      var counts = S.letters || {}, best = [], min = 1e9, i;
      for (i = 0; i < nOpts; i++) { if (i === prevCorrect || i === lastPos) continue; var c = counts[LET[i]] || 0; if (c < min) { min = c; best = [i]; } else if (c === min) best.push(i); }
      if (!best.length) for (i = 0; i < nOpts; i++) if (i !== prevCorrect) best.push(i);
      return best[Math.floor(rng() * best.length)];
    }
    /* options: array of option indexes into q.o with correct index set; returns display order (array of original indexes) */
    function placeMC(S, q, prevCorrect) {
      var n = q.o.length, target = pickLetterIndex(S, n, prevCorrect, (S.lastPos || {})[q.id]);
      var others = shuffle(q.o.map(function (_, i) { return i; }).filter(function (i) { return i !== q.c; }));
      var order = []; for (var i = 0; i < n; i++) order.push(i === target ? q.c : others.shift());
      return order;
    }
    function placeDrop(choices, correct) { /* shuffle with correct not first-always */
      var idx = choices.map(function (_, i) { return i; }), order = shuffle(idx);
      return order;
    }
    function placeRows(q) { /* matching table / blanks: different dropdown positions per row */
      var rows = (q.ty === "match") ? q.r.length : q.o.length, best = null;
      for (var tries = 0; tries < 12; tries++) {
        var orders = [], pos = [];
        for (var r = 0; r < rows; r++) {
          var ch = q.ty === "match" ? q.o : q.o[r], ord = shuffle(ch.map(function (_, i) { return i; }));
          orders.push(ord); pos.push(ord.indexOf(q.ty === "match" ? q.c[r] : q.c[r]));
        }
        best = orders;
        var same = pos.every(function (p) { return p === pos[0]; });
        if (!(rows > 1 && same)) break;
      }
      return best;
    }

    return {
      Q: Q, byId: byId, shuffle: shuffle, status: status, missed: missed, isHR: isHR, ready: ready, restNeeded: restNeeded,
      interleave: interleave, spread: spread, fixTF: fixTF, buildLimited: buildLimited, buildPretest: buildPretest,
      buildLastPass: buildLastPass, buildTimed: buildTimed, nextEndless: nextEndless, placeMC: placeMC, placeRows: placeRows,
      topicStats: topicStats, level: level, starred: starred, fmt: fmt, LET: LET, clamp: clamp, prevBlocked: prevBlocked
    };
  }
  var api = { make: make, clamp: clamp };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.DrillCore = api;
})(typeof window !== "undefined" ? window : globalThis);
