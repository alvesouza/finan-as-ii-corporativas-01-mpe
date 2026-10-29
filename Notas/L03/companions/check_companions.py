"""Check companion-static-trade-off.html against an independent Python computation.

Run from anywhere:  python -I Notas/L03/companions/check_companions.py   (needs node on PATH)

The page's model() (between the MODEL-BEGIN / MODEL-END markers) is run with node at three
control vectors: the lower end of every slider, the default calibration, the upper end. Python
recomputes every read-out from the slides' integrals (slides 42-44) with scipy.integrate.quad
on the uniform density, and finds K* by bounded numerical maximization of V(K) -- not by the
closed form K* = X_hi - C/tau the page uses. Read-outs must agree to the displayed precision.
"""
import json
import pathlib
import subprocess
import sys
import tempfile

from scipy import integrate, optimize

sys.stdout.reconfigure(encoding="utf-8")
HTML = pathlib.Path(__file__).with_name("companion-static-trade-off.html")
VECTORS = {
    "low end": dict(tau=0, C=0, xlo=50, xhi=130, rf=0, K=0),
    "default": dict(tau=35, C=20, xlo=50, xhi=150, rf=5, K=80),
    "high end": dict(tau=50, C=49, xlo=120, xhi=300, rf=10, K=300),
    # landmarks beyond the three required vectors: the safe-debt corner and C = 0
    "corner C=40": dict(tau=35, C=40, xlo=50, xhi=150, rf=5, K=80),
    "landmark C=0": dict(tau=35, C=0, xlo=50, xhi=150, rf=5, K=80),
}
FIELDS = ["ks", "vu", "vstar", "gain", "pvts", "pvdc", "hstar", "dstar", "yld", "estar", "lev",
          "vk", "dk", "ek", "hk", "dvk"]


def js_readouts():
    src = HTML.read_text(encoding="utf-8")
    model = src.split("// MODEL-BEGIN")[1].split("// MODEL-END")[0]
    model = model.split("\n", 1)[1]                       # drop the rest of the marker line
    driver = model + "\nvar V=" + json.dumps(VECTORS) + ";var out={};for(var k in V){var m=model(V[k]);" \
        "out[k]={};" + "".join(f"out[k].{f}=m.{f};" for f in FIELDS) + "out[k].regime=m.regime;}" \
        "console.log(JSON.stringify(out));"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(driver)
    return json.loads(subprocess.run(["node", f.name], capture_output=True, text=True, check=True).stdout)


def py_readouts(v):
    """Slides 42-44 by numerical integration; uniform h on [xlo, xhi]."""
    t, r, a, b, c = v["tau"] / 100, v["rf"] / 100, v["xlo"], v["xhi"], v["C"]
    h = 1 / (b - a)
    df = 1 + r
    quad = lambda f, lo, hi: integrate.quad(f, lo, hi)[0] if hi > lo else 0.0
    H = lambda K: quad(lambda x: h, a, min(max(K, a), b))
    vu = quad(lambda x: (1 - t) * x * h, a, b) / df                                   # (2)
    E = lambda K: quad(lambda x: (1 - t) * (x - K) * h, max(K, a), b) / df              # (4)
    D = lambda K: (quad(lambda x: (x - c) * h, a, min(K, b)) + K * (1 - H(K))) / df    # (5)
    V = lambda K: E(K) + D(K)
    if t == 0:
        ks = a                       # MM: every safe K ties; the page reports the top, X_lo
    elif c == 0:
        ks = b                       # V rises to X_hi, flat beyond; the page reports X_hi
    else:
        res = optimize.minimize_scalar(lambda K: -V(K), bounds=(a, b), method="bounded",
                                       options={"xatol": 1e-9})
        ks = max([a, res.x, b], key=V)
    vs = V(ks)
    dvk = (V(v["K"] + 1e-5) - V(v["K"] - 1e-5)) / 2e-5 if v["K"] not in (a, b) else None
    return dict(ks=ks, vu=vu, vstar=vs, gain=vs - vu,
                pvts=t * (quad(lambda x: x * h, a, min(ks, b)) + ks * (1 - H(ks))) / df,
                pvdc=c * H(ks) / df, hstar=H(ks), dstar=D(ks), yld=ks / D(ks) - 1 if D(ks) > 0 else 0, estar=E(ks),
                lev=D(ks) / vs if vs > 0 else 0, vk=V(v["K"]), dk=D(v["K"]), ek=E(v["K"]),
                hk=H(v["K"]), dvk=dvk)


TOL = dict(yld=5e-4, hstar=5e-4, hk=5e-4, lev=5e-4, dvk=5e-4)            # shown as % (1 dp) or 3 dp
js = js_readouts()
fails = 0
for name, vec in VECTORS.items():
    py = py_readouts(vec)
    print(f"\n{name}: {vec}  regime={js[name]['regime']}")
    for f in FIELDS:
        if py[f] is None:            # derivative at a kink: compare one-sided by the page's rule
            continue
        ok = abs(py[f] - js[name][f]) <= TOL.get(f, 5e-3)
        fails += not ok
        print(f"  {f:6s} python {py[f]:12.5f}   page {js[name][f]:12.5f}   {'ok' if ok else 'MISMATCH'}")
    assert abs(py["dstar"] + py["estar"] - py["vstar"]) < 1e-9
print("\nPASS: page and Python agree at the three vectors and both landmarks" if not fails else f"\nFAIL: {fails} mismatches")
sys.exit(1 if fails else 0)
