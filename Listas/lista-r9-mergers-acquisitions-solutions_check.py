"""Numeric checks for Listas/lista-r9-mergers-acquisitions-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-r9-mergers-acquisitions-solutions_check.py  -> PASS <n> checks
Symbolic results are asserted at a parameter point that satisfies the exercise's assumptions.
Default tolerance 1e-6 absolute; looser tolerances are stated where a printed value is rounded.
"""
import math

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a boolean condition (inequality results); count the check."""
    global N
    assert cond, label
    N += 1


def bisect(f, lo, hi, it=200):
    """Root of f on [lo, hi] by bisection; f(lo), f(hi) must differ in sign."""
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


# --- Ex 1: Higgins 9.1 (illustrative numbers in the solution)
chk("1c max premium poorly managed (%)", (140 - 100) / 100 * 100, 40)
chk("1c max premium well managed (%)", (105 - 100) / 100 * 100, 5)
chk("1d gap liquidation-price", 50 - 40, 10)
chk("1e MBO gain per share", 80 - 30, 50)

# --- Ex 2: G&T 20.5 + 20.8
chk("2 riskless debt stable", 100 - 10, 90)
chk("2 riskless debt volatile", 100 - 60, 40)
chk("2 manager share of $1 before", 0.05 * 1, 0.05)
chk("2 manager share of $1 after", 0.15 * 1, 0.15)
chk("2 ratio", 0.15 / 0.05, 3)

# --- Ex 3: Higgins 5.10 (Figure 5.3 read-off values)
e3_before, e3_after = 8.5, 28.5
chk("3 announcement jump (points)", e3_after - e3_before, 20)
e3_day0 = 100 + e3_before + (e3_after - e3_before) / 3
chk("3 index end of day 0 if spread over 3 days", e3_day0, 115.1666667, 1e-6)
e3_ret = (100 + e3_after) / e3_day0 - 1
chk("3 return day 0 close -> day 2 close", e3_ret, 0.115774, 1e-6)
chk("3e expected value of a target share", 0.3 * 75 + 0.6 * 60 + 0.1 * 35, 62)
ok("3e price above bid", 0.3 * 75 + 0.6 * 60 + 0.1 * 35 > 60)

# --- Ex 4: Amaro 7.2.4 #3 (tax shield illustration)
chk("4 PV perpetual tax shield", 0.34 * 600, 204)

# --- Ex 5: Grossman-Hart with toehold theta
e5_v, e5_q, e5_c, e5_th, e5_p = 100, 80, 1, 0.10, 100
e5_book = e5_v - e5_p * (1 - e5_th) - e5_c
chk("5 book profit v - p(1-theta) - c", e5_book, 9)
ok("5 book condition theta > 1 + (c - v)/p", e5_th > 1 + (e5_c - e5_v) / e5_p)
chk("5 threshold theta at p = v is c/v", 1 + (e5_c - e5_v) / e5_p, e5_c / e5_v)
e5_inc = e5_th * (e5_v - e5_q) - e5_c
chk("5 incremental profit at p = v", e5_inc, 1)
chk("5 incremental = book - theta q", e5_book - e5_th * e5_q, e5_inc)
chk("5 no toehold profit at p = v", e5_v - e5_p - e5_c, -1)
e5_pmax = e5_v + (e5_th * (e5_v - e5_q) - e5_c) / (1 - e5_th)
chk("5 highest profitable bid", e5_pmax, 101.1111111, 1e-6)

# --- Ex 6: Higgins 9.3
e6_cost = 60 * 82e6 + 1.46e9
chk("6a equity paid", 60 * 82e6, 4.92e9, 1)
chk("6a cost of acquisition", e6_cost, 6.38e9, 1)
chk("6b value of control", (60 - 33) * 82e6, 2.214e9, 1)
chk("6b premium %", (60 - 33) / 33 * 100, 81.818182, 1e-5)
chk("6 pre-bid equity value", 33 * 82e6, 2.706e9, 1)

# --- Ex 7: Higgins 9.9
e7_PV = 2 * 30
e7_V1, e7_V2 = 1 * 8, 1 * 35
chk("7 P market value", e7_PV, 60)
chk("7 V1 market value", e7_V1, 8)
chk("7 V2 market value", e7_V2, 35)
e7_sh = 3 / 2
chk("7 combined shares max", e7_sh, 1.5)
chk("7 new shares max", e7_sh - 1, 0.5)
chk("7 value new shares", (e7_sh - 1) * 60, 30)
chk("7 premium V1 %", (30 / 8 - 1) * 100, 275)
chk("7 premium V2 %", (30 / 35 - 1) * 100, -14.285714, 1e-5)
chk("7 V2 at market: shares issued", 35 / 60, 0.5833333, 1e-6)
chk("7 V2 at market: EPS", 3 / (1 + 35 / 60), 1.8947368, 1e-6)
chk("7 V2 at market: price", (60 + 35) / (1 + 35 / 60), 60)
chk("7 V1 at max premium: price", (60 + 8) / 1.5, 45.333333, 1e-5)
chk("7 V1 at max premium: P holders lose", 60 - (60 + 8) / 1.5, 14.666667, 1e-5)
chk("7 V1 transfer to V1 holders", 30 - 8, 22)

# --- Ex 8: Hansen uniform (0,100), w = 1.5 v
chk("8 E(w|C) at C = 80", 1.5 * 80 / 2, 0.75 * 80)
e8_gain = lambda C: (C / 100) * (0.75 * C - C)
ok("8 cash gain negative for all C in (0,100]", all(e8_gain(c) < 0 for c in range(1, 101)))
chk("8 cash gain at C = 100", e8_gain(100), -25)
chk("8 beta_min(x) at x = 100", 100 / (100 + 150), 0.4)
chk("8 beta_max(x) at x = 100", 75 / (100 + 75), 0.4285714, 1e-6)
chk("8 crossing x", 3750 / 25, 150)
chk("8 at x = 150 the bounds coincide", 100 / 300 - 75 / 225, 0)
chk("8 acquirer gain x=100, beta=0.4", (1 - 0.4) * (100 + 75) - 100, 5)
e8_g = lambda x, vs: (vs / 100) * ((1 - vs / (x + 1.5 * vs)) * (x + 0.75 * vs) - x)
chk("8 cutoff gain formula", e8_g(100, 100), (100 / 100) * 100 * (0.375 * 100 - 0.25 * 100) / 250)
ok("8 x = 160: no cutoff gives a gain", all(e8_g(160, v) <= 1e-12 for v in range(1, 101)))
ok("8 x = 100: full-acceptance stock deal gains", e8_g(100, 100) > 0)

# --- Ex 9: Fishman (1988), illustration v1, v2 ~ U[0,1], v = 0.6, c2 = 0.02
e9_v, e9_c2 = 0.6, 0.02
e9_w = 1 - math.sqrt(2 * e9_c2)
e9_r = 1 - math.sqrt(6 * e9_c2)
chk("9 w", e9_w, 0.8)
chk("9 r", e9_r, 0.6535898, 1e-6)
ok("9 v < r < w", e9_v < e9_r < e9_w)
e9_pbar = e9_v * e9_v + (e9_r**2 - e9_v**2) / 2 + e9_r * (1 - e9_r)
chk("9 pbar(r)", e9_pbar, 0.62, 1e-9)
chk("9 g(r) > c2", (1 - e9_r) ** 2 / 2, 0.06, 1e-9)

# --- Ex 10: Jegadeesh-Chowdhry, alpha_m = 0.3, ZL = 40, ZH = 80, P = ln
G = lambda pi, a, Z: math.log(pi) * (0.5 * Z - (0.5 - a) * pi)
e10_ZM = 0.4 * 40 + 0.6 * 80
chk("10 ZM", e10_ZM, 64)
chk("10 G(64,.3;80)", G(64, 0.3, 80), 113.1216, 1e-4)
chk("10 G(64,.3;40)", G(64, 0.3, 40), 29.944, 1e-3)
e10_ap = (G(64, 0.3, 80) / math.log(40) - 20) / 40
chk("10 alpha'", e10_ap, 0.26664, 1e-5)
chk("10 high type indifferent", G(40, e10_ap, 80), G(64, 0.3, 80), 1e-9)
chk("10 G(40,a';40)", G(40, e10_ap, 40), 39.3440, 1e-4)
chk("10 book's rounded value 39.337 within 0.01", G(40, e10_ap, 40), 39.337, 0.01)
ok("10 low type strictly better", G(40, e10_ap, 40) > G(64, 0.3, 40))
ok("10 alpha' < alpha_m", e10_ap < 0.3)
chk("10 cost of lower toehold = pi * dalpha (high)", G(40, 0.3, 80) - G(40, e10_ap, 80), 40 * math.log(40) * (0.3 - e10_ap), 1e-9)
chk("10 cost of lower toehold same for low type", G(40, 0.3, 40) - G(40, e10_ap, 40), G(40, 0.3, 80) - G(40, e10_ap, 80), 1e-9)

# --- Ex 11: Tirole 11.1, v = 2, vhat = 3 (vhat - v = 1), what = 2, m = 1 free share per untendered share
e11_v, e11_vh, e11_w, e11_m = 2.0, 3.0, 2.0, 1.0
e11_k = (1 + e11_m) / (2 + e11_m)
chk("11 kappa' (voting)", e11_k, 2 / 3)
e11_tot = e11_k + (1 + e11_m) * (1 - e11_k)
chk("11 votes of raider after issue", e11_k / e11_tot, 0.5)
e11_du = (1 + e11_m) * e11_vh / e11_tot - e11_vh
e11_dr = e11_vh - e11_vh / e11_tot
chk("11 Delta_u voting", e11_du, e11_m * e11_vh / 2)
chk("11 Delta_r voting", e11_dr, e11_m * e11_vh / (2 * (1 + e11_m)))
chk("11 Delta_u = 1.5", e11_du, 1.5)
chk("11 Delta_r = 0.75", e11_dr, 0.75)
chk("11 conservation", e11_k * e11_dr, (1 - e11_k) * e11_du)
chk("11 kappa'(Du + Dr) = Du", e11_k * (e11_du + e11_dr), e11_du)
e11_P = 1 + e11_du
e11_beta = lambda P: P / (1 + e11_du)
e11_pi = lambda P: e11_beta(P) * e11_w + e11_k * (e11_beta(P) * (e11_vh - e11_dr) + (1 - e11_beta(P)) * e11_v - (e11_v + P))
chk("11 profit formula at P = 1.2", e11_pi(1.2), e11_beta(1.2) * (e11_w - e11_du))
chk("11 optimal premium", e11_P, 2.5)
chk("11 profit at optimum", e11_pi(e11_P), 0.5)
e11_dnv = e11_vh * e11_m / (2 + e11_m)
chk("11 non-voting Delta = vhat/3", e11_dnv, 1.0)
chk("11 non-voting premium", 1 + e11_dnv, 2.0)
chk("11 non-voting profit", e11_w - e11_dnv, 1.0)
chk("11 m for Delta* = what, non-voting", 2 * e11_w / (e11_vh - e11_w), 4)
chk("11 m for Delta* = what, voting", 2 * e11_w / e11_vh, 4 / 3)
chk("11 kappa' at m = 4/3", (1 + 4 / 3) / (2 + 4 / 3), 0.7)
chk("11 Delta_u at m = 4/3 equals what", (4 / 3) * e11_vh / 2, e11_w)

# --- Ex 12: Hansen dominance, v ~ U[0,100], w = 1.2 v + 30, x = 200
w12 = lambda v: 1.2 * v + 30
e12_x, e12_C = 200.0, 60.0
e12_F, e12_Ew = e12_C / 100, 1.2 * e12_C / 2 + 30
chk("12 E(w|C=60)", e12_Ew, 66)
e12_cash = e12_F * (e12_Ew - e12_C)
chk("12 cash gain", e12_cash, 3.6)
e12_b = e12_C / (e12_x + w12(e12_C))
chk("12 beta*", e12_b, 0.1986755, 1e-6)
e12_stock = e12_F * (1 - e12_b) * (e12_Ew + e12_x) + (1 - e12_F) * e12_x - e12_x
chk("12 stock gain", e12_stock, 7.8913907, 1e-6)
chk("12 difference = F beta* (w(C) - E)", e12_stock - e12_cash, e12_F * e12_b * (w12(e12_C) - e12_Ew))
ok("12 acceptance set same: v/(x+w) increasing", all((v + 1) / (e12_x + w12(v + 1)) > v / (e12_x + w12(v)) for v in range(0, 100)))
e12_Cs = 30 / 0.8
chk("12 optimal cash offer", e12_Cs, 37.5)
chk("12 FOC at C*", w12(e12_Cs) - e12_Cs - e12_Cs, 0)
chk("12 optimal cash gain", (e12_Cs / 100) * (1.2 * e12_Cs / 2 + 30 - e12_Cs), 5.625)
e12_b2 = e12_Cs / (e12_x + w12(e12_Cs))
e12_s2 = (e12_Cs / 100) * ((1 - e12_b2) * (1.2 * e12_Cs / 2 + 30 + e12_x) - e12_x)
ok("12 stock beats optimal cash", e12_s2 > 5.625)
chk("12 stock gain at C*", e12_s2, 5.625 + 0.375 * e12_b2 * (w12(37.5) - 52.5))

# --- Ex 13: Fishman (1989), gamma = 0.6, v = 0.6, v2+ ~ U[0,1], v1+ = 0.9, v1- = 0.4
e13_g, e13_v, e13_hi, e13_lo = 0.6, 0.6, 0.9, 0.4
e13_pd = e13_v * e13_v + (e13_hi**2 - e13_v**2) / 2 + e13_hi * (1 - e13_hi)
chk("13 p_d", e13_pd, 0.675)
e13_pc = e13_g * e13_pd + (1 - e13_g) * e13_lo
chk("13 p_c", e13_pc, 0.565)
chk("13 p_c - p_d = (1-g)(v1- - p_d)", e13_pc - e13_pd, (1 - e13_g) * (e13_lo - e13_pd))
ok("13 p_c < p_d", e13_pc < e13_pd)
chk("13 gamma = 1 -> equal", 1.0 * e13_pd + 0 * e13_lo, e13_pd)

# --- Ex 14: Tirole 14.2, x = .8, nu = .3, rho1 = 1.5, rho0 = .6, P = .3, A = 1
x, nu, r1, r0, P = 0.8, 0.3, 1.5, 0.6, 0.3
mu = 1 - (1 - x) * (1 - nu) / x
chk("14 mu", mu, 0.825)
chk("14 consistency (14.3)", x * mu + (1 - x) * (1 - nu), x)
a = x * r1 + (1 - x) * (1 - nu) * r0 - 1
kap = x * (1 - mu) * (r1 - r0)
ah = x * r1 + (1 - x) * (1 - nu) * P - 1
kh = x * (1 - mu) * (r1 - P)
chk("14 alpha", a, 0.284)
chk("14 kappa", kap, 0.126)
chk("14 alpha hat", ah, 0.242)
chk("14 kappa hat", kh, 0.168)
chk("14 alpha hat = alpha - (1-x)(1-nu)(rho0-P)", ah, a - (1 - x) * (1 - nu) * (r0 - P))
chk("14 kappa hat = kappa + x(1-mu)(rho0-P)", kh, kap + x * (1 - mu) * (r0 - P))
chk("14 sum invariant", ah + kh, a + kap)
Dn = 1 - x * r0 - (1 - x) * (1 - nu) * P
chk("14 denominator", Dn, 0.478)
chk("14 book denominator form", 1 + (1 - x) * (1 - nu) * (r0 - P) - r0 * (x + (1 - x) * (1 - nu)), Dn)
Ii = lambda Ai, Ij: (Ai + x * (1 - mu) * (r0 - P) * Ij) / Dn
chk("14 slope dIi/dIj", x * (1 - mu) * (r0 - P) / Dn, 0.0878661, 1e-6)
Isym = 1 / (1 - r0 * (x + (1 - x) * (1 - nu)))
chk("14 symmetric I = kA", Isym, 2.2935780, 1e-6)
chk("14 fixed point", Ii(1, Isym), Isym)
chk("14 symmetric NPV", (ah + kh) * Isym, 0.9403670, 1e-6)
chk("14 independent of P (P = 0)", 1 / (1 - x * r0 - (1 - x) * (1 - nu) * 0 - x * (1 - mu) * (r0 - 0)), Isym)
e14_lend = lambda Ai, Ij: x * r0 * Ii(Ai, Ij) + (1 - x) * (1 - nu) * P * Ii(Ai, Ij) + x * (1 - mu) * (r0 - P) * Ij - (Ii(Ai, Ij) - Ai)
chk("14 lender breaks even (asym, Ij = 3)", e14_lend(1, 3), 0)
e14_nu_star = 1 - (1 - x * r1) / ((1 - x) * r0)
ok("14 alpha > 0 for all nu here (x rho1 > 1)", x * r1 > 1 and e14_nu_star > 1)
# second parameter point with x rho1 < 1 (x = 0.6): thresholds where alpha (P = rho0) and alpha hat (P = .3) vanish
x2 = 0.6
chk("14 nu* (P = rho0, x = .6)", 1 - (1 - x2 * r1) / ((1 - x2) * r0), 0.5833333, 1e-6)
chk("14 nu-hat* (P = .3, x = .6)", 1 - (1 - x2 * r1) / ((1 - x2) * P), 0.1666667, 1e-6)
chk("14 alpha at nu* is zero", x2 * r1 + (1 - x2) * (1 - 0.5833333333333333) * r0 - 1, 0)

# --- Ex 15: Tirole 14.3, F exponential(lam = 2), rho0 = .6, rho1 = 1.5, x = .8, J = A = 1
lam, r0, r1, x, J, A = 2.0, 0.6, 1.5, 0.8, 1.0, 1.0
Fe = lambda t: 1 - math.exp(-lam * t)
fe = lambda t: lam * math.exp(-lam * t)
ok("15 monotone hazard f/F decreasing", all(fe(t + 0.01) / Fe(t + 0.01) < fe(t) / Fe(t) for t in [0.05 * i + 0.01 for i in range(60)]))


def integ(g, lo, hi, n=4000):
    """Composite Simpson rule on [lo, hi] (n even)."""
    h = (hi - lo) / n
    s = g(lo) + g(hi) + sum((4 if i % 2 else 2) * g(lo + i * h) for i in range(1, n))
    return s * h / 3


def U15(rs, P):
    """Safe firm's NPV for cutoff rs given price P (investment from the breakeven condition)."""
    cost = integ(lambda t: (P + t - r0) * fe(t), 0, rs)
    gain = integ(lambda t: (r1 - P - t) * fe(t), 0, rs)
    I = (A - (1 - x) * J * cost) / (1 - r0)
    return (r1 - 1) * I + (1 - x) * J * gain


P0 = 0.4
grid = [0.3 + 0.001 * i for i in range(601)]
best = max(grid, key=lambda rs: U15(rs, P0))
chk("15 argmax cutoff = 1 - P", best, 1 - P0, 1.5e-3)
chk("15 FOC bracket zero at s = 1", (r1 - 1) * (1 - r0) - (r1 - 1) * (1 - r0), 0)
chk("15 credit line per unit L* = 1 - rho0", 1 - r0, 0.4)
Peq = bisect(lambda p: Fe(1 - p) - p * fe(1 - p), 1e-9, 1 - 1e-9)
chk("15 equilibrium P (lam=2)", Peq, 0.6039700, 1e-6)
ok("15 0 < P < 1", 0 < Peq < 1)
chk("15 rho* = 1 - P", 1 - Peq, 0.3960300, 1e-6)
chk("15 F(rho*)", Fe(1 - Peq), 0.5470891, 1e-6)
Gp = math.exp(lam * (1 - Peq))  # (F/f)' for the exponential
dPdL = Gp / (1 + Gp)
PL = lambda L: bisect(lambda p: Fe(r0 + L - p) - p * fe(r0 + L - p), 1e-9, r0 + L - 1e-9)
fd = (PL(0.4 + 1e-5) - PL(0.4 - 1e-5)) / 2e-5
chk("15 dP/dL = G'/(1+G')", fd, dPdL, 1e-5)
ok("15 0 < dP/dL < 1", 0 < dPdL < 1)
chk("15 dP/dL value", dPdL, 0.6882735, 1e-6)
# (iii) uniform on [rb - e, rb + e] (f/F = 1/(t - rb + e) decreasing): corner P = 1 - rb - e
rb, e = 0.5, 0.05
prof = lambda p: min(max((1 - p - (rb - e)) / (2 * e), 0), 1) * p
pg = [0.30 + 0.0001 * i for i in range(3001)]
pbest = max(pg, key=prof)
chk("15 spike: P = 1 - rb - e", pbest, 1 - rb - e, 1e-4)
ok("15 spike: corner condition 1 - rb > 3e", 1 - rb > 3 * e)
chk("15 spike: F(rho*) = 1", min(max((1 - pbest - (rb - e)) / (2 * e), 0), 1), 1)

# --- extra displayed intermediates (detailed solutions)
chk("3 sell index", 100 + 28.5, 128.5)
chk("8 cash gain coefficient -0.25/100", e8_gain(10) / 10**2, -0.0025)
chk("9 (r^2 - .36)/2", (e9_r**2 - 0.36) / 2, 0.0336, 1e-4)
chk("9 r(1-r)", e9_r * (1 - e9_r), 0.2264, 1e-4)
chk("10 ln 64", math.log(64), 4.15888, 1e-5)
chk("10 ln 40", math.log(40), 3.688879, 1e-6)
chk("10 20 + 40 alpha'", G(64, 0.3, 80) / math.log(40), 30.6656, 1e-4)
chk("10 cost of toehold cut at bid 40", 40 * math.log(40) * (0.3 - e10_ap), 4.92, 5e-3)
chk("10 0.5 - alpha' times 40", (0.5 - e10_ap) * 40, 9.3344, 1e-4)
chk("11 raider share value m=1", e11_vh * (2 + e11_m) / (2 * (1 + e11_m)), 2.25)
chk("11 untendered share value m=1", e11_vh * (2 + e11_m) / 2, 4.5)
chk("12 stock minus cash", e12_F * e12_b * (w12(e12_C) - e12_Ew), 4.29, 5e-3)
chk("12 w(C*) and E(w|C*)", w12(37.5) + 1.2 * 37.5 / 2 + 30, 75 + 52.5)
chk("13 p_d pieces", (0.9**2 - 0.6**2) / 2, 0.225)
chk("14 1 - x rho0", 1 - 0.8 * 0.6, 0.52)
chk("14 0.6 x 0.94", 0.6 * 0.94, 0.564)
chk("15 exponent 2(1-P)", 2 * (1 - Peq), 0.792, 1e-3)
chk("15 cutoff slope 1/(1+G')", 1 - dPdL, 1 / (1 + Gp))

print(f"PASS {N} checks")
