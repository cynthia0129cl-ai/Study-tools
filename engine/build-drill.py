#!/usr/bin/env python3
"""Builds the drill page from a config, validating every item. Usage: build-drill.py config.json [--guide-url URL] [--out FILE]"""
import sys, os, re, json, argparse, collections
from build_common import *

TYPES = {"mc", "sata", "cloze", "blanks", "order", "tf", "match"}


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def sentences(t):
    t = re.sub(r"\([^()]*\)\s*$", "", t.strip())
    return len([x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])", t) if x.strip()])


def validate(cfg, items, concepts):
    errs, warns = [], []
    topics = {t["id"] for t in cfg["topics"]}
    cids = {c["id"] for c in concepts}
    seen = {}
    expl_total = expl_done = 0
    tfbal = collections.defaultdict(lambda: [0, 0])
    for n, it in enumerate(items):
        tag = "item %d (%s)" % (n, it["q"][:50])
        if it["topic"] not in topics: errs.append(tag + ": unknown topic " + it["topic"])
        if it["concept"] not in cids: errs.append(tag + ": unknown concept " + it["concept"])
        if it["type"] not in TYPES: errs.append(tag + ": unknown type")
        k = norm(it["q"])
        if k in seen: errs.append(tag + ": duplicate of item %d" % seen[k])
        seen[k] = n
        if not re.search(r"\([^()]*\)\s*$", it["why"]): errs.append(tag + ": the key idea must end with a source in brackets")
        ns = sentences(it["why"])
        if ns < 3 or ns > 5: warns.append(tag + ": key idea has %d sentences" % ns)
        t, o, c = it["type"], it["options"], it["correct"]
        wrong_opts = []
        if t == "mc":
            if not (0 <= c < len(o)): errs.append(tag + ": answer index out of range")
            wrong_opts = [x for i, x in enumerate(o) if i != c]
            if len(o) not in (4, 5): errs.append(tag + ": mc needs 4 or 5 options")
        elif t == "tf":
            wrong_opts = [o[1 - c]]
            tfbal[it["topic"]][0 if c == 0 else 1] += 1
        elif t == "sata":
            if any(not (0 <= i < len(o)) for i in c): errs.append(tag + ": answer index out of range")
            wrong_opts = [x for i, x in enumerate(o) if i not in c]
            if len(c) < 2 or len(wrong_opts) < 1: errs.append(tag + ": sata needs 2+ right and 1+ wrong")
        elif t in ("blanks", "cloze"):
            for b, ch in enumerate(o):
                if not (0 <= c[b] < len(ch)): errs.append(tag + ": blank answer out of range")
                wrong_opts += [x for i, x in enumerate(ch) if i != c[b]]
            if len(set(wrong_opts)) != len(wrong_opts): errs.append(tag + ": duplicate wrong option text across blanks")
            if not (1 <= len(o) <= 4): errs.append(tag + ": blanks need 1 to 4 blanks")
            for b in range(len(o)):
                if "[%d]" % (b + 1) not in it["q"]: errs.append(tag + ": missing [%d] marker" % (b + 1))
        elif t == "order":
            if not (3 <= len(o) <= 8): errs.append(tag + ": order needs 3 to 8 steps")
        elif t == "match":
            if not (3 <= len(it["rows"]) <= 4): errs.append(tag + ": match needs 3 or 4 rows")
            for r, ci in enumerate(c):
                if not (0 <= ci < len(o)): errs.append(tag + ": match answer out of range")
            wrong_opts = list(o)  # every choice needs a description
        for w in wrong_opts:
            expl_total += 1
            if w in it["explain"] and it["explain"][w].strip(): expl_done += 1
            else: errs.append(tag + ": wrong option without explanation: " + str(w)[:60])
        if t != "match":
            right = set()
            if t == "mc": right = {o[c]}
            elif t == "sata": right = {o[i] for i in c}
            elif t == "tf": right = {o[c]}
            elif t in ("blanks", "cloze"): right = {ch[c[b]] for b, ch in enumerate(o)}
            for k2 in it["explain"]:
                if k2 in right: errs.append(tag + ": explanation attached to a correct option: " + k2[:50])
            for k2 in it["misc"]:
                if k2 not in wrong_opts: errs.append(tag + ": misconception label on a non-wrong option")
    for tp, (a, b) in tfbal.items():
        if a != b: errs.append("topic %s: true/false is %d true and %d false; it must be exactly half and half" % (tp, a, b))
    per = 2 if len(cfg["topics"]) > 10 else 3
    for t in topics:
        n = len([i for i in items if i["topic"] == t and not i["lp"]])
        if n < per: errs.append("topic %s has only %d non-last-pass questions; the pre-test needs %d" % (t, n, per))
        if not [i for i in items if i["topic"] == t]: errs.append("topic %s has no questions" % t)
    covered = len([i for i in items if i["concept"] in cids])
    return errs, warns, expl_done, expl_total, covered, tfbal


def build(cfg, guide_url=None, out=None):
    items = load_items(cfg)
    rp = apply_rationales(items, load_rationales(cfg))
    if rp:
        sys.exit("BUILD REFUSED:\n  " + "\n  ".join(rp))
    concepts = load_concepts(cfg)
    secs, links = load_guide(cfg)
    attach_key_ideas(secs, concepts)
    errs, warns, ed, et, covered, tfbal = validate(cfg, items, concepts)
    errs += check_links(concepts, secs, links)
    # concept coverage
    for c in concepts:
        if not [i for i in items if i["concept"] == c["id"]]: errs.append("concept %s has no questions" % c["id"])
    if errs:
        sys.exit("BUILD REFUSED:\n  " + "\n  ".join(errs[:60]) + ("\n  ... %d more" % (len(errs) - 60) if len(errs) > 60 else ""))
    Q = []
    for n, it in enumerate(items):
        q = dict(id=n, t=it["topic"], ty=it["type"], q=it["q"], o=it["options"], c=it["correct"], w=it["why"],
                 x=it["explain"], m=it["misc"], k=it["concept"], lp=1 if it["lp"] else 0)
        if it["type"] == "match": q["r"] = it["rows"]
        Q.append(q)
    con = {}
    for c in concepts:
        con[c["id"]] = dict(title=c["title"], unit=c["unit"], points=c["points"], source=c["source"], guide=links[c["id"]])
    gurl = guide_url or cfg["guide"]["url"]
    data = dict(cfg=dict(title=cfg["title"], eyebrow=cfg["eyebrow"], sub=cfg["sub"], key=cfg["storage_key"],
                         topics=cfg["topics"], highRoi=cfg["high_roi_topics"], lastPassNote=cfg["last_pass_note"],
                         guide=dict(url=gurl)), Q=Q, concepts=con)
    core = open(os.path.join(HERE, "engine-core.js")).read()
    readme = open(os.path.join(HERE, "readme-study-system.html")).read()
    tpl = open(os.path.join(HERE, "drill-template.html")).read()
    page = (tpl.replace("__TITLE__", cfg["title"] + " Drill").replace("__CORE__", core.replace("</script", "<\\/script"))
            .replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
            .replace("__README__", json.dumps(readme.replace("<h1>Read me</h1>", "<h1>Read me</h1>"), ensure_ascii=False).replace("</", "<\\/")))
    outp = out or os.path.join(cfg["_dir"], cfg["out"])
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    open(outp, "w").write(page)
    json.dump(data, open(os.path.join(os.path.dirname(outp), "_data.json"), "w"))
    # report
    print("DRILL BUILD OK -> %s (%d KB)" % (outp, len(page) // 1024))
    print("questions: %d" % len(Q))
    bt = collections.Counter(i["topic"] for i in items)
    for t in cfg["topics"]:
        fm = collections.Counter(i["type"] for i in items if i["topic"] == t["id"])
        lp = len([i for i in items if i["topic"] == t["id"] and i["lp"]])
        print("  %-34s %3d  (last pass %d)  %s" % (t["name"], bt[t["id"]], lp, dict(fm)))
    print("formats:", dict(collections.Counter(i["type"] for i in items)))
    print("last pass: %d questions" % sum(1 for i in items if i["lp"]))
    print("explained %d of %d wrong options" % (ed, et))
    print("concepts: %d, questions covered %d of %d" % (len(concepts), covered, len(items)))
    print("true/false per topic (true,false):", {k: tuple(v) for k, v in tfbal.items()})
    if warns:
        print("warnings (%d):" % len(warns))
        for w in warns: print("  -", w)
    return Q


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("config"); ap.add_argument("--guide-url"); ap.add_argument("--out")
    a = ap.parse_args()
    build(load_config(a.config), a.guide_url, a.out)
