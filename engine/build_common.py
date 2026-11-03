import json, re, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import qlib

QLIB_NAMES = {n: getattr(qlib, n) for n in ("mc", "sata", "tf", "order", "blanks", "match2")}


def load_config(path):
    path = os.path.abspath(path)
    cfg = json.load(open(path))
    cfg["_dir"] = os.path.dirname(path)
    return cfg


def exec_files(paths, base, extra=None):
    ns = dict(QLIB_NAMES)
    if extra:
        ns.update(extra)
    for p in paths:
        code = open(os.path.join(base, p)).read()
        exec(compile(code, p, "exec"), ns)
    return ns


def load_items(cfg):
    items = []
    for p in cfg["items_module"]:
        ns = exec_files([p], cfg["_dir"])
        items.extend(ns["ITEMS"])
    return items


def load_concepts(cfg):
    out = []
    for p in cfg["concepts"]:
        ns = exec_files([p], cfg["_dir"])
        out.extend(ns["CONCEPTS"])
    return out


def load_guide(cfg):
    secs, links = [], {}
    for p in cfg["guide"]["parts"]:
        ns = exec_files([p], cfg["_dir"])
        secs.extend(ns["SECTIONS"])
        links.update(ns.get("LINKS", {}))
    return secs, links


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(s))).strip()


def attach_key_ideas(secs, concepts):
    """A guide section's Key ideas are its concept's points, so card and guide cannot drift apart."""
    by = {c["id"]: c for c in concepts}
    for s in secs:
        s["key_ideas"] = list(by[s["id"]]["points"]) if s["id"] in by else []
    return secs


def check_links(concepts, secs, links):
    """The builder refuses a card fact its linked sections do not contain."""
    sec_by = {s["id"]: s for s in secs}
    problems = []
    for c in concepts:
        ids = links.get(c["id"])
        if not ids:
            problems.append("concept %s has no guide link" % c["id"]); continue
        text = ""
        for i in ids:
            if i not in sec_by:
                problems.append("concept %s links to missing guide section %s" % (c["id"], i)); continue
            text += " " + " ".join(plain(x) for x in sec_by[i]["key_ideas"])
        for p in c["points"]:
            if plain(p) not in text:
                problems.append("card fact for %s not found in its guide section: %s" % (c["id"], p[:70]))
    return problems


def load_rationales(cfg):
    out = {}
    for p in cfg.get("rationales", []):
        ns = exec_files([p], cfg["_dir"])
        out.update(ns["WHY"])
    return out


def apply_rationales(items, why):
    """WHY keys are the question text or a substring of it; each must match exactly one question."""
    problems = []
    for key, text in why.items():
        hits = [it for it in items if key in it["q"]]
        if len(hits) != 1:
            problems.append("rationale key matches %d questions: %s" % (len(hits), key[:60]))
            continue
        hits[0]["why"] = text
    return problems
