// Builds site/content.js from the markdown files in content/.
// Usage: node tools/build.mjs
import fs from "node:fs";
import path from "node:path";
import { marked } from "marked";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const dir = path.join(root, "content");
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".md")).sort();

const LABELS = {
  matters: "Why it matters", patho: "Patho", ss: "Signs & symptoms", dx: "Diagnosis",
  tx: "Treatment", watch: "Watch", nursing: "Nursing", pearl: "Pearl",
  note: "Class note", slides: "Slides",
};
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const slug = (s) => s.toLowerCase().replace(/<[^>]+>/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const plain = (html) => html.replace(/<[^>]+>/g, " ").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/\s+/g, " ").trim();

const renderer = new marked.Renderer();
renderer.image = (href, title, text) =>
  `<figure><img loading="lazy" src="${href.replace(/\.png$/, ".jpg")}" alt="${esc(text)}"><figcaption>${esc(text)}</figcaption></figure>`;
renderer.table = (header, body) => `<div class="tablewrap"><table><thead>${header}</thead><tbody>${body}</tbody></table></div>`;
marked.use({ renderer, gfm: true, breaks: false });

function parseFile(name) {
  const lines = fs.readFileSync(path.join(dir, name), "utf8").split("\n");
  const meta = {};
  let title = "";
  let i = 0;
  while (i < lines.length && !lines[i].startsWith("# ")) i++;
  title = lines[i].slice(2).trim();
  i++;
  while (i < lines.length && (lines[i].startsWith("@") || !lines[i].trim())) {
    const m = lines[i].match(/^@(\w+):\s*(.*)$/);
    if (m) meta[m[1]] = m[2];
    i++;
  }
  return { name, title, meta, body: lines.slice(i).join("\n") };
}

function renderBlocks(md, chapter, qa) {
  const out = [];
  const lines = md.split("\n");
  let buf = [];
  const flush = () => {
    if (buf.join("").trim()) out.push(marked.parse(buf.join("\n")));
    buf = [];
  };
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^:::(\w+)(?:\s+(.*))?$/);
    if (!m) { buf.push(lines[i]); continue; }
    flush();
    const kind = m[1], title = m[2] || "";
    const inner = [];
    i++;
    while (i < lines.length && lines[i].trim() !== ":::") inner.push(lines[i++]);
    const innerMd = inner.join("\n");
    if (kind === "qa") {
      const items = innerMd.split("\n").filter((l) => l.includes("⟶"));
      out.push(`<div class="qa">${items.map((l) => {
        const [q, a] = l.split("⟶").map((x) => x.trim());
        qa.push({ q: plain(marked.parseInline(q)), a: plain(marked.parseInline(a)), aHtml: marked.parseInline(a), qHtml: marked.parseInline(q), chapter });
        return `<details class="qaitem"><summary>${marked.parseInline(q)}</summary><div class="ans">${marked.parseInline(a)}</div></details>`;
      }).join("")}</div>`);
    } else if (kind === "calc") {
      out.push(`<div class="calcnote">${marked.parse(innerMd)}<a class="btn" href="#tools">Open the dosage calculator</a></div>`);
    } else if (kind === "slides") {
      out.push(`<details class="callout slides"><summary><span class="tag">Slide</span> ${esc(title)}</summary><div class="cbody">${marked.parse(innerMd)}</div></details>`);
    } else {
      const label = LABELS[kind] || kind;
      const head = title || label;
      out.push(`<aside class="callout ${kind}"><div class="chead">${kind === "note" ? '<span class="tag">Class note</span> ' + esc(title) : esc(head)}</div><div class="cbody">${marked.parse(innerMd)}</div></aside>`);
    }
  }
  flush();
  return out.join("\n");
}

const parsed = files.map(parseFile);
const chapters = [];
const byId = {};
for (const p of parsed) {
  const id = p.meta.merge || p.meta.id;
  if (!id) throw new Error("no id in " + p.name);
  if (!byId[id]) {
    byId[id] = { id, title: p.title, part: p.meta.part || "", summary: p.meta.summary || "", bodies: [] };
    chapters.push(byId[id]);
  }
  byId[id].bodies.push(p.body);
}

const allQA = [];
const searchIndex = [];
const out = chapters.map((ch) => {
  const md = ch.bodies.join("\n\n");
  const segs = [];
  let cur = { heading: ch.title, lines: [] };
  let inBlock = false;
  for (const l of md.split("\n")) {
    if (/^:::\w+/.test(l)) inBlock = true;
    else if (l.trim() === ":::") inBlock = false;
    const h = !inBlock && l.match(/^## (.*)$/);
    if (h) { segs.push(cur); cur = { heading: h[1].trim(), lines: [] }; }
    else cur.lines.push(l);
  }
  segs.push(cur);
  const sections = [];
  const html = segs.filter((s) => s.lines.join("").trim() || s !== segs[0]).map((s, idx) => {
    const id = `${ch.id}--${slug(s.heading) || idx}`;
    const body = renderBlocks(s.lines.join("\n"), ch.id, allQA);
    const isIntro = s === segs[0];
    if (!isIntro) sections.push({ id, title: s.heading });
    searchIndex.push({ ch: ch.id, chTitle: ch.title, id, title: s.heading, text: plain(body) });
    return `<section id="${id}">${isIntro ? "" : `<h2>${marked.parseInline(s.heading)}<a class="anchor" href="#${id}" aria-label="Link to section">#</a></h2>`}${body}</section>`;
  }).join("\n");
  return { id: ch.id, title: ch.title, part: ch.part, summary: ch.summary, sections, html };
});

const data = { chapters: out, search: searchIndex, qa: allQA, built: new Date().toISOString() };
fs.writeFileSync(path.join(root, "site", "content.js"), "window.CONTENT = " + JSON.stringify(data) + ";\n");
console.log(out.map((c) => `${c.id}: ${c.sections.length} sections, ${(c.html.length / 1024) | 0}KB`).join("\n"));
console.log("QA items:", allQA.length, "search entries:", searchIndex.length);
