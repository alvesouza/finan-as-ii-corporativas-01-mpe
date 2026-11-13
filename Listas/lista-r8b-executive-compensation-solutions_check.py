"""Numeric checks for Listas/lista-r8b-executive-compensation-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-r8b-executive-compensation-solutions_check.py  -> PASS <n> checks
Symbolic results are asserted at a parameter point that satisfies each exercise's assumptions.
Tolerance: 1e-6 absolute unless stated.
"""
import math

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a strict inequality or logical condition; count the check."""
    global N
    assert cond, label
    N += 1


def bisect(g, lo, hi, it=200):
    """Root of g on [lo, hi] by bisection; g(lo) and g(hi) must differ in sign."""
    glo = g(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        if (g(mid) > 0) == (glo > 0):
            lo, glo = mid, g(mid)
        else:
            hi = mid
    return (lo + hi) / 2


# --- Ex 1: Ross CQ 1.16 (Irani pay) and G&T Jensen-Murphy sensitivity
chk("1 average yearly pay 2003-07", 550 / 5, 110)
chk("1 2007 pay vs average", 54.4 / 110, 0.494545, 1e-6)
chk("1 value increase that 54.4m is 1% of", 54.4 / 0.01, 5440)
chk("1 Jensen-Murphy $ per $1000", 30_000 / 10_000_000 * 1000, 3)
chk("1 G&T IBM: 1% of 10% of 100bn (in $m)", 0.01 * 0.10 * 100_000, 100)

# --- Ex 2: Berk Ch. 22 Problem 3 (GreenFrame)
e2_loss = 0.03 * 50
chk("2 CEO share of value lost", e2_loss, 1.5)
chk("2 CEO net gain", 5 - e2_loss, 3.5)
ok("2 CEO better off", 5 - e2_loss > 0)
chk("2 stake that makes him indifferent", 5 / 50, 0.10)
chk("2 Berk text: 1% of 100m", 0.01 * 100, 1)
chk("2 value destruction that offsets 5m at 3%", 5 / 0.03, 166.666667, 1e-6)

# --- Ex 3: G&T 18.1 (RJR baking plan; Jensen-Meckling jet)
chk("3 RJR pretax return", 148 / 2800, 0.0528571, 1e-6)
chk("3 manager's cost of a 1m jet at 5%", 0.05 * 1_000_000, 50_000)

# --- Ex 4: Higgins 1.2 (Braintree)
chk("4 ROE", 100 / 5000, 0.02)
chk("4 ROA", 100 / 7000, 0.0142857, 1e-6)
chk("4 liabilities", 7000 - 5000, 2000)
chk("4 equity charge at 10%", 0.10 * 5000, 500)
chk("4 economic profit", 100 - 0.10 * 5000, -400)
chk("4 Polaris equity charge", 0.10 * 1434, 143.4)
chk("4 Polaris economic earnings", 414 - 143, 271)

# --- Ex 5: G&T 18.7 (Example 18.5, options struck at 20)
chk("5 Jack option payoff", max(0, 30 - 20), 10)
chk("5 Peggy option payoff", max(0, 15 - 20), 0)

# --- Ex 6: G&T 18.9, Tirole-style IC illustration: bonus >= B / (likelihood gap)
e6_B = 1.0
e6_bw = e6_B / (0.6 - 0.4)
e6_be = e6_B / (0.9 - 0.3)
chk("6 bonus on wins", e6_bw, 5)
chk("6 expected pay on wins", 0.6 * e6_bw, 3)
chk("6 bonus on expert rating", e6_be, 1.6666667, 1e-6)
chk("6 expected pay on rating", 0.9 * e6_be, 1.5)
chk("6 saving from the more informative signal", 0.6 * e6_bw - 0.9 * e6_be, 1.5)

# --- Ex 7: G&T 18.6, filtering a common (oil-price) factor with R^2 = 0.7
chk("7 residual variance share", 1 - 0.7, 0.3, 1e-12)
chk("7 slope multiple at equal pay risk", 1 / math.sqrt(0.3), 1.8257419, 1e-6)

# --- Ex 8: G&T 18.3 (High Tech / Super Tech)
chk("8 Jacobs stake value", 0.51 * 50, 25.5)
chk("8 option 1: Jacobs share after issue", 25.5 / 75, 0.34)
ok("8 option 1 loses majority", 25.5 / 75 < 0.5)
chk("8 option 2: look-through share of Super Tech", 0.51 * 0.55, 0.2805)
chk("8 option 2: gain to Jacobs of shifting $1 to High Tech", 0.51 - 0.51 * 0.55, 0.2295)
chk("8 option 2: Super Tech post-money", 25 / 0.45, 55.555556, 1e-6)
chk("8 option 2: High Tech stake value", 0.55 * 25 / 0.45, 30.555556, 1e-6)
chk("8 option 1: new project share of firm", 25 / 75, 0.333333, 1e-6)

# --- Ex 9: G&T 18.8 (Cybertex), V = 100, repurchase at fair price
e9_E0, e9_E1 = 50, 20
e9_m = 0.01 * e9_E0
chk("9 manager's equity value", e9_m, 0.5)
chk("9 buyback size", 80 - 50, 30)
chk("9 ownership after recap", e9_m / e9_E1, 0.025)
chk("9 cost per $1 wasted, before", 0.01, 0.01)
chk("9 multiple of skin in the game", (e9_m / e9_E1) / 0.01, 2.5)
chk("9 D/E before and after", (50 / 50) * 4, 80 / 20)

# --- Ex 10: Amaro 3.1.5 #3, U = alpha*(Vbar - F) + 2c*sqrt(F), c = 0.5, Vbar = 100
def e10_F(a, c=0.5):
    """Optimal perks F*(alpha) = (c/alpha)^2 from h'(F) = c/sqrt(F) = alpha."""
    return (c / a) ** 2


chk("10 F* at alpha 0.10", e10_F(0.10), 25)
chk("10 V at alpha 0.10", 100 - e10_F(0.10), 75)
chk("10 FOC at alpha 0.10", 0.5 / math.sqrt(25), 0.10)
chk("10 F* at alpha 0.20", e10_F(0.20), 6.25)
chk("10 effective alpha with options", 0.10 + 0.10 * 0.5, 0.15)
chk("10 F* with options", e10_F(0.15), 11.111111, 1e-6)
chk("10 V with options", 100 - e10_F(0.15), 88.888889, 1e-6)
chk("10 value gain", e10_F(0.10) - e10_F(0.15), 13.888889, 1e-6)
for a in (0.05, 0.1, 0.15, 0.3):
    h = 1e-6
    ok(f"10 dF/dalpha < 0 at {a}", (e10_F(a + h) - e10_F(a - h)) / (2 * h) < 0)
    chk(f"10 dF/dalpha = 1/h''(F) at {a}", (e10_F(a + h) - e10_F(a - h)) / (2 * h),
        1 / (-0.5 * 0.5 * e10_F(a) ** -1.5), 1e-3)

# --- Ex 11: Amaro 3.1.5 #4, slope df/dw = R_P/(R_P + R_A), checked on a non-CARA agent
chk("11 slope with R_P=1, R_A=3", 1 / (1 + 3), 0.25)
# principal U = -exp(-x) (R_P = 1), agent G = ln f (R_A = 1/f), lambda = 1:
# (3.4): exp(-(w - f)) = 1/f  <=>  f*exp(f - w) = 1
def e11_f(w):
    return bisect(lambda f: f * math.exp(f - w) - 1, 1e-9, w + 5)


for w in (2.0, 5.0, 10.0):
    f = e11_f(w)
    h = 1e-5
    slope = (e11_f(w + h) - e11_f(w - h)) / (2 * h)
    chk(f"11 slope = R_P/(R_P+R_A) at w={w}", slope, 1 / (1 + 1 / f), 1e-5)
    ok(f"11 0 < slope < 1 at w={w}", 0 < slope < 1)

# --- Ex 12: Amaro 3.1.5 #6, CARA: f = delta/(alpha+delta) w + ln(lambda)/(alpha+delta)
e12_d, e12_a = 2.0, 6.0
for lam in (1.0, math.e):
    for w in (0.0, 4.0, 10.0):
        f = e12_d / (e12_a + e12_d) * w + math.log(lam) / (e12_a + e12_d)
        chk(f"12 (3.4) holds lam={lam:.3f} w={w}", math.exp(-e12_d * (w - f)), lam * math.exp(-e12_a * f), 1e-9)
        # similarity (3.5): U(w - f) = (alpha*lambda/delta) G(f), b = 0
        Uv = -(1 / e12_d) * math.exp(-e12_d * (w - f))
        Gv = -(1 / e12_a) * math.exp(-e12_a * f)
        chk(f"12 (3.5) holds lam={lam:.3f} w={w}", Uv, e12_a * lam / e12_d * Gv, 1e-9)
chk("12 slope", e12_d / (e12_a + e12_d), 0.25)
chk("12 intercept with lambda = e", 1 / 8, 0.125)

# --- Ex 13: Tirole 3.10
pH, pL, R, B, I = 0.9, 0.5, 10, 0.8, 8
dp = pH - pL
ok("13 (3.1)", pH * R - I > 0)
ok("13 (3.2)", pL * R - I + B < 0)
chk("13 B/dp", B / dp, 2)
PH = pH * (R - B / dp)
chk("13 pledgeable, high-powered", PH, 7.2)
xhat = pH * B / (dp ** 2 * R)
chk("13 x-hat", xhat, 0.45)


def PLow(x):
    return (x * pL + (1 - x) * pH) * R


def NPV1(x):
    return pH * R - I + (1 - x) * B


def NPV2(x):
    return x * (pL * R + B) + (1 - x) * (pH * R + B) - I


chk("13 pledgeable low-powered x=0.2", PLow(0.2), 8.2)
chk("13 PLow = pH R - x dp R", PLow(0.2), pH * R - 0.2 * dp * R)
chk("13 NPV1 x=0.2", NPV1(0.2), 1.64)
chk("13 NPV2 x=0.2", NPV2(0.2), 1.0)
chk("13 NPV gap = x(dp R - B)", NPV1(0.2) - NPV2(0.2), 0.2 * (dp * R - B))
ok("13 dp R > B", dp * R > B)
ok("13 x=0.2, I-A=7.6: (1) fails", PH < 7.6)
ok("13 x=0.2, I-A=7.6: (2) holds", PLow(0.2) >= 7.6)
chk("13 pledgeable low-powered x=0.6", PLow(0.6), 6.6)
ok("13 x=0.6, I-A=7: (1) holds", PH >= 7)
ok("13 x=0.6, I-A=7: (2) fails", PLow(0.6) < 7)
for x in (0.1, 0.3, 0.44, 0.46, 0.7):
    ok(f"13 PLow > PH iff x < xhat (x={x})", (PLow(x) > PH) == (x < xhat))
# (ii) menu: congruent type takes dissonant scheme (2,0) unless her own pays >= pH*2
chk("13 congruent's value of the dissonant scheme", pH * 2 + (1 - pH) * 0, 1.8)

# --- Ex 14: Amaro 3.1.5 #5, discrete Shavell example, G = sqrt(f), c = 1, k = 4
p_H, p_L, c, k = 0.8, 0.4, 1.0, 4.0
uL = k + c - p_H * c / (p_H - p_L)
uH = uL + c / (p_H - p_L)
chk("14 u_L", uL, 3)
chk("14 u_H", uH, 5.5)
chk("14 f_L", uL ** 2, 9)
chk("14 f_H", uH ** 2, 30.25)
chk("14 IR", p_H * uH + (1 - p_H) * uL - c, k)
chk("14 IC binding", (p_H - p_L) * (uH - uL), c)
chk("14 expected pay", p_H * uH ** 2 + (1 - p_H) * uL ** 2, 26)
chk("14 first-best pay", (k + c) ** 2, 25)
chk("14 agency cost", p_H * uH ** 2 + (1 - p_H) * uL ** 2 - (k + c) ** 2, 1)
inv_GH, inv_GL = 2 * uH, 2 * uL   # 1/G'(f) = 2 sqrt(f)
chk("14 1/G' at f_H", inv_GH, 11)
chk("14 1/G' at f_L", inv_GL, 6)
lr_H = (p_H - p_L) / p_H
lr_L = ((1 - p_H) - (1 - p_L)) / (1 - p_H)
psi = (inv_GH - inv_GL) / (lr_H - lr_L)
lam = inv_GH - psi * lr_H
chk("14 likelihood term H", lr_H, 0.5)
chk("14 likelihood term L", lr_L, -2)
chk("14 psi", psi, 2)
chk("14 lambda", lam, 10)
chk("14 lambda = E_H[1/G']", p_H * inv_GH + (1 - p_H) * inv_GL, lam)
ok("14 psi > 0 (IC binds)", psi > 0)
chk("14 expected output", p_H * 40 + (1 - p_H) * 10, 34)
# risk-neutral agent: sell the firm, f = theta - K
K = p_H * 40 + (1 - p_H) * 10 - c - k
chk("14 fixed rent K", K, 29)
chk("14 agent EU", p_H * (40 - K) + (1 - p_H) * (10 - K) - c, k)
ok("14 agent prefers effort", (p_H - p_L) * (40 - 10) >= c)
chk("14 f_L negative (no limited liability)", 10 - K, -19)

# --- Ex 15: Tirole 7.9
def npv(a, rH, qH, R, L, I, zr, zq):
    return a * (L + zr * (rH * R - L)) + (1 - a) * (L + zq * (qH * R - L)) - I


def pledge(a, rH, qH, R, L, b, zr, zq, Pi):
    """Pledgeable income; Pi = q-type's expected rent z^q q_H R_b^q + (1-z^q) T^q."""
    return a * (L + zr * (rH * (R - b) - L)) + (1 - a) * (zq * qH * R + (1 - zq) * L - Pi)


# Case 2: q_H R < L
a, rH, qH, dP, Bb, R, L, tau, I, A = 0.5, 0.95, 0.3, 0.2, 0.6, 10, 3.5, 0.1, 5, 0.5
b = Bb / dP
X = R - b
pHb = a * rH + (1 - a) * qH
chk("15c2 b", b, 3)
ok("15c2 q_H R < L", qH * R < L)
ok("15c2 (7.11) structure", qH * X < L < rH * X)
ok("15c2 (7.10)", I - A > max(pHb * X, L))
ok("15c2 (7.11)", I - A < a * rH * X + (1 - a) * L)
ok("15c2 q_L >= 0", qH - dP >= 0)
T = 1 * (qH - tau) * b
chk("15c2 T*", T, 0.6)
P_gp = pledge(a, rH, qH, R, L, b, 1, 0, T)
chk("15c2 P with golden parachute", P_gp, 4.775)
chk("15c2 P linear form", P_gp, L + 1 * (a * (rH * X - L) - (1 - a) * (qH - tau) * b))
ok("15c2 funded", P_gp >= I - A)
chk("15c2 NPV with golden parachute", npv(a, rH, qH, R, L, I, 1, 0), 1.5)
th = (qH - tau) / qH
chk("15c2 theta", th, 2 / 3)
P_ng = pledge(a, rH, qH, R, L, b, 1, th, th * qH * b)
chk("15c2 P without parachute (z^q = theta)", P_ng, 4.6083333, 1e-6)
chk("15c2 NPV without parachute", npv(a, rH, qH, R, L, I, 1, th), 1.3333333, 1e-6)
chk("15c2 NPV gain of parachute", npv(a, rH, qH, R, L, I, 1, 0) - npv(a, rH, qH, R, L, I, 1, th),
    (1 - a) * th * (L - qH * R))
chk("15c2 P without manipulation", pledge(a, rH, qH, R, L, b, 1, 0, 0), 5.075)
ok("15c2 r-type does not claim q", T < rH * b)
# grid: over (z^r, z^q) and minimal rent, the best funded contract has z^q = 0 and rent = T*
best = None
for i in range(101):
    for j in range(101):
        zr, zq = i / 100, j / 100
        Pi = max(zr * (qH - tau) * b, zq * qH * b)
        if pledge(a, rH, qH, R, L, b, zr, zq, Pi) >= I - A - 1e-12:
            v = npv(a, rH, qH, R, L, I, zr, zq)
            if best is None or v > best[0] + 1e-12:
                best = (v, zr, zq, Pi)
chk("15c2 grid optimum NPV", best[0], 1.5)
chk("15c2 grid optimum z^r", best[1], 1)
chk("15c2 grid optimum z^q", best[2], 0)
chk("15c2 grid optimum rent = T*", best[3], 0.6)

# Case 1: q_H R > L
a, rH, qH, dP, Bb, R, L, I, A = 0.5, 0.9, 0.5, 0.3, 1.5, 10, 4, 4.5, 0.4
b = Bb / dP
X = R - b
pHb = a * rH + (1 - a) * qH
chk("15c1 b", b, 5)
ok("15c1 (7.9)", qH * R > L)
ok("15c1 (7.11) structure", qH * X < L < rH * X)
ok("15c1 (7.10)", I - A > max(pHb * X, L))
ok("15c1 (7.11)", I - A < a * rH * X + (1 - a) * L)
zstar = (I - A - a * rH * X - (1 - a) * L) / ((1 - a) * (qH * X - L))
chk("15c1 z*", zstar, 0.2)
chk("15c1 (7.12)", pledge(a, rH, qH, R, L, b, 1, zstar, zstar * qH * b), I - A)
chk("15c1 marginal NM relaxation q_H R_b + dT/dz^q", qH * b + (qH * (R - b) - L), qH * R - L)
chk("15c1 = 1", qH * R - L, 1)
for tau, funded in ((0.45, True), (0.1, False)):
    th = 1 - tau / qH
    best = None
    for i in range(101):
        for j in range(101):
            zr, zq = i / 100, j / 100
            Pi = max(zr * (qH - tau) * b, zq * qH * b)
            if pledge(a, rH, qH, R, L, b, zr, zq, Pi) >= I - A - 1e-12:
                v = npv(a, rH, qH, R, L, I, zr, zq)
                if best is None or v > best[0] + 1e-12:
                    best = (v, zr, zq, Pi)
    ok(f"15c1 tau={tau}: funded iff theta <= z*", (best is not None) == funded == (th <= zstar + 1e-12))
    if best:
        chk(f"15c1 tau={tau}: no parachute (rent = z^q q_H b)", best[3], best[2] * qH * b)
        chk(f"15c1 tau={tau}: z^q = z*", best[2], zstar)
chk("15c1 P(1, theta=0.8)", pledge(a, rH, qH, R, L, b, 1, 0.8, 0.8 * qH * b), 3.65)
chk("15c1 P with parachute at (1, z*)", pledge(a, rH, qH, R, L, b, 1, 0.2, 0.4 * b), 3.35)

print(f"PASS {N} checks")
