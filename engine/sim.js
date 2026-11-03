// Simulations for the drill engine. Usage: node sim.js dist/<exam>/_data.json
const fs = require('fs'); const DC = require('./engine-core.js');
const D = JSON.parse(fs.readFileSync(process.argv[2]));
let seed = 12345; const rng = () => (seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296;
const core = DC.make({ Q: D.Q, highRoi: D.cfg.highRoi, rng });
const topics = D.cfg.topics.map(t => t.id), LET = 'ABCDEF';
const fresh = () => ({ q: {}, stars: {}, ans: 0, avg: { s: 0, c: 0 }, letters: {}, lastPos: {}, prev: [] });
function answer(S, q, ok, t) { const r = S.q[q.id] || (S.q[q.id] = { n: 0, ok: 0, ms: 0, rs: 0 }); r.n++; S.ans++; r.c = S.ans; r.t = t;
  if (ok) { r.ok++; r.last = 'r'; r.rs++; r.ms = 0 } else { r.last = 'w'; r.rs = 0; r.ms++ } r.g = false; S.avg.s += 40; S.avg.c++; }
let T = 1e12; const H = 3600e3;
// 1. answer letters
{ const S = fresh(); let prev = -1; const cnt = {}; let same = 0, n = 0, moved = 0, again = 0;
  const mcs = D.Q.filter(q => q.ty === 'mc'); const seen = {};
  for (let i = 0; i < 4000; i++) { const q = mcs[Math.floor(rng() * mcs.length)]; const ord = core.placeMC(S, q, prev); const pos = ord.indexOf(q.c);
    S.letters[LET[pos]] = (S.letters[LET[pos]] || 0) + 1; cnt[LET[pos]] = (cnt[LET[pos]] || 0) + 1; if (pos === prev) same++; prev = pos; n++;
    if (seen[q.id] !== undefined) { again++; if (seen[q.id] !== pos) moved++ } S.lastPos[q.id] = pos; seen[q.id] = pos; }
  console.log('1. ANSWER LETTERS over', n, 'multiple-choice questions (4- and 5-option mixed):', cnt, '| same letter as previous question:', same, '| repeats whose answer moved:', moved, 'of', again); }
// 2. true/false
{ const S = fresh(); const tfPer = {}; let longest = 0; let streak = 0, last = null, tot = 0;
  for (let s = 0; s < 400; s++) { const r = core.buildLimited(S, D.Q, 60, T); T += 5 * H; S.prev = []; 
    r.list.forEach(q => { const rec = S.q[q.id]; answer(S, q, rng() < 0.6, T); });
    const tfs = r.list.filter(q => q.ty === 'tf'); tfs.forEach(q => { tfPer[q.t] = tfPer[q.t] || [0, 0]; tfPer[q.t][q.c === 0 ? 0 : 1]++; tot++; if (last === q.c) streak++; else { streak = 1; last = q.c } longest = Math.max(longest, streak) }); last = null; streak = 0 }
  const pct = Object.fromEntries(Object.entries(tfPer).map(([k, v]) => [k, Math.round(100 * v[0] / (v[0] + v[1])) + '% true']));
  console.log('2. TRUE/FALSE over', tot, 'presentations: per topic', JSON.stringify(pct), '| longest run of identical answers within a session:', longest); }
// 3. chained sessions
{ const S = fresh(); const hrOK = []; let sessions = 0, returned = 0, bad = 0; const rows = [];
  let prevIds = [];
  for (let s = 0; s < 12; s++) { const one = s % 2 === 0; const pickT = one ? [topics[(s / 2) % topics.length | 0]] : topics; const pool = D.Q.filter(q => pickT.includes(q.t)); const N = Math.min(one ? 8 : 20, pool.length);
    const prev = S.prev.slice(); const r = core.buildLimited(S, pool, N, T); const back = r.list.filter(q => prev.includes(q.id));
    back.forEach(q => { const rec = S.q[q.id]; if (!(core.isHR(S, q) || (rec && rec.ms >= 2))) bad++ ; returned++ });
    rows.push((one ? 'one topic' : 'all topics') + ' N=' + r.list.length + ' came back from previous session: ' + back.length);
    S.prev = r.list.map(q => q.id); r.list.forEach(q => answer(S, q, rng() < 0.55, T)); T += 20 * 60e3; }
  console.log('3. CHAINED SESSIONS (single topics and all topics alternating, 12 sessions):\n   ' + rows.join('\n   ') + '\n   total came back: ' + returned + ', of which NOT high-ROI and NOT consistently missed: ' + bad); }
// 4. pre-test
{ const S = fresh(); let adj = 0, lpc = 0, miss = 0; const per = topics.length > 10 ? 2 : 3; let runs = 50, size = 0;
  for (let k = 0; k < runs; k++) { const l = core.buildPretest(S, topics); size = l.length; l.forEach((q, i) => { if (q.lp) lpc++; if (i && l[i - 1].t === q.t) adj++ }); const c = {}; l.forEach(q => c[q.t] = (c[q.t] || 0) + 1); topics.forEach(t => { if (c[t] !== per) miss++ }) }
  const l = core.buildPretest(S, topics); l.forEach(q => answer(S, q, rng() < .7, T)); const st = core.topicStats(S, topics); const lv = topics.filter(t => st[t].n).length;
  console.log('4. PRE-TEST x' + runs + ': ' + size + ' questions each (' + per + ' per topic, ' + topics.length + ' topics); last-pass questions: ' + lpc + '; same topic twice in a row: ' + adj + '; topics without exactly ' + per + ': ' + miss + '; after running one to the end, levels saved for ' + lv + ' of ' + topics.length + ' topics'); }
// 5. timed plans
{ for (const mins of [30, 45]) { const S = fresh(); const warm = core.buildLimited(S, D.Q, 70, T); warm.list.forEach(q => answer(S, q, rng() < .45, T)); S.prev = []; T += 20 * H; S.avg = { s: 40 * 20, c: 20 };
    let res = []; for (let k = 0; k < 5; k++) { const p = core.buildTimed(S, D.Q, mins, T); let adj = 0; p.list.forEach((q, i) => { if (i && p.list[i - 1].t === q.t) adj++ }); const tot = p.mix.weak + p.mix.review + p.mix.fresh; res.push({ N: p.list.length, mix: [Math.round(100 * p.mix.weak / tot), Math.round(100 * p.mix.review / tot), Math.round(100 * p.mix.fresh / tot)], adj }) }
    console.log('5. TIMED ' + mins + ' MIN (with 70 saved answers, 45% right, 40 s/question): ' + res.map(r => r.N + ' questions, mix weak/review/new ' + r.mix.join('/') + '%, same topic twice in a row ' + r.adj).join(' | ')) } }
