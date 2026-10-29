(function () {
  const C = window.CONTENT;
  const chapters = C.chapters;
  const $ = (s, r = document) => r.querySelector(s);
  const page = $("#page"), side = $("#side");
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} },
  };
  let done = store.get("done", {});

  // theme
  const root = document.documentElement;
  const savedTheme = store.get("theme", null);
  if (savedTheme) root.setAttribute("data-theme", savedTheme);
  $("#theme").onclick = () => {
    const cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next); store.set("theme", next);
  };
  $("#menu").onclick = () => document.body.classList.toggle("navopen");

  function renderNav(activeId) {
    const items = chapters.map((c) => `<a href="#/${c.id}" class="${c.id === activeId ? "active" : ""} ${done[c.id] ? "done" : ""}"><small>${c.part}</small>${c.title}</a>`).join("");
    side.innerHTML = `<a href="#/" class="${activeId === "home" ? "active" : ""}"><small>Home</small>Overview and progress</a>
      <h4>Study</h4>${items}
      <h4>Practice</h4>
      <a href="#/flashcards" class="${activeId === "flashcards" ? "active" : ""}"><small>Quiz yourself</small>Flashcards (${C.qa.length} questions)</a>
      <a href="#/tools" class="${activeId === "tools" ? "active" : ""}"><small>Tools</small>Dosage calculator</a>`;
  }

  function home() {
    const n = chapters.filter((c) => done[c.id]).length;
    const pct = Math.round((n / chapters.length) * 100);
    page.innerHTML = `<div class="eyebrow">NUR 291 · Exam 1</div>
      <h1>Oncology, Heme, Immune &amp; Repro</h1>
      <p class="lede">Everything from your two study guides, your purple class notes, the lecture slides and your bioterrorism PowerPoint, organized by chapter. Callout colors show what each box is. Click a section chip to jump around, or use the search bar for any term.</p>
      <div class="card"><div class="row" style="justify-content:space-between"><strong>Your progress</strong><span>${n} of ${chapters.length} chapters marked studied</span></div>
      <div class="progress"><i style="width:${pct}%"></i></div>
      <div class="row" style="margin-top:10px"><a class="btn" href="#/start">Start with the blueprint and cram sheet</a><a class="btn ghost" href="#/flashcards">Flashcards</a><button class="btn ghost" onclick="window.print()">Print</button></div></div>
      <div class="home-grid">${chapters.map((c) => `<a href="#/${c.id}"><small>${c.part} ${done[c.id] ? "· ✓ studied" : ""}</small><h3>${c.title}</h3><p>${c.summary}</p></a>`).join("")}</div>
      <div class="card" style="margin-top:16px"><strong>How the colors work</strong>
      <div class="row" style="margin-top:8px;gap:6px">
        ${[["matters","Why it matters"],["patho","Patho"],["ss","Signs &amp; symptoms ★"],["dx","Diagnosis"],["tx","Treatment"],["watch","Watch"],["nursing","Nursing"],["pearl","Pearl"],["note","Class note"]].map(([k, l]) => `<span class="callout ${k}" style="margin:0;padding:3px 12px;border-left-width:4px"><span class="chead" style="padding:0">${l}</span></span>`).join("")}
      </div></div>`;
  }

  function chapter(id, sec) {
    const c = chapters.find((x) => x.id === id);
    if (!c) return home();
    const i = chapters.indexOf(c);
    const prev = chapters[i - 1], next = chapters[i + 1];
    page.innerHTML = `<div class="eyebrow">${c.part}</div><h1>${c.title}</h1><p class="lede">${c.summary}</p>
      <div class="toc">${c.sections.map((s) => `<a href="#/${c.id}/${s.id}">${s.title.replace(/[*_`]/g, "")}</a>`).join("")}</div>
      <div class="donebar"><button class="iconbtn" id="mark">${done[c.id] ? "✓ Studied (click to undo)" : "Mark chapter as studied"}</button></div>
      ${c.html}
      <div class="pager">${prev ? `<a class="btn ghost" href="#/${prev.id}">← ${prev.title}</a>` : "<span></span>"}${next ? `<a class="btn ghost" href="#/${next.id}">${next.title} →</a>` : ""}</div>
      <div class="footer">Built from your uploaded study guides. Always confirm anything marked “Class vs book” with your instructor.</div>`;
    $("#mark").onclick = () => { done[c.id] = !done[c.id]; store.set("done", done); chapter(id, sec); renderNav(id); };
    if (sec) setTimeout(() => { const el = document.getElementById(sec); if (el) el.scrollIntoView(); }, 30);
    else window.scrollTo(0, 0);
  }

  // flashcards
  let deck = [], idx = 0, shown = false, filter = "all";
  function buildDeck() {
    deck = C.qa.filter((x) => filter === "all" || x.chapter === filter);
    for (let i = deck.length - 1; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0; [deck[i], deck[j]] = [deck[j], deck[i]]; }
    idx = 0; shown = false;
  }
  function flashcards() {
    if (!deck.length) buildDeck();
    const qaChapters = [...new Set(C.qa.map((x) => x.chapter))];
    const card = deck[idx];
    const missed = store.get("missed", {});
    page.innerHTML = `<div class="eyebrow">Practice</div><h1>Flashcards</h1>
      <p class="lede">Practice questions from your slides, chapters and class PLQs. Click the card to flip it.</p>
      <div class="row"><label>Chapter <select id="fsel"><option value="all">All (${C.qa.length})</option>${qaChapters.map((k) => `<option value="${k}" ${k === filter ? "selected" : ""}>${(chapters.find((c) => c.id === k) || {}).title || k}</option>`).join("")}</select></label>
      <button class="iconbtn" id="shuf">Shuffle</button><button class="iconbtn" id="rev">Review missed (${Object.keys(missed).length})</button></div>
      <div class="card flash" id="fc" style="margin-top:14px">${card ? `<small>Card ${idx + 1} of ${deck.length}</small><div>${card.qHtml}</div>${shown ? `<div class="a">${card.aHtml}</div>` : `<small style="margin-top:14px">tap to reveal the answer</small>`}` : "No cards."}</div>
      <div class="row" style="margin-top:12px;justify-content:center">
        <button class="btn ghost" id="prevc">← Back</button>
        ${shown ? `<button class="btn" id="gotit">Got it</button><button class="btn ghost" id="missit">Missed it</button>` : ""}
        <button class="btn ghost" id="nextc">Next →</button></div>`;
    $("#fc").onclick = () => { shown = !shown; flashcards(); };
    $("#fsel").onchange = (e) => { filter = e.target.value; buildDeck(); flashcards(); };
    $("#shuf").onclick = () => { buildDeck(); flashcards(); };
    $("#rev").onclick = () => { const m = store.get("missed", {}); deck = C.qa.filter((x) => m[x.q]); idx = 0; shown = false; flashcards(); };
    const go = (d) => { idx = (idx + d + deck.length) % Math.max(deck.length, 1); shown = false; flashcards(); };
    $("#prevc").onclick = () => go(-1); $("#nextc").onclick = () => go(1);
    if (shown) {
      $("#gotit").onclick = () => { const m = store.get("missed", {}); delete m[card.q]; store.set("missed", m); go(1); };
      $("#missit").onclick = () => { const m = store.get("missed", {}); m[card.q] = 1; store.set("missed", m); go(1); };
    }
    window.scrollTo(0, 0);
  }

  function tools() {
    page.innerHTML = `<div class="eyebrow">Tools</div><h1>Dosage calculator</h1>
      <p class="lede">Dosage calculation is worth 2 exam questions. Check your own work here. Always check units first.</p>
      <div class="calc">
        <div class="card"><h3>Basic: (D ÷ H) × Q</h3>
          <label>Desired dose (D)</label><input type="number" step="any" id="d1"><label>Dose on hand (H)</label><input type="number" step="any" id="h1"><label>Quantity it comes in (Q, e.g., mL)</label><input type="number" step="any" id="q1">
          <div class="out" id="o1">–</div></div>
        <div class="card"><h3>Weight-based</h3>
          <label>Dose per kg (mg/kg)</label><input type="number" step="any" id="d2"><label>Weight</label><input type="number" step="any" id="w2">
          <label>Unit</label><select id="u2"><option value="kg">kg</option><option value="lb">lb (÷ 2.2)</option></select>
          <div class="out" id="o2">–</div></div>
        <div class="card"><h3>IV rate</h3>
          <label>Total volume (mL)</label><input type="number" step="any" id="v3"><label>Time (hours)</label><input type="number" step="any" id="t3"><label>Drop factor (gtt/mL, optional)</label><input type="number" step="any" id="f3">
          <div class="out" id="o3">–</div></div>
        <div class="card"><h3>Heparin / units per hour</h3>
          <label>Ordered units/hr</label><input type="number" step="any" id="u4"><label>Total units in bag</label><input type="number" step="any" id="b4"><label>Bag volume (mL)</label><input type="number" step="any" id="m4">
          <div class="out" id="o4">–</div></div>
      </div>
      <p class="footer">Conversions: 1 kg = 2.2 lb · 1 g = 1,000 mg · 1 mg = 1,000 mcg · 1 tsp = 5 mL · 1 tbsp = 15 mL · 1 oz = 30 mL.</p>`;
    const n = (id) => parseFloat($("#" + id).value);
    const r = (x, p = 1) => (Math.round(x * 10 ** p) / 10 ** p);
    const upd = () => {
      const [D, H, Q] = [n("d1"), n("h1"), n("q1")];
      $("#o1").textContent = H && !isNaN(D) && !isNaN(Q) ? `${r((D / H) * Q)} (same unit as Q)` : "–";
      let w = n("w2"); if ($("#u2").value === "lb") w = w / 2.2;
      $("#o2").textContent = !isNaN(n("d2")) && !isNaN(w) ? `${r(n("d2") * w)} mg (${r(w, 2)} kg)` : "–";
      const [V, T, F] = [n("v3"), n("t3"), n("f3")];
      $("#o3").textContent = V && T ? `${r(V / T)} mL/hr` + (F ? ` · ${Math.round((V * F) / (T * 60))} gtt/min` : "") : "–";
      const [U, B, M] = [n("u4"), n("b4"), n("m4")];
      $("#o4").textContent = U && B && M ? `${r(U / (B / M))} mL/hr` : "–";
    };
    page.querySelectorAll("input,select").forEach((e) => (e.oninput = upd));
    window.scrollTo(0, 0);
  }

  // search
  const q = $("#q"), res = $("#results");
  const hl = (t, terms) => terms.reduce((s, w) => s.replace(new RegExp("(" + w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>"), t);
  q.addEventListener("input", () => {
    const terms = q.value.toLowerCase().split(/\s+/).filter((t) => t.length > 1);
    if (!terms.length) { res.style.display = "none"; return; }
    const hits = [];
    for (const s of C.search) {
      const hay = (s.title + " " + s.text).toLowerCase();
      if (!terms.every((t) => hay.includes(t))) continue;
      const score = terms.reduce((a, t) => a + (s.title.toLowerCase().includes(t) ? 20 : 0) + (hay.split(t).length - 1), 0);
      const pos = hay.indexOf(terms[0]);
      const snip = s.text.slice(Math.max(0, pos - 60), pos + 110);
      hits.push({ s, score, snip });
    }
    hits.sort((a, b) => b.score - a.score);
    res.innerHTML = hits.length ? hits.slice(0, 25).map((h) => `<a href="#/${h.s.ch}/${h.s.id}"><strong>${hl(h.s.title, terms)}</strong><small>${h.s.chTitle}</small><small>…${hl(h.snip, terms)}…</small></a>`).join("") : `<a><small>No matches</small></a>`;
    res.style.display = "block";
  });
  document.addEventListener("click", (e) => { if (!e.target.closest(".search")) res.style.display = "none"; });
  res.addEventListener("click", () => { res.style.display = "none"; q.value = ""; });
  document.addEventListener("keydown", (e) => { if (e.key === "/" && document.activeElement.tagName !== "INPUT") { e.preventDefault(); q.focus(); } });

  function route() {
    document.body.classList.remove("navopen");
    const [, a, b] = location.hash.split("/");
    if (!a) { renderNav("home"); home(); window.scrollTo(0, 0); }
    else if (a === "flashcards") { renderNav("flashcards"); flashcards(); }
    else if (a === "tools") { renderNav("tools"); tools(); }
    else { renderNav(a); chapter(a, b); }
  }
  addEventListener("hashchange", route);
  route();
})();
