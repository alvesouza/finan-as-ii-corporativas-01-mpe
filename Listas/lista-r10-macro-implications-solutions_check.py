"""Numeric checks for Listas/lista-r10-macro-implications-solutions.tex and -solutions-short.tex.

Every symbolic result in the solutions is evaluated at a parameter point that satisfies the
exercise's assumptions, and every number printed in the PDFs is asserted here.
Run: python -I Listas/lista-r10-macro-implications-solutions_check.py  -> PASS <n> checks
"""
import math

from scipy.optimize import brentq, minimize_scalar

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a strict inequality or sign condition; count the check."""
    global N
    assert cond, label
    N += 1


def argmax(f, a, b):
    return minimize_scalar(lambda z: -f(z), bounds=(a, b), method="bounded",
                           options={"xatol": 1e-12}).x


# ---- Ex 1: Tirole 13.1, credit-market equilibrium (G uniform on [0, I], S(r) = 2r) ----
def e1_r(pH, R, B, dp, I=1.0, s=2.0):
    P = pH * (R - B / dp)                          # pledgeable income
    # S(r) + int_0^I A g dA = [1 - G(A*)] I with A* = I - P/(1+r)  ->  (s r + I/2)(1+r) = P
    return brentq(lambda r: (s * r + I / 2) * (1 + r) - P, 0, 5)
e1_r1, e1_r2 = e1_r(0.8, 1.5, 0.3, 0.4), e1_r(0.8, 1.5, 0.2, 0.4)
chk("1 r(B=0.3)", e1_r1, (-2.5 + math.sqrt(6.25 + 0.8)) / 4)
chk("1 r(B=0.3) printed", e1_r1, 0.038795, 1e-6)
chk("1 r(B=0.2) printed", e1_r2, 0.110272, 1e-6)
chk("1 A*(B=0.3)", 1 - 0.6 / (1 + e1_r1), 0.422, 1e-3)
ok("1 r rises when B falls", e1_r2 > e1_r1)
chk("1 financed share B=0.3", 0.6 / (1 + e1_r1), 0.577592, 1e-6)
chk("1 financed share B=0.2", 0.8 / (1 + e1_r2), 0.720544, 1e-6)
chk("1 A*(B=0.2)", 1 - 0.8 / (1 + e1_r2), 0.279456, 1e-6)
ok("1 (1+r)I <= pH R", (1 + e1_r2) * 1 <= 1.2)
# implicit derivative dr/dB < 0 matches finite difference
e1_h = 1e-6
e1_fd = (e1_r(0.8, 1.5, 0.3 + e1_h, 0.4) - e1_r(0.8, 1.5, 0.3 - e1_h, 0.4)) / (2 * e1_h)
e1_A = 1 - 0.6 / (1 + e1_r1)
e1_dAdB = 0.8 / (0.4 * (1 + e1_r1))
e1_dAdr = 0.6 / (1 + e1_r1) ** 2
chk("1 dr/dB formula", -(1 * 1 * e1_dAdB) / (2 + 1 * 1 * e1_dAdr), e1_fd, 1e-5)

# ---- Ex 2: Tirole 16.2, time-consistent policy (gamma = k tau^2 / 2) ----
e2 = dict(pH=0.5, R=2.0, Bdp=1.0, k=20.0, A=1.0)
def e2_I(t): return e2["A"] / (1 - (e2["pH"] + t) * (e2["R"] - e2["Bdp"]))
def e2_W(t): return ((e2["pH"] + t) * e2["R"] - 1 - e2["k"] * t * t / 2) * e2_I(t)
e2_ts = e2["R"] / e2["k"]
chk("2 tau*", e2_ts, 0.1)
chk("2 I(tau*)", e2_I(e2_ts), 2.5)
e2_tc = argmax(e2_W, 0, 0.45)
chk("2 tau^c closed form", e2_tc, (10 - math.sqrt(60)) / 20, 1e-7)
chk("2 tau^c printed", e2_tc, 0.112702, 1e-6)
ok("2 tau^c > tau*", e2_tc > e2_ts)
e2_dI = (e2_I(e2_tc + 1e-7) - e2_I(e2_tc - 1e-7)) / 2e-7
chk("2 FOC commitment", (e2["k"] * e2_tc - e2["R"]) * e2_I(e2_tc),
    ((e2["pH"] + e2_tc) * e2["R"] - 1 - e2["k"] * e2_tc ** 2 / 2) * e2_dI, 1e-6)
chk("2 W(tau^c)", e2_W(e2_tc), 0.254033, 1e-6)
chk("2 W(tau*)", e2_W(e2_ts), 0.25)
# (iii) weight omega on investors: gamma'(tau) = R - (1-omega) R_l / I
e2_om = 0.5
e2_Rl = (e2["R"] - e2["Bdp"])                     # R_l / I at the binding IC
chk("2 tau(omega)", (e2["R"] - (1 - e2_om) * e2_Rl) / e2["k"], 0.075)

# ---- Ex 3: Tirole 15.3, imperfect correlation ----
e3 = dict(lam=0.3, rL=0.2, r0=0.6, rH=1.0, r1=1.8, A=1.0)
e3_rbar = (1 - e3["lam"]) * e3["rL"] + e3["lam"] * e3["rH"]
e3_I = e3["A"] / (1 + e3_rbar - e3["r0"])
e3_th = (e3_I - e3["A"]) / ((e3_I - e3["A"]) + (e3["rH"] - e3["r0"]) * e3_I)
chk("3 rbar", e3_rbar, 0.44)
chk("3 I", e3_I, 1 / 0.84)
chk("3 theta*", e3_th, 2 / 7)
def e3_supply(th): return (1 - th) * (1 - e3["lam"]) * (e3["r0"] - e3["rL"]) * e3_I
def e3_need(th): return (th + (1 - th) * e3["lam"]) * (e3["rH"] - e3["r0"]) * e3_I
chk("3 supply = need at theta*", e3_supply(e3_th), e3_need(e3_th), 1e-12)
chk("3 supply at theta*", e3_supply(e3_th), 0.238095, 1e-6)
ok("3 self-sufficient below theta*", e3_supply(0.2) > e3_need(0.2))
ok("3 shortage above theta*", e3_supply(0.4) < e3_need(0.4))
ok("3 (15.2) holds", (1 - e3["lam"]) * (e3["rH"] - e3["rL"]) < 1)
ok("3 good state fine", (e3_th + (1 - e3_th) * (1 - e3["lam"])) * (e3["r0"] - e3["rL"])
   > (1 - e3_th) * e3["lam"] * (e3["rH"] - e3["r0"]))

# ---- Ex 4: Review Problem 5, B0(t) = ln(1+t) ----
e4 = dict(r0=0.6, r1=1.5, A=1.0, SD=0.5)
def e4_I(t): return e4["A"] / (1 - (1 - t) * e4["r0"])
e4_t = brentq(lambda t: 1 / (1 + t) - e4["SD"] / (e4_I(t) - e4["A"]), 0, 0.99)
e4_th = e4["SD"] / (e4_I(e4_t) - e4["A"])
def e4_Ub(t): return ((e4["r1"] - 1) - (t - math.log(1 + t)) * e4["r0"]) * e4_I(t)
chk("4 t*", e4_t, 0.333333, 1e-6)
chk("4 theta*", e4_th, 0.75, 1e-6)
chk("4 I*", e4_I(e4_t), 1.666667, 1e-6)
chk("4 Ub*", e4_Ub(e4_t), 0.787682, 1e-6)
ok("4 SD < r0 A/(1-r0)", e4["SD"] < e4["r0"] * e4["A"] / (1 - e4["r0"]))
e4_t2 = brentq(lambda t: 1 / (1 + t) - 0.6 / (e4_I(t) - e4["A"]), 0, 0.99)
ok("4 more SD lowers t*", e4_t2 < e4_t)
ok("4 more SD raises Ub", e4_Ub(e4_t2) > e4_Ub(e4_t))
chk("4 t*(SD=0.6)", e4_t2, 0.276984, 1e-6)
chk("4 I*(SD=0.6)", e4_I(e4_t2), 1.766190, 1e-6)
chk("4 Ub*(SD=0.6)", e4_Ub(e4_t2), 0.848673, 1e-6)
chk("4 theta*(SD=0.6)", 1 / (1 + e4_t2), 0.783095, 1e-6)
chk("4 (iv) domestic payoff", e4["r0"] * (e4["A"] + e4["SD"]), 0.9)
chk("4 commit t=0", argmax(e4_Ub, 0, 0.9), 0.0, 1e-4)
chk("4 Ub(0)", e4_Ub(0), 1.25)
chk("4 (iv) I = A + SD", e4["A"] + e4["SD"], 1.5)
ok("4 (iv) domestic return > 0", e4["r0"] * (e4["A"] + e4["SD"]) > e4["SD"])

# ---- Ex 5: Tirole 16.1, borrowing abroad ----
e5 = dict(p=0.5, R=3.0, mu=0.6, muH=0.8, A=1.0, D=0.2, Rx=2.0)
e5_den = 1 - (e5["p"] * e5["R"] - e5["mu"])
e5_I = e5["A"] / e5_den
chk("5 I", e5_I, 10)
chk("5 Ub", (e5["p"] * e5["R"] - 1) * e5_I, 5)
# (ii) tax/guarantee: tau, sigma with government budget balance leave I unchanged
e5_tau = 0.1
e5_Rl = (e5["p"] * (1 - e5_tau) * e5["R"] * e5_I - e5["mu"] * e5_I) / e5["p"]   # IC binding
e5_sig = e5["p"] * e5_tau * e5["R"] * e5_I / ((1 - e5["p"]) * e5_Rl)
chk("5 (ii) R_l", e5_Rl, 15)
chk("5 (ii) sigma", e5_sig, 0.2)
chk("5 (ii) p R_l", e5["p"] * e5_Rl, 7.5)
chk("5 (ii) (1-p) sigma R_l", (1 - e5["p"]) * e5_sig * e5_Rl, 1.5)
chk("5 (ii) investors break even", e5["p"] * e5_Rl + (1 - e5["p"]) * e5_sig * e5_Rl,
    e5_I - e5["A"], 1e-9)
e5_ID = (e5["A"] - e5["D"]) / e5_den
chk("5 I with debt", e5_ID, 8)
chk("5 book Ub with debt", (e5["p"] * e5["R"] - 1) * e5_ID, 4)
chk("5 consumption loss", e5["mu"] * e5_I - e5["mu"] * e5_ID, e5["mu"] * e5["D"] / e5_den)
chk("5 consumption loss printed", e5["mu"] * e5["D"] / e5_den, 1.2)
chk("5 (iii) Ub(muH)", (e5["p"] * e5["R"] - 1) * e5["A"] / (1 - e5["p"] * e5["R"] + e5["muH"]),
    5 / 3)
e5_e = (1 + e5["A"] / e5["Rx"]) * (e5["p"] * e5["R"] - e5["mu"])
chk("5 (iv) e", e5_e, 1.35)
chk("5 (iv) I = A + Rx", e5["A"] / (1 - (e5["p"] * e5["R"] - e5["mu"]) / e5_e), 3)
chk("5 (iv) e Rx = p Rl", e5_e * e5["Rx"], e5["p"] * (e5_e * (3 - e5["A"]) / e5["p"]))

# ---- Ex 6: Tirole 14.1, Shleifer-Vishny with R(I) = 2 sqrt(I) ----
e6 = dict(x=0.8, nu=0.0, pH=0.8, Bdp=0.5)
e6["mu"] = (2 * e6["x"] - 1) / e6["x"]
def e6_R(I): return 2 * math.sqrt(I)
def e6_Ub(Ij, Ii):
    x, nu, mu, pH, b = e6["x"], e6["nu"], e6["mu"], e6["pH"], e6["pH"] * e6["Bdp"]
    price_rev = pH * (e6_R(Ii + Ij) - e6_R(Ii)) - b * Ij        # P_j I_j
    return -Ij + x * pH * e6_R(Ij) + x * (1 - mu) * b * Ii + (1 - x) * (1 - nu) * price_rev
def e6_ext(I):
    pis = e6["x"] * (1 - e6["mu"])
    return pis * e6["pH"] * (e6["Bdp"] - (1 / math.sqrt(I) - 1 / math.sqrt(2 * I)))
chk("6 consistency x(1-mu) = (1-x)(1-nu)", e6["x"] * (1 - e6["mu"]),
    (1 - e6["x"]) * (1 - e6["nu"]), 1e-12)
for e6_I0, e6_want in ((1.0, 0.033137), (0.25, -0.013726)):
    e6_fd = (e6_Ub(e6_I0, e6_I0 + 1e-6) - e6_Ub(e6_I0, e6_I0 - 1e-6)) / 2e-6
    chk(f"6 externality formula I={e6_I0}", e6_ext(e6_I0), e6_fd, 1e-6)
    chk(f"6 externality printed I={e6_I0}", e6_ext(e6_I0), e6_want, 1e-6)
ok("6 price revenue positive", e6["pH"] * (e6_R(0.5) - e6_R(0.25)) - 0.4 * 0.25 > 0)
chk("6 price revenue I=1", e6["pH"] * (e6_R(2) - e6_R(1)) - 0.4, 0.262742, 1e-6)

# ---- Ex 7: Tirole 14.4, rho0 ~ U[0, 1], rhohat0 = 0.7, Delta rho = 0.5 ----
e7_lo, e7_hi, e7_hat, e7_drho = 0.0, 1.0, 0.7, 0.5
def e7_F(c): return (c - e7_lo) / (e7_hi - e7_lo)
def e7_pi(c): return e7_F(c) * e7_hat + (e7_hi ** 2 - c ** 2) / (2 * (e7_hi - e7_lo))
def e7_v(c): return e7_pi(c) + e7_drho * (1 - e7_F(c))
def e7_Ub(c): return (e7_v(c) - 1) / (1 - e7_pi(c))           # per unit of A
e7_c = argmax(e7_Ub, e7_lo, e7_hi)
chk("7 cutoff FOC", e7_c, e7_hat - (1 - e7_pi(e7_c)) / (1 - e7_F(e7_c)), 1e-6)
chk("7 cutoff closed form", e7_c, 1 - math.sqrt(0.6), 1e-6)
chk("7 cutoff printed", e7_c, 0.225403, 1e-6)
chk("7 v(c*)", e7_v(e7_c), 1.019677, 1e-5)
ok("7 rhohat - Delta rho < c* < rhohat", e7_hat - e7_drho < e7_c < e7_hat)
chk("7 I/A", 1 / (1 - e7_pi(e7_c)), 2.720193, 1e-5)
chk("7 Ub/A", e7_Ub(e7_c), 0.053526, 1e-5)
e7_cb = argmax(lambda c: e7_v(c) / (1 - e7_pi(c)), e7_lo, e7_hi)   # book's gross objective
ok("7 book objective also inside bounds", e7_hat - e7_drho < e7_cb < e7_hat)
chk("7 book-objective cutoff", e7_cb, 0.591681, 1e-5)

# ---- Ex 8: Review Problem 6 ----
e8 = dict(lam=0.4, rho=1.2, r0=0.5, r1=2.0, A=1.0)
def e8_c(x): return (1 + e8["lam"] * e8["rho"] * x) / (1 - e8["lam"] + e8["lam"] * x)
def e8_I(x): return e8["A"] / ((1 + e8["lam"] * e8["rho"] * x)
                              - (1 - e8["lam"] + e8["lam"] * x) * e8["r0"])
def e8_Ub(x):
    return ((1 - e8["lam"] + e8["lam"] * x) * e8["r1"] - (1 + e8["lam"] * e8["rho"] * x)) * e8_I(x)
for e8_x in (0.0, 0.5, 1.0):
    chk(f"8 Ub identity x={e8_x}", e8_Ub(e8_x),
        (e8["r1"] - e8_c(e8_x)) / (e8_c(e8_x) - e8["r0"]) * e8["A"], 1e-12)
ok("8 x=1 optimal since (1-lam)rho<=1", e8_Ub(1) > e8_Ub(0.5) > e8_Ub(0))
chk("8 I(1)", e8_I(1), 1 / 0.98)
chk("8 Ub(1)", e8_Ub(1), 0.52 / 0.98)
chk("8 shortage", (e8["rho"] - e8["r0"]) * e8_I(1), 0.714286, 1e-6)
ok("8 index insufficient", e8["rho"] - e8["r0"] > (1 - e8["lam"]) * e8["r0"])
chk("8 aggregate slack = I - A", ((1 - e8["lam"]) * e8["r0"] - e8["lam"] * (e8["rho"] - e8["r0"]))
    * e8_I(1), e8_I(1) - e8["A"], 1e-12)

# ---- Ex 9: Tirole 16.4, soft budget constraint ----
e9 = dict(yH=3.0, yL=1.0, w=0.8, Rc=0.5, rho=0.5, I=1.0, A=0.5, lam=0.3, wu=0.4)
ok("9 w < yL < w + R", e9["w"] < e9["yL"] < e9["w"] + e9["Rc"])
e9_pl = e9["rho"] * (e9["yH"] - e9["w"] - e9["Rc"]) + (1 - e9["rho"]) * (e9["yL"] - e9["w"] - e9["Rc"])
chk("9 pledgeable x=1", e9_pl, 0.7)
ok("9 financing", e9["I"] - e9["A"] <= e9_pl)
chk("9 NPV x=1", e9["rho"] * (e9["yH"] - e9["w"]) + (1 - e9["rho"]) * (e9["yL"] - e9["w"]) - e9["I"], 0.2)
chk("9 NPV x=0", e9["rho"] * (e9["yH"] - e9["w"]) - e9["I"], 0.1)
chk("9 L*", e9["w"] + e9["Rc"] - e9["yL"], 0.3)
ok("9 bailout assumption", e9["lam"] * (e9["w"] - e9["wu"] + e9["Rc"]) <= (1 + e9["lam"]) * e9["yL"])
e9_s = e9["w"] + e9["Rc"] - e9["yL"]
chk("9 W continue - W stop (L=0)", (e9["yL"] - e9["lam"] * e9_s) - (-e9["lam"] * e9["wu"]), 1.03)
chk("9 expected deadweight", (1 - e9["rho"]) * e9["lam"] * e9_s, 0.045)

# ---- Ex 10: Tirole 15.2, G uniform on [0,1], J = 0.3, Rc = 0.2, I = 0.5 ----
e10_J, e10_Rc, e10_I = 0.3, 0.2, 0.5
def e10_inv(ys): return (1 - ys ** 2) / 2 - (1 - ys) * (e10_J + e10_Rc)   # investors' gross
e10_A0 = e10_I - e10_inv(e10_J)
e10_A1 = e10_I - e10_inv(e10_J + e10_Rc)
chk("10 A0*", e10_A0, 0.395)
chk("10 A1*", e10_A1, 0.375)
e10_A = 0.385
e10_y = brentq(lambda y: e10_inv(y) - (e10_I - e10_A), e10_J, e10_J + e10_Rc)
chk("10 y*", e10_y, (1 - math.sqrt(0.08)) / 2)
chk("10 y* printed", e10_y, 0.358579, 1e-6)
chk("10 max liquidity need", e10_J + e10_Rc - e10_y, 0.141421, 1e-6)
chk("10 shortfall", (e10_J + e10_Rc - e10_y) ** 2 / 2, 0.01, 1e-9)
chk("10 surplus", (1 - (e10_J + e10_Rc)) ** 2 / 2, 0.125)
chk("10 net = I - A", 0.125 - (e10_J + e10_Rc - e10_y) ** 2 / 2, e10_I - e10_A, 1e-9)
# (iv) two equally likely states: y ~ U[0,1] or U[0,0.6]; threshold common
def e10_net(ys, b): return ((b ** 2 - ys ** 2) / 2 - (b - ys) * (e10_J + e10_Rc)) / b
def e10_npv(ys, b): return ((b ** 2 - ys ** 2) / 2 - (b - ys) * e10_J) / b
e10_A4 = 0.45
def e10_obj(ys1, ys2):
    return 0.5 * (e10_npv(ys1, 1.0) + e10_npv(ys2, 0.6))
def e10_cons(ys1, ys2):
    return 0.5 * (e10_net(ys1, 1.0) + e10_net(ys2, 0.6)) - (e10_I - e10_A4)
e10_yc = brentq(lambda y: e10_cons(y, y), e10_J, e10_J + e10_Rc)    # common threshold
e10_m = (e10_yc - e10_J) / e10_Rc                                     # mu/(1+mu)
e10_eps = 1e-4                                                        # perturb: shift between states
def e10_best_shift():
    def val(d):
        y2 = brentq(lambda y: e10_cons(e10_yc + d, y), e10_J, e10_J + e10_Rc)
        return e10_obj(e10_yc + d, y2)
    return val(e10_eps) <= val(0) + 1e-12 and val(-e10_eps) <= val(0) + 1e-12
ok("10 state-independent threshold is optimal", e10_best_shift())
chk("10 (iv) y* printed", e10_yc, 0.341886, 1e-6)
e10_minnet = min(e10_net(e10_yc, 1.0), e10_net(e10_yc, 0.6))
chk("10 (iv) outside liquidity needed", -e10_minnet, 0.0125, 1e-6)
chk("10 (iv) y* closed form", e10_yc, (1 - math.sqrt(0.1)) / 2, 1e-9)
chk("10 (iv) m", e10_m, 0.209431, 1e-6)
chk("10 (iv) good-state net", e10_net(e10_yc, 1.0), 0.1125, 1e-9)

# ---- Ex 11: Tirole 13.3, R(I) = I^0.5, pH = 0.8, B/dp = 0.5, K = 0.5, A = 0.1 ----
e11 = dict(al=0.5, pH=0.8, Bdp=0.5, K=0.5, A=0.1)
e11_b = e11["pH"] * e11["Bdp"]
def e11_IFB(P): return (e11["al"] * e11["pH"] * P) ** (1 / (1 - e11["al"]))
def e11_gap(I, P): return e11["pH"] * (P * I ** e11["al"] - e11["Bdp"] * I) - (I + e11["K"] - e11["A"])
def e11_ISB(P):
    IF = e11_IFB(P)
    Im = (e11["al"] * e11["pH"] * P / (1 + e11_b)) ** (1 / (1 - e11["al"]))   # max of the gap
    return IF if e11_gap(IF, P) >= 0 else brentq(lambda I: e11_gap(I, P), Im, IF)
e11_IFB0 = (e11["K"] - e11["A"]) / ((1 - e11["al"]) / e11["al"] - e11_b)
e11_P0 = e11_IFB0 ** (1 - e11["al"]) / (e11["al"] * e11["pH"])
chk("11 IFB(P0)", e11_IFB0, 2 / 3)
chk("11 P0", e11_P0, 2.041241, 1e-6)
chk("11 gap zero at P0", e11_gap(e11_IFB(e11_P0), e11_P0), 0, 1e-9)
ok("11 FB NPV covers K at P0", (1 - e11["al"]) / e11["al"] * e11_IFB0 >= e11["K"])
e11_sFB = e11_IFB0 / ((1 - e11["al"]) * e11_P0)
e11_sSB = e11_IFB0 / (e11["al"] * e11_P0 * e11_b)
chk("11 FB slope at P0", e11_sFB, 0.653197, 1e-6)
chk("11 SB slope at P0", e11_sSB, 1.632993, 1e-6)
chk("11 slope ratio", e11_sSB / e11_sFB, (1 - e11["al"]) / (e11["al"] * e11_b))
e11_P = 1.9
e11_dSB = (e11_ISB(e11_P + 1e-6) - e11_ISB(e11_P - 1e-6)) / 2e-6
e11_dFB = (e11_IFB(e11_P + 1e-6) - e11_IFB(e11_P - 1e-6)) / 2e-6
e11_I = e11_ISB(e11_P)
chk("11 dISB/dP formula", e11["pH"] * e11_I ** e11["al"]
    / (1 + e11_b - e11["al"] * e11["pH"] * e11_P * e11_I ** (e11["al"] - 1)), e11_dSB, 1e-5)
ok("11 SB steeper at P=1.9", e11_dSB > e11_dFB)
ok("11 SB below FB at P=1.9", e11_I < e11_IFB(e11_P))
chk("11 ISB(1.9)", e11_I, 0.406557, 1e-6)
chk("11 IFB(1.9)", e11_IFB(e11_P), 0.5776, 1e-9)

# ---- Ex 12: Tirole 15.1, R(X) = th X^al ----
e12 = dict(lam=0.3, pH=0.9, Bdp=1.0, th=2.0, al=0.8, A=0.2)
e12_b = e12["pH"] * e12["Bdp"]
def e12_R(X): return e12["th"] * X ** e12["al"]
def e12_inv(Rp): return (Rp / (e12["th"] * e12["al"])) ** (1 / (e12["al"] - 1))   # R'^{-1}
def e12_P(X): return e12["pH"] * (e12_R(X) - e12["Bdp"] * X)
def e12_solve(rho, q=1.0):
    """I, J, m = mu/(1+mu) from (1'), (3), (4'') with net need N(J) = rho J - P(J)."""
    lam, pH, b = e12["lam"], e12["pH"], e12_b
    def IJ(m):
        I = e12_inv((1 / (1 - lam) + m * b) / pH)
        J = e12_inv((rho + b * (1 - lam * (1 - m) / (lam + q - 1))) / pH)
        return I, J
    def be(m):
        I, J = IJ(m)
        N = rho * J - e12_P(J)
        return (1 - lam) * e12_P(I) + lam * (e12_P(J) - rho * J) - (q - 1) * N - I + e12["A"]
    m = brentq(be, 1e-9, 1 - 1e-9)
    return (*IJ(m), m)
e12_I, e12_J, e12_m = e12_solve(1.6)
ok("12 rho > 1/(1-lam) -> J < I", e12_J < e12_I)
e12_Iu, e12_Ju, _ = e12_solve(1.3)
ok("12 rho < 1/(1-lam) -> unconstrained J > I", e12_Ju > e12_Iu)
e12_N = 1.6 * e12_J - e12_P(e12_J)
ok("12 net need positive", e12_N > 0)
chk("12 I*", e12_I, 0.643244, 1e-6)
chk("12 J*", e12_J, 0.383471, 1e-6)
chk("12 L* (net)", e12_N, 0.122577, 1e-6)
chk("12 L* book convention rho J*", 1.6 * e12_J, 0.613554, 1e-6)
# (4'') verified by brute force: for q = 1.1 maximise Ub - (q-1)N subject to (1') binding
e12_q = 1.1
def e12_obj(J):
    lam, q = e12["lam"], e12_q
    N = 1.6 * J - e12_P(J)
    I = brentq(lambda I: (1 - lam) * e12_P(I) + lam * (e12_P(J) - 1.6 * J) - (q - 1) * N - I
               + e12["A"], 1e-3, 50)
    return (1 - lam) * e12["pH"] * e12_R(I) + lam * (e12["pH"] * e12_R(J) - 1.6 * J) - I - (q - 1) * N
e12_Jbf = argmax(e12_obj, 0.05, 0.9)
_, e12_Jq, _ = e12_solve(1.6, e12_q)
chk("12 (4'') matches brute force", e12_Jq, e12_Jbf, 1e-4)
ok("12 premium lowers J", e12_Jq < e12_J)
e12_V = (1 - e12["lam"]) * e12_P(e12_I) + e12["lam"] * e12_P(e12_J)
ok("12 (iii) V > lam rho J", e12_V > e12["lam"] * 1.6 * e12_J)
e12_lhs, e12_rhs = (1 - e12["lam"]) * e12_P(e12_I), (1 + e12["lam"]) * e12_N
ok("12 (iii) index condition holds here", e12_lhs >= e12_rhs)
chk("12 (iii) index lhs", e12_lhs, 0.480017, 1e-6)
chk("12 (iii) index rhs", e12_rhs, 0.159350, 1e-6)
chk("12 m = mu/(1+mu)", e12_m, 0.160310, 1e-6)
chk("12 J at q=1.1", e12_Jq, 0.239918, 1e-6)
chk("12 rho=1.3 unconstrained I", e12_Iu, 0.552051, 1e-6)
chk("12 rho=1.3 unconstrained J", e12_Ju, 0.834348, 1e-6)

# ---- Ex 13: Tirole 15.4 ----
e13 = dict(lam=0.5, rL=0.2, r0=0.6, rH=1.0, r1=2.0, A=1.0)
e13_rbar = (1 - e13["lam"]) * e13["rL"] + e13["lam"] * e13["rH"]
ok("13 assumption", (1 - e13["lam"]) * e13["r1"] < 1 + (1 - e13["lam"]) * e13["rL"])
ok("13 positive NPV with x=1", e13["r1"] > 1 + e13_rbar)
e13_qq = 1 + (e13["r1"] - 1 - e13_rbar) / (e13["rH"] - e13["r0"])
e13_Llo = (e13["rH"] - e13["r0"]) * e13["A"] / (e13["r1"] - e13["r0"])
e13_Lhi = (e13["rH"] - e13["r0"]) * e13["A"] / (1 + e13_rbar - e13["r0"])
chk("13 qbarbar", e13_qq, 2.0)
chk("13 L_low", e13_Llo, 0.285714, 1e-6)
chk("13 L_high", e13_Lhi, 0.4)
ok("13 x=1 at qbarbar", e13["lam"] * e13["r1"] > e13["lam"] * e13["rH"]
   + (e13_qq - 1) * (e13["rH"] - e13["r0"]))
def e13_eq(LS):
    if LS <= e13_Llo:
        return e13_qq, LS / (e13["rH"] - e13["r0"])
    if LS <= e13_Lhi:
        I = LS / (e13["rH"] - e13["r0"])
        q = 1 + (e13["A"] / I - 1 - e13_rbar + e13["r0"]) / (e13["rH"] - e13["r0"])
        return q, I
    return 1.0, e13["A"] / (1 + e13_rbar - e13["r0"])
chk("13 q(0.35)", e13_eq(0.35)[0], 1.357143, 1e-6)
chk("13 I(0.35)", e13_eq(0.35)[1], 0.875)
chk("13 I(0.2)", e13_eq(0.2)[1], 0.5)
e13_grid = [0.05 * k for k in range(1, 11)]
ok("13 I nondecreasing in LS", all(e13_eq(a)[1] <= e13_eq(b)[1] + 1e-12
                                    for a, b in zip(e13_grid, e13_grid[1:])))
chk("13 continuity at L_low", e13_eq(e13_Llo + 1e-12)[0], e13_qq, 1e-6)

# ---- Ex 14: Tirole 13.2 ----
e14_a, e14_Ah, e14_r1, e14_r0, e14_Imin = 0.4, 1.0, 1.5, 0.5, 3.5
for e14_y in (0.7, 2.0):
    e14_c, e14_L = (1 - e14_a) * e14_y, e14_a * e14_y
    chk(f"14 warm glow U(y={e14_y})", (e14_c / (1 - e14_a)) ** (1 - e14_a) * (e14_L / e14_a) ** e14_a,
        e14_y, 1e-12)
def e14_beta(r): return e14_a * (e14_r1 - e14_r0) / (1 - e14_r0 / (1 + r))
e14_r = 0.05
e14_Ainf = e14_Ah / (1 - e14_beta(e14_r))
e14_At = 10.0
for _ in range(400):
    e14_At = e14_Ah + e14_a * (e14_r1 - e14_r0) * e14_At / (1 - e14_r0 / (1 + e14_r))
chk("14 convergence to A_inf", e14_At, e14_Ainf, 1e-9)
chk("14 A_inf(r=0.05)", e14_Ainf, 4.230769, 1e-6)
e14_A0s = (1 - e14_r0 / (1 + e14_r)) * e14_Imin
e14_AL = e14_Ah / (1 - e14_a * (1 + e14_r))
chk("14 A0*", e14_A0s, 1.833333, 1e-6)
chk("14 A_inf^L", e14_AL, 1.724138, 1e-6)
ok("14 poverty trap: A_L < A0* <= A_inf", e14_AL < e14_A0s <= e14_Ainf)
e14_Iinf = e14_Ainf / (1 - e14_r0 / (1 + e14_r))
e14_k = (e14_Iinf - e14_Ainf) / (e14_AL + e14_Iinf - e14_Ainf)
chk("14 kappa unequal", e14_k, 0.690476, 1e-6)
chk("14 loan market unequal", e14_k * e14_AL, (1 - e14_k) * (e14_Iinf - e14_Ainf), 1e-12)
e14_Aeq = e14_Ah / (1 - e14_a * e14_r1)
e14_Ieq = e14_r1 * e14_Ah / ((1 - e14_a * e14_r1) * (e14_r1 - e14_r0))
chk("14 A_inf equal", e14_Aeq, 2.5)
chk("14 I_inf equal", e14_Ieq, 3.75)
chk("14 kappa equal = rho0/rho1", (e14_Ieq - e14_Aeq) / e14_Ieq, e14_r0 / e14_r1, 1e-12)
chk("14 beta at 1+r = rho1", e14_beta(e14_r1 - 1), e14_a * e14_r1, 1e-12)
ok("14 equal SS feasible", e14_Ieq >= e14_Imin and e14_Aeq >= (1 - e14_r0 / e14_r1) * e14_Imin)
chk("14 A0* at 1+r = rho1", (1 - e14_r0 / e14_r1) * e14_Imin, 7 / 3)
chk("14 beta(0.05)", e14_beta(e14_r), 0.763636, 1e-6)
chk("14 I_inf(r=0.05)", e14_Iinf, 8.076923, 1e-6)

# ---- Ex 15: Tirole 16.3, u = U log c, v = kap log g ----
e15 = dict(pH=0.8, R=2.0, r0=0.4, S=0.3, A=1.0, Rs=2.0, kap=1.0, U=6.0)
def e15_I(e): return e15["A"] / (1 - (e15["S"] / e + e15["r0"]))
def e15_e_commit(g):   # p_H R I(e) + R* - g = U/e + I(e) - A  (c1*(e) = U/e from u' = e)
    return brentq(lambda e: e15["pH"] * e15["R"] * e15_I(e) + e15["Rs"] - g - e15["U"] / e
                  - e15_I(e) + e15["A"], 0.7, 50)
def e15_Wc(g):
    e = e15_e_commit(g)
    return e15["S"] * e15_I(e) + e15["U"] * math.log(e15["U"] / e) + e15["kap"] * math.log(g)
e15_gc = argmax(e15_Wc, 0.01, 1.9)
e15_ec = e15_e_commit(e15_gc)
ok("16.3 e increasing in g (commitment)", e15_e_commit(e15_gc + 0.01) > e15_ec)
ok("16.3 underspending v' > e", e15["kap"] / e15_gc > e15_ec)
e15_de = (e15_e_commit(e15_gc + 1e-6) - e15_e_commit(e15_gc - 1e-6)) / 2e-6
e15_dI = (e15_I(e15_ec + 1e-6) - e15_I(e15_ec - 1e-6)) / 2e-6
chk("16.3 commitment FOC", e15["kap"] / e15_gc,
    e15_ec * (1 - (e15["S"] / e15_ec + e15["pH"] * e15["R"] - 1) * e15_dI * e15_de), 1e-5)
def e15_e_ex(g, Ib):   # fixed I: d* = r0 I, d = S I
    return (e15["U"] + e15["S"] * Ib) / (e15["pH"] * e15["R"] * Ib + e15["Rs"] - g - e15["r0"] * Ib)
def e15_g_nc(Ib):
    return argmax(lambda g: e15["S"] * Ib + e15["U"] * math.log(e15["U"] / e15_e_ex(g, Ib))
                  + e15["kap"] * math.log(g),
                  0.01, 1.99)
def e15_fp(e):         # rational expectations: e used in I(e) equals ex post e
    Ib = e15_I(e)
    return e15_e_ex(e15_g_nc(Ib), Ib) - e
e15_enc = brentq(e15_fp, 1.5, 2.0)
e15_Inc = e15_I(e15_enc)
e15_gnc = e15_g_nc(e15_Inc)
ok("16.3 overspending v' < e", e15["kap"] / e15_gnc < e15_enc)
e15_dex = (e15_e_ex(e15_gnc + 1e-6, e15_Inc) - e15_e_ex(e15_gnc - 1e-6, e15_Inc)) / 2e-6
chk("16.3 noncommitment FOC", e15["kap"] / e15_gnc,
    e15_enc * (1 - e15["S"] * e15_Inc / e15_enc ** 2 * e15_dex), 1e-5)
ok("16.3 g higher, e higher, I lower without commitment",
   e15_gnc > e15_gc and e15_enc > e15_ec and e15_Inc < e15_I(e15_ec))
ok("16.3 welfare lower without commitment", e15_Wc(e15_gnc) < e15_Wc(e15_gc))
chk("16.3 g commit", e15_gc, 0.508893, 1e-5)
chk("16.3 e commit", e15_ec, 1.504114, 1e-5)
chk("16.3 g noncommit", e15_gnc, 0.701486, 1e-5)
chk("16.3 e noncommit", e15_enc, 1.598417, 1e-5)
chk("16.3 I(e) identity", e15_I(2.0), 1 / 0.45)
chk("16.3 I commit", e15_I(e15_ec), 2.496585, 1e-5)
chk("16.3 I noncommit", e15_Inc, 2.425335, 1e-5)
chk("16.3 v' commit", e15["kap"] / e15_gc, 1.965050, 1e-5)
chk("16.3 v' noncommit", e15["kap"] / e15_gnc, 1.425545, 1e-5)
chk("16.3 W commit", e15_Wc(e15_gc), 8.374789, 1e-5)
chk("16.3 W noncommit", e15_Wc(e15_gnc), 8.309522, 1e-5)

# ---- intermediate numbers displayed in the solutions ----
chk("1 A*(B=0.3) 4dp", 1 - 0.6 / (1 + e1_r1), 0.4224, 1e-4)
chk("3 I - A", e3_I - e3["A"], 0.190476, 1e-6)
chk("3 (rH - r0) I", (e3["rH"] - e3["r0"]) * e3_I, 0.476190, 1e-6)
chk("4 ln(4/3)", math.log(4 / 3), 0.287682, 1e-6)
chk("6 R'(1) - R'(2)", 1 - 1 / math.sqrt(2), 0.292893, 1e-6)
chk("6 R'(0.25) - R'(0.5)", 2 - math.sqrt(2), 0.585786, 1e-6)
chk("8 c(1)", e8_c(1), 1.48)
chk("13 Ibar", e13["A"] / (e13["r1"] - e13["r0"]), 0.714286, 1e-6)
chk("14 I_inf - A_inf", e14_Iinf - e14_Ainf, 3.846154, 1e-6)

print(f"PASS {N} checks")
