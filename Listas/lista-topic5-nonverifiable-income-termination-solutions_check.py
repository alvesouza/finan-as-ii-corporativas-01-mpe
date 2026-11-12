"""Numeric checks for Listas/lista-topic5-nonverifiable-income-termination-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-topic5-nonverifiable-income-termination-solutions_check.py  -> PASS <n> checks
"""
import math  # noqa: F401  (fragments use it)

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1

# ======================================================================
# t5a
# Topic 5 list, exercises 1-7. Run after check_header.py (defines chk).
from fractions import Fraction as Fr

# ---- Ex 1: Grinblatt-Titman 16.10 (Eastern Airlines numbers p. 576; own example) ----
def ex1_eq(V, F): return max(V - F, 0)
def ex1_debt(V, F): return min(V, F)
ex1_F, ex1_hi, ex1_lo, ex1_VL = 500, 600, 200, 480
chk("1 E_cont", 0.5 * ex1_eq(ex1_hi, ex1_F) + 0.5 * ex1_eq(ex1_lo, ex1_F), 50)
chk("1 E_liq", ex1_eq(ex1_VL, ex1_F), 0)
chk("1 D_cont", 0.5 * ex1_debt(ex1_hi, ex1_F) + 0.5 * ex1_debt(ex1_lo, ex1_F), 350)
chk("1 D_liq", ex1_debt(ex1_VL, ex1_F), 480)
chk("1 V_cont", 0.5 * ex1_hi + 0.5 * ex1_lo, 400)
chk("1 loss", ex1_VL - (0.5 * ex1_hi + 0.5 * ex1_lo), 80)
ex1_F2, ex1_hi2, ex1_lo2 = 500, 800, 300
chk("1 V_cont2", 0.5 * ex1_hi2 + 0.5 * ex1_lo2, 550)
chk("1 D_cont2", 0.5 * ex1_debt(ex1_hi2, ex1_F2) + 0.5 * ex1_debt(ex1_lo2, ex1_F2), 400)
chk("1 D_liq2", ex1_debt(500, ex1_F2), 500)

# ---- Ex 2: (5.11) and its fixed point ----
def ex2_r1(R, L, X, pi, f, fd):
    e = fd * (1 - f) / (f * (1 - fd))           # Bayes, inverse of (t5e2-bayes)
    qd = pi + fd * (1 - pi)
    M = max(L, qd * X / R)
    Pu = f * (1 - e)
    r1 = R if R <= M else (R - (1 - Pu) * M) / Pu
    Vd = min(r1, M)
    return r1, Vd, Pu, e
# case B point: break-even P_u r1 + P_d Vd = R and (5.11) both hold
ex2_R, ex2_L, ex2_X, ex2_pi, ex2_f, ex2_fd = 1.1, 0.5, 1.5, 0.3, 0.6, 0.3
ex2_r1v, ex2_Vd, ex2_Pu, ex2_e = ex2_r1(ex2_R, ex2_L, ex2_X, ex2_pi, ex2_f, ex2_fd)
chk("2 Bayes", ex2_f * ex2_e / (ex2_f * ex2_e + 1 - ex2_f), ex2_fd)
chk("2 break-even B", ex2_Pu * ex2_r1v + (1 - ex2_Pu) * ex2_Vd, ex2_R)
chk("2 (5.11) B", (ex2_R - (1 - ex2_Pu) * ex2_Vd) / ex2_Pu, ex2_r1v)
chk("2 caseB r1>R", ex2_r1v > ex2_R, True)
chk("2 caseB r1>M", ex2_r1v > ex2_Vd, True)
# case A point (Exercise 5 parameters): r1 = R
chk("2 caseA r1=R", ex2_r1(1, 1, 1.75, 0.5, 0.5, 1 / 3)[0], 1)

# ---- Ex 3: d beta0 / dq <= 0 ----
def ex3_beta(q, K, y, a, cbar):
    return K / (q * y / 2 + (1 - q) * a**2 * y**2 / (4 * cbar))
def ex3_dbeta(q, K, y, a, cbar):
    Pi = q * y / 2 + (1 - q) * a**2 * y**2 / (4 * cbar)
    return -K * (y / 2 - a**2 * y**2 / (4 * cbar)) / Pi**2
ex3_p = (0.5, 1.0, 4.0, 0.8, 2.0)                # q, K, y, alpha, cbar with alpha*y/2 <= cbar
ex3_h = 1e-6
ex3_num = (ex3_beta(ex3_p[0] + ex3_h, *ex3_p[1:]) - ex3_beta(ex3_p[0] - ex3_h, *ex3_p[1:])) / (2 * ex3_h)
chk("3 derivative formula", ex3_num, ex3_dbeta(*ex3_p), 1e-6)
chk("3 negative", ex3_dbeta(*ex3_p) < 0, True)
chk("3 factorised Pi'", 4.0 / 2 - 0.8**2 * 16 / 8, (4.0 / 2) * (1 - 0.8 * 0.8 * 4.0 / (2 * 2.0)))
chk("3 knife-edge zero", ex3_dbeta(0.5, 1.0, 4.0, 1.0, 2.0), 0)   # alpha=1, y/2=cbar
chk("3 L0 <= y/2", 0.8**2 * 16 / 8 <= 4.0 / 2, True)

# ---- Ex 4: renegotiation gain ----
ex4_q, ex4_ygg, ex4_ybb, ex4_ybg = 0.6, 0.9, 0.5, 0.2
ex4_lgg, ex4_lbb, ex4_lbg = 0.3, 0.1, 0.25
ex4_T = ex4_ybb - ex4_ybg
ex4_wt = ex4_q * ex4_lgg + (1 - ex4_q) * ex4_lbg
ex4_w = ex4_q * ex4_lgg + (1 - ex4_q) * (ex4_lbb + ex4_T)
chk("4 gain formula", ex4_w - ex4_wt, (1 - ex4_q) * ((ex4_ybb + ex4_lbb) - (ex4_ybg + ex4_lbg)))
chk("4 gain > 0", ex4_w - ex4_wt > 0, True)
chk("4 investor stays at pi2", ex4_q * ex4_ygg + (1 - ex4_q) * (ex4_ybb - ex4_T),
    ex4_q * ex4_ygg + (1 - ex4_q) * ex4_ybg)
chk("4 corrected book line", ex4_q * ex4_lgg + (1 - ex4_q) * (ex4_ybb + ex4_lbb) - (1 - ex4_q) * ex4_ybg, ex4_w)

# ---- Ex 5: Diamond (1991) example, exact fractions ----
L5, R5, pi5, X5, C5, f5, fd5 = Fr(1), Fr(1), Fr(1, 2), Fr(7, 4), Fr(0), Fr(1, 2), Fr(1, 3)
q5 = pi5 + f5 * (1 - pi5)
qd5 = pi5 + fd5 * (1 - pi5)
e5 = fd5 * (1 - f5) / (f5 * (1 - fd5))
chk("5 q", q5, Fr(3, 4)); chk("5 qd", qd5, Fr(2, 3)); chk("5 e", e5, Fr(1, 2))
chk("5 P_up", (1 - e5) * f5, Fr(1, 4)); chk("5 P_down", 1 - (1 - e5) * f5, Fr(3, 4))
rho5 = R5**2 / q5
chk("5 rho", rho5, Fr(4, 3)); chk("5 rho dec", float(rho5), 1.3333, 1e-4); chk("5 rho<=X", rho5 <= X5, True)
Pu5 = (1 - e5) * f5
r1_5 = R5 / (Pu5 + (1 - Pu5))                    # (5.11) with V_s^d = r1
chk("5 r1", r1_5, 1)
chk("5 qdX/R", qd5 * X5 / R5, Fr(7, 6)); chk("5 qdX/R dec", float(qd5 * X5 / R5), 1.1667, 1e-4)
chk("5 guess ok", r1_5 <= max(L5, qd5 * X5 / R5), True)
chk("5 rollover up", r1_5 * R5, 1)
chk("5 rollover down", r1_5 * R5 / qd5, Fr(3, 2)); chk("5 down<=X", r1_5 * R5 / qd5 <= X5, True)
chk("5 new lenders BE", qd5 * Fr(3, 2), R5 * r1_5)
Ul5 = X5 + C5 - rho5
chk("5 U_l", Ul5, Fr(5, 12)); chk("5 U_l dec", float(Ul5), 0.4167, 1e-4)
Vld5 = qd5 * rho5 / R5
chk("5 V_l^d", Vld5, Fr(8, 9))
def lemma5(Vd): return X5 + C5 - R5**2 / f5 + R5 * Vd * e5 * (1 / fd5 - 1 / qd5)
chk("5 lemma long", lemma5(Vld5), Fr(5, 12))
chk("5 lemma -1/4", X5 + C5 - R5**2 / f5, Fr(-1, 4)); chk("5 lemma 2/3", Vld5 * e5 * (3 - Fr(3, 2)), Fr(2, 3))
chk("5 LT BE (5.11 form)", Pu5 * rho5 / R5 + (1 - Pu5) * Vld5, R5)
Us5 = e5 * (X5 + C5 - R5 * r1_5 / qd5) + (1 - e5) * (X5 + C5 - r1_5 * R5)
chk("5 U_s", Us5, Fr(1, 2)); chk("5 lemma short", lemma5(r1_5), Fr(1, 2))
chk("5 U_s parts", X5 - Fr(3, 2), Fr(1, 4)); chk("5 U_s parts2", X5 - 1, Fr(3, 4))
chk("5 lemma 3/4", R5 * r1_5 * e5 * (1 / fd5 - 1 / qd5), Fr(3, 4))
chk("5 gain", Us5 - Ul5, Fr(1, 12)); chk("5 gain dec", float(Us5 - Ul5), 0.0833, 1e-4)

# ---- Ex 6: Bolton-Scharfstein general contracts (identities at one point) ----
pL6, B06, B6, D6, M6, I6, A6 = 0.5, 0.2, 0.6, 1.0, 3.0, 0.8, 0.5
zS6, zF6, rS6, RSS6, RFS6 = 0.6, 0.2, 0.3, 1.5, 1.3
dp6 = 1 - pL6
W6 = zS6 * RSS6 + (1 - zS6) * rS6
raw6 = W6 - (B06 + pL6 * W6 + (1 - pL6) * zF6 * RFS6)
chk("6 IC' equivalence", raw6, dp6 * (zS6 * RSS6 + (1 - zS6) * rS6 - zF6 * RFS6) - B06)
Ub6 = lambda z: D6 - I6 + z * (D6 - I6)
chk("6 IR' equivalence", D6 - (1 - zS6) * rS6 + zS6 * (D6 - I6 - RSS6) - (I6 - A6), Ub6(zS6) - W6 + A6)
RSSt6 = RSS6 + (1 - zS6) * rS6 / zS6            # shift r_b^S into R_b^SS
chk("6 shift keeps W", zS6 * RSSt6, W6)
chk("6 shift raises RSS", RSSt6 > RSS6, True)
chk("6 lower RFS relaxes IC", dp6 * (W6 - zF6 * B6 / dp6) - dp6 * (W6 - zF6 * RFS6), dp6 * zF6 * (RFS6 - B6 / dp6))
zFb6 = zS6 - D6 / (M6 - D6)                      # (PD) binding (here negative: identity only)
chk("6 IC with PD binding", zS6 * RSS6 - zFb6 * RFS6, zS6 * (RSS6 - RFS6) + D6 / (M6 - D6) * RFS6)
chk("6 utility=NPV at binding IR", (Ub6(zS6) + A6) - A6, D6 - I6 + zS6 * (D6 - I6))

# ---- Ex 7: Tirole 3.14 ----
pH7, pL7, gh7, gl7, R7, L7, B7, I7 = 0.8, 0.5, 0.9, 0.3, 10.0, 4.0, 0.6, 7.0
dp7, dg7 = pH7 - pL7, gh7 - gl7
chk("7 assumptions", gh7 * R7 > L7 > gl7 * R7 and pH7 * gh7 * R7 + (1 - pH7) * L7 > I7, True)
P7 = pH7 * gh7 * R7 + (1 - pH7) * L7 - pH7 * B7 / dp7
Abar7 = I7 - P7
chk("7 Abar", Abar7, 0.6)
Rb7 = B7 / (dp7 * dg7); Lb7 = gl7 * Rb7
chk("7 effort IC binds", dp7 * (gh7 * Rb7 - Lb7), B7)
rent7 = pH7 * gh7 * Rb7 + (1 - pH7) * Lb7
chk("7 rent decomposition", rent7, pH7 * B7 / dp7 + gl7 * B7 / (dp7 * dg7))
chk("7 bracket identity", pH7 * gh7 + (1 - pH7) * gl7, gl7 + pH7 * dg7)
chk("7 threshold", I7 - (P7 - gl7 * B7 / (dp7 * dg7)), Abar7 + gl7 * B7 / (dp7 * dg7))
# brute force: min rent over a grid of (R_b, L_b) satisfying the three constraints
ex7_best = min(pH7 * gh7 * rb + (1 - pH7) * lb
               for rb in [i / 200 for i in range(0, 2001)]
               for lb in [max(gl7 * rb, 0)]                 # rent rises in L_b: take its lower bound
               if dp7 * (gh7 * rb - lb) >= B7 - 1e-12 and gh7 * rb >= lb)
chk("7 grid min rent", ex7_best, rent7, 5e-3)
# continuing after both signals: same rent, lower pledgeable income
chk("7 no-liquidation rent", (pH7 * gh7 + (1 - pH7) * gl7) * B7 / (dp7 * dg7), rent7)

# ======================================================================
# t5b
# Checks for Topic-5 list, exercises 8-13 (run after check_header.py, which defines chk and math).
from itertools import permutations

# ---------------- Exercise 8 (Tirole 5.7): FOC (1) and comparative statics, numerically ----------
# Example (ours): R(I) = a I - b I^2/2 (R/I - R' = bI/2 increasing), rho ~ U[0, rb].
e8pH, e8Bdp, e8a, e8b, e8rb, e8r = 0.8, 0.5, 1.2, 0.1, 1.0, 0.8
e8F = lambda x: x / e8rb
e8G = lambda x: x * x / (2 * e8rb)          # int_0^x rho f = int_0^x F (uniform)
e8R = lambda I: e8a * I - e8b * I * I / 2
e8Rp = lambda I: e8a - e8b * I


def e8_opt_given_rho(rs, A):
    """Best I for cutoff rs: min(unconstrained argmax of U_b, largest I meeting IR_l)."""
    k1 = e8r + e8F(rs) * e8pH * (e8a - e8Bdp) - 1 - e8G(rs)   # IR slack = A + k1 I - k2 I^2
    k2 = e8F(rs) * e8pH * e8b / 2
    Imax = (k1 + math.sqrt(k1 * k1 + 4 * k2 * A)) / (2 * k2)
    Iu = (e8r + e8F(rs) * e8pH * e8a - 1 - e8G(rs)) / (e8F(rs) * e8pH * e8b)
    I = min(Imax, Iu)
    return I, e8r * I + e8F(rs) * e8pH * e8R(I) - I - e8G(rs) * I


def e8_solve(A):
    """Maximise U_b over the cutoff by golden-section search."""
    lo, hi = 0.3, 0.999
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        m1, m2 = hi - g * (hi - lo), lo + g * (hi - lo)
        if e8_opt_given_rho(m1, A)[1] < e8_opt_given_rho(m2, A)[1]:
            lo = m1
        else:
            hi = m2
    rs = (lo + hi) / 2
    return rs, e8_opt_given_rho(rs, A)[0]


e8_prev = None
for e8A in (0.10, 0.16, 0.25):
    e8rs, e8I = e8_solve(e8A)
    e8lhs = e8pH * (e8Rp(e8I) - e8R(e8I) / e8I)
    e8rhs = (1 - e8r - e8G(e8rs)) / e8F(e8rs)
    chk("8 FOC (1) holds at optimum", e8lhs, e8rhs, 1e-6)
    e8rho1 = e8pH * e8R(e8I) / e8I
    e8rho0 = e8rho1 - e8pH * e8Bdp
    chk("8 rho0 < rho* < rho1", float(e8rho0 < e8rs < e8rho1), 1.0)
    chk("8 free cash flow r > rho*", float(e8r > e8rs), 1.0)
    chk("8 dA/dI = F pH B/((1+mu)dp) > 0",
        1 - e8r + e8G(e8rs) - e8F(e8rs) * e8pH * (e8Rp(e8I) - e8Bdp),
        e8F(e8rs) * e8pH * e8Bdp * (e8rs - e8rho0) / (e8rho1 - e8rho0), 1e-6)
    if e8_prev:
        chk("8 I and rho* rise with A", float(e8I > e8_prev[1] and e8rs > e8_prev[0]), 1.0)
        chk("8 short-term debt per unit r-rho* falls with A", float(e8r - e8rs < e8r - e8_prev[0]), 1.0)
    e8_prev = (e8rs, e8I)
# h decreasing for the uniform: f(intF-(1-r)) < F^2 at the optimum cutoffs
chk("8 h'(rho*)<0 (uniform)", float((1 / e8rb) * (e8G(e8_prev[0]) - (1 - e8r)) < e8F(e8_prev[0]) ** 2), 1.0)

# ---------------- Exercise 9 (Tirole 5.9): tau(I1) = th*sqrt(I1) ----------------------------------
e9p, e9th, e9R, e9r, e9I = 0.3, 0.2, 2.0, 0.5, 1.0
e9tau = lambda x: e9th * math.sqrt(x)
e9taup = lambda x: e9th / (2 * math.sqrt(x))
e9I1s = (e9th * e9R / 2) ** 2
chk("9 FOC tau'(I1*)R = 1", e9taup(e9I1s) * e9R, 1.0)
chk("9 tau'(r)R < 1 so I1* < r", float(e9taup(e9r) * e9R < 1 and e9I1s < e9r), 1.0)
# first-best structure with rb = 0 (max short-term debt); r - I1* < I forces Rl > 0
e9rl = e9r - e9I1s
e9Rl = (e9I - e9rl) / (e9p + e9tau(e9I1s))
e9Rb = e9R - e9Rl
chk("9 Rl>0 and Rb<R", float(0 < e9Rl < e9R), 1.0)
# secret deal of size d: dU_b = [1 - tau'(I1)Rb] d to first order
e9d = 1e-7
e9U0 = (e9p + e9tau(e9I1s)) * e9Rb
e9dRl = e9d / (e9p + e9tau(e9I1s))
e9U1 = (e9p + e9tau(e9I1s - e9d)) * (e9Rb + e9dRl)
chk("9 dU_b/d = 1 - tau'(I1*)Rb", (e9U1 - e9U0) / e9d, 1 - e9taup(e9I1s) * e9Rb, 1e-5)
chk("9 dU_b/d = Rl/R (gain = other lenders' loss)", (e9U1 - e9U0) / e9d, e9Rl / e9R, 1e-5)
# collusion-proof structure: rb = 0, tau'(I1)Rb = 1, I = r - I1 + [p + tau(I1)](R - Rb)
e9lo, e9hi = 1e-12, e9I1s
for _ in range(200):
    e9m = (e9lo + e9hi) / 2
    e9val = e9r - e9m + (e9p + e9tau(e9m)) * (e9R - 1 / e9taup(e9m)) - e9I
    e9lo, e9hi = (e9lo, e9m) if e9val < 0 else (e9m, e9hi)
e9I1 = e9m
chk("9 collusion-proof I1 < I1*", float(e9I1 < e9I1s), 1.0)
chk("9 collusion-proof Rb < R", float(1 / e9taup(e9I1) < e9R), 1.0)
chk("9 short-term payout larger", float(e9r - e9I1 > e9r - e9I1s), 1.0)

# ---------------- Exercise 10 (Amaro de Matos 5.2.5 #2): Shapley bargaining ----------------------
def shapley(players, v):
    """Shapley value by enumerating orderings; v maps frozenset -> worth."""
    out = {p: 0.0 for p in players}
    perms = list(permutations(players))
    for o in perms:
        s = frozenset()
        for p in o:
            out[p] += v(s | {p}) - v(s)
            s = s | {p}
    return {p: x / len(perms) for p, x in out.items()}


e10y, e10yA, e10yB, e10al, e10cb, e10q, e10K = 10.0, 4.0, 3.0, 0.8, 6.0, 0.6, 2.0
e10D = e10y - e10yA - e10yB
chk("10 Delta", e10D, 3.0)


def e10v(scale):
    def v(s):
        if "M" not in s:
            return 0.0
        has1, has2 = "1" in s, "2" in s
        return scale * (e10y if has1 and has2 else e10yA if has1 else e10yB if has2 else 0.0)
    return v


e10sh = shapley(["M", "1", "2"], e10v(1.0))
chk("10 manager share S = y/2 - D/6", e10sh["M"], e10y / 2 - e10D / 6)
chk("10 S numeric", e10sh["M"], 4.5)
chk("10 creditors y - S = y/2 + D/6", e10sh["1"] + e10sh["2"], e10y / 2 + e10D / 6)
chk("10 creditors numeric", e10sh["1"] + e10sh["2"], 5.5)
chk("10 one creditor y - S", e10y / 2, 5.0)
e10shL = shapley(["M", "1", "2"], e10v(e10al))       # M = buyer, worth alpha*y
chk("10 buyer share", e10shL["M"], 3.6)
chk("10 buyer prob", e10shL["M"] / e10cb, 0.6)
chk("10 creditors' liquidity share", e10shL["1"] + e10shL["2"], 4.4)
e10Lbar = (e10shL["M"] / e10cb) * (e10shL["1"] + e10shL["2"])
chk("10 Lbar formula", e10Lbar, e10al**2 * e10y**2 / (4 * e10cb) - e10al**2 * e10D**2 / (36 * e10cb))
chk("10 Lbar numeric", e10Lbar, 2.64)
e10L1 = (e10al * e10y / 2 / e10cb) * (e10al * e10y / 2)
chk("10 L one creditor", e10L1, e10al**2 * e10y**2 / (4 * e10cb))
chk("10 L one creditor numeric", e10L1, 2.666667, 1e-6)
chk("10 buyer prob one creditor", e10al * e10y / 2 / e10cb, 2 / 3)
chk("10 Lo - Lbar", e10L1 - e10Lbar, 0.026667, 1e-6)
e10D1 = e10q * e10y / 2 + (1 - e10q) * e10L1
e10D2 = e10q * (e10y / 2 + e10D / 6) + (1 - e10q) * e10Lbar
e10D2m = e10q * (e10y / 2 - e10D / 6) + (1 - e10q) * e10Lbar
chk("10 D1", e10D1, 4.066667, 1e-6)
chk("10 D2", e10D2, 4.356)
chk("10 D2 misprint", e10D2m, 3.756)
chk("10 beta1", e10K / e10D1, 0.491803, 1e-6)
chk("10 beta2", e10K / e10D2, 0.459137, 1e-6)
chk("10 beta misprint", e10K / e10D2m, 0.532481, 1e-6)
chk("10 D2-D1 formula", e10D2 - e10D1, e10q * e10D / 6 - (1 - e10q) * e10al**2 * e10D**2 / (36 * e10cb))
e10qbar = e10al**2 * e10D / (6 * e10cb + e10al**2 * e10D)
chk("10 qbar", e10qbar, 0.050633, 1e-6)
e10ql = 0.02
chk("10 D2-D1 at q=0.02", e10ql * e10D / 6 - (1 - e10ql) * e10al**2 * e10D**2 / (36 * e10cb), -0.016133, 1e-6)
chk("10 participation conditions", float(e10al * e10y / 2 <= e10cb and e10shL["M"] <= e10cb), 1.0)
chk("10 strategic gain y-S two minus one", e10D / 6, 0.5)
chk("10 alpha^2 y^2/(4cb)", e10al**2 * e10y**2 / (4 * e10cb), 2.666667, 1e-6)
chk("10 alpha^2 D^2/(36cb)", e10al**2 * e10D**2 / (36 * e10cb), 0.026667, 1e-6)

# ---------------- Exercise 11 (Amaro de Matos 5.2.5 #4): U^L - U^N = e(Chat - C) ------------------
def e11_payoffs(X, C, L, R, pi, f, fd, Vd):
    e = fd * (1 - f) / (f * (1 - fd))
    Pd = 1 - (1 - e) * f
    qd = pi + fd * (1 - pi)
    UN = X + C - R**2 / f + R * Vd * e * (1 / fd - 1 / qd)
    r1N = (R - Pd * Vd) / ((1 - e) * f)
    UN_direct = e * (X + C - R * Vd / qd) + (1 - e) * (X + C - r1N * R)
    r1L = (R - Pd * L) / ((1 - e) * f)
    UL = (1 - e) * (X + C - r1L * R)
    Chat = L * R / fd - X - R * Vd * (1 / fd - 1 / qd)
    return e, Pd, qd, UN, UN_direct, UL, Chat


for (e11X, e11C, e11L, e11R, e11pi, e11f, e11fd, e11V) in [
        (1.4, 0.35, 1.0, 1.0, 0.5, 0.5, 1 / 3, 8 / 9),
        (2.0, 0.1, 0.9, 1.1, 0.4, 0.6, 0.25, 0.7)]:
    e11 = e11_payoffs(e11X, e11C, e11L, e11R, e11pi, e11f, e11fd, e11V)
    chk("11 Bayes fd = fe/Pd", e11f * e11[0] / e11[1], e11fd)
    chk("11 Lemma 5.2.1 payoff form", e11[3], e11[4])
    chk("11 UL - UN = e(Chat - C)", e11[5] - e11[3], e11[0] * (e11[6] - e11C))
# (5.12) => C <= (LR - qd X)/fd <= Chat whenever Vd <= qd X / R
e11X, e11L, e11R, e11pi, e11fd = 1.4, 1.0, 1.0, 0.5, 1 / 3
e11qd = e11pi + e11fd * (1 - e11pi)
e11C = (e11L * e11R - e11qd * e11X) / e11fd          # largest C allowed by (5.12)
for e11V in (0.5, 0.8, e11qd * e11X / e11R):
    e11Ch = e11L * e11R / e11fd - e11X - e11R * e11V * (1 / e11fd - 1 / e11qd)
    chk("11 (5.12) bound <= Chat", float(e11C <= e11Ch + 1e-12), 1.0)
chk("11 equality at Vd = qdX/R", e11Ch, e11C)

# ---------------- Exercise 12 (Amaro de Matos 5.2.5 #5-#6) ---------------------------------------
def e12(X, C, f, L=1.0, R=1.0, pi=0.5, fd=1 / 3):
    q = pi + f * (1 - pi)
    rho = R**2 / q
    e = fd * (1 - f) / (f * (1 - fd))
    Pd = 1 - (1 - e) * f
    qd = pi + fd * (1 - pi)
    roll = qd * X / R
    # short-term: no liquidation if r1 = R (from 5.11 with Vd = r1) can be rolled over
    if roll >= R:
        r1, Vd, liq = R, R, False
        Fd = R * r1 / qd
        UST = e * (X + C - Fd) + (1 - e) * (X + C - r1 * R)
    else:
        Vd, liq = max(L, roll), True
        r1 = (R - Pd * Vd) / ((1 - e) * f)
        Fd = None
        UST = (1 - e) * (X + C - r1 * R)
    ULT = X + C - rho
    VdL = qd * rho / R
    Chat = L * R / fd - X - R * VdL * (1 / fd - 1 / qd)
    return dict(q=q, rho=rho, e=e, Pd=Pd, qd=qd, roll=roll, r1=r1, Vd=Vd, liq=liq, Fd=Fd,
                UST=UST, ULT=ULT, VdL=VdL, Chat=Chat)


e12a = e12(1.75, 0.0, 0.5)
chk("12.0 q", e12a["q"], 0.75)
chk("12.0 rho", e12a["rho"], 4 / 3)
chk("12.0 e", e12a["e"], 0.5)
chk("12.0 Pd", e12a["Pd"], 0.75)
chk("12.0 qd", e12a["qd"], 2 / 3)
chk("12.0 qdX/R", e12a["roll"], 7 / 6)
chk("12.0 r1", e12a["r1"], 1.0)
chk("12.0 no liquidation", float(e12a["liq"]), 0.0)
chk("12.0 refinance face", e12a["Fd"], 1.5)
chk("12.0 refinance face <= X", float(e12a["Fd"] <= 1.75), 1.0)
chk("12.0 U_LT", e12a["ULT"], 5 / 12)
chk("12.0 U_LT dec", e12a["ULT"], 0.416667, 1e-6)
chk("12.0 U_ST", e12a["UST"], 0.5)
chk("12.0 VdL", e12a["VdL"], 8 / 9)
chk("12.0 U_ST pieces", 0.5 * (1.75 - 1.5), 1 / 8)
chk("12.0 U_ST pieces2", 0.5 * (1.75 - 1.0), 3 / 8)
chk("12.0 Lemma 5.2.1 form, Vd=1", 1.75 - 2 + 1 * 0.5 * (3 - 1.5), 0.5)
chk("12.0 Lemma 5.2.1 form, Vd=8/9", 1.75 - 2 + (8 / 9) * 0.5 * (3 - 1.5), 5 / 12)
chk("12.0 Chat (with Vd=1) < 0", 1 / (1 / 3) - 1.75 - 1 * (3 - 1.5), -0.25)

e12b = e12(1.4, 0.35, 0.5)
chk("12.6 qdX/R", e12b["roll"], 14 / 15)
chk("12.6 qdX/R dec", e12b["roll"], 0.933333, 1e-6)
chk("12.6 liquidation", float(e12b["liq"]), 1.0)
chk("12.6 Vd = L", e12b["Vd"], 1.0)
chk("12.6 r1", e12b["r1"], 1.0)
chk("12.6 rho <= X", float(e12b["rho"] <= 1.4), 1.0)
chk("12.6 U_ST", e12b["UST"], 0.375)
chk("12.6 U_LT", e12b["ULT"], 0.416667, 1e-6)
chk("12.6 X+C", 1.4 + 0.35, 1.75)
chk("12.6 Chat", e12b["Chat"], 0.266667, 1e-6)
chk("12.6 Chat exact", e12b["Chat"], 4 / 15)
chk("12.6 gap e(Chat-C)", e12b["e"] * (e12b["Chat"] - 0.35), e12b["UST"] - e12b["ULT"])
chk("12.6 gap value", e12b["UST"] - e12b["ULT"], -0.041667, 1e-6)
chk("12.6 (5.12) lhs", (e12b["qd"] * 1.4 + (1 / 3) * 0.35) / 1.0, 1.05)
chk("12.6 fdC", (1 / 3) * 0.35, 0.116667, 1e-6)
chk("12.6 3 - 1.4", 3 - 1.4, 1.6)

e12c = e12(1.4, 0.35, 0.75)
chk("12.6' e", e12c["e"], 1 / 6)
chk("12.6' q", e12c["q"], 7 / 8)
chk("12.6' rho", e12c["rho"], 8 / 7)
chk("12.6' rho dec", e12c["rho"], 1.142857, 1e-6)
chk("12.6' Pd", e12c["Pd"], 3 / 8)
chk("12.6' liquidation", float(e12c["liq"]), 1.0)
chk("12.6' r1", e12c["r1"], 1.0)
chk("12.6' U_ST", e12c["UST"], 0.625)
chk("12.6' U_LT", e12c["ULT"], 17 / 28)
chk("12.6' U_LT dec", e12c["ULT"], 0.607143, 1e-6)
chk("12.6' VdL", e12c["VdL"], 16 / 21)
chk("12.6' Chat", e12c["Chat"], 16 / 35)
chk("12.6' Chat dec", e12c["Chat"], 0.457143, 1e-6)
chk("12.6' gap", e12c["UST"] - e12c["ULT"], 0.017857, 1e-6)
chk("12.6' gap e(Chat-C)", e12c["e"] * (e12c["Chat"] - 0.35), e12c["UST"] - e12c["ULT"])
e12S = 0.5 * (1 - 1 + (1 / 3) * (0.35 + 1.4 - 1)) / ((1 - 0.5) * (1 - (1 / 3) * (0.35 + 1.4)))
chk("12 Prop 5.2.1 bound", e12S, 0.6)
chk("12 Prop num", (1 / 3) * 0.75, 0.25)
chk("12 Prop den", 1 - (1 / 3) * 1.75, 0.416667, 1e-6)
# alternative reading: keep e = 1/2 at f = 3/4 -> fd = 3/5, no liquidation, ST still preferred
e12d = e12(1.4, 0.35, 0.75, fd=0.6)
chk("12 alt e", e12d["e"], 0.5)
chk("12 alt qd", e12d["qd"], 0.8)
chk("12 alt qdX/R", e12d["roll"], 1.12)
chk("12 alt no liquidation", float(e12d["liq"]), 0.0)
chk("12 alt U_ST", e12d["UST"], 0.625)

# ---------------- Exercise 13 (Tirole 4.9): uniform r, pH(r) = 0.3 + 0.5 r, R = 2, B/dp = 1.6 ----
e13rho1 = lambda r: (0.3 + 0.5 * r) * 2.0
e13rho0 = lambda r: (0.3 + 0.5 * r) * (2.0 - 1.6)
chk("13 rho1", e13rho1(0.0), 0.6)
chk("13 rho0 intercept", e13rho0(0.0), 0.12)
chk("13 rho0 slope", e13rho0(1.0) - e13rho0(0.0), 0.2)
chk("13 E[r + rho0]", 0.5 + (e13rho0(0) + e13rho0(1)) / 2, 0.72)


def e13P(x, Linv):
    """Investors' income (besides nothing else) with cutoff x and liquidation payoff Linv."""
    return 0.5 + 0.12 * (1 - x) + 0.1 * (1 - x * x) + Linv * x


def e13root(Linv, target):
    """Lowest root of 0.72 + (Linv - 0.12)x - 0.1x^2 = target."""
    b = Linv - 0.12
    return (b - math.sqrt(b * b - 0.4 * (target - 0.72))) / 0.2


# case (v): L = 0.5, I - A = 0.75
e13rs = e13root(0.5, 0.75)
chk("13v r*", e13rs, 0.080659, 1e-6)
chk("13v P(r*) = I-A", e13P(e13rs, 0.5), 0.75)
chk("13v rho0(r*)", e13rho0(e13rs), 0.136132, 1e-6)
chk("13v dr*/dA", -1 / (0.5 - e13rho0(e13rs)), -2.748249, 1e-6)
chk("13v rhat", (0.25 - 0.12) / 0.2, 0.65)
chk("13v Pc(r*)", e13P(e13rs, 0.25), 0.75 - e13rs * 0.25)
chk("13v Pc(rhat)", e13P(0.65, 0.25), 0.76225)
e13rss = e13root(0.25, 0.75)
chk("13v r**", e13rss, 0.3)
e13loss = 0.1 * (e13rss - e13rs) + (e13rss**2 - e13rs**2) / 2
chk("13v NPV loss", e13loss, 0.063681, 1e-6)
chk("13v (1),(2)", float(0.6 > 0.5 and 0.5 + 0.5 > 0.75 > 0.72), 1.0)
# case (iv): L = 0.3, I - A = 0.78
e13rs4 = e13root(0.3, 0.78)
chk("13iv r*", e13rs4, 0.441742, 1e-6)
chk("13iv rhat", (0.15 - 0.12) / 0.2, 0.15)
chk("13iv rho0(r*) <= L", float(e13rho0(e13rs4) <= 0.3), 1.0)
e13max = 0.5 + 0.15 * 0.15 + 0.12 * 0.85 + 0.1 * (1 - 0.15**2)
chk("13iv max pledgeable under court", e13max, 0.72225)
# brute-force: no cutoff policy (any x) reaches I - A under the court
chk("13iv no x works", float(max(e13P(k / 1000, 0.15) for k in range(1001)) < 0.78), 1.0)
chk("13iv (1),(2)", float(0.6 > 0.3 and 0.5 + 0.3 > 0.78 > 0.72), 1.0)

# ---------------- extra checks: every remaining printed number --------------------------------------
chk("10 one-creditor buy prob printed", e10al * e10y / 2 / e10cb, 0.666667, 1e-6)
chk("10 alpha^2 Delta", e10al**2 * e10D, 1.92)
chk("10 6cb + alpha^2 Delta", 6 * e10cb + e10al**2 * e10D, 37.92)
chk("10 alpha^2*100/24", 0.64 * 100 / 24, 2.666667, 1e-6)
chk("12.6' Chat - C", e12c["Chat"] - 0.35, 0.107143, 1e-6)
chk("12.6' 1.6 - 8/7", 1.6 - 8 / 7, e12c["Chat"])
chk("12.6 1.6 - 4/3", 1.6 - 4 / 3, e12b["Chat"])
chk("13v discriminant", 0.38**2 - 4 * 0.1 * 0.03, 0.1324)
chk("13v sqrt", math.sqrt(0.1324), 0.363868, 1e-6)
chk("13v loss part 1", 0.1 * (e13rss - e13rs), 0.021934, 1e-6)
chk("13v loss part 2", (e13rss**2 - e13rs**2) / 2, 0.041747, 1e-6)
chk("13v sqrt court", math.sqrt(0.13**2 - 0.4 * 0.03), 0.07)
chk("13iv 0.15^2", 0.15 * 0.15, 0.0225)
chk("13iv int 0.12", 0.12 * 0.85, 0.102)
chk("13iv int 0.1", 0.1 * (1 - 0.15**2), 0.09775)
chk("13v Pc(rhat) form", 0.72 + 0.13 * 0.65 - 0.1 * 0.65**2, 0.76225)

# ---------------- deeper solutions (2026-11-12): new intermediate lines --------------------------
# Ex 2: r1 - R = P_d (R - M) / P_u in case B
ex2_M = max(ex2_L, (ex2_pi + ex2_fd * (1 - ex2_pi)) * ex2_X / ex2_R)
chk("2 r1-R identity", ex2_r1v - ex2_R, (1 - ex2_Pu) * (ex2_R - ex2_M) / ex2_Pu)
chk("2 r1-M identity", ex2_r1v - ex2_M, (ex2_R - ex2_M) / ex2_Pu)
# Ex 3: inefficiency (1-q) beta (y - L0) falls with q (numerical derivative)
ex3_L0 = 0.8**2 * 16 / 8
ex3_ineff = lambda q: (1 - q) * ex3_beta(q, *ex3_p[1:]) * (4.0 - ex3_L0)
chk("3 inefficiency derivative", (ex3_ineff(0.5 + ex3_h) - ex3_ineff(0.5 - ex3_h)) / (2 * ex3_h),
    (4.0 - ex3_L0) * (-ex3_beta(*ex3_p) + 0.5 * ex3_dbeta(*ex3_p)), 1e-6)
chk("3 inefficiency falls", float((4.0 - ex3_L0) * (-ex3_beta(*ex3_p) + 0.5 * ex3_dbeta(*ex3_p)) < 0), 1.0)
# Ex 5: intermediate fractions
chk("5 e num", fd5 * (1 - f5), Fr(1, 6)); chk("5 e den", f5 * (1 - fd5), Fr(1, 3))
chk("5 Bayes check", f5 * e5 / (f5 * e5 + 1 - f5), Fr(1, 3))
chk("5 U_l 21-16", Fr(21 - 16, 12), Fr(5, 12))
chk("5 lemma -3+8", Fr(-3 + 8, 12), Fr(5, 12))
chk("5 R^2/f", R5**2 / f5, 2); chk("5 1/fd-1/qd", 1 / fd5 - 1 / qd5, Fr(3, 2))
chk("5 lemma short 3/4 part", Fr(1, 4) * 0 + R5 * 1 * e5 * Fr(3, 2), Fr(3, 4))
# Ex 6: (PD) gain of firm 1 from predation
chk("6 PD gain", zF6 * D6 + (1 - zF6) * M6 - (zS6 * D6 + (1 - zS6) * M6), (zS6 - zF6) * (M6 - D6))
# Ex 10: Shapley pieces
chk("10 Delta arithmetic", 10 - 4 - 3, 3)
chk("10 S = (3y - D)/6", (3 * e10y - e10D) / 6, e10sh["M"])
chk("10 S = (2y+yA+yB)/6", (2 * e10y + e10yA + e10yB) / 6, e10sh["M"])
chk("10 Lbar = a^2(9y^2-D^2)/(36cb)", e10al**2 * (9 * e10y**2 - e10D**2) / (36 * e10cb), e10Lbar)
# Ex 11: long-term break-even is (5.11) with r1 = rho/R, since P_u + P_d q^d = q
for (e11pi, e11f, e11fd, e11R) in [(0.5, 0.5, 1 / 3, 1.0), (0.4, 0.6, 0.25, 1.1)]:
    e11e = e11fd * (1 - e11f) / (e11f * (1 - e11fd))
    e11Pu, e11Pd = (1 - e11e) * e11f, 1 - (1 - e11e) * e11f
    e11qd, e11q = e11pi + e11fd * (1 - e11pi), e11pi + e11f * (1 - e11pi)
    chk("11 Pu + Pd qd = q", e11Pu + e11Pd * e11qd, e11q)
    e11rho = e11R**2 / e11q
    chk("11 LT break-even", e11Pu * e11rho / e11R + e11Pd * e11qd * e11rho / e11R, e11R)
    chk("11 Pd/f = e/fd", e11Pd / e11f, e11e / e11fd)
chk("11 Chat example", 3 - 1.75 - 1 * 1 * (3 - 1.5), -0.25)
# Ex 12: intermediate fractions and the lemma line
chk("12 e (1/6)/(1/3)", (1 / 6) / (1 / 3), 0.5)
chk("12 e' (1/12)/(1/2)", (1 / 12) / (1 / 2), 1 / 6)
chk("12 Pd' = 1 - 5/8", 1 - (5 / 6) * (3 / 4), 3 / 8)
chk("12 (1-e)f at f=3/4", (5 / 6) * (3 / 4), 5 / 8)
chk("12 r1 at f=3/4", (1 - (3 / 8) * 1) / (5 / 8), 1.0)
chk("12 lemma1 Vd=1", -0.25 + 0.75 * 1, 0.5)
chk("12 lemma1 Vd=8/9", -0.25 + 0.75 * (8 / 9), 5 / 12)
chk("12.6 X+C-1", 1.4 + 0.35 - 1, 0.75)
chk("12.6 diff identity", -0.5 * 1.75 + 0.5 * 1 * 1 / (1 / 3) - 0.5 * 1 * (8 / 9) * (3 - 1.5),
    e12b["e"] * (e12b["Chat"] - 0.35))
chk("12.6' VdL = (2/3)(8/7)", (2 / 3) * (8 / 7), 16 / 21)
chk("12 Prop num 1-1+(1/3)(0.75)", 1 - 1 + (1 / 3) * 0.75, 0.25)
# Ex 13: every new intermediate number
chk("13 rho1 = (0.3+0.5r)2", (0.3 + 0.5 * 0.7) * 2, 0.6 + 0.7)
chk("13 rho0 = (0.3+0.5r)0.4", (0.3 + 0.5 * 0.7) * (2 - 1.6), 0.12 + 0.2 * 0.7)
chk("13 E[r+rho0] pieces", 0.5 + 0.12 + 0.2 * 0.5, 0.72)
for e13x in (0.0, 0.3, 0.8):
    chk("13 P(x) closed form", e13P(e13x, 0.5), 0.72 + (0.5 - 0.12) * e13x - 0.1 * e13x**2)
chk("13v 0.38^2", 0.38**2, 0.1444); chk("13v 4(0.1)(0.03)", 4 * 0.1 * 0.03, 0.012)
chk("13v L - rho0(r*)", 0.5 - e13rho0(e13rs), 0.363868, 1e-6)
chk("13v -1/0.363868", -1 / 0.363868, -2.748249, 1e-6)
chk("13v 0.13*0.65", 0.13 * 0.65, 0.0845); chk("13v 0.1*0.65^2", 0.1 * 0.65**2, 0.04225)
chk("13v 0.13^2", 0.13**2, 0.0169); chk("13v disc court", 0.0169 - 0.012, 0.0049)
chk("13v rho1-L = 0.1+r", e13rho1(0.2) - 0.5, 0.1 + 0.2)
chk("13iv 0.18^2", 0.18**2, 0.0324); chk("13iv 4(0.1)(0.06)", 4 * 0.1 * 0.06, 0.024)
chk("13iv disc", 0.0324 - 0.024, 0.0084); chk("13iv sqrt", math.sqrt(0.0084), 0.091652, 1e-6)
chk("13iv r* from root", (0.18 - math.sqrt(0.0084)) / 0.2, 0.441742, 1e-6)
chk("13iv rho0(r*)", e13rho0(e13rs4), 0.208348, 1e-6)
chk("13iv sum", 0.5 + 0.0225 + 0.102 + 0.09775, 0.72225)

print(f"PASS {N} checks")
