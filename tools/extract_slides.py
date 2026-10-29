#!/usr/bin/env python3
"""Extract the word-for-word PowerPoint blocks from the first study guide text
and write them as markdown (one file per chapter) for the site build."""
import re, sys, os

src, outdir = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")

chapters = ["13", "33", "34", "26", "65", "66", "11", "18", "19"]
ids = {"13": "cancer", "33": "heme-assess", "34": "heme-disorders", "26": "lung",
       "65": "female", "66": "male", "11": "pain", "18": "immune", "19": "immune"}
order = {"13": "01", "26": "02", "33": "03", "34": "04", "18": "05", "19": "05", "65": "07", "66": "08", "11": "09"}

starts = [i for i, l in enumerate(lines) if "▣ CAll" in l or l.strip().startswith("▣ CAll")]
assert len(starts) == len(chapters), (len(starts), starts)

footer = re.compile(r"NUR291 Exam 1 Study Guide ·")
slide_re = re.compile(r"^\s*▣ (SLIDES|IMAGE-ONLY SLIDES)\s*(\d+)?\s*·?\s*(.*)$")
para_start = re.compile(r"^(\[Image|Figure|Episode \d|Wrap-?[Uu]p|Table \d|Learning Objectives)")
label = re.compile(r"^[A-Z][A-Za-z0-9'’&/,\- ]{2,38}: ")

ACR = ["OPQRST-AAA","WHO","NSAIDS","NSAID","CBC","TNM","XLA","DIC","PID","CVID","IGA","IGG","SCID","HIV","BPH","TURP","PSA","SVC","IVIG","DNA","ITP","HIT","IDA","PV","CMC","TENS","DBS","RBC","WBCS","WBC","BTK","HYPER-IGM","B","T","II","IV","I","III","V","ST","TIBC","PT","INR","PTT","LAP","CAUTION","DIGEORGE","WISKOTT–ALDRICH","HODGKIN'S","NON-HODGKIN'S","ASSESS","ACT","TEACH","EVALUATE"]
KEEP = {"OPQRST-AAA":"OPQRST-AAA","WHO":"WHO","NSAIDS":"NSAIDs","NSAID":"NSAID","CBC":"CBC","TNM":"TNM","XLA":"XLA","DIC":"DIC","PID":"PID","CVID":"CVID","IGA":"IgA","IGG":"IgG","SCID":"SCID","HIV":"HIV","BPH":"BPH","TURP":"TURP","PSA":"PSA","SVC":"SVC","IVIG":"IVIG","DNA":"DNA","ITP":"ITP","HIT":"HIT","IDA":"IDA","PV":"PV","CMC":"CMC","TENS":"TENS","DBS":"DBS","RBC":"RBC","WBCS":"WBCs)","WBC":"WBC","BTK":"BTK","HYPER-IGM":"Hyper-IgM","TIBC":"TIBC","PT":"PT","INR":"INR","PTT":"PTT","LAP":"LAP","CAUTION":"CAUTION","DIGEORGE":"DiGeorge","WISKOTT–ALDRICH":"Wiskott–Aldrich","HODGKIN'S":"Hodgkin's","NON-HODGKIN'S":"non-Hodgkin's"}
def sentence(t):
    t = t.strip()
    if not t:
        return t
    words = t.split(" ")
    out = []
    for i, w in enumerate(words):
        core = w.strip(",.:;&")
        if core in KEEP:
            out.append(w.replace(core, KEEP[core]))
        else:
            out.append(w.lower())
    r = " ".join(out)
    return r[:1].upper() + r[1:]

for ch, st in zip(chapters, starts):
    end = len(lines)
    for j in range(st + 1, len(lines)):
        if re.match(r"^\d\d [A-Z]", lines[j]):
            end = j
            break
    slides, cur = [], None
    for l in lines[st:end]:
        if footer.search(l):
            continue
        m = slide_re.match(l)
        if m:
            kind, num, title = m.groups()
            if kind.startswith("IMAGE"):
                cur = {"title": "Image-only slides (written out)", "num": None, "paras": []}
            else:
                cur = {"title": sentence(title) or "", "num": num, "paras": []}
            slides.append(cur)
            continue
        if cur is None:
            continue
        s = l.strip()
        if not s:
            continue
        if s.startswith("H ") and "T H E W H O L E" in s:
            continue
        if not cur["paras"] or para_start.match(s) or (label.match(s) and len(cur["paras"][-1]) > 0 and cur["paras"][-1].endswith((".", ")", "]")) ) :
            cur["paras"].append(s)
        else:
            cur["paras"][-1] += " " + s
    out = []
    for sl in slides:
        head = f"Slide {sl['num']}" if sl["num"] else "Slides"
        if sl["title"]:
            head += f" · {sl['title']}"
        out.append(f":::slides {head}")
        out.append("\n\n".join(sl["paras"]))
        out.append(":::\n")
    name = f"{order[ch]}z-slides-ch{ch}.md"
    body = [f"# Slides ch{ch}", f"@merge: {ids[ch]}", "", f"## Chapter {ch} PowerPoint, word for word",
            "Your instructor's slides for this chapter, kept in slide order.", ""] + out
    open(os.path.join(outdir, name), "w", encoding="utf-8").write("\n".join(body))
    print(name, len(slides), "slides")
