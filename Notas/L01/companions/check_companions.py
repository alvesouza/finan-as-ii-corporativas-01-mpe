"""Verify companion-leverage-roe.html against an independent Python implementation.

Run from the repo root:  python -I Notas/L01/companions/check_companions.py
Extracts the page's own ``model()`` (between the MODEL-BEGIN / MODEL-END markers), runs it in
node at the three control vectors of /companion Step 6 (low end, default, high end) plus the
page's landmark presets, and compares every read-out with the Python version below to 1e-12.
Also asserts the slide-50 and Higgins 13e numbers. Fails loudly if node is missing.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
PAGE = pathlib.Path(__file__).resolve().parent / "companion-leverage-roe.html"


def model(s):
    """Python twin of the page's model(): L01-05 eqs. (5.16)-(5.21). Rates in percent, as the sliders."""
    t, r = s["tau"] / 100, s["rd"] / 100
    D, E = s["w"] * s["cap"], (1 - s["w"]) * s["cap"]
    interest = r * D
    ebt = s["ebit"] - interest
    tax = t * ebt
    ni = ebt - tax
    roic = s["ebit"] * (1 - t) / s["cap"]
    de = D / E
    spread = roic - r * (1 - t)
    return dict(D=D, E=E, de=de, interest=interest, ebt=ebt, tax=tax, ni=ni, roic=roic, roe=ni / E,
                roa=ni / s["cap"], atrd=r * (1 - t), spread=spread, identity=roic + de * spread, swing=1 + de)


VECTORS = {
    "low end": dict(ebit=0, cap=500, w=0, rd=0, tau=0),
    "default (slide 50, Company A)": dict(ebit=120, cap=1000, w=0.9, rd=10, tau=40),
    "high end": dict(ebit=400, cap=2000, w=0.9, rd=20, tau=50),
}
LANDMARKS = {
    "Company B": dict(ebit=120, cap=1000, w=0, rd=10, tau=40),
    "flat": dict(ebit=120, cap=1000, w=0.9, rd=12, tau=40),
    "Higgins 13e": dict(ebit=120, cap=1000, w=0.9, rd=10, tau=25),
    "negative spread": dict(ebit=120, cap=1000, w=0.9, rd=16, tau=40),
}


def run_js(vectors):
    """Run the page's model() in node on each vector; return the list of result dicts."""
    html = PAGE.read_text(encoding="utf-8")
    block = re.search(r"// MODEL-BEGIN.*?\n(.*?)// MODEL-END", html, re.S).group(1)
    node = shutil.which("node")
    assert node, "node not found on PATH"
    js = block + "\nconsole.log(JSON.stringify(" + json.dumps(vectors) + ".map(model)));"
    out = subprocess.run([node, "-e", js], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def main():
    allv = {**VECTORS, **LANDMARKS}
    js = run_js(list(allv.values()))
    n = 0
    for (name, v), jr in zip(allv.items(), js):
        py = model(v)
        for k, pv in py.items():
            assert abs(pv - jr[k]) <= 1e-12 * max(1.0, abs(pv)), (name, k, pv, jr[k])
            n += 1
        assert abs(py["roe"] - py["identity"]) < 1e-12, name       # eq. (5.20) holds exactly
        if name in VECTORS:
            print(f"{name:32s} ROE {100 * py['roe']:8.3f}%  ROA {100 * py['roa']:7.3f}%  "
                  f"ROIC {100 * py['roic']:6.3f}%  D/E {py['de']:5.2f}  JS == Python")
    a = model(VECTORS["default (slide 50, Company A)"])
    assert (round(a["roe"], 12), round(a["roa"], 12), round(a["roic"], 12)) == (0.18, 0.018, 0.072)  # slide 50
    b = model(LANDMARKS["Company B"])
    assert round(b["roe"], 12) == round(b["roa"], 12) == round(b["roic"], 12) == 0.072
    f = model(LANDMARKS["flat"])
    assert abs(f["roe"] - f["roic"]) < 1e-12                          # spread 0: ROE flat in D/E
    h = model(LANDMARKS["Higgins 13e"])
    assert (round(h["roe"], 12), round(h["roic"], 12), round(h["roa"], 12)) == (0.225, 0.09, 0.0225)  # pp. 55-56
    g = model(LANDMARKS["negative spread"])
    assert abs(g["roe"] + 0.144) < 1e-12
    print(f"PASS: {n} read-out comparisons at {len(allv)} vectors (3 Step-6 vectors + {len(LANDMARKS)} landmarks)")


if __name__ == "__main__":
    main()
