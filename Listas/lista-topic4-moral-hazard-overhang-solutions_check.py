"""Numeric checks for Listas/lista-topic4-moral-hazard-overhang-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-topic4-moral-hazard-overhang-solutions_check.py  -> PASS <n> checks
"""
import math  # noqa: F401  (fragments use it)

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1

# ======================================================================
# t4a
# Topic 4 list, exercises 1-8. Run after check_header.py (defines chk). Amounts in $ million.

# --- Ex 1: DIP financing (Lily example, G&T pp. 564-566; lecture Topic 4B slides 22-31)
e1_F, e1_I, e1_X = 110, 100, 150
chk("1 junior max", max(0 + e1_X - e1_F, 0), 40)
chk("1 NPV Lily", e1_X - e1_I, 50)
chk("1 old debt with DIP", min(0 + e1_X - e1_I, e1_F), 50)
e1_V = {"boom": 500, "slump": 200}
e1_Fl, e1_Il, e1_add, e1_p = 300, 60, 100, 0.5
e1_D0 = sum(e1_p * min(v, e1_Fl) for v in e1_V.values())
e1_E0 = sum(e1_p * max(v - e1_Fl, 0) for v in e1_V.values())
chk("1 D0", e1_D0, 250)
chk("1 E0", e1_E0, 100)
e1_old = {s: min(v + e1_add - e1_Il, e1_Fl) for s, v in e1_V.items()}
chk("1 old boom", e1_old["boom"], 300)
chk("1 old slump", e1_old["slump"], 240)
e1_D1 = sum(e1_p * x for x in e1_old.values())
e1_eq = {s: max(v + e1_add - e1_Il - e1_Fl, 0) for s, v in e1_V.items()}
chk("1 eq boom", e1_eq["boom"], 240)
chk("1 eq slump", e1_eq["slump"], 0)
e1_E1 = sum(e1_p * x for x in e1_eq.values())
chk("1 D1", e1_D1, 270)
chk("1 E1", e1_E1, 120)
chk("1 dD", e1_D1 - e1_D0, 20)
chk("1 dE", e1_E1 - e1_E0, 20)
chk("1 NPV lecture", e1_add - e1_Il, 40)
chk("1 sum = NPV", (e1_D1 - e1_D0) + (e1_E1 - e1_E0), e1_add - e1_Il)

# --- Ex 2: G&T 16.1
e2_p, e2_C, e2_F = 0.5, 100, 100
e2_X = {"A": (120, 60), "B": (101, 101)}
e2_V = {j: e2_p * a + (1 - e2_p) * b for j, (a, b) in e2_X.items()}
chk("2 VA", e2_V["A"], 90)
chk("2 NPVA", e2_V["A"] - e2_C, -10)
chk("2 VB", e2_V["B"], 101)
chk("2 NPVB", e2_V["B"] - e2_C, 1)
e2_eq = {j: [max(x - e2_F, 0) for x in xs] for j, xs in e2_X.items()}
e2_dt = {j: [min(x, e2_F) for x in xs] for j, xs in e2_X.items()}
for got, want in zip(e2_eq["A"] + e2_eq["B"], [20, 0, 1, 1]):
    chk("2 equity state", got, want)
for got, want in zip(e2_dt["A"] + e2_dt["B"], [100, 60, 100, 100]):
    chk("2 debt state", got, want)
e2_E = {j: e2_p * a + (1 - e2_p) * b for j, (a, b) in e2_eq.items()}
e2_D = {j: e2_p * a + (1 - e2_p) * b for j, (a, b) in e2_dt.items()}
chk("2 EA", e2_E["A"], 10)
chk("2 DA", e2_D["A"], 80)
chk("2 EB", e2_E["B"], 1)
chk("2 DB", e2_D["B"], 100)
chk("2 dV", e2_V["A"] - e2_V["B"], -11)
chk("2 dD", e2_D["A"] - e2_D["B"], -20)
chk("2 EA-EB", e2_E["A"] - e2_E["B"], 9)
chk("2 split", (e2_V["A"] - e2_V["B"]) - (e2_D["A"] - e2_D["B"]), 9)

# --- Ex 3: Berk 16.25
e3_F, e3_r, e3_L0, e3_L1, e3_K = 15, 0.10, 10, 35, 20
e3_Da = min(e3_L0, e3_F) / (1 + e3_r)
e3_Ea = max(e3_L0 - e3_F, 0) / (1 + e3_r)
chk("3 Da", e3_Da, 9.0909, 5e-5)
chk("3 Ea", e3_Ea, 0)
chk("3 PV incr", (e3_L1 - e3_L0) / (1 + e3_r), 22.7273, 5e-5)
e3_NPV = -e3_K + (e3_L1 - e3_L0) / (1 + e3_r)
chk("3 NPV", e3_NPV, 2.7273, 5e-5)
chk("3 gross NPV", -e3_K + e3_L1 / (1 + e3_r), 11.8182, 5e-5)
e3_Dc = min(e3_L1, e3_F) / (1 + e3_r)
e3_Ec = max(e3_L1 - e3_F, 0) / (1 + e3_r)
chk("3 Dc", e3_Dc, 13.6364, 5e-5)
chk("3 Ec", e3_Ec, 18.1818, 5e-5)
chk("3 dE", e3_Ec - e3_Ea - e3_K, -1.8182, 5e-5)
chk("3 dD", e3_Dc - e3_Da, 4.5455, 5e-5)
chk("3 sum = NPV", (e3_Ec - e3_Ea - e3_K) + (e3_Dc - e3_Da), e3_NPV)
chk("3 overhang gap", e3_F - e3_L0, 5)
for got, want in [(e3_Da, 9.09), (e3_NPV, 2.73), (e3_Ec, 18.18), (e3_Dc, 13.64),
                  (e3_Ec - e3_K, -1.82), (e3_Dc - e3_Da, 4.55)]:
    chk("3 short rounding", got, want, 5e-3)

# --- Ex 4: short-term debt illustration with Ex 2 numbers
e4_L = 100
chk("4 EA", e2_V["A"] - e4_L, -10)
chk("4 EB", e2_V["B"] - e4_L, 1)
chk("4 max raise under A < L", float(e2_V["A"] < e4_L), 1)

# --- Ex 5: Tirole 3.1 at one parameter point
e5_I, e5_R, e5_pH, e5_pL, e5_B, e5_A = 100, 150, 0.8, 0.4, 30, 10
e5_dp = e5_pH - e5_pL
chk("5 (3.2)", e5_pL * e5_R - e5_I + e5_B, -10)
chk("5 B/dp", e5_B / e5_dp, 75)
e5_P = e5_pH * (e5_R - e5_B / e5_dp)
chk("5 P", e5_P, 60)
e5_Abar = e5_I - e5_P
chk("5 Abar", e5_Abar, 40)
chk("5 Abar (3.3)", e5_pH * e5_B / e5_dp - (e5_pH * e5_R - e5_I), 40)
chk("5 NPV", e5_pH * e5_R - e5_I, 20)
e5_x = e5_A / e5_Abar
chk("5 x*", e5_x, 0.25)
e5_Ub = e5_x * (e5_pH * e5_R - e5_I)
chk("5 Ub*", e5_Ub, 5)
chk("5 investor outlay", e5_x * e5_I - e5_A, 15)
chk("5 investor return", e5_x * e5_P, 15)
# R_b from binding breakeven at x*: x pH (R - Rb) = x I - A
e5_Rb = e5_R - (e5_x * e5_I - e5_A) / (e5_x * e5_pH)
chk("5 Rb = B/dp", e5_Rb, e5_B / e5_dp)
chk("5 Ub identity (3)", e5_x * e5_pH * e5_Rb - e5_A, e5_Ub)
# shirking bound: x(pL Rb + B) - Ahat <= x(pL R + B - I) at an arbitrary Rb < B/dp with binding IR
e5_Rs = 50
e5_Ahat_s = e5_x * e5_I - e5_x * e5_pL * (e5_R - e5_Rs)
chk("5 shirk payoff", e5_x * (e5_pL * e5_Rs + e5_B) - e5_Ahat_s, e5_x * (e5_pL * e5_R + e5_B - e5_I))
# deferred-payment reading fails: x(I - Ahat) <= x P needs Ahat >= Abar
chk("5 alt reading", float(e5_I - e5_A > e5_P), 1)

# --- Ex 6: Berk 16.26 Zymase
e6_S = {"A": [(1.0, 75)], "B": [(0.5, 140), (0.5, 0)], "C": [(0.1, 300), (0.9, 40)]}
e6_EX = {j: sum(p * x for p, x in st) for j, st in e6_S.items()}
chk("6 EXA", e6_EX["A"], 75)
chk("6 EXB", e6_EX["B"], 70)
chk("6 EXC", e6_EX["C"], 66)
chk("6 C parts", 0.1 * 300 + 0 * 0, 30)
chk("6 C parts2", 0.9 * 40, 36)


def e6_claims(F):
    eq = {j: sum(p * max(x - F, 0) for p, x in st) for j, st in e6_S.items()}
    dt = {j: sum(p * min(x, F) for p, x in st) for j, st in e6_S.items()}
    return eq, dt


e6_E40, e6_D40 = e6_claims(40)
chk("6 E40 A", e6_E40["A"], 35)
chk("6 E40 B", e6_E40["B"], 50)
chk("6 E40 C", e6_E40["C"], 26)
chk("6 states 40", (140 - 40) + (300 - 40), 100 + 260)
chk("6 D40 B", e6_D40["B"], 20)
chk("6 D40 A", e6_D40["A"], 40)
chk("6 D40 C", e6_D40["C"], 40)
chk("6 choice 40", float(max(e6_E40, key=e6_E40.get) == "B"), 1)
e6_E110, e6_D110 = e6_claims(110)
chk("6 E110 A", e6_E110["A"], 0)
chk("6 E110 B", e6_E110["B"], 15)
chk("6 E110 C", e6_E110["C"], 19)
chk("6 states 110", (140 - 110) + (300 - 110), 30 + 190)
chk("6 D110 C", e6_D110["C"], 47)
chk("6 D110 C parts", 0.1 * 110, 11)
chk("6 D110 A", e6_D110["A"], 75)
chk("6 D110 B", e6_D110["B"], 55)
chk("6 choice 110", float(max(e6_E110, key=e6_E110.get) == "C"), 1)
chk("6 cost40", e6_EX["A"] - e6_EX["B"], 5)
chk("6 cost110", e6_EX["A"] - e6_EX["C"], 9)
chk("6 E+D=V (110,C)", e6_E110["C"] + e6_D110["C"], e6_EX["C"])

# --- Ex 7: G&T 16.12-16.13 Ajax
e7_F, e7_I, e7_pi = 70, 75, 0.2
e7_X1 = (85, 150)
e7_X2 = (5, 170)


def e7_ev(xs):
    return e7_pi * xs[0] + (1 - e7_pi) * xs[1]


chk("7 V parts", e7_pi * e7_X1[0], 17)
chk("7 V parts2", (1 - e7_pi) * e7_X1[1], 120)
chk("7 V", e7_ev(e7_X1), 137)
chk("7 NPV", e7_ev(e7_X1) - e7_I, 62)
e7_eq1 = tuple(max(x - e7_F, 0) for x in e7_X1)
chk("7 eq rec", e7_eq1[0], 15)
chk("7 eq fav", e7_eq1[1], 80)
chk("7 E parts", e7_pi * e7_eq1[0], 3)
chk("7 E parts2", (1 - e7_pi) * e7_eq1[1], 64)
e7_E1 = e7_ev(e7_eq1)
chk("7 Emax", e7_E1, 67)
chk("7 not fundable", float(e7_E1 < e7_I), 1)
e7_D1 = e7_ev(tuple(min(x, e7_F) for x in e7_X1))
chk("7 D safe", e7_D1, 70)
chk("7 split", e7_D1 + (e7_E1 - e7_I), 62)
chk("7 V2 parts", e7_pi * e7_X2[0], 1)
chk("7 V2 parts2", (1 - e7_pi) * e7_X2[1], 136)
chk("7 V2", e7_ev(e7_X2), 137)
chk("7 NPV2", e7_ev(e7_X2) - e7_I, 62)
e7_eq2 = tuple(max(x - e7_F, 0) for x in e7_X2)
chk("7 eq2 rec", e7_eq2[0], 0)
chk("7 eq2 fav", e7_eq2[1], 100)
e7_E2 = e7_ev(e7_eq2)
chk("7 E2", e7_E2, 80)
chk("7 fraction", e7_I / e7_E2, 0.9375)
chk("7 old share", 1 - e7_I / e7_E2, 0.0625)
chk("7 old value", e7_E2 - e7_I, 5)
e7_D2 = e7_ev(tuple(min(x, e7_F) for x in e7_X2))
chk("7 D2", e7_D2, 57)
chk("7 D2 parts2", (1 - e7_pi) * e7_F, 56)
chk("7 D2+E2", e7_D2 + e7_E2, 137)
chk("7 transfer", e7_D1 - e7_D2, 13)
chk("7 transfer2", e7_E2 - e7_E1, 13)
# renegotiated face under the safe process: equity worth >= I iff F' <= V - I (when F' <= 85)
e7_Fr = e7_ev(e7_X1) - e7_I
chk("7 F' max", e7_Fr, 62)
chk("7 equity at F'", e7_ev(tuple(max(x - e7_Fr, 0) for x in e7_X1)), e7_I)
chk("7 F' > D2", float(e7_Fr > e7_D2), 1)

# --- Ex 8: Tirole 3.15
def e8_Abar(I, pH, R, B, dp):
    return pH * B / dp - (pH * R - I)


# identity Abar^A - Abar^B = (pHA - pHB) B/dp at the numerical point of Step 4
e8_I, e8_dp, e8_B = 100, 0.2, 9
e8_pHA, e8_RA, e8_pHB, e8_RB = 0.8, 150, 0.6, 200
e8_pLA, e8_pLB = e8_pHA - e8_dp, e8_pHB - e8_dp
chk("8 pLA", e8_pLA, 0.6)
chk("8 pLB", e8_pLB, 0.4)
chk("8 equal pHR", e8_pHA * e8_RA, e8_pHB * e8_RB)
chk("8 NPV", e8_pHA * e8_RA - e8_I, 20)
chk("8 (3.2) A", e8_pLA * e8_RA - e8_I + e8_B, -1)
chk("8 (3.2) B", e8_pLB * e8_RB - e8_I + e8_B, -11)
chk("8 B/dp", e8_B / e8_dp, 45)
chk("8 RA-B/dp", e8_RA - e8_B / e8_dp, 105)
chk("8 RB-B/dp", e8_RB - e8_B / e8_dp, 155)
e8_PA = e8_pHA * (e8_RA - e8_B / e8_dp)
e8_PB = e8_pHB * (e8_RB - e8_B / e8_dp)
chk("8 PA", e8_PA, 84)
chk("8 PB", e8_PB, 93)
chk("8 AbarA", e8_I - e8_PA, 16)
chk("8 AbarB", e8_I - e8_PB, 7)
chk("8 AbarA (3.3)", e8_Abar(e8_I, e8_pHA, e8_RA, e8_B, e8_dp), 16)
chk("8 AbarB (3.3)", e8_Abar(e8_I, e8_pHB, e8_RB, e8_B, e8_dp), 7)
chk("8 diff", (e8_I - e8_PA) - (e8_I - e8_PB), 9)
chk("8 diff formula", (e8_pHA - e8_pHB) * e8_B / e8_dp, 9)
chk("8 nonpledgeable A", e8_pHA * e8_B / e8_dp, 36)
chk("8 nonpledgeable B", e8_pHB * e8_B / e8_dp, 27)
# second point for the identity
chk("8 identity pt2", e8_Abar(50, 0.9, 10, 2, 0.5) - e8_Abar(50, 0.7, 9 / 0.7, 2, 0.5), 0.2 * 2 / 0.5)
# book's extension example, A = 0
x_A, x_I, x_dp, x_B = 0, 120, 0.3, 45
x_pHA, x_RA, x_pHB, x_RB = 0.9, 200, 0.5, 360
x_pLA, x_pLB = x_pHA - x_dp, x_pHB - x_dp
chk("8x pHR A", x_pHA * x_RA, 180)
chk("8x pHR B", x_pHB * x_RB, 180)
chk("8x B/dp", x_B / x_dp, 150)
chk("8x RB-B/dp", x_RB - x_B / x_dp, 210)
chk("8x PB", x_pHB * (x_RB - x_B / x_dp), 105)
chk("8x pLB RB", x_pLB * x_RB, 72)
chk("8x pLA RA", x_pLA * x_RA, 120)
chk("8x pLA RA + B", x_pLA * x_RA + x_B, 165)
chk("8x cond1", float(x_I - x_A > x_pHB * (x_RB - x_B / x_dp)), 1)
chk("8x cond2", float(x_I - x_A > x_pLB * x_RB), 1)
chk("8x cond3", float(x_I - x_A <= x_pLA * x_RA + 1e-9), 1)
chk("8x cond4", float(x_I < x_pLA * x_RA + x_B), 1)
chk("8x B NPV under shirking < 0", float(x_pLB * x_RB + x_B - x_I < 0), 1)

# ======================================================================
# t4b
# Checks for t4b fragments (exercises 9-15 of lista-topic4). Run after check_header.py (defines chk).
# Symbolic results are checked at parameter points; printed numbers are reproduced.

# ---------------------------------------------------------------- Ex 9 (Tirole 3.2)
e9_pH, e9_pL, e9_B, e9_R, e9_I, e9_c0 = 0.8, 0.4, 1.0, 10.0, 6.5, 1.0
e9_dp = e9_pH - e9_pL
assert e9_I > e9_pH * (e9_R - e9_B / e9_dp) and e9_pL * e9_R + e9_B < e9_I
e9_Abar_rn = e9_I - e9_pH * (e9_R - e9_B / e9_dp)
e9_Abar = e9_I + e9_c0 - e9_pH * (e9_R - e9_B / e9_dp)
chk("9 Abar risk neutral", e9_Abar_rn, 0.5)
chk("9 Abar c0", e9_Abar, 1.5)
chk("9 Abar = Abar_rn + c0", e9_Abar, e9_Abar_rn + e9_c0)
# same Abar from the general formula A_min = pH h(c_min) + (1-pH) c_min - NPV, h(c)=c+B/dp
e9_NPV = e9_pH * e9_R - e9_I
chk("9 general floor formula", e9_pH * (e9_c0 + e9_B / e9_dp) + (1 - e9_pH) * e9_c0 - e9_NPV, e9_Abar)
chk("9 pH=1 threshold", e9_I + e9_c0 - e9_R, -2.5)
# brute force of (i): min expected payment pH cS + (1-pH) cF s.t. cF,cS >= c0, dp (cS-cF) >= B
e9_best = min(e9_pH * cs + (1 - e9_pH) * cf
              for cf in [e9_c0 + 0.01 * k for k in range(300)]
              for cs in [cf + e9_B / e9_dp + 0.01 * j for j in range(300)])
chk("9 min rent = c0 + pH B/dp", e9_best, e9_c0 + e9_pH * e9_B / e9_dp, 1e-9)

# (ii) u = sqrt(c) (c >= 0 is the limited-liability floor, u(0)=0). B in utils.
import math
e9_u = math.sqrt
e9_uinv = lambda v: v * v
e9_h = lambda c: e9_uinv(e9_u(c) + e9_B / e9_dp)
e9_ALL = e9_I - e9_pH * e9_R + e9_pH * e9_h(0.0)
chk("9 A_LL sqrt", e9_ALL, 6.5 - 8 + 0.8 * 6.25)
def e9_bind(A):
    """cF solving pH h(c) + (1-pH) c = A + NPV (bisection)."""
    lo, hi = 0.0, 100.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if e9_pH * e9_h(m) + (1 - e9_pH) * m < A + e9_NPV: lo = m
        else: hi = m
    return lo
e9_A = 5.0
e9_cF = e9_bind(e9_A); e9_cS = e9_h(e9_cF)
e9_V = e9_pH * e9_u(e9_cS) + (1 - e9_pH) * e9_u(e9_cF)
chk("9 V = u(cF) + pH B/dp", e9_V, e9_u(e9_cF) + e9_pH * e9_B / e9_dp, 1e-9)
# grid search of the program at A=5: for each cF the objective rises in cS, so cS is the largest
# value the budget allows; scan cF and keep IC-feasible points
e9_gbest = -1e9
for i in range(0, 200001):
    cf = 0.00005 * i
    cs = (e9_A + e9_NPV - (1 - e9_pH) * cf) / e9_pH
    if e9_dp * (e9_u(cs) - e9_u(cf)) >= e9_B - 1e-12:
        e9_gbest = max(e9_gbest, e9_pH * e9_u(cs) + (1 - e9_pH) * e9_u(cf))
chk("9 grid optimum = binding solution", e9_gbest, e9_V, 1e-4)
assert e9_cF > 0  # insurance in failure: debt (cF=0) not optimal above A_LL
# infeasible below A_LL: at cF=0 the cheapest IC contract costs pH h(0) > A + NPV
assert e9_pH * e9_h(0.0) > (e9_ALL - 0.1) + e9_NPV

# ---------------------------------------------------------------- Ex 10 (Tirole 3.18)
e10_RS, e10_RF, e10_pH, e10_pL, e10_B, e10_I, e10_A = 12.0, 2.0, 0.8, 0.4, 1.6, 9.0, 3.0
e10_dp = e10_pH - e10_pL; e10_R = e10_RS - e10_RF
e10_NPV = e10_pH * e10_RS + (1 - e10_pH) * e10_RF - e10_I
e10_Abar = e10_I - e10_RF - e10_pH * (e10_R - e10_B / e10_dp)
chk("10 Abar two forms", e10_Abar, e10_pH * e10_B / e10_dp - e10_NPV)
e10_D = (e10_I - e10_A - (1 - e10_pH) * e10_RF) / e10_pH
assert e10_RF < e10_D <= e10_RS - e10_B / e10_dp
chk("10 lenders break even under debt", e10_pH * e10_D + (1 - e10_pH) * e10_RF, e10_I - e10_A)
e10_RbFmax = e10_A - e10_Abar
e10_RbS = (e10_A + e10_NPV - (1 - e10_pH) * e10_RbFmax) / e10_pH
chk("10 IC binds at RbF max", e10_dp * (e10_RbS - e10_RbFmax), e10_B, 1e-9)
chk("10 payoff = A + NPV", e10_pH * e10_RbS + (1 - e10_pH) * e10_RbFmax, e10_A + e10_NPV, 1e-9)

# ---------------------------------------------------------------- Ex 11 (Tirole 3.11)
e11_I2, e11_R2, e11_pH2, e11_pL2 = 20.0, 40.0, 0.75, 0.25
e11_dp2 = e11_pH2 - e11_pL2
e11_Blo, e11_Bhi = 7.0, 9.0
e11_NPV2 = e11_pH2 * e11_R2 - e11_I2
chk("11 NPV2", e11_NPV2, 10.0)
e11_Bmin_req = e11_dp2 * e11_NPV2 / e11_pH2
chk("11 B2 lower-bound requirement", e11_Bmin_req, 20 / 3)
assert e11_Blo > e11_Bmin_req and e11_pL2 * e11_R2 + e11_Bhi < e11_I2
e11_Bhat = lambda R: e11_dp2 * (e11_NPV2 + R) / e11_pH2
e11_F = lambda b: min(1.0, max(0.0, (b - e11_Blo) / (e11_Bhi - e11_Blo)))
e11_W = lambda R: R + e11_F(e11_Bhat(R)) * e11_NPV2
chk("11 Bhat(0)", e11_Bhat(0.0), 20 / 3)
chk("11 range low", (e11_Blo * e11_pH2 / e11_dp2) - e11_NPV2, 0.5)
chk("11 range high", (e11_Bhi * e11_pH2 / e11_dp2) - e11_NPV2, 3.5)
e11_mu = 1 + (1 / (e11_Bhi - e11_Blo)) * (e11_dp2 / e11_pH2) * e11_NPV2
chk("11 mu", e11_mu, 13 / 3)
chk("11 mu numeric slope", (e11_W(2.0 + 1e-6) - e11_W(2.0 - 1e-6)) / 2e-6, 13 / 3, 1e-5)
chk("11 W(R) = (13R-5)/3 at R=2", e11_W(2.0), (13 * 2 - 5) / 3)
e11_I1, e11_R1, e11_pH1, e11_pL1, e11_B1 = 4.5, 10.0, 0.5, 0.25, 0.5
e11_dp1 = e11_pH1 - e11_pL1
assert e11_pL1 * e11_R1 + e11_B1 < e11_I1 < e11_pH1 * e11_R1
chk("11 B1/dp1", e11_B1 / e11_dp1, 2.0)
e11_Abar1 = e11_I1 - e11_pH1 * (e11_R1 - e11_B1 / e11_dp1)
chk("11 Abar1 alone", e11_Abar1, 0.5)
e11_Rt = (3 * e11_B1 / e11_dp1 + 5) / 13
chk("11 Rtilde", e11_Rt, 11 / 13)
chk("11 Rtilde value", e11_Rt, 0.846154, 1e-6)
chk("11 W(Rtilde) = B1/dp1", e11_W(e11_Rt), e11_B1 / e11_dp1, 1e-12)
e11_PI = e11_pH1 * (e11_R1 - e11_Rt)
chk("11 pledgeable with project 2", e11_PI, 119 / 26)
chk("11 pledgeable value", e11_PI, 4.576923, 1e-6)
chk("11 new threshold", e11_I1 - e11_PI, -1 / 13)
chk("11 new threshold value", e11_I1 - e11_PI, -0.076923, 1e-6)
e11_Rb_A0 = e11_R1 - e11_I1 / e11_pH1
chk("11 Rb1 at A1=0", e11_Rb_A0, 1.0)
assert e11_Rb_A0 >= e11_Rt
chk("11 pledgeable alone", e11_pH1 * (e11_R1 - e11_B1 / e11_dp1), 4.0)

# ---------------------------------------------------------------- Ex 12 (Tirole 3.6)
e12_pH, e12_pL, e12_R, e12_B, e12_A = 0.9, 0.6, 1.25, 0.2, 1.0
e12_dp = e12_pH - e12_pL
assert e12_pH * e12_R > 1 > e12_pL * e12_R + e12_B and e12_pH * e12_R < 1 + e12_pH * e12_B / e12_dp
e12_k = 1 / (1 - e12_pH * (e12_R - e12_B / e12_dp))
def e12_reneg_exists(I, Rb, n=4001):
    """Brute force: some Rhat >= BI/dp with both parties weakly better off."""
    lo = e12_B * I / e12_dp
    for j in range(n):
        Rh = lo + (e12_R * I - lo) * j / (n - 1)
        if e12_pH * Rh >= e12_B * I + e12_pL * Rb - 1e-12 and \
           e12_pH * (e12_R * I - Rh) >= e12_pL * (e12_R * I - Rb) - 1e-12:
            return True
    return False
e12_cond = lambda I, Rb: e12_dp * e12_R * I - e12_pH * e12_B * I / e12_dp + e12_pL * Rb
e12_I = 2.0
for e12_Rb in [0.0, 0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 1.0, 1.2, 1.3]:
    assert e12_Rb < e12_B * e12_I / e12_dp
    assert e12_reneg_exists(e12_I, e12_Rb) == (e12_cond(e12_I, e12_Rb) >= 0), e12_Rb
chk("12 condition is linear: root", -(e12_dp * e12_R - e12_pH * e12_B / e12_dp) * e12_I / e12_pL, 0.75)
# (iii) capacity with renegotiation (entrepreneur has bargaining power), case pH B/dp >= dp R
assert e12_pH * e12_B / e12_dp >= e12_dp * e12_R
e12_Imax = e12_k * e12_A
e12_Rb = (e12_pH * e12_B / e12_dp - e12_dp * e12_R) * e12_Imax / e12_pL
chk("12 lender breaks even at kA", e12_pL * (e12_R * e12_Imax - e12_Rb), e12_Imax - e12_A, 1e-9)
chk("12 renegotiation condition binds at kA", e12_cond(e12_Imax, e12_Rb), 0.0, 1e-9)
assert 0 <= e12_Rb < e12_B * e12_Imax / e12_dp
e12_Rhat = e12_R * e12_Imax - e12_pL * (e12_R * e12_Imax - e12_Rb) / e12_pH
chk("12 renegotiated stake = BI/dp", e12_Rhat, e12_B * e12_Imax / e12_dp, 1e-9)
# case 2: dp R > pH B/dp -> capacity A/(1 - pL R) < kA
e12b_pH, e12b_pL, e12b_R, e12b_B = 0.9, 0.3, 1.5, 0.3
e12b_dp = e12b_pH - e12b_pL
assert e12b_pH * e12b_R > 1 > e12b_pL * e12b_R + e12b_B and e12b_pH * e12b_R < 1 + e12b_pH * e12b_B / e12b_dp
assert e12b_dp * e12b_R > e12b_pH * e12b_B / e12b_dp
e12b_k = 1 / (1 - e12b_pH * (e12b_R - e12b_B / e12b_dp))
assert 1 / (1 - e12b_pL * e12b_R) < e12b_k

# ---------------------------------------------------------------- Ex 13 (Tirole 4.17)
def e13_solve(A, b, pH=0.5, k=3.0, al=0.95):
    """theta = mu/(1+mu) from the binding breakeven; R(I)=k I^al, phi(C)=ln(1+C)."""
    I_of = lambda th: (pH * k * al / (1 + th * b)) ** (1 / (1 - al))
    C_of = lambda th: 1 / (1 - th / (1 - pH)) - 1
    G = lambda th: pH * k * I_of(th) ** al - b * I_of(th) - I_of(th) + pH * C_of(th) \
        + (1 - pH) * math.log(1 + C_of(th)) + A
    lo, hi = 1e-12, (1 - pH) * (1 - 1e-12)
    assert G(lo) < 0 < G(hi)
    for _ in range(300):
        m = 0.5 * (lo + hi)
        if G(m) < 0: lo = m
        else: hi = m
    th = 0.5 * (lo + hi)
    return th, I_of(th), C_of(th)
e13_th1, e13_I1, e13_C1 = e13_solve(1.0, 1.0)
e13_th4, e13_I4, e13_C4 = e13_solve(1.0, 4.0)
chk("13 I(b=1)", e13_I1, 4.1203, 5e-5)
chk("13 C(b=1)", e13_C1, 1.9003, 5e-5)
chk("13 I(b=4)", e13_I4, 0.3815, 5e-5)
chk("13 C(b=4)", e13_C4, 0.3292, 5e-5)
chk("13 theta(b=1)", e13_th1, 0.3276, 5e-5)
chk("13 theta(b=4)", e13_th4, 0.1238, 5e-5)
assert e13_C4 < e13_C1 and e13_I4 < e13_I1  # collateral FALLS with agency cost here
# first best not pledgeable: I* = (pH k al)^(1/(1-al)), pledgeable pH R(I*) - b I* < I* - A
e13_Istar = (0.5 * 3 * 0.95) ** 20
assert 0.5 * 3 * e13_Istar ** 0.95 - 1.0 * e13_Istar < e13_Istar - 1.0
# limited liability Rb >= 0  <=>  C <= b I / pH
assert e13_C1 <= 1.0 * e13_I1 / 0.5 and e13_C4 <= 4.0 * e13_I4 / 0.5
# sign condition: theta_b > 0 iff eps(1+theta b) > theta(1-theta) b, eps = 1-al = 0.05
e13_lhs = lambda th, b: 0.05 * (1 + th * b)
e13_rhs = lambda th, b: th * (1 - th) * b
chk("13 lhs b=1", e13_lhs(e13_th1, 1.0), 0.0664, 5e-5)
chk("13 rhs b=1", e13_rhs(e13_th1, 1.0), 0.2203, 5e-5)
assert e13_lhs(e13_th1, 1.0) < e13_rhs(e13_th1, 1.0)
e13_tha, _, e13_Ca = e13_solve(1.0, 1.0 + 1e-5)
assert e13_Ca < e13_C1  # local check: dC/db < 0 where the condition fails
# with al = 0.5 (eps = 0.5) and b = 4, condition holds and C rises with b
e13_t, _, e13_c = e13_solve(1.0, 4.0, k=4.0, al=0.5)
e13_t2, _, e13_c2 = e13_solve(1.0, 4.0 + 1e-5, k=4.0, al=0.5)
assert 0.5 * (1 + e13_t * 4) > e13_t * (1 - e13_t) * 4 and e13_c2 > e13_c
# balance sheet: A down -> theta up, I down, C up (al=0.95, b=1)
e13_thA, e13_IA, e13_CA = e13_solve(0.5, 1.0)
assert e13_thA > e13_th1 and e13_IA < e13_I1 and e13_CA > e13_C1
# brute force at b=4: grid over I with minimal C confirms the KKT point
def e13_brute(A, b, pH=0.5, k=3.0, al=0.95):
    best = (-1e9, 0, 0)
    for i in range(1, 6001):
        I = 0.001 * i
        need = I - A - pH * k * I ** al + b * I
        if need <= 0: C = 0.0
        else:
            lo, hi = 0.0, 1e4
            for _ in range(100):
                m = 0.5 * (lo + hi)
                if pH * m + (1 - pH) * math.log(1 + m) < need: lo = m
                else: hi = m
            C = hi
        U = pH * k * I ** al - I - (1 - pH) * (C - math.log(1 + C))
        if U > best[0]: best = (U, I, C)
    return best
e13_bb = e13_brute(1.0, 4.0)
chk("13 brute I", e13_bb[1], e13_I4, 2e-3)
chk("13 brute C", e13_bb[2], e13_C4, 2e-3)

# ---------------------------------------------------------------- Ex 14 (Tirole 7.3)
e14_x, e14_pH, e14_pL, e14_B, e14_R, e14_L0, e14_I = 0.6, 0.8, 0.4, 1.0, 10.0, 3.0, 5.5
e14_dp = e14_pH - e14_pL
e14_tau = lambda L: (9 - L * L) / 90
e14_dtau = lambda L: -2 * L / 90
chk("14 tau(L0)=0", e14_tau(e14_L0), 0.0)
chk("14 condition (2)", e14_dtau(e14_L0) * e14_R, -(1 - e14_x) / e14_x)
assert e14_L0 <= e14_pH * (e14_R - e14_B / e14_dp)
e14_NPV = lambda L: (1 - e14_x) * L + e14_x * (e14_pH + e14_tau(L)) * e14_R - e14_I
assert max(e14_NPV(0.001 * i) for i in range(10001)) <= e14_NPV(e14_L0) + 1e-12
chk("14 NPV*", e14_NPV(e14_L0), 0.5)
e14_Abar = e14_I - (1 - e14_x) * e14_L0 - e14_x * e14_pH * (e14_R - e14_B / e14_dp)
chk("14 Abar", e14_Abar, 0.7)
e14_rb = e14_x * e14_tau(0.0) * (e14_B / e14_dp) / (1 - e14_x)
chk("14 rb", e14_rb, 0.375)
e14_Astar = e14_I - (1 - e14_x) * (e14_L0 - e14_rb) - e14_x * e14_pH * (e14_R - e14_B / e14_dp)
chk("14 Astar", e14_Astar, 0.85)
chk("14 Astar - Abar", e14_Astar - e14_Abar, e14_x * e14_tau(0.0) * e14_B / e14_dp)
# entrepreneur's maintenance choice under the step contract: L0 optimal (weakly), and with rb
# slightly lower she deviates to L = 0
def e14_Ue(L, rb):
    return (1 - e14_x) * (rb if L >= e14_L0 else 0.0) + e14_x * (e14_pH + e14_tau(L)) * e14_B / e14_dp
assert all(e14_Ue(0.001 * i, e14_rb) <= e14_Ue(e14_L0, e14_rb) + 1e-12 for i in range(5001))
assert e14_Ue(0.0, e14_rb - 1e-3) > e14_Ue(e14_L0, e14_rb - 1e-3)
assert (1 - e14_x) * e14_L0 + e14_x * e14_pL * e14_R + e14_x * e14_B - e14_I < 0

# ---------------------------------------------------------------- Ex 15 (Tirole 4.9)
# r ~ U[0,1]; pH(r) = 0.5 + 0.4 r; dp = 0.2; R = 10; B = 1.2 -> R - B/dp = 4; L = 4.5
e15_R, e15_dp, e15_B, e15_L = 10.0, 0.2, 1.2, 4.5
e15_pH = lambda r: 0.5 + 0.4 * r
e15_rho1 = lambda r: e15_pH(r) * e15_R
e15_rho0 = lambda r: e15_pH(r) * (e15_R - e15_B / e15_dp)
assert e15_rho1(0.0) > e15_L  # condition (1) (rho1 increasing)
e15_Er = 0.5
e15_Erho0 = 2.8  # integral of 2 + 1.6 r over [0,1]
chk("15 E rho0", sum(e15_rho0((i + 0.5) / 1e5) for i in range(100000)) / 1e5, e15_Erho0, 1e-8)
e15_P = lambda c: e15_Er + e15_L * c + 2 * (1 - c) + 0.8 * (1 - c * c)
e15_Pc = lambda c: e15_Er + 0.5 * e15_L * c + 2 * (1 - c) + 0.8 * (1 - c * c)
chk("15 P(0)", e15_P(0.0), 3.3)
chk("15 P(1)", e15_P(1.0), 5.0)
e15_rhat = (0.5 * e15_L - 2) / 1.6
chk("15 rhat", e15_rhat, 0.15625)
chk("15 Pc max", e15_Pc(e15_rhat), 3.319531, 1e-6)
assert all(e15_Pc(0.001 * i) <= e15_Pc(e15_rhat) + 1e-12 for i in range(1001))
def e15_root(f, target, lo, hi):
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(m) < target: lo = m
        else: hi = m
    return 0.5 * (lo + hi)
# case (iv): I - A = 4.0
e15_rs4 = e15_root(e15_P, 4.0, 0.0, 1.0)
chk("15 r* (I-A=4)", e15_rs4, (2.5 - math.sqrt(6.25 - 4 * 0.8 * 0.7)) / 1.6)
chk("15 r* (I-A=4) value", e15_rs4, 0.3109, 5e-5)
assert e15_rs4 > e15_rhat and e15_Pc(e15_rhat) < 4.0
chk("15 rho0(r*) iv", e15_rho0(e15_rs4), 2.4975, 5e-5)
# case (v): I - A = 3.31
e15_rs5 = e15_root(e15_P, 3.31, 0.0, 1.0)
e15_rss = e15_root(e15_Pc, 3.31, 0.0, e15_rhat)
chk("15 r* (I-A=3.31)", e15_rs5, 0.0040, 5e-5)
chk("15 r** (I-A=3.31)", e15_rss, 0.0471, 5e-5)
assert e15_rs5 < e15_rss <= e15_rhat
e15_dNPV = 0.5 * (e15_rss - e15_rs5) + 2 * (e15_rss ** 2 - e15_rs5 ** 2)  # int (rho1 - L) dr
chk("15 NPV loss", e15_dNPV, 0.0260, 5e-5)
# dr*/dA = -1/[(L - rho0(r*)) f(r*)]: finite difference at I - A = 4
e15_rs4b = e15_root(e15_P, 4.0 - 1e-6, 0.0, 1.0)
chk("15 dr*/dA", (e15_rs4b - e15_rs4) / 1e-6, -1 / (e15_L - e15_rho0(e15_rs4)), 1e-4)

# ---------------------------------------------------------------- printed illustrations
chk("10 NPV", e10_NPV, 1.0)
chk("10 Abar", e10_Abar, 2.2)
chk("10 D", e10_D, 7.0)
chk("10 RbF max", e10_RbFmax, 0.8)
chk("10 RbS at RbF max", e10_RbS, 4.8)
chk("13 b = pH B/dp (B=0.5)", 0.5 * 0.5 / 0.25, 1.0)
chk("13 b = pH B/dp (B=2)", 0.5 * 2.0 / 0.25, 4.0)
chk("14 tau(0)", e14_tau(0.0), 0.1)
chk("14 B/dp", e14_B / e14_dp, 2.5)
chk("15 rho1(0)", e15_rho1(0.0), 5.0)
chk("15 R - B/dp", e15_R - e15_B / e15_dp, 4.0)
chk("15 rhat formula", (2.25 - 2) / 1.6, e15_rhat)
chk("9 pH(R-B/dp)", e9_pH * (e9_R - e9_B / e9_dp), 6.0)
chk("11 W slope check mu formula", 1 + 0.5 * (0.5 / 0.75) * 10, 13 / 3)
chk("11 pledgeable alone value", 0.5 * (10 - 2), 4.0)

# ---------------------------------------------------------------- deeper-format additions (2026-11-12)
# Ex 1: intermediate lines
chk("1 status quo old debt Lily", min(0, e1_F), 0)
chk("1 assets boom with project", e1_V["boom"] + e1_add, 600)
chk("1 assets slump with project", e1_V["slump"] + e1_add, 300)
chk("1 boom first argument", e1_V["boom"] + e1_add - e1_Il, 540)
chk("1 D0 parts", 0.5 * 300 + 0.5 * 200, 150 + 100)
chk("1 D1 parts", 0.5 * 300 + 0.5 * 240, 150 + 120)
chk("1 eq slump arg", max(e1_V["slump"] + e1_add - e1_Il - e1_Fl, 0), 0)
# Ex 2: parts and adding-up
chk("2 VA parts", 0.5 * 120 + 0.5 * 60, 60 + 30)
chk("2 VB parts", 0.5 * 101, 50.5)
chk("2 EA+DA", e2_E["A"] + e2_D["A"], e2_V["A"])
chk("2 EB+DB", e2_E["B"] + e2_D["B"], e2_V["B"])
# Ex 3: pitfall figure (face value discounted)
chk("3 face/1.1", e3_F / (1 + e3_r), 13.6364, 5e-5)
# Ex 7: old shareholders' value
chk("7 old value via share", (1 - e7_I / e7_E2) * e7_E2, 5)
# Ex 9: Abar arithmetic
chk("9 Abar arithmetic", (6.5 + 1) - 0.8 * (10 - 1 / 0.4), 7.5 - 6)
# Ex 10: illustration arithmetic
chk("10 B/dp", e10_B / e10_dp, 4.0)
chk("10 NPV parts", 0.8 * 12 + 0.2 * 2 - 9, 9.6 + 0.4 - 9)
chk("10 D arithmetic", (9 - 3 - 0.2 * 2) / 0.8, 5.6 / 0.8)
chk("10 D upper bound", e10_RS - e10_B / e10_dp, 8.0)
chk("10 RbS arithmetic", (3 + 1 - 0.2 * 0.8) / 0.8, 3.84 / 0.8)
chk("10 IC at RbF max", 0.4 * (4.8 - 0.8), 1.6)
# Ex 11: W(R) intermediate forms at R = 2
chk("11 W intermediate", 2.0 + 5 * (2 * 2.0 - 1) / 3, (13 * 2.0 - 5) / 3)
chk("11 mu = 1 + 10/3", e11_mu, 1 + 10 / 3)
chk("11 13 Rt = 11", 13 * e11_Rt, 11.0)
# Ex 14: illustration arithmetic
chk("14 tau'(3) R", e14_dtau(3.0) * e14_R, -2 / 3)
chk("14 U* parts", 0.4 * 3 + 0.6 * 0.8 * 10 - 5.5, 1.2 + 4.8 - 5.5)
chk("14 Abar parts", 5.5 - 1.2 - 0.6 * 0.8 * (10 - 2.5), 5.5 - 1.2 - 3.6)
# Ex 15: closed forms with r ~ U[0,1]
for c in (0.0, 0.2, 0.7, 1.0):
    chk("15 P(c) closed form", e15_P(c), 3.3 + 2.5 * c - 0.8 * c * c, 1e-12)
    chk("15 Pc(c) closed form", e15_Pc(c), 3.3 + 0.25 * c - 0.8 * c * c, 1e-12)
chk("15 Pc(rhat) pieces", 3.3 + 0.25 * 0.15625 - 0.8 * 0.15625 ** 2, 3.3 + 0.0390625 - 0.0195313, 1e-7)
chk("15 r** closed form", e15_rss, (0.25 - math.sqrt(0.0625 - 0.032)) / 1.6, 1e-9)
chk("15 rho1 - L", e15_rho1(0.3) - e15_L, 0.5 + 4 * 0.3, 1e-12)

# ---------------------------------------------------------------- original exercises 16-19 (2026-11-12)
# Ex 16: Indarte default cutoff. u = sqrt, Y ~ U[5, 25], A = 5, E = 4, D = 12, sigma = 1.
e16_A, e16_E, e16_D, e16_s, e16_lo, e16_hi = 5, 4, 12, 1.0, 5, 25
e16_F = lambda a: (a - e16_lo) / (e16_hi - e16_lo)
e16_cd = e16_A + e16_E
chk("16 D - A", e16_D - e16_A, 7)
chk("16 P(cash-flow)", e16_F(e16_D - e16_A), 0.1)
chk("16 u(A+E) - sigma", math.sqrt(e16_cd) - e16_s, 2.0)
e16_cr = (math.sqrt(e16_cd) - e16_s) ** 2
chk("16 c_r", e16_cr, 4.0)
e16_Ys = e16_D - e16_A + e16_cr
chk("16 Y*", e16_Ys, 11.0)
chk("16 D + E", e16_D + e16_E, 16)
chk("16 garnishment at Y*", e16_Ys - e16_E, 7.0)
e16_p = e16_F(e16_Ys)
chk("16 p", e16_p, 0.3)
chk("16 strategic part", e16_p - e16_F(e16_D - e16_A), 0.2)
chk("16 Y=6 A+Y", e16_A + 6, 11)
chk("16 Y=6 creditors", 6 - e16_E, 2)
chk("16 Y=9 repay C", e16_A + 9 - e16_D, 2)
chk("16 Y=9 repay u", math.sqrt(2), 1.414214, 5e-7)
chk("16 Y=9 creditors", 9 - e16_E, 5)
chk("16 Y=20 repay C", e16_A + 20 - e16_D, 13)
chk("16 Y=20 repay u", math.sqrt(13), 3.605551, 5e-7)
chk("16 E[Y|Y<Y*]", (e16_lo + e16_Ys) / 2, 8.0)
chk("16 E[Y-E|default]", (e16_lo + e16_Ys) / 2 - e16_E, 4.0)
assert math.sqrt(9 - 7) < 2 and math.sqrt(20 - 7) > 2  # Y = 9 defaults, Y = 20 repays


# Ex 17: comparative statics, pricing, welfare.
def e17_regime_B(sig, D, A=5, E=4, lo=5, hi=25):
    """Cutoff, p, lender value Q and EU (net of sigma) for face D; u = sqrt, Y ~ U[lo, hi]."""
    cr = (math.sqrt(A + E) - sig) ** 2
    Ys = D - A + cr
    p = (Ys - lo) / (hi - lo)
    Q = (hi - Ys) / (hi - lo) * D + ((Ys - E) ** 2 - (lo - E) ** 2) / 2 / (hi - lo)
    Eu = p * math.sqrt(A + E) + (2 / 3) * ((A + hi - D) ** 1.5 - cr ** 1.5) / (hi - lo)
    EC = p * (A + E) + ((A + hi - D) ** 2 - cr ** 2) / 2 / (hi - lo)
    return cr, Ys, p, Q, Eu - sig * p, Eu, EC


def e17_D(sig):
    """Smallest D with Q(D) = 9.6: D^2 - 42 D + 385 - (c_r - 9)^2 = 0."""
    cr = (3 - sig) ** 2
    return 21 - math.sqrt(56 + (cr - 9) ** 2)


e17_up = lambda C: 1 / (2 * math.sqrt(C))
chk("17 u'(4)", e17_up(4), 0.25)
chk("17 u'(9)", e17_up(9), 1 / 6)
e17_ratio = e17_up(9) / e17_up(4)
chk("17 ratio", e17_ratio, 2 / 3)
chk("17 dY/dA", e17_ratio - 1, -1 / 3)
chk("17 dY/dsigma", -1 / e17_up(4), -4)
chk("17 dp/dD", 1 / 20, 0.05)
chk("17 dp/dA", (e17_ratio - 1) / 20, -1 / 60)
chk("17 dp/dsigma", -4 / 20, -0.2)
chk("17 dp/dE", e17_ratio / 20, 1 / 30)
# finite-difference check of the derivatives at the baseline
for name, f, want in (("D", lambda h: e17_regime_B(1, 12 + h)[1], 1.0),
                      ("sigma", lambda h: e17_regime_B(1 + h, 12)[1], -4.0),
                      ("A", lambda h: e17_regime_B(1, 12, A=5 + h)[1], -1 / 3),
                      ("E", lambda h: e17_regime_B(1, 12, E=4 + h)[1], 2 / 3)):
    chk("17 FD dY*/d" + name, (f(1e-6) - f(-1e-6)) / 2e-6, want, 1e-5)
e17_b = e17_regime_B(1.0, 12)
chk("17 Q(12)", e17_b[3], 9.6, 1e-12)
chk("17 Q parts", 0.7 * 12 + (49 - 1) / 2 / 20, 8.4 + 1.2)
chk("17 rate baseline", 12 / 9.6 - 1, 0.25)
chk("17 D_B(sigma=1)", e17_D(1.0), 12.0, 1e-12)
chk("17 40Q formula at 12", -144 + 42 * 12 + (4 - 9) ** 2 - 1, 384)
# Regime N
e17_EUN = (2 / 3) * ((5 + 25 - 9.6) ** 1.5 - (5 + 5 - 9.6) ** 1.5) / 20
chk("17 20.4^1.5", 20.4 ** 1.5, 92.139373, 5e-6)
chk("17 0.4^1.5", 0.4 ** 1.5, 0.252982, 5e-7)
chk("17 EU_N", e17_EUN, 3.062880, 5e-7)
chk("17 CE_N", e17_EUN ** 2, 9.381232, 5e-6)
chk("17 E[C_N]", 5 + 15 - 9.6, 10.4)
# Regime B, sigma = 1
chk("17 18^1.5", 18 ** 1.5, 76.367532, 5e-6)
chk("17 EU_B(1)", e17_b[4], 2.878918, 5e-7)
chk("17 EU_B(1) parts", 0.6 + (76.367532 - 8) / 30, 2.878918, 5e-7)
chk("17 CE_B(1)", e17_b[4] ** 2, 8.288168, 5e-6)
chk("17 E[C_B](1)", e17_b[6], 10.4, 1e-12)
chk("17 E[C_B](1) parts", 0.3 * 9 + (18 ** 2 - 4 ** 2) / 2 / 20, 2.7 + 7.7)
chk("17 Eu(C_B)(1)", e17_b[5], 3.178918, 5e-7)
chk("17 insurance gain (1)", e17_b[5] - e17_EUN, 0.116038, 5e-7)
assert e17_b[4] < e17_EUN
# Regime B, sigma = 0.1
e17_cr1 = (3 - 0.1) ** 2
chk("17 c_r(0.1)", e17_cr1, 8.41, 1e-12)
chk("17 (c_r-9)^2", (e17_cr1 - 9) ** 2, 0.3481, 1e-12)
chk("17 constant", 385 - 0.3481, 384.6519, 1e-12)
chk("17 discriminant", 441 - 384.6519, 56.3481, 1e-12)
chk("17 sqrt disc", math.sqrt(56.3481), 7.506537, 5e-7)
e17_D1 = e17_D(0.1)
chk("17 D_B(0.1)", e17_D1, 13.493463, 5e-7)
e17_c = e17_regime_B(0.1, e17_D1)
chk("17 Q(D_B(0.1))", e17_c[3], 9.6, 1e-9)
chk("17 Y*(0.1)", e17_c[1], 16.903463, 5e-7)
chk("17 p(0.1)", e17_c[2], 0.595173, 5e-7)
chk("17 rate(0.1)", e17_D1 / 9.6 - 1, 0.405569, 5e-7)
chk("17 Y*-E < D", e17_D1 - (e17_c[1] - 4), 9 - 8.41, 1e-9)
chk("17 30 - D", 30 - e17_D1, 16.506537, 5e-7)
chk("17 (30-D)^1.5", (30 - e17_D1) ** 1.5, 67.063152, 5e-6)
chk("17 2.9^3", 8.41 ** 1.5, 24.389, 1e-9)
chk("17 EU_B(0.1)", e17_c[4], 3.148474, 5e-7)
chk("17 CE_B(0.1)", e17_c[4] ** 2, 9.912888, 5e-6)
chk("17 E[C_B](0.1)", e17_c[6], 10.4, 1e-9)
chk("17 sigma p (0.1)", 0.1 * e17_c[2], 0.059517, 5e-7)
chk("17 Eu(C_B)(0.1)", e17_c[5], 3.207991, 5e-7)
chk("17 insurance gain (0.1)", e17_c[5] - e17_EUN, 0.145111, 5e-7)
chk("17 crossing point", 9 + 9.6 - 5, 13.6)
assert e17_c[4] > e17_EUN
# sigma-bar by bisection
e17_l, e17_h = 0.0, 1.0
for _ in range(60):
    e17_m = (e17_l + e17_h) / 2
    if e17_regime_B(e17_m, e17_D(e17_m))[4] > e17_EUN:
        e17_l = e17_m
    else:
        e17_h = e17_m
chk("17 sigma-bar", e17_l, 0.264820, 5e-7)
# Monte-Carlo-free cross-check of Q by midpoint quadrature at sigma = 0.1
e17_n = 200000
e17_Qnum = sum(min(max(5 + (i + 0.5) * 20 / e17_n - 4, 0), e17_D1) if 5 + (i + 0.5) * 20 / e17_n < e17_c[1]
               else e17_D1 for i in range(e17_n)) / e17_n
chk("17 Q quadrature", e17_Qnum, 9.6, 1e-5)  # jump at Y* limits midpoint accuracy

# Ex 18: two-type, two-effort Karlan-Zinman model.
e18_pi = {("S", "H"): 0.9, ("S", "L"): 0.8, ("R", "H"): 0.7, ("R", "L"): 0.5}
e18_Y = {"S": 1.35, "R": 1.80}
e18_c, e18_rL, e18_rH, e18_Cn, e18_Cd = 0.17, 0.10, 0.30, 0.25, 0.45


def e18_gain(t, rc, Cb):
    """Gain from H over L before its cost: dpi * [Y - (1 + rc) + Cb]."""
    return (e18_pi[(t, "H")] - e18_pi[(t, "L")]) * (e18_Y[t] - (1 + rc) + Cb)


def e18_eff(t, rc, Cb):
    return "H" if e18_gain(t, rc, Cb) >= e18_c - 1e-12 else "L"


def e18_U(t, r, Cb):
    e = e18_eff(t, r, Cb)
    p = e18_pi[(t, e)]
    return p * (e18_Y[t] - 1 - r) - (1 - p) * Cb - (e18_c if e == "H" else 0)


for (t, rc, Cb, g, e) in (("S", 0.1, 0.25, 0.05, "L"), ("S", 0.1, 0.45, 0.07, "L"),
                          ("S", 0.3, 0.25, 0.03, "L"), ("S", 0.3, 0.45, 0.05, "L"),
                          ("R", 0.1, 0.25, 0.19, "H"), ("R", 0.1, 0.45, 0.23, "H"),
                          ("R", 0.3, 0.25, 0.15, "L"), ("R", 0.3, 0.45, 0.19, "H")):
    chk(f"18 gain {t} {rc} {Cb}", e18_gain(t, rc, Cb), g, 1e-12)
    assert e18_eff(t, rc, Cb) == e, (t, rc, Cb)
    assert abs(e18_gain(t, rc, Cb) - e18_c) > 1e-9  # no ties
chk("18 U S rL", e18_U("S", 0.1, 0.25), 0.15, 1e-12)
chk("18 U S rH", e18_U("S", 0.3, 0.25), -0.01, 1e-12)
chk("18 U R rL", e18_U("R", 0.1, 0.25), 0.245, 1e-12)
chk("18 U R rL low effort", 0.5 * 0.7 - 0.5 * 0.25, 0.225, 1e-12)
chk("18 U R rH", e18_U("R", 0.3, 0.25), 0.125, 1e-12)
chk("18 U R rH high effort", 0.7 * 0.5 - 0.3 * 0.25 - 0.17, 0.105, 1e-12)


def e18_cell(ro, rc, Cb):
    """Default rate among takers at offer ro, contract rc, default cost Cb."""
    takers = [t for t in "SR" if e18_U(t, ro, e18_Cn) >= 0]
    return sum(1 - e18_pi[(t, e18_eff(t, rc, Cb))] for t in takers) / len(takers)


e18_tab = {(g, k): e18_cell(ro, rc, Cb) for g, ro, rc in (("A", .1, .1), ("B", .3, .1), ("C", .3, .3))
           for k, Cb in (("no", e18_Cn), ("yes", e18_Cd))}
for key, want in ((("A", "no"), 0.25), (("A", "yes"), 0.25), (("B", "no"), 0.3), (("B", "yes"), 0.3),
                  (("C", "no"), 0.5), (("C", "yes"), 0.3)):
    chk(f"18 cell {key}", e18_tab[key], want, 1e-12)
chk("18 selection", e18_tab[("B", "no")] - e18_tab[("A", "no")], 0.05, 1e-12)
chk("18 burden no", e18_tab[("C", "no")] - e18_tab[("B", "no")], 0.20, 1e-12)
chk("18 burden yes", e18_tab[("C", "yes")] - e18_tab[("B", "yes")], 0.0, 1e-12)
chk("18 dynamic C", e18_tab[("C", "yes")] - e18_tab[("C", "no")], -0.20, 1e-12)
chk("18 naive", e18_tab[("C", "no")] - e18_tab[("A", "no")], 0.25, 1e-12)
chk("18 max 1+rc no", e18_Y["R"] + e18_Cn - e18_c / 0.2, 1.20, 1e-12)
chk("18 max 1+rc yes", e18_Y["R"] + e18_Cd - e18_c / 0.2, 1.40, 1e-12)
chk("18 c/dpi", e18_c / 0.2, 0.85, 1e-12)
chk("18 pledgeable R no", 0.7 * 1.20, 0.84, 1e-12)
chk("18 pledgeable R yes", 0.7 * 1.40, 0.98, 1e-12)

# Ex 19: hypothetical three-rate results.
e19_n = {("A", 0): 600, ("A", 1): 600, ("B", 0): 750, ("B", 1): 750, ("C", 0): 750, ("C", 1): 750}
e19_d = {("A", 0): 69, ("A", 1): 51, ("B", 0): 132, ("B", 1): 108, ("C", 0): 141, ("C", 1): 114}
for k, want in ((("A", 0), 0.115), (("A", 1), 0.085), (("B", 0), 0.176), (("B", 1), 0.144),
                (("C", 0), 0.188), (("C", 1), 0.152)):
    chk(f"19 cell {k}", e19_d[k] / e19_n[k], want, 1e-12)
e19_g = {g: (e19_d[(g, 0)] + e19_d[(g, 1)], e19_n[(g, 0)] + e19_n[(g, 1)]) for g in "ABC"}
e19_dyn = {k: (sum(e19_d[(g, k)] for g in "ABC"), sum(e19_n[(g, k)] for g in "ABC")) for k in (0, 1)}
chk("19 dA", e19_g["A"][0] / e19_g["A"][1], 0.10, 1e-12)
chk("19 dB", e19_g["B"][0] / e19_g["B"][1], 0.16, 1e-12)
chk("19 dC", e19_g["C"][0] / e19_g["C"][1], 0.17, 1e-12)
chk("19 d no", e19_dyn[0][0] / e19_dyn[0][1], 342 / 2100, 1e-12)
chk("19 d no value", 342 / 2100, 0.162857, 5e-7)
chk("19 d yes", e19_dyn[1][0] / e19_dyn[1][1], 0.13, 1e-12)
for g, want in (("A", -0.030), ("B", -0.032), ("C", -0.036)):
    chk(f"19 within dyn {g}", e19_d[(g, 1)] / e19_n[(g, 1)] - e19_d[(g, 0)] / e19_n[(g, 0)], want, 1e-12)


def e19_z(a, b):
    """Difference of proportions a - b, unpooled SE, z, 95% CI."""
    (x1, n1), (x2, n2) = a, b
    p1, p2 = x1 / n1, x2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    return p1 - p2, se, (p1 - p2) / se, p1 - p2 - 1.96 * se, p1 - p2 + 1.96 * se


for name, res, want in (("sel", e19_z(e19_g["B"], e19_g["A"]), (0.06, 0.012830, 4.6767, 0.034854, 0.085146)),
                        ("burden", e19_z(e19_g["C"], e19_g["B"]), (0.01, 0.013552, 0.7379, -0.016563, 0.036563)),
                        ("dyn", e19_z(e19_dyn[1], e19_dyn[0]), (-69 / 2100, 0.010899, -3.0148, -0.054218, -0.011496))):
    for lab, got, w, tol in zip(("diff", "se", "z", "lo", "hi"), res, want, (1e-9, 5e-7, 5e-5, 5e-7, 5e-7)):
        chk(f"19 {name} {lab}", got, w, tol)
chk("19 dyn diff value", -69 / 2100, -0.032857, 5e-7)
# OLS by FWL: beta_b = n-weighted within-group difference; group fits = mean - beta_b / 2
e19_bb = sum((e19_g[g][1]) * (e19_d[(g, 1)] / e19_n[(g, 1)] - e19_d[(g, 0)] / e19_n[(g, 0)]) for g in "ABC") / 4200
chk("19 beta_b (share)", e19_bb, -69 / 2100, 1e-12)
chk("19 beta_b pp", 100 * e19_bb, -3.285714, 5e-7)
chk("19 beta_o", (16 - 10) / (40 - 30), 0.6)
chk("19 beta_c", (17 - 16) / (40 - 30), 0.1)
e19_alpha = 10 - 100 * e19_bb / 2 - 30 * (0.6 + 0.1)
chk("19 alpha", e19_alpha, -9.357143, 5e-7)
for g, ro, rc in (("A", 30, 30), ("B", 40, 30), ("C", 40, 40)):
    for k in (0, 1):
        fit = e19_alpha + 0.6 * ro + 0.1 * rc + 100 * e19_bb * k
        chk(f"19 group mean from fit {g}", fit - 100 * e19_bb * (k - 0.5), 100 * e19_g[g][0] / e19_g[g][1], 1e-9)
# OLS normal equations solved directly (Gauss-Jordan on the 4x4 X'X), to confirm FWL
e19_XtX = [[0.0] * 4 for _ in range(4)]
e19_Xty = [0.0] * 4
for (g, k), n in e19_n.items():
    ro, rc = {"A": (30, 30), "B": (40, 30), "C": (40, 40)}[g]
    x = (1.0, ro, rc, k)
    for i in range(4):
        e19_Xty[i] += x[i] * 100 * e19_d[(g, k)]
        for j in range(4):
            e19_XtX[i][j] += x[i] * x[j] * n
e19_M = [row[:] + [e19_Xty[i]] for i, row in enumerate(e19_XtX)]
for i in range(4):
    piv = max(range(i, 4), key=lambda r: abs(e19_M[r][i]))
    e19_M[i], e19_M[piv] = e19_M[piv], e19_M[i]
    e19_M[i] = [v / e19_M[i][i] for v in e19_M[i]]
    for r in range(4):
        if r != i:
            e19_M[r] = [a - e19_M[r][i] * b for a, b in zip(e19_M[r], e19_M[i])]
for i, want in enumerate((e19_alpha, 0.6, 0.1, 100 * e19_bb)):
    chk(f"19 OLS coef {i}", e19_M[i][4], want, 1e-7)
# (d) lender's expected gross repayment
chk("19 R(30%)", 0.90 * 1.30, 1.17, 1e-12)
chk("19 R(40%)", 0.83 * 1.40, 1.162, 1e-12)
chk("19 rate effect", 0.90 * 0.10, 0.09, 1e-12)
chk("19 selection effect", -0.06 * 1.40, -0.084, 1e-12)
chk("19 burden effect", -0.01 * 1.40, -0.014, 1e-12)
chk("19 decomposition", 0.09 - 0.084 - 0.014, 1.162 - 1.17, 1e-12)
chk("19 R(40%) if pool A", 0.90 * 1.40, 1.26, 1e-12)
# (e) Holmstrom-Tirole with a dynamic incentive
e19_pH, e19_pL, e19_B, e19_R = 0.9, 0.5, 0.2, 1.5
e19_dp = e19_pH - e19_pL
chk("19 dp", e19_dp, 0.4, 1e-12)
chk("19 B/dp", e19_B / e19_dp, 0.5, 1e-12)
chk("19 P0", e19_pH * (e19_R - e19_B / e19_dp), 0.9, 1e-12)
chk("19 Abar0", 1 - 0.9, 0.1, 1e-12)
chk("19 Rb min with Cb", e19_B / e19_dp - 0.2, 0.3, 1e-12)
chk("19 P1", e19_pH * (e19_R - e19_B / e19_dp + 0.2), 1.08, 1e-12)
chk("19 Abar1", 1 - 1.08, -0.08, 1e-12)
chk("19 NPV", e19_pH * e19_R - 1, 0.35, 1e-12)
chk("19 shirk NPV", e19_pL * e19_R + e19_B - 1, -0.05, 1e-12)
chk("19 deadweight", (1 - e19_pH) * 0.2, 0.02, 1e-12)
chk("19 net utility", 0.35 - 0.02, 0.33, 1e-12)

# Ex 16-19: intermediate lines printed in the solutions
chk("16 F(7) = 2/20", 2 / 20, 0.1)
chk("16 F(11) = 6/20", 6 / 20, 0.3)
chk("17 EU_N numerator", 92.139373 - 0.252982, 91.886391, 1e-9)
chk("17 EU_B(1) integral part", (76.367532 - 8) / 30, 2.278918, 5e-7)
chk("17 Q(12) integral", (7 ** 2 - 1 ** 2) / 40, 1.2)
chk("17 E[C_B](1) 308/40", 308 / 40, 7.7)
chk("17 D_B/9.6 (0.1)", e17_D1 / 9.6, 1.405569, 5e-7)
chk("17 Y*-E (0.1)", e17_c[1] - 4, 12.903463, 5e-7)
chk("17 p*2.9", e17_c[2] * 2.9, 1.726002, 5e-7)
chk("17 integral part (0.1)", (67.063152 - 24.389) / 30, 1.422472, 5e-7)
chk("17 EU_B(0.1) parts", 1.726002 + 1.422472, 3.148474, 1e-6)
chk("17 9 - c_r (0.1)", 9 - 8.41, 0.59, 1e-12)
chk("18 dynamic raises pledgeable", 0.7 * (1.40 - 1.20), 0.14, 1e-12)
chk("18 max 1+rc = 0.95 + Cb", e18_Y["R"] - e18_c / 0.2, 0.95, 1e-12)
for got, want in ((0.16 * 0.84 / 1500, 0.0000896), (0.10 * 0.90 / 1200, 0.0000750), (0.0000896 + 0.0000750, 0.0001646),
                  (0.17 * 0.83 / 1500, 0.0000941), (0.0000941 + 0.0000896, 0.0001837),
                  (0.13 * 0.87 / 2100, 0.0000539), (0.162857 * 0.837143 / 2100, 0.0000649),
                  (0.0000539 + 0.0000649, 0.0001188)):
    chk("19 SE pieces", got, want, 5e-8)
chk("19 beta_b weighted sum", 1200 * -3.0 + 1500 * -3.2 + 1500 * -3.6, -13800, 1e-9)
chk("19 alpha pieces", 10 + 1.642857 - 21, -9.357143, 1e-9)
chk("19 C vs A", 17 - 10, 7)
chk("19 shirk parts", 0.5 * 1.5 + 0.2 - 1, 0.75 + 0.2 - 1, 1e-12)

print(f"PASS {N} checks")
