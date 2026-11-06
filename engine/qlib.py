"""Authoring helpers. Content files call these; each returns a plain dict the builder validates.
wrongs: {option text: "why it is wrong"}  or  {option text: ("why it is wrong", "misconception label")}
"""

def _split(wrongs):
    ex, misc = {}, {}
    for k, v in wrongs.items():
        if isinstance(v, tuple):
            ex[k] = v[0]
            if len(v) > 1 and v[1]:
                misc[k] = v[1]
        else:
            ex[k] = v
    return ex, misc


def mc(topic, concept, q, right, wrongs, why, lp=False):
    ex, misc = _split(wrongs)
    return dict(topic=topic, concept=concept, type="mc", q=q, options=[right] + list(wrongs.keys()), correct=0,
                why=why, explain=ex, misc=misc, lp=lp)


def sata(topic, concept, q, rights, wrongs, why, lp=False):
    ex, misc = _split(wrongs)
    return dict(topic=topic, concept=concept, type="sata", q=q + " Select all that apply.",
                options=list(rights) + list(wrongs.keys()), correct=list(range(len(rights))), why=why,
                explain=ex, misc=misc, lp=lp)


def tf(topic, concept, q, truth, why, wrong_pick, lp=False):
    """q is the scenario plus the statement. wrong_pick explains the choice that is wrong."""
    wrong_label = "False" if truth else "True"
    return dict(topic=topic, concept=concept, type="tf", q=q, options=["True", "False"], correct=0 if truth else 1,
                why=why, explain={wrong_label: wrong_pick}, misc={}, lp=lp)


def order(topic, concept, q, steps, why, lp=False):
    return dict(topic=topic, concept=concept, type="order", q=q, options=list(steps), correct=list(range(len(steps))),
                why=why, explain={}, misc={}, lp=lp)


def blanks(topic, concept, q, blank_list, why, lp=False):
    """q has [1], [2]... markers. blank_list: [(right, {wrong: why or (why,label)}), ...]"""
    opts, correct, ex, misc = [], [], {}, {}
    for right, wr in blank_list:
        e, m = _split(wr)
        opts.append([right] + list(wr.keys()))
        correct.append(0)
        ex.update(e)
        misc.update(m)
    return dict(topic=topic, concept=concept, type="blanks" if len(blank_list) > 1 else "cloze", q=q, options=opts,
                correct=correct, why=why, explain=ex, misc=misc, lp=lp)


def match(topic, concept, q, pairs, extra, why, lp=False):
    """pairs: [(row prompt, right choice)]; extra: {wrong-only choice: why}. Every choice must be explained:
    for choices that are the right answer of some row pass an explanation in `describe` via why_each."""
    raise NotImplementedError


def match2(topic, concept, q, pairs, describe, why, lp=False):
    """pairs: [(row prompt, right choice)] ; describe: {choice: 'what that choice actually is/belongs to'}"""
    choices = [r for _, r in pairs]
    for c in describe:
        if c not in choices:
            choices.append(c)
    return dict(topic=topic, concept=concept, type="match", q=q, rows=[p for p, _ in pairs], options=choices,
                correct=[choices.index(r) for _, r in pairs], why=why, explain=dict(describe), misc={}, lp=lp)


def num(topic, concept, q, answer, unit, setup, why, near=None, lp=False):
    """Typed numeric answer (dosage). near: {classic wrong number as text: why it is wrong}."""
    return dict(topic=topic, concept=concept, type="num", q=q, options=[], correct=dict(answer=answer, unit=unit, setup=setup,
                near=near or {}), why=why, explain={}, misc={}, lp=lp)


def note(item, text, src="quiz", qno=None):
    """Attach a flag (lecture vs book, key problems) and a source tag to an item."""
    item["note"] = text
    item["src"] = src
    if qno:
        item["qno"] = qno
    return item


def quiz(item, qno, text=None):
    item["src"] = "quiz"
    item["qno"] = qno
    item["lp"] = True
    if text:
        item["note"] = text
    return item
