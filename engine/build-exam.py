#!/usr/bin/env python3
"""Builds the Mastery Study Guide and then the drill from one config, with the shared Read me in both.
Usage: build-exam.py exams/<exam>/config-<exam>.json [--guide-url URL] [--drill-url URL]"""
import argparse, importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_common import load_config


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("config"); ap.add_argument("--guide-url"); ap.add_argument("--drill-url")
    ap.add_argument("--outdir")
    a = ap.parse_args()
    cfg = load_config(a.config)
    g, d = load("build-guide"), load("build-drill")
    gout = dout = None
    if a.outdir:
        gout = os.path.join(a.outdir, os.path.basename(cfg["guide"]["out"]))
        dout = os.path.join(a.outdir, os.path.basename(cfg["out"]))
    g.build(cfg, a.drill_url, gout)
    d.build(cfg, a.guide_url, dout)
