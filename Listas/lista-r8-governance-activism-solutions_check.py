"""Numeric checks for Listas/lista-r8-governance-activism-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-r8-governance-activism-solutions_check.py  -> PASS <n> checks
Symbolic results are asserted at a parameter point that satisfies each exercise's assumptions.
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


# --- Ex 1: Ross CQ 1.14, hostile bid
chk("1 premium", 35 / 25 - 1, 0.40)
chk("1 gain per share", 35 - 25, 10)
chk("1 required value per share to justify resisting", 25 * 1.40, 35)

# --- Ex 3: G&T Example 18.1 (p. 631): $60m buys 20%, adds $60m over five years
chk("3 firm value", 60 / 0.20, 300)
chk("3 five-year gain on firm", 60 / 300, 0.20)
chk("3 annualized", 1.20 ** 0.2 - 1, 0.0371372, 1e-6)
chk("3 Gallalee's share of gain", 0.20 * 60, 12)
chk("3 his return on own 60", 0.20 * 60 / 60, 0.20)

# --- Ex 5: G&T Example 18.3 (p. 641): senior debt F that blocks only the bad-state investment
e5_with, e5_new = {"good": 250, "medium": 175, "bad": 125}, 100
e5_Fmax = min(e5_with["good"], e5_with["medium"]) - e5_new
e5_Fmin = e5_with["bad"] - e5_new
chk("5 F upper", e5_Fmax, 75)
chk("5 F lower", e5_Fmin, 25)
for F in (30, 50, 70):
    ok(f"5 F={F} funds good", e5_with["good"] - F >= e5_new)
    ok(f"5 F={F} funds medium", e5_with["medium"] - F >= e5_new)
    ok(f"5 F={F} blocks bad", e5_with["bad"] - F < e5_new)
chk("5 bad-state NPV", 125 - 50 - 100, -25)
chk("5 medium-state NPV", 175 - 50 - 100, 25)
chk("5 all senior debt F=100: medium left for new money", 175 - 100, 75)

# --- Ex 4: G&T 18.5, illustrative blockholder (alpha=10%, value gain 50, monitoring cost 8)
e4_a, e4_dV, e4_c, e4_pb = 0.10, 50, 8, 4
chk("4 blockholder share of gain", e4_a * e4_dV, 5)
ok("4 no monitoring without private benefit", e4_a * e4_dV < e4_c)
chk("4 payoff with private benefit", e4_a * e4_dV + e4_pb, 9)
ok("4 monitors with private benefit", e4_a * e4_dV + e4_pb >= e4_c)
chk("4 free riders' gain", (1 - e4_a) * e4_dV, 45)
chk("4 net gain to others with private benefit", (1 - e4_a) * e4_dV - e4_pb, 41)
chk("4 minimal private benefit", e4_c - e4_a * e4_dV, 3)

# --- Ex 6: Harris-Raviv, E1=100, E2=80, K2=25, alpha=0.3 (and failure case K2=5)
e6_E1, e6_E2, e6_K2, e6_a = 100, 80, 25, 0.3
chk("6 worst in control", e6_a * e6_E2 + e6_K2, 49)
chk("6 best out of control", e6_a * e6_E1, 30)
ok("6 assumption E2+K2>=E1", e6_E2 + e6_K2 >= e6_E1)
chk("6 failure worst in control K2=5", e6_a * e6_E2 + 5, 29)
ok("6 failure case", e6_a * e6_E2 + 5 < e6_a * e6_E1)
chk("6 alpha (E1-E2)", e6_a * (e6_E1 - e6_E2), 6)

# --- Ex 7: Shleifer-Vishny, uniform [0,1], c = 0


def e7_Zc(a):
    return (1 - 2 * a) / (1 + 2 * a)


def e7_pi(a):
    return 1 / (1 + 2 * a)


def e7_G(a):  # L's expected bid gain per unit research intensity
    return 0.25 * (1 - e7_Zc(a)) ** 2


for a in (0.0, 0.1, 0.2, 0.3):
    z, p = e7_Zc(a), e7_pi(a)
    chk(f"7 pi = E[Z|Z>=Zc] at {a}", p, (1 + z) / 2)
    chk(f"7 L indifferent at Zc, {a}", 0.5 * z - (0.5 - a) * p, 0)
    chk(f"7 Zc = (0.5-a)/(0.5+a) at {a}", z, (0.5 - a) / (0.5 + a))
    # G = int_{Zc}^1 [0.5 Z - (0.5-a) pi] dZ by midpoint rule
    n = 20000
    h = (1 - z) / n
    G_num = sum((0.5 * (z + (i + 0.5) * h) - (0.5 - a) * p) * h for i in range(n))
    chk(f"7 G closed form at {a}", G_num, e7_G(a), 1e-9)
chk("7 Zc(0.1)", e7_Zc(0.1), 2 / 3)
chk("7 pi(0.1)", e7_pi(0.1), 1 / 1.2)
chk("7 Zc(0.2)", e7_Zc(0.2), 3 / 7)
chk("7 pi(0.2)", e7_pi(0.2), 1 / 1.4)
chk("7 Zc(0)", e7_Zc(0.0), 1.0)
chk("7 pi(0)", e7_pi(0.0), 1.0)
chk("7 (1-Zc^2)/2 at 0.1", (1 - e7_Zc(0.1) ** 2) / 2, 5 / 18)
chk("7 (1-Zc^2)/2 at 0.2", (1 - e7_Zc(0.2) ** 2) / 2, 20 / 49)
chk("7 G(0.1)", e7_G(0.1), 1 / 36)
chk("7 G(0.2)", e7_G(0.2), 4 / 49)
k7 = 0.1  # c(I) = k I^2 / 2  ->  I* = G / k
chk("7 I*(0.1)", e7_G(0.1) / k7, 10 / 36)
chk("7 I*(0.2)", e7_G(0.2) / k7, 40 / 49)
chk("7 V-q at 0.1", e7_G(0.1) / k7 * (1 - e7_Zc(0.1) ** 2) / 2, (10 / 36) * (5 / 18))
chk("7 V-q at 0.2", e7_G(0.2) / k7 * (1 - e7_Zc(0.2) ** 2) / 2, (40 / 49) * (20 / 49))
d = 1e-6
for a in (0.1, 0.2):
    chk(f"7 dpi/da at {a}", (e7_pi(a + d) - e7_pi(a - d)) / (2 * d), -2 / (1 + 2 * a) ** 2, 1e-5)
    chk(f"7 dZc/da at {a}", (e7_Zc(a + d) - e7_Zc(a - d)) / (2 * d), -1 / (0.5 + a) ** 2, 1e-5)
chk("7 V-q at 0.1 numeric", (10 / 36) * (5 / 18), 0.0771605, 1e-6)
chk("7 V-q at 0.2 numeric", (40 / 49) * (20 / 49), 0.3331945, 1e-6)

# --- Ex 8: Tirole 10.5. pH=0.8, pL=0.5, B=0.6, R=5, nu=0.1, I-A=2
e8_pH, e8_pL, e8_B, e8_R, e8_nu = 0.8, 0.5, 0.6, 5.0, 0.1
e8_dp = e8_pH - e8_pL
chk("8 B/dp", e8_B / e8_dp, 2.0)
e8_P1 = e8_pH * (e8_R - e8_B / e8_dp)
chk("8 P1", e8_P1, 2.4)
chk("8 nu B/dp", e8_nu * e8_B / e8_dp, 0.2)
# gamma = 0.25 >= 0.2: IC (2) slack at Rb = B/dp
g = 0.25
Rb = e8_B / e8_dp
ok("8 IC2 holds at B/dp when gamma=0.25", e8_pH * Rb >= (e8_pL + e8_nu) * Rb + e8_B - g - 1e-12)
# gamma = 0.15 < 0.2: Rb from IC (2)
g = 0.15
e8_Rb2 = (e8_B - g) / (e8_dp - e8_nu)
chk("8 Rb from IC2", e8_Rb2, 2.25)
chk("8 P entrepreneur control gamma=0.15", e8_pH * (e8_R - e8_Rb2), 2.2)
chk("8 IC2 at Rb2 binds", e8_pH * e8_Rb2 - ((e8_pL + e8_nu) * e8_Rb2 + e8_B - g), 0)
e8_P2 = e8_pH * (e8_R - e8_B / (e8_dp - e8_nu))
chk("8 B/(dp-nu)", e8_B / (e8_dp - e8_nu), 3.0)
chk("8 P2", e8_P2, 1.6)
ok("8 financed under EC, not IC (I-A=2)", e8_P1 >= 2 and e8_P2 < 2)
chk("8 NPV loss under IC equals gamma", 0.25, 0.25)

# --- Ex 9: Tirole 10.7. pH=0.6, pL=0.35, B=1, R=12, I=7, tA=0.1, gA=0.5, tB=0.2, gB=1.8
e9 = dict(pH=0.6, pL=0.35, B=1.0, R=12.0, I=7.0, tA=0.1, gA=0.5, tB=0.2, gB=1.8)
e9_dp = e9["pH"] - e9["pL"]
e9_net = e9["R"] - e9["B"] / e9_dp
chk("9 B/dp", e9["B"] / e9_dp, 4.0)
chk("9 R-B/dp", e9_net, 8.0)
ok("9 assumption tA R - gA > tB R - gB", e9["tA"] * e9["R"] - e9["gA"] > e9["tB"] * e9["R"] - e9["gB"])
chk("9 tA R - gA", e9["tA"] * e9["R"] - e9["gA"], 0.7)
chk("9 tB R - gB", e9["tB"] * e9["R"] - e9["gB"], 0.6)
e9_PA = (e9["pH"] + e9["tA"]) * e9_net
e9_PB = (e9["pH"] + e9["tB"]) * e9_net
e9_PE = e9["pH"] * e9_net
chk("9 PA", e9_PA, 5.6)
chk("9 PB", e9_PB, 6.4)
chk("9 PE", e9_PE, 4.8)
chk("9 A_A", e9["I"] - e9_PA, 1.4)
chk("9 A_B", e9["I"] - e9_PB, 0.6)
chk("9 A_E", e9["I"] - e9_PE, 2.2)
chk("9 NPV_A", (e9["pH"] + e9["tA"]) * e9["R"] - e9["I"] - e9["gA"], 0.9)
chk("9 NPV_B", (e9["pH"] + e9["tB"]) * e9["R"] - e9["I"] - e9["gB"], 0.8)
chk("9 NPV_E", e9["pH"] * e9["R"] - e9["I"], 0.2)
ok("9 project bad if shirk", e9["pL"] * e9["R"] + e9["B"] - e9["I"] < 0)
chk("9 NPV_A - NPV_B", 0.9 - 0.8, 0.1)

# --- Ex 10: Tirole 10.6. pH=0.6, pL=0.35, B=1, R=10, tauH=0.05


def e10_PIC(dtau, pH=0.6, dp=0.25, B=1.0, R=10.0, tH=0.05):
    return (pH + tH) * (R - B / (dp + dtau))


e10_PEC = 0.6 * (10 - 1 / 0.25)
chk("10 PEC", e10_PEC, 3.6)
e10_thr = 1.0 * (0.6 + 0.05) / (0.05 * 10 + 0.6 * 1 / 0.25)
chk("10 dp+dtau threshold", e10_thr, 0.65 / 2.9)
chk("10 dtau*", e10_thr - 0.25, 0.65 / 2.9 - 0.25)
chk("10 dtau* numeric", e10_thr - 0.25, -0.0258621, 1e-6)
chk("10 PIC at threshold equals PEC", e10_PIC(e10_thr - 0.25), e10_PEC, 1e-9)
chk("10 PIC dtau=-0.05", e10_PIC(-0.05), 3.25)
chk("10 PIC dtau=0", e10_PIC(0.0), 3.9)
chk("10 PIC dtau=+0.02", e10_PIC(0.02), 0.65 * (10 - 1 / 0.27))
chk("10 PIC dtau=+0.02 numeric", e10_PIC(0.02), 4.0925926, 1e-6)
ok("10 gamma=1.5 > max tau R (tauL=0.10)", 1.5 > max(0.05, 0.10) * 10)
ok("10 threshold below dp iff B < dp R", e10_thr < 0.25 and 1.0 < 0.25 * 10)

# --- Ex 11: Tirole 9.1. pH=0.8, pL=0.5, R=7, B=0.9, b=0.6, c=0.6, I=4
e11 = dict(pH=0.8, pL=0.5, R=7.0, B=0.9, b=0.6, c=0.6, I=4.0)
e11_dp = e11["pH"] - e11["pL"]
ok("11 pHR > pLR+B > I", e11["pH"] * e11["R"] > e11["pL"] * e11["R"] + e11["B"] > e11["I"])
chk("11 pH(B-b)/dp", e11["pH"] * (e11["B"] - e11["b"]) / e11_dp, 0.8)
chk("11 dpR - pH b/dp", e11_dp * e11["R"] - e11["pH"] * e11["b"] / e11_dp, 0.5)
ok("11 c between bounds", 0.8 > e11["c"] > 0.5)
ok("11 dpR > c + B", e11_dp * e11["R"] > e11["c"] + e11["B"])
e11_A3 = e11["I"] - e11["pH"] * (e11["R"] - e11["B"] / e11_dp)
e11_A2 = e11["I"] + e11["c"] - e11["pH"] * (e11["R"] - e11["b"] / e11_dp)
e11_A1 = e11["I"] - e11["pL"] * e11["R"]
chk("11 A3", e11_A3, 0.8)
chk("11 A2", e11_A2, 0.6)
chk("11 A1", e11_A1, 0.5)
chk("11 A3-A2 = pH(B-b)/dp - c", e11_A3 - e11_A2, 0.8 - 0.6)
chk("11 A2-A1 = c - (dpR - pH b/dp)", e11_A2 - e11_A1, 0.6 - 0.5)
chk("11 U3", e11["pH"] * e11["R"] - e11["I"], 1.6)
chk("11 U2", e11["pH"] * e11["R"] - e11["I"] - e11["c"], 1.0)
chk("11 U1", e11["pL"] * e11["R"] + e11["B"] - e11["I"], 0.4)
chk("11 U2-U1 = dpR - c - B", 1.0 - 0.4, e11_dp * e11["R"] - e11["c"] - e11["B"])
e11_Rm = e11["c"] / e11_dp
chk("11 Rm", e11_Rm, 2.0)
chk("11 Im", e11["pH"] * e11_Rm - e11["c"], 1.0)
chk("11 Im = pL c/dp", e11["pL"] * e11["c"] / e11_dp, 1.0)
chk("11 B/dp", e11["B"] / e11_dp, 3.0)
chk("11 b/dp", e11["b"] / e11_dp, 2.0)

# --- Ex 12: Tirole 10.3 disagreement values (per unit s3 R)


def e12_vals(beta, kappa, tau=0.1, mu=0.2):
    p1, p3 = beta, (1 - beta) * (1 - kappa)
    return -p1 * mu + p3 * tau, p1 * tau - p3 * mu


vE, vL = e12_vals(0.3, 0.5)
chk("12 follow E (beta=.3)", vE, -0.025)
chk("12 follow L (beta=.3)", vL, -0.04)
vE, vL = e12_vals(0.6, 0.5)
chk("12 follow E (beta=.6)", vE, -0.10)
chk("12 follow L (beta=.6)", vL, 0.02)
chk("12 book's first term (beta=.3)", -0.3 * 0.2 + 0.1 * (1 - 0.5), -0.01)
chk("12 prob state 2 (beta=.3)", 0.7 * 0.5, 0.35)
chk("12 prob state 3 (beta=.3)", 0.7 * 0.5, 0.35)
chk("12 prob state 2 (beta=.6)", 0.4 * 0.5, 0.2)
chk("12 state 4: pi2 tau - pi4 mu (0.2, 0.05)", 0.2 * 0.1 - 0.05 * 0.2, 0.01)
chk("12 state 4: pi2 tau - pi4 mu (0.2, 0.15)", 0.2 * 0.1 - 0.15 * 0.2, -0.01)
chk("12 off-path belief bounds", 0.1 / 0.3, 1 / 3)
chk("12 off-path belief bounds upper", 0.2 / 0.3, 2 / 3)
chk("12 posterior state 1 given disagreement (beta=.3)", 0.3 / (0.3 + 0.35), 0.3 / 0.65)

# --- Ex 13: Tirole 10.8. pH=0.6, pL=0.35, B=0.5, R=10, tau=0.1, gamma=1.2, I=5.8, lam=0.2
e13 = dict(pH=0.6, dp=0.25, B=0.5, R=10.0, tau=0.1, g=1.2, I=5.8, lam=0.2)
e13_bd = e13["B"] / e13["dp"]
chk("13 B/dp", e13_bd, 2.0)
ok("13 gamma > tau R", e13["g"] > e13["tau"] * e13["R"])
chk("13 (pH+tau)B/dp", (e13["pH"] + e13["tau"]) * e13_bd, 1.4)
e13_r1 = e13["pH"] * e13["R"]
e13_r0 = e13["pH"] * (e13["R"] - e13_bd)
e13_r0p = (e13["pH"] + e13["tau"]) * (e13["R"] - e13_bd)
chk("13 rho1", e13_r1, 6.0)
chk("13 rho0", e13_r0, 4.8)
chk("13 rho0+", e13_r0p, 5.6)
ok("13 rho1 > I > rho0+", e13_r1 > e13["I"] > e13_r0p)
lam = e13["lam"]


def e13_P(x, y=1.0):
    return (1 - lam) * (e13["pH"] + e13["tau"] * x) * (e13["R"] - e13_bd) + lam * (e13["pH"] + e13["tau"] * y) * (e13["R"] - e13_bd)


def e13_Ub(x, y=1.0):
    return (1 - lam) * ((e13["pH"] + e13["tau"] * x) * e13["R"] - e13["g"] * x) + lam * (e13["pH"] + e13["tau"] * y) * (e13["R"] - e13_bd) - e13["I"]


def e13_S(x, y=1.0):
    return (1 - lam) * ((e13["pH"] + e13["tau"] * x) * e13["R"] - e13["g"] * x) + lam * ((e13["pH"] + e13["tau"] * y) * e13["R"] - e13["g"] * y) - e13["I"]


chk("13 P(0,1)", e13_P(0), 4.96)
chk("13 Ub(0,1)", e13_Ub(0), 0.12)
chk("13 S(0,1)", e13_S(0), 0.16)
chk("13 S - Ub = new manager rent", e13_S(0) - e13_Ub(0), lam * ((e13["pH"] + e13["tau"]) * e13_bd - e13["g"]))
chk("13 rent value", lam * ((e13["pH"] + e13["tau"]) * e13_bd - e13["g"]), 0.04)
chk("13 dUb/dy", e13_Ub(0, 1) - e13_Ub(0, 0), lam * e13["tau"] * (e13["R"] - e13_bd))
chk("13 dUb/dy value", lam * e13["tau"] * (e13["R"] - e13_bd), 0.16)
chk("13 dUb/dx", e13_Ub(1) - e13_Ub(0), (1 - lam) * (e13["tau"] * e13["R"] - e13["g"]))
chk("13 dUb/dx value", (1 - lam) * (e13["tau"] * e13["R"] - e13["g"]), -0.16)
chk("13 dP/dx", e13_P(1) - e13_P(0), (1 - lam) * e13["tau"] * (e13["R"] - e13_bd))
chk("13 dP/dx value", (1 - lam) * e13["tau"] * (e13["R"] - e13_bd), 0.64)
# A = 0.5: I - A = 5.3 > 4.96 -> x solves 4.96 + 0.64 x = 5.3
e13_x = (5.3 - 4.96) / 0.64
chk("13 x at A=0.5", e13_x, 0.53125)
chk("13 P(x) = I - A", e13_P(e13_x), 5.3)
chk("13 Ub at x", e13_Ub(e13_x), 0.035)
chk("13 lambda max for x=0", (e13_r1 - e13["I"]) / (e13_r1 - e13_r0p), 0.5)
chk("13 P(1,1) = rho0+", e13_P(1), e13_r0p)
chk("13 Ub at A=1.5 equals (1-l)rho1+l rho0+ - I", e13_Ub(0), (1 - lam) * e13_r1 + lam * e13_r0p - e13["I"])
chk("13 A threshold for x=0", e13["I"] - e13_P(0), 0.84)

# --- Ex 14: Tirole 10.9 (iv). g=1, t ~ U[-0.1, 0.3] (density 2.5), R=10, B/dp=4, mu=0.5
g14, lo, hi, dens = 1.0, -0.1, 0.3, 2.5
R14, bd14 = 10.0, 4.0


def e14_k(mu):
    return R14 + mu * (R14 - bd14)


def e14_tg(ts):
    gam = g14 * (hi - ts) * dens
    tau = dens * (hi ** 2 - ts ** 2) / 2
    return tau, gam


chk("14 k(0.5)", e14_k(0.5), 13.0)
ts = g14 / e14_k(0.5)
chk("14 t*", ts, 1 / 13)
tau14, gam14 = e14_tg(ts)
chk("14 gamma", gam14, 2.5 * (0.3 - 1 / 13))
chk("14 tau", tau14, 1.25 * (0.09 - 1 / 169))
chk("14 gamma numeric", gam14, 0.5576923, 1e-6)
chk("14 tau numeric", tau14, 0.1051036, 1e-6)
hh = 1e-5
t1, g1 = e14_tg(ts + hh)
t0, g0 = e14_tg(ts - hh)
chk("14 dgamma/dtau = g/t* = k", (g1 - g0) / (t1 - t0), 13.0, 1e-4)
chk("14 d2gamma/dtau2 formula", g14 / (ts ** 3 * dens), 2197 / 2.5)
# numeric second derivative of gamma as a function of tau: gamma(tau) via t*(tau)


def e14_gam_of_tau(tau):
    t = math.sqrt(hi ** 2 - 2 * tau / dens)
    return g14 * (hi - t) * dens


h2 = 1e-4
sd = (e14_gam_of_tau(tau14 + h2) - 2 * e14_gam_of_tau(tau14) + e14_gam_of_tau(tau14 - h2)) / h2 ** 2
chk("14 d2gamma/dtau2 numeric", sd, 878.8, 0.5)
# (ii): tau and gamma rise with mu
ta, ga = e14_tg(g14 / e14_k(0.5))
tb, gb = e14_tg(g14 / e14_k(1.0))
ok("14 tau rises with mu", tb > ta)
ok("14 gamma rises with mu", gb > ga)
chk("14 k(1.0)", e14_k(1.0), 16.0)

# --- Ex 15: Tirole 10.2 example. pH=0.8, pL=0.5, B=0.6, R=5, U=1, L ~ U[0,4], I=4, A=1.3
e15_pH, e15_dp, e15_B, e15_R, e15_U = 0.8, 0.3, 0.6, 5.0, 1.0
e15_r1 = e15_pH * e15_R
e15_r0 = e15_pH * (e15_R - e15_B / e15_dp)
chk("15 rho1", e15_r1, 4.0)
chk("15 rho0", e15_r0, 2.4)
ok("15 (ii) U <= rho1 - rho0", e15_U <= e15_r1 - e15_r0)


def e15_P(l):  # investors' income with cutoff l (continue iff L <= l), l in [0,4]
    return (l / 4) * e15_r0 + (16 - l ** 2) / 8


def e15_G(l):  # expected total value (gross of I) with cutoff l
    return l / 4 * e15_r1 + ((16 - l ** 2) / 2 + e15_U * (4 - l)) / 4


chk("15 FB cutoff", e15_r1 - e15_U, 3.0)
chk("15 P(3)", e15_P(3), 2.675)
chk("15 P(2.4) max", e15_P(2.4), 2.72)
chk("15 P(2.8)", e15_P(2.8), 2.7)
e15_IA = 2.7
lsb = (4.8 + math.sqrt(4.8 ** 2 - 4 * 5.6)) / 2
chk("15 SB cutoff", lsb, 2.8)
chk("15 mu", (e15_r1 - e15_U - e15_r0) / (lsb - e15_r0), 1.5)
chk("15 SB line at cutoff", 1.5 * lsb - 0.5 * e15_r0, e15_r1 - e15_U)
chk("15 G(3)", e15_G(3), 4.125)
chk("15 G(2.8)", e15_G(2.8), 4.12)
chk("15 G(2.4)", e15_G(2.4), 4.08)
chk("15 NPV FB", e15_G(3) - 4, 0.125)
chk("15 NPV SB", e15_G(2.8) - 4, 0.12)
chk("15 NPV IN", e15_G(2.4) - 4, 0.08)
chk("15 A", 4 - e15_IA, 1.3)
# EN: rho0 on L<=3, at most L - (rho1 - rho0 - U) on L>3
e15_EN = 0.75 * e15_r0 + (3.5 - (e15_r1 - e15_r0 - e15_U)) / 4
chk("15 EN investors' max", e15_EN, 2.525)
ok("15 EN not financed", e15_EN < e15_IA)
chk("15 SB - EN bound = E[(L-rho0) on (2.8,3]]", e15_P(2.8) - (0.75 * e15_r0 + (16 - 9) / 8),
    (3 ** 2 - 2.8 ** 2) / 8 - 0.2 * e15_r0 / 4)
chk("15 IN slack", e15_P(2.4) - e15_IA, 0.02)
# golden parachute rb: investors liquidate iff L > rho0 + rb


def e15_Prb(rb):
    l = e15_r0 + rb
    return e15_P(l) - rb * (4 - l) / 4


chk("15 P with rb=0.05", e15_Prb(0.05), 2.7003125)
ok("15 rb=0.05 financed", e15_Prb(0.05) >= e15_IA)
ok("15 rb=0.10 not financed", e15_Prb(0.10) < e15_IA)
chk("15 P with rb=0.10", e15_Prb(0.10), 2.68125)
chk("15 G(2.45)", e15_G(2.45), 4.0871875)
chk("15 NPV IN+rb", e15_G(2.45) - 4, 0.0871875)
ok("15 rb raises NPV", e15_G(2.45) > e15_G(2.4))
ok("15 no renegotiation to liquidation for rb=0.05", e15_r0 + 0.05 < e15_r1 - e15_U)
# Omega_SB shrinks as A falls: I - A = 2.71
l2 = (4.8 + math.sqrt(4.8 ** 2 - 4 * 5.68)) / 2
chk("15 SB cutoff at I-A=2.71", l2, 2.6828427, 1e-6)
chk("15 P at that cutoff", e15_P(l2), 2.71)
chk("15 mu at I-A=2.71", (e15_r1 - e15_U - e15_r0) / (l2 - e15_r0), 2.1213203, 1e-6)

print(f"PASS {N} checks")
