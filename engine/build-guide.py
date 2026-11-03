#!/usr/bin/env python3
"""Builds the Mastery Study Guide page from a config. Usage: build-guide.py config.json [--drill-url URL] [--out FILE]"""
import sys, os, re, html, argparse
from build_common import *


def esc(s):
    return html.escape(s, quote=False)


def blanks_html(t):
    out = esc(t)
    return re.sub(r"\{\{(.+?)\}\}", lambda m: '<button class="blk" type="button">%s</button>' % m.group(1), out)


def build(cfg, drill_url=None, out=None):
    concepts = load_concepts(cfg)
    secs, links = load_guide(cfg)
    attach_key_ideas(secs, concepts)
    problems = check_links(concepts, secs, links)
    if problems:
        sys.exit("GUIDE LINK PROBLEMS:\n  " + "\n  ".join(problems))
    con = {c["id"]: c for c in concepts}
    topics = cfg["topics"]
    body, toc = [], []
    for t in topics:
        mine = [c for c in concepts if c["unit"] == t["id"]]
        if not mine:
            continue
        toc.append('<a href="#u-%s">%s</a>' % (t["id"], esc(t["name"])))
        body.append('<div class="unit" id="u-%s"><h2>%s</h2></div>' % (t["id"], esc(t["name"])))
        for c in mine:
            s = next((x for x in secs if x["id"] == c["id"]), None)
            if not s:
                sys.exit("no guide section for concept " + c["id"])
            acts = "".join("<li>%s</li>" % esc(a) for a in s["act"])
            bl = "".join("<li>%s</li>" % blanks_html(b) for b in s["blanks"])
            ki = "".join("<li>%s</li>" % esc(p) for p in s["key_ideas"])
            body.append(
                '<section class="sec" id="%s"><h2>%s</h2>'
                '<div class="lab">Mechanism first</div><p>%s</p>'
                '<div class="lab">Priority actions</div><ul>%s</ul>'
                '<div class="lab">Patient example</div><p>%s</p>'
                '<div class="lab">Common trap</div><div class="trap"><p>%s</p></div>'
                '<div class="lab">Memory trick</div><div class="mem"><p>%s</p></div>'
                '<div class="lab">Tap to reveal the blanks</div><ul>%s</ul>'
                '<div class="key"><b class="t">Key ideas</b><ul>%s</ul><div class="small">Source: %s</div></div></section>'
                % (c["id"], esc(c["title"]), esc(s["mech"]), acts, esc(s["ex"]), esc(s["trap"]), esc(s["mem"]), bl, ki, esc(c["source"])))
    tpl = open(os.path.join(HERE, "guide-shell.html")).read()
    readme = open(os.path.join(HERE, "readme-study-system.html")).read()
    page = (tpl.replace("__TITLE__", esc(cfg["guide"].get("title", cfg["title"] + " Mastery Study Guide")))
            .replace("__EYEBROW__", esc(cfg["eyebrow"])).replace("__SUB__", esc(cfg["guide"].get("sub", cfg["sub"])))
            .replace("__TOC__", "".join(toc)).replace("__BODY__", "\n".join(body)).replace("__README__", readme)
            .replace("__DRILL_URL__", drill_url or cfg["guide"].get("drill_url", cfg["out"])))
    outp = out or os.path.join(cfg["_dir"], cfg["guide"]["out"])
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    open(outp, "w").write(page)
    print("guide: %d sections in %d units, %d KB -> %s" % (len(secs), len(toc), len(page) // 1024, outp))
    return secs, links


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("config"); ap.add_argument("--drill-url"); ap.add_argument("--out")
    a = ap.parse_args()
    build(load_config(a.config), a.drill_url, a.out)
