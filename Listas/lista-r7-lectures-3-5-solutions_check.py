"""Numeric checks for Listas/lista-r7-lectures-3-5-solutions.tex.

Covers the exercises written in that file: 3, 9, 10, 12.
The other sixteen are checked in the topic scripts:
  lista-topic3-asymmetric-information-solutions_check.py   -> R7 1, 5, 6, 11, 19, 20 (topic3 EX 1, 4, 7, 8, 13, 14)
  lista-topic4-moral-hazard-overhang-solutions_check.py     -> R7 2, 4, 7, 8, 14, 16, 17, 18 (topic4 EX 1, 2, 6, 7, 12, 13, 14, 15)
  lista-topic5-nonverifiable-income-termination-solutions_check.py -> R7 13, 15 (topic5 EX 3, 10)

Run: python -I Listas/lista-r7-lectures-3-5-solutions_check.py  -> PASS <n> checks
"""
import math

N = 0


def chk(label, got, want, tol=1e-4):
    """Assert |got - want| <= tol (absolute; default matches 4-decimal printing); count it."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a printed inequality holds; count it."""
    global N
    assert cond, label
    N += 1


# --- Ex 3: Amaro 3.1.5 #7 (illustrative numbers) -----------------------------------
F = 100
chk("e3 E safe", 120 - F, 20)
chk("e3 E risky", 0.5 * (200 - F), 50)
chk("e3 debt risky", 0.5 * 100 + 0.5 * 20, 60)
chk("e3 transfer", 100 - 60, 40)
chk("e3 value loss", 120 - (0.5 * 200 + 0.5 * 20), 10)
chk("e3 convert threshold good state", F / 200, 0.5)
chk("e3 convert threshold safe", F / 120, 0.8333)
gam_min = 1 - 20 / 100  # 20 >= 100(1-gamma)
chk("e3 gamma*", gam_min, 0.8)
g = 0.82
chk("e3 E risky gamma", 0.5 * (1 - g) * 200, 18)
chk("e3 safe no conversion", g * 120, 98.4)
ok("e3 no conversion safe", g * 120 < F)
ok("e3 safe preferred", 20 > 0.5 * (1 - g) * 200)
X, J, Y, K = 90, 20, 28, 95
chk("e3 NPV no call", (X + Y - F) - J, -2)
chk("e3 Kmax", X + Y - J, 98)
chk("e3 NPV with call", X + Y - K - J, 3)
chk("e3 debt gain", K - X, 5)
chk("e3 project NPV", Y - J, 8)

# --- Ex 9: GT 16.3 ---------------------------------------------------------------
L, XA, Bh, Bl = 120, 135, 161, 69
chk("e9 PV B", 0.5 * Bh + 0.5 * Bl, 115)
ok("e9 ranking", XA > L > 0.5 * Bh + 0.5 * Bl)
debt_ahead = 100 + 40 + 20.50
chk("e9 debt ahead", debt_ahead, 160.50)
chk("e9 E_A", max(XA - debt_ahead, 0), 0)
chk("e9 E_B", 0.5 * max(Bh - debt_ahead, 0) + 0.5 * max(Bl - debt_ahead, 0), 0.25)
JJ_B = 0.5 * min(max(Bh - 100, 0), 60.50) + 0.5 * min(max(Bl - 100, 0), 60.50) - 20
chk("e9 JJ under B", JJ_B, 10.25)
JJ_A = min(max(XA - 100, 0), 60.50) - 20
chk("e9 JJ under A", JJ_A, 15)
sen_B = 20 + 0.5 * min(Bh, 100) + 0.5 * min(Bl, 100)
chk("e9 senior under B", sen_B, 104.5)
chk("e9 sum B", sen_B + JJ_B + 0.25, 115)
chk("e9 sum A", 120 + JJ_A + 0, 135)
chk("e9 senior loss", 120 - sen_B, 15.5)
chk("e9 value destroyed", 120 - 115, 5)

# --- Ex 10: Myers (1977), V(s)=s, s'=100, I=40 ------------------------------------
sp, I = 100.0, 40.0


def integ(f, a, b, n=200000):
    """Midpoint rule for int_a^b f(s) ds."""
    h = (b - a) / n
    return h * sum(f(a + (k + 0.5) * h) for k in range(n))


q = 1 / sp
VE = integ(lambda s: q * (s - I), I, sp)
chk("e10 VE", VE, 18)
P = 20.0
VD = integ(lambda s: q * (s - I), I + P, sp)
chk("e10 VD(20)", VD, 16)
chk("e10 VD closed", ((sp - I) ** 2 - P**2) / 200, 16)
chk("e10 loss", integ(lambda s: q * (s - I), I, I + P), 2)
chk("e10 loss closed", P**2 / 200, 2)
D = lambda P: P * (sp - I - P) / sp
chk("e10 D(20)", D(20), 8)
chk("e10 E(20)", integ(lambda s: q * (s - I - P), I + P, sp), 8)
chk("e10 D+E", D(20) + 8, 16)
Pstar = max((D(i / 1000), i / 1000) for i in range(0, 60001))[1]
chk("e10 P*", Pstar, 30)
chk("e10 D(30)", D(30), 9)
chk("e10 loss at P*", 30**2 / 200, 4.5)
# dVD/dP = -q P / V'(s_b) (V' = 1) by finite difference
h = 1e-4
dVD = (((sp - I) ** 2 - (P + h) ** 2) - ((sp - I) ** 2 - (P - h) ** 2)) / 200 / (2 * h)
chk("e10 dVD/dP", dVD, -q * P)

# --- Ex 12: Tirole 3.3, pH=0.8, R=2 ------------------------------------------------
pH, R = 0.8, 2.0
ok("e12 pH R > 1", pH * R > 1)
ok("e12 pH^2 R < 4", pH**2 * R < 4)
ok("e12 pH^2 R < 2", pH**2 * R < 2)
Dn = lambda x: x * (pH * R - x) / R
Nf = lambda x: x * x / (2 * R) + R / 2
Vf = lambda x: pH * x + R / 2 - x * x / (2 * R)
Q = lambda x: 1 - Dn(x)
chk("e12 Q identity", Q(1.1), 1 - pH * 1.1 + 1.1**2 / R, tol=1e-12)
chk("e12 V = N + D", Vf(1.1), Nf(1.1) + Dn(1.1), tol=1e-12)
# (ii)
chk("e12 B* cap", pH * R / 2, 0.8)
chk("e12 rl cap", R - (pH * R / 2) / pH, 1.0)
chk("e12 D at cap", Dn(0.8), 0.32)
chk("e12 k at cap", 1 / (1 - Dn(0.8)), 1.4706)
chk("e12 debt cap", 1 / (1 - Dn(0.8)) - 1, 0.4706)
cap_grid = max((Dn(i / 100000), i / 100000) for i in range(0, 160001))[1]
chk("e12 argmax D", cap_grid, 0.8)
# (iii)
U = lambda x: Nf(x) / Q(x) - 1  # per unit of A
xs = ((1 - R) + math.sqrt((1 - R) ** 2 + pH**2 * R**2)) / pH
chk("e12 sqrt arg", (1 - R) ** 2 + pH**2 * R**2, 3.56)
chk("e12 B* opt", xs, 1.1085)
grid = max((U(i / 100000), i / 100000) for i in range(80000, 160001))[1]
chk("e12 grid argmax", grid, xs, tol=2e-5)
gpoly = lambda x: -pH / 2 * x * x + (1 - R) * x + pH * R * R / 2
chk("e12 g(B*)=0", gpoly(xs), 0, tol=1e-12)
# g equals R(N'Q - N Q') at arbitrary points
for x in (0.5, 1.0, 1.4):
    chk(f"e12 g identity x={x}", R * ((x / R) * Q(x) - Nf(x) * (2 * x / R - pH)), gpoly(x), tol=1e-12)
ok("e12 bounds", pH * R / 2 < xs < pH * R)
ok("e12 g>0 at pHR/2", gpoly(pH * R / 2) > 0)
ok("e12 g<0 at pHR", gpoly(pH * R) < 0)
chk("e12 rl opt", R - xs / pH, 0.6144)
chk("e12 D opt", Dn(xs), 0.2724)
chk("e12 k opt", 1 / Q(xs), 1.3744)
chk("e12 U opt", U(xs), 0.7966)
chk("e12 U at pHR/2", U(0.8), 0.7059)
chk("e12 U at pHR", U(1.6), 0.64)
chk("e12 U = (V-1)k", (Vf(xs) - 1) / Q(xs), U(xs), tol=1e-12)
# book's objective V*k has a different maximizer, also inside the bounds
xb = max((Vf(i / 100000) / Q(i / 100000), i / 100000) for i in range(80000, 160001))[1]
chk("e12 book objective argmax", xb, 0.947, tol=5e-4)
ok("e12 book argmax in bounds", pH * R / 2 < xb < pH * R)
# (iv)
kiv = 1 / (1 - pH * pH * R + (pH * R) ** 2 / (2 * R))
chk("e12 iv denominator", 1 - 1.28 + 0.64, 0.36)
chk("e12 iv k", kiv, 2.7778)
chk("e12 iv V", Vf(pH * R), 1.64)
chk("e12 iv U", (Vf(pH * R) - 1) * kiv, 1.7778)
chk("e12 iv k closed", 1 / (1 - pH**2 * R / 2), kiv, tol=1e-12)
inv = lambda x: pH * x - x * x / (2 * R)
xiv = max((inv(i / 100000), i / 100000) for i in range(0, 200001))[1]
chk("e12 iv argmax investors' income", xiv, pH * R)
chk("e12 iv entrepreneur gets E[B] I", (R / 2) * kiv - 1, (Vf(pH * R) - 1) * kiv, tol=1e-12)

print(f"PASS {N} checks")
