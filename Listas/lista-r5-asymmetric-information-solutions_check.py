"""Numeric checks for Listas/lista-r5-asymmetric-information-solutions.tex.

Covers the exercises written in that file: 2, 4, 8, 11, 12, 15.
Exercises 1, 3, 5, 6, 7, 9, 10, 13, 14 are Topic 3 exercises 5, 2, 3, 6, 11, 9, 10, 15, 12
and are checked in lista-topic3-asymmetric-information-solutions_check.py.

Run: python -I Listas/lista-r5-asymmetric-information-solutions_check.py  -> PASS <n> checks
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


# --- Ex 2: GT 19.2 (Example 19.6 numbers; perpetuity values are our illustration) ---
chk("e2 good coverage", 50 / 40, 1.25)
chk("e2 bad coverage", 30 / 40, 0.75)
e2_VG, e2_VB, e2_w = 55 / 0.10, 27.5 / 0.10, 0.2
chk("e2 VG", e2_VG, 550)
chk("e2 VB", e2_VB, 275)
chk("e2 C threshold", e2_w / (1 - e2_w) * (e2_VG - e2_VB), 68.75)
# credibility condition (1-w)C >= w(VG-VB) at the threshold, and good-type gain w(VG-VB) > 0
ok("e2 good gains", e2_w * (e2_VG - e2_VB) > 0)

# --- Ex 4: Berk 17.14-17.18 (AMC) ---------------------------------------------
EV0, EVH, EVL, C, N0 = 400, 600, 200, 100, 10
P0 = (EV0 + C) / N0
chk("e4 P0", P0, 50)
n = C / P0
chk("e4 n before", n, 2)
chk("e4 N1", N0 - n, 8)
chk("e4 before H", EVH / (N0 - n), 75)
chk("e4 before L", EVL / (N0 - n), 25)
PnH, PnL = (EVH + C) / N0, (EVL + C) / N0
chk("e4 news H", PnH, 70)
chk("e4 news L", PnL, 30)
chk("e4 nH", C / PnH, 1.4286)
chk("e4 N1H", N0 - C / PnH, 8.5714)
chk("e4 after H", EVH / (N0 - C / PnH), 70)
chk("e4 nL", C / PnL, 3.3333)
chk("e4 N1L", N0 - C / PnL, 6.6667)
chk("e4 after L", EVL / (N0 - C / PnL), 30)
chk("e4 gain early (good)", EVH / (N0 - n) - EVH / (N0 - C / PnH), 5)
chk("e4 gain late (bad)", EVL / (N0 - C / PnL) - EVL / (N0 - n), 5)
chk("e4 pitfall H", (EVH + C) / 8, 87.5)
chk("e4 pitfall L", (EVL + C) / 8, 37.5)

# --- Ex 8: Amaro 3.2.6 #1 (Ross 1977) --------------------------------------------
g0, g1, L, c, t = 1.0, 1.0, 10.0, 1.0, 2.0
Bt = g0 / (4 * g1 * L) * (t**2 - c**2)
chk("e8 B(2)", Bt, 0.075)
a = lambda B: math.sqrt(4 * g1 * L * B / g0 + c**2)
chk("e8 a(B)", a(Bt), 2)
chk("e8 bankruptcy prob", Bt / t, 0.0375)
chk("e8 expected penalty", g1 * L * Bt / t, 0.375)
# truthful B maximizes M(B;t) = g0 a(B)/2 + g1 (t/2 - L B/t) over a grid in [0, t)
M = lambda B: 0.5 * g0 * a(B) + g1 * (0.5 * t - L * B / t)
best = max((M(i / 100000), i / 100000) for i in range(0, 200000))[1]
chk("e8 argmax M is B(t)", best, Bt, tol=1e-4)
# dM/dB = g1 L (1/a - 1/t): sign checks either side
dM = lambda B: g1 * L * (1 / a(B) - 1 / t)
ok("e8 dM>0 below", dM(0.05) > 0)
ok("e8 dM<0 above", dM(0.10) < 0)
# limits: gamma0 = 0 -> B = 0; gamma1 -> 0 -> B -> infinity
chk("e8 gamma0=0", 0 / (4 * g1 * L) * (t**2 - c**2), 0)
ok("e8 gamma1 small", 1.0 / (4 * 1e-9 * L) * (t**2 - c**2) > 1e6)

# --- Ex 11: Tirole 6.9 (herding) ---------------------------------------------------
R, I, q, p, r, th, al = 10, 5, 0.55, 0.9, 0.6, 0.5, 0.5
ok("e11 qR>I", q * R > I)
ok("e11 p>max(q,r)", p > max(q, r))
m = al * p + (1 - al) * q
chk("e11 m", m, 0.725)
chk("e11 Rb1", R - I / m, 3.1034)
piF = th * p + (1 - th) * r
chk("e11 piF", piF, 0.75)
RbF, RbU = R - I / piF, R - I / q
chk("e11 RbF", RbF, 3.3333)
chk("e11 RbU", RbU, 0.9091)
chk("e11 r RbF", r * RbF, 2.0)
chk("e11 p RbU", p * RbU, 0.8182)
ok("e11 herding condition", r * RbF >= p * RbU)
ok("e11 piF>q", piF > q)
Uh = (1 - al) * q * RbU + al * piF * RbF
chk("e11 U herd part U", (1 - al) * q * RbU, 0.25)
chk("e11 U herd part F", al * piF * RbF, 1.25)
chk("e11 U herd", Uh, 1.5)
chk("e11 U herd closed form", ((1 - al) * q + al * th * p + al * (1 - th) * r) * R - I, 1.5)
chk("e11 U no obs", m * R - I, 2.25)
chk("e11 loss", al * (1 - th) * (p - r) * R, 0.75)
chk("e11 loss = difference", (m * R - I) - Uh, 0.75)

# --- Ex 12: Amaro 3.2.6 #5 (issue costs) -----------------------------------------
Sa, E, cst, bbar = 100.0, 10.0, 1.0, 10.0
bs = (-218 + math.sqrt(218**2 + 4 * 120)) / 2
chk("e12 sqrt arg", 218**2 + 4 * 120, 48004)
chk("e12 b*", bs, 0.5491)
Pp = Sa + (bs + bbar) / 2 - cst
chk("e12 P'", Pp, 104.27, tol=5e-3)
chk("e12 fixed point", (E + cst) * Sa / Pp - E, bs, tol=1e-9)
ok("e12 P'>P", Pp > Sa)
chk("e12 bound", (E + cst) / E * Sa, 110)
ok("e12 bound holds", Pp < (E + cst) / E * Sa)
ok("e12 c=0 all issue", E * Sa / (Sa + bbar / 2) - E < 0)
# symmetric-information rule (b-c)(S+a+E+b) >= 0 matches P'(E+b) >= (S+a)(E+c) with P'=S+a+b-c
for bb in (0.3, 1.0, 2.5):
    lhs = (Sa + bb - cst) * (E + bb) - Sa * (E + cst)
    chk(f"e12 symm identity b={bb}", lhs, (bb - cst) * (Sa + E + bb), tol=1e-9)

# --- Ex 15: Tirole 6.3 (reputational capital) ------------------------------------
pH, pL, p1H, p1L, R, I, A, b, B, al = 0.9, 0.5, 0.9, 0.1, 10.0, 8.0, 1.0, 0.2, 2.4, 0.5
dp, d1, one = pH - pL, p1H - p1L, I - A
mm = lambda x: pH - (1 - x) * dp
chk("e15 dp", dp, 0.4)
chk("e15 d1", d1, 0.8)
chk("e15 R-b/dp", R - b / dp, 9.5)
chk("e15 pH(R-b/dp)", pH * (R - b / dp), 8.55)
chk("e15 pH(R-B/dp)", pH * (R - B / dp), 3.6)
ok("e15 (i) window", pH * (R - b / dp) > one > max(pH * (R - B / dp), pL * R))
oaS = (1 - al) * p1L / ((1 - al) * p1L + al * p1H)
aS = 1 - oaS
chk("e15 1-alphaS", oaS, 0.1)
chk("e15 m(alphaS)", mm(aS), 0.86)
chk("e15 m(alpha)", mm(al), 0.7)
chk("e15 m(alpha)(9.5)", mm(al) * 9.5, 6.65)
chk("e15 m(alphaS)(9.5)", mm(aS) * 9.5, 8.17)
ok("e15 second assumption", mm(al) * (R - b / dp) < one < mm(aS) * (R - b / dp))
RbS = R - one / mm(aS)
chk("e15 Rb(alphaS)", RbS, 1.8605)
chk("e15 d1 A", d1 * A, 0.8)
chk("e15 d1(pL RbS + B)", d1 * (pL * RbS + B), 2.6642)
ok("e15 first assumption", b < d1 * A < B < d1 * (pL * RbS + B))
ok("e15 consistency d1 > dp/pH", d1 > dp / pH)
ok("e15 dp1 = dp infeasible", not (dp > dp / pH))
ok("e15 Rb(alpha) < B/dp", RbS < B / dp)
ok("e15 pH R > I", pH * R > I)
ok("e15 pL R + B < I", pL * R + B < I)
Rbs = B * (1 - d1) / (d1 * pL)
chk("e15 Rb*", Rbs, 1.2)
ok("e15 interior Rb* >= b/dp", Rbs >= b / dp)
ok("e15 interior jump", d1 * (pL * b / dp + B) <= B)
mp = one / (R - Rbs)
chk("e15 m(alpha'S)", mp, 0.79545)
oap = (pH - mp) / dp
chk("e15 1-alpha'S", oap, 0.26136)
chk("e15 alpha'S", 1 - oap, 0.73864)
piB = al * p1H / (1 - al) * oap / (1 - oap)
chk("e15 piB", piB, 0.31846)
y = (piB - p1L) / d1
chk("e15 y", y, 0.27308)
# Bayes' rule reproduces alpha'S from y, and the B-type is indifferent there
post = al * p1H / (al * p1H + (1 - al) * (p1L + y * d1))
chk("e15 Bayes check", post, 1 - oap, tol=1e-9)
chk("e15 indifference", d1 * (pL * (R - one / mm(post)) + B), B, tol=1e-9)
ahat = 1 - (pH - one / (R - b / dp)) / dp
chk("e15 alphahat", ahat, 0.59211)
ok("e15 ordering", al < ahat < 1 - oap < aS)
chk("e15 b-type reinvests", pH * Rbs, 1.08)
ok("e15 pH Rb* >= A", pH * Rbs >= A)
ok("e15 B-type reinvests", pL * Rbs + B >= A)

print(f"PASS {N} checks")
