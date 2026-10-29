"""Check companion-mm-state-prices.html against an independent Python model.

Run:  python -I Notas/L02/companions/check_companions.py
Extracts the page's own `model` function (between the MODEL-BEGIN / MODEL-END markers), runs it
with node at the control vectors below, recomputes every read-out here from slides 55-105's
expressions, and asserts agreement to 1e-9 (the page displays at most 3 decimals / 0.01%).
Also asserts the slide numbers at the default and at the presets. Requires `node` on PATH.
"""
import json, pathlib, re, subprocess, sys, tempfile

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE / "companion-mm-state-prices.html"

EX = dict(xb=3.15, xs=1.05, pb=1 / 2.8, ps=1 / 1.05 - 1 / 2.8)
VECTORS = {
    "low end (every control at its minimum)": dict(xb=0, xs=0, pb=0.05, ps=0.05, F=0),
    "default (slides 55-71, D = 1)": dict(EX, F=1.05),
    "high end (every control at its maximum)": dict(xb=5, xs=3, pb=0.9, ps=0.9, F=5),
    # presets, checked too
    "preset D = 0.4 (slide 78)": dict(EX, F=0.42),
    "preset D = 0.5 (slide 80)": dict(EX, F=0.525),
    "preset risky F = 2.1": dict(EX, F=2.1),
}


def py_model(s):
    """Independent read-outs. s: dict with xb, xs (payoffs), pb, ps (state prices), F (face).
    Returns the same keys as the page's model(); None where a return is undefined."""
    q, tiny = 0.5, 1e-12
    A = s["pb"] * s["xb"] + s["ps"] * s["xs"]
    debt = [min(x, s["F"]) for x in (s["xb"], s["xs"])]
    eq = [max(x - s["F"], 0) for x in (s["xb"], s["xs"])]
    D = s["pb"] * debt[0] + s["ps"] * debt[1]
    E = s["pb"] * eq[0] + s["ps"] * eq[1]
    return dict(
        A=A, npv=A - 1, D=D, E=E, bond=s["F"] * (s["pb"] + s["ps"]),
        put=s["pb"] * max(s["F"] - s["xb"], 0) + s["ps"] * max(s["F"] - s["xs"], 0),
        rf=1 / (s["pb"] + s["ps"]) - 1,
        rA=q * (s["xb"] + s["xs"]) / A - 1 if A > tiny else None,
        rD=q * sum(debt) / D - 1 if D > tiny else None,
        rE=q * sum(eq) / E - 1 if E > tiny else None,
        y=s["F"] / D - 1 if D > tiny else None,
        de=D / E if E > tiny else None,
        safe=s["F"] <= min(s["xb"], s["xs"]),
    )


html = PAGE.read_text(encoding="utf-8")
js = re.search(r"// MODEL-BEGIN.*?\n(.*?)// MODEL-END", html, re.S).group(1)
names = list(VECTORS)
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
    fh.write(js + "\nconsole.log(JSON.stringify(" + json.dumps([VECTORS[k] for k in names]) + ".map(model)));\n")
out = subprocess.run(["node", fh.name], capture_output=True, text=True, check=True).stdout
pathlib.Path(fh.name).unlink()
page = json.loads(out)

for name, got in zip(names, page):
    want = py_model(VECTORS[name])
    assert set(got) == set(want), (name, set(got) ^ set(want))
    for k, w in want.items():
        g = got[k]
        if w is None or isinstance(w, bool):
            assert g == w, (name, k, g, w)
        else:
            assert abs(g - w) < 1e-9, (name, k, g, w)
        # MM I: put-call parity reproduces A at every vector
    assert abs(want["E"] + want["bond"] - want["put"] - want["A"]) < 1e-12
    shown = {k: (None if v is None else (v if isinstance(v, bool) else round(v, 4))) for k, v in want.items()}
    print(f"{name}: {shown}")

d = py_model(VECTORS["default (slides 55-71, D = 1)"])
assert round(d["A"], 2) == 1.75 and round(d["D"], 2) == 1.0 and round(d["E"], 2) == 0.75  # slide 68
assert round(d["rD"], 4) == 0.05 and round(d["rE"], 4) == 0.40 and round(d["rA"], 4) == 0.20  # slide 71
assert d["safe"]
d4 = py_model(VECTORS["preset D = 0.4 (slide 78)"])
assert round(d4["D"], 3) == 0.4 and round(d4["E"], 2) == 1.35 and round(100 * d4["rE"], 1) == 24.4
d5 = py_model(VECTORS["preset D = 0.5 (slide 80)"])
assert round(d5["E"], 2) == 1.25 and round(d5["rE"], 4) == 0.26
dr = py_model(VECTORS["preset risky F = 2.1"])
assert round(dr["D"], 3) == 1.375 and round(100 * dr["rD"], 2) == 14.55 and round(100 * dr["y"], 1) == 52.7
assert not dr["safe"] and dr["y"] > dr["rD"]                                                 # slide 105
print(f"PASS: page model == Python model at {len(names)} control vectors; slide numbers reproduced.")
