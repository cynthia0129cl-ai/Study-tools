#!/usr/bin/env python3
"""Assembles the single-file study system. Usage: python3 build_study.py [out.html]"""
import sys, os, re, json, collections
MYDIR = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.join(MYDIR, "..", "engine")
sys.path.insert(0, ENG)
from build_common import *
EX = os.path.join(ENG, "exams", "oncology-exam1")

def ld(base, files):
    out = []
    for f in files:
        out += exec_files([f], base)["ITEMS"]
    return out

CHAPTERS = [
 ("ch1", "Cancer Basics: Risk, Staging, Biopsy", "Basics", ["risk", "stage", "biopsy"]),
 ("ch2", "Labs and Blood Counts", "Labs", ["labs", "pv"]),
 ("ch3", "Leukemia and Neutropenia", "Leukemia", ["leuk", "neut"]),
 ("ch4", "Lymphoma and Myeloma", "Lymphoma/MM", ["hodgkin", "mm"]),
 ("ch5", "Lung Cancer", "Lung", ["lung"]),
 ("ch6", "Breast, Ovarian, Uterine and Cervical Cancer", "Female repro", ["breast", "uterine", "cervical"]),
 ("ch7", "Prostate and Testicular Cancer", "Male repro", ["prostate", "testis"]),
 ("ch8", "Pain, Dosage and End of Life", "Pain/Dose/EOL", ["pain", "dose", "eol"]),
]
TOPIC_NAMES = {t["id"]: t["name"] for t in load_config(os.path.join(EX, "config-oncology.json"))["topics"]}
TOPIC_NAMES.update(pv="Polycythemia vera", pain="Pain management", dose="Dosage calculations")
TOPIC_NAMES["prostate"] = "Prostate cancer and BPH: post-op complications"
EXAM_COUNT = {"leuk": 5, "prostate": 5, "dose": 2, "eol": 2}
T2C = {t: c[0] for c in CHAPTERS for t in c[3]}

EMPH = {
 "ch1": ["Cancer risk factors, cancer staging (size of tumor, TNM) using the table in Davis, and biopsy procedures are on your priority list."],
 "ch2": ["Labs (CBC, WBC, platelets) are a priority topic."],
 "ch3": ["Leukemia is worth 5 questions: risk factors and medications.", "Neutropenic precautions are a priority topic."],
 "ch4": ["Hodgkin lymphoma: complications and symptoms.", "Multiple myeloma: nursing interventions."],
 "ch5": ["Lung cancer is a priority topic."],
 "ch6": ["Breast cancer in men and women: medications (Davis).", "Cervical cancer guidelines and uterine cancer."],
 "ch7": ["Prostate cancer is worth 5 questions: complications after surgery.", "Testicular cancer."],
 "ch8": ["End of life is worth 2 questions: the difference between hospice and palliative care.", "Dosage calculations are worth 2 questions."],
}
EXTRA_CORE = {}  # filled from items' key ideas for concepts with no card

def tk_of(why):
    w = re.sub(r"\s*\([^()]*\)\s*$", "", why.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])", w)
    return parts[0].strip() if parts else w

def conv(it, qid, rs):
    t = it["type"]
    d = dict(id=qid, ty="blanks" if t == "cloze" else t, ch=T2C[it["topic"]], t=it["topic"], cn=it["concept"], q=it["q"],
             o=it["options"], c=it["correct"], x=it.get("explain", {}), tk=tk_of(it["why"]), w=it["why"])
    if t == "match": d["rows"] = it["rows"]
    if it.get("lp"): d["lp"] = 1
    if it.get("note"): d["note"] = it["note"]
    if it.get("src"): d["src"] = it["src"]
    if it.get("qno"): d["qno"] = it["qno"]
    if rs: d["rs"] = 1
    return d

def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def main(out):
    base = ld(EX, ["items-oncology-a.py", "items-oncology-b.py", "items-oncology-c.py"]) + ld(MYDIR, ["items-oncology-d.py", "items-quiz334.py", "items-oncology-e.py", "items-new-slides.py"])
    res = ld(MYDIR, ["variants-oncology.py", "variants-e.py"])
    errs = []
    why = exec_files(["rationales-oncology.py"], EX)["WHY"]
    errs += apply_rationales(base, why)
    seen = {}
    for n, it in enumerate(base + res):
        k = norm(it["q"])
        if k in seen: errs.append("duplicate question: " + it["q"][:70])
        seen[k] = n
        if it["topic"] not in T2C: errs.append("topic without chapter: " + it["topic"])
        t, o = it["type"], it["options"]
        need = []
        if t == "mc": need = [x for i, x in enumerate(o) if i != it["correct"]]
        elif t == "sata": need = [x for i, x in enumerate(o) if i not in it["correct"]]
        elif t == "tf": need = [o[1 - it["correct"]]]
        elif t in ("blanks", "cloze"):
            for b, ch in enumerate(o): need += [x for i, x in enumerate(ch) if i != it["correct"][b]]
        elif t == "match": need = list(it["explain"].keys())
        for x in need:
            if not it["explain"].get(x): errs.append("no rationale for option '%s' in: %s" % (x[:40], it["q"][:60]))
        if t == "num" and not it["correct"].get("setup"): errs.append("num without setup: " + it["q"][:50])
        if t == "sata" and len(it["correct"]) < 2: errs.append("sata with <2 answers: " + it["q"][:50])
    if errs:
        print("\n".join(errs[:60])); print(len(errs), "problems"); sys.exit(1)
    Q = [conv(it, "q%03d" % (i + 1), False) for i, it in enumerate(base)] + [conv(it, "r%03d" % (i + 1), True) for i, it in enumerate(res)]
    # core facts per chapter from concept cards + key ideas of the concepts that have no card
    concepts = load_concepts({"_dir": EX, "concepts": ["concepts-oncology.py"]})
    have = {c["id"] for c in concepts}
    core = collections.defaultdict(list)
    for c in concepts:
        ch = T2C.get(c["unit"])
        if ch: core[ch] += [plain(p) for p in c["points"]]
    done = set()
    for it in base:
        if it["concept"] not in have and it["concept"] not in done and it.get("src") != "quiz-skip":
            done.add(it["concept"]); core[T2C[it["topic"]]].append(re.sub(r"\s*\([^()]*\)\s*$", "", it["why"]))
    diff = collections.defaultdict(list)
    for it in base:
        n = it.get("note", "")
        if re.search(r"Lecture vs book|Wording problem|Key problem|rationale printed", n):
            diff[T2C[it["topic"]]].append(n)
    pearls = {c[0]: dict(emph=EMPH[c[0]], diff=diff.get(c[0], []), core=core.get(c[0], [])) for c in CHAPTERS}
    review_first = [q["id"] for q in Q if q.get("src") == "quiz" and q.get("qno") in (2, 5, 18, 22, 24, 28, 41)]
    chap_ids = [c[0] for c in CHAPTERS]
    def S(ch=None, **k):
        d = dict(k)
        if ch: d["ch"] = ch
        return d
    plan = [
     dict(date="2026-11-06", label="Fri Nov 6 · heavy day", tasks=[
      dict(id="p1", label="Redo the quiz questions you missed", sub="7 questions from your NUR 334 practice quiz", set=dict(ids=review_first)),
      dict(id="p2", label="Leukemia and neutropenia: 25 questions", sub="Highest-weighted chapter (leukemia is 5 questions)", set=S(["ch3"], count=25)),
      dict(id="p3", label="Labs and blood counts: 25 questions", sub="CBC, WBC, platelets, polycythemia", set=S(["ch2"], count=25)),
      dict(id="p4", label="Read the Leukemia and Labs pearls", sub="10 minutes", go="pearls")]),
     dict(date="2026-11-07", label="Sat Nov 7 · heavy day", tasks=[
      dict(id="p5", label="Prostate and testicular: 25 questions", sub="Prostate is 5 questions; post-op complications", set=S(["ch7"], count=25)),
      dict(id="p6", label="Cancer basics: 25 questions", sub="Risk factors, TNM staging, biopsy", set=S(["ch1"], count=25)),
      dict(id="p7", label="Lymphoma and myeloma: 20 questions", sub="Hodgkin symptoms and complications; myeloma nursing", set=S(["ch4"], count=20)),
      dict(id="p8", label="SATA Lab: 10 questions", sub="Select-all practice", set=S(None, count=10, ty=dict(sata=1, match=1)))]),
     dict(date="2026-11-08", label="Sun Nov 8 · lighter day", tasks=[
      dict(id="p9", label="Breast, uterine and cervical: 20 questions", sub="Medications and cervical screening guidelines", set=S(["ch6"], count=20)),
      dict(id="p10", label="Lung cancer: 15 questions", sub="", set=S(["ch5"], count=15)),
      dict(id="p11", label="Pain, dosage and end of life: 15 questions", sub="Hospice vs palliative; the numeric questions", set=S(["ch8"], count=15)),
      dict(id="p12", label="Retry everything you missed", sub="Review & Retry", go="review")]),
     dict(date="2026-11-09", label="Mon Nov 9 · day before the exam", tasks=[
      dict(id="p13", label="Timed practice exam: 50 questions", sub="50 minutes, no feedback until you submit", set=dict(mode="exam", count=50)),
      dict(id="p14", label="Retry the questions you missed on the practice exam", sub="Review & Retry", go="review"),
      dict(id="p15", label="Skim all the pearls, then stop and sleep", sub="", go="pearls")]),
     dict(date="2026-11-10", label="Tue Nov 10 · exam day", tasks=[
      dict(id="p16", label="Look over the pearls once", sub="No new material today.", go="pearls")]),
    ]
    topics = [dict(id=t, name=TOPIC_NAMES[t], ch=T2C[t], exam=EXAM_COUNT.get(t, 0)) for c in CHAPTERS for t in c[3]]
    bank = dict(meta=dict(key="study:nur-oncology-heme-exam1:v1", examDate="2026-11-10", examLabel="Exam 1 · Tuesday, November 10"),
                chapters=[dict(id=c[0], name=c[1], short=c[2]) for c in CHAPTERS], topics=topics, Q=Q, pearls=pearls, plan=plan, reviewFirst=review_first)
    js = json.dumps(bank, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open(os.path.join(MYDIR, "app-template.html"), encoding="utf-8").read()
    html = tpl.replace("__TITLE__", "Heme Cancer Study System").replace("__EYEBROW__", "NUR 291 · Exam 1 · Tue Nov 10").replace("__BRAND__", "Oncology and Heme Study System").replace("__BANK__", js)
    art = os.path.join(MYDIR, "_artifact-page.html")
    open(art, "w", encoding="utf-8").write(html)
    k = html.index('<div class="wrap">')
    full = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + html[:k] + '</head><body>\n' + html[k:] + '\n</body></html>\n'
    open(out, "w", encoding="utf-8").write(full)
    base_n = collections.Counter(q["ch"] for q in Q if not q.get("rs"))
    print("base", sum(base_n.values()), "reserve", len(Q) - sum(base_n.values()), "bytes", len(html))
    for c in CHAPTERS: print(c[0], c[1], base_n[c[0]], collections.Counter(q["ty"] for q in Q if q["ch"] == c[0] and not q.get("rs")).most_common())
    print("reviewFirst", review_first)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(MYDIR, "..", "dist", "NUR-Oncology-Heme-Study-System.html"))
