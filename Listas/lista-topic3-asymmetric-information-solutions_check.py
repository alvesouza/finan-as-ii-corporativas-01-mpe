"""Numeric checks for Listas/lista-topic3-asymmetric-information-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-topic3-asymmetric-information-solutions_check.py  -> PASS <n> checks
"""
import math  # noqa: F401  (fragments use it)

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1

# ======================================================================
# t3a
# Topic 3 list, exercises 1-8: every number printed in detailed.tex / short.tex.
# Run after check_header.py (provides chk, math).

# --- Ex 1: Ross Cap. 15 Q3 -------------------------------------------------
e1_P0, e1_u, e1_o, e1_Q, e1_pi, e1_pip = 40, 7, 5, 1000, 0.5, 1.0
chk("e1 true value under", e1_P0 + e1_u, 47)
chk("e1 true value over", e1_P0 - e1_o, 35)
chk("e1 full gain", e1_Q * e1_u - e1_Q * e1_o, 2000)
chk("e1 rationed gain part", e1_pi * e1_Q * e1_u, 3500)
chk("e1 expected gain", e1_pi * e1_Q * e1_u - e1_pip * e1_Q * e1_o, -1500)
e1_ustar = e1_pip / e1_pi * e1_o
chk("e1 break-even underpricing", e1_ustar, 10)
chk("e1 average initial return", (e1_ustar - e1_o) / 2, 2.5)

# --- Ex 2: GT 19.4 (lecture example) ---------------------------------------
e2_R, e2_I, e2_p, e2_q, e2_a = 50, 30, 0.8, 0.7, 0.5
e2_m = e2_a * e2_p + (1 - e2_a) * e2_q
chk("e2 m", e2_m, 0.75)
chk("e2 NPV", e2_p * e2_R - e2_I, 10)
e2_UG = lambda A, m: (e2_p * e2_R - e2_I) - (e2_I - A) * (e2_p / m - 1)
chk("e2 UG(0)", e2_UG(0, e2_m), 8)
chk("e2 UG(15)", e2_UG(15, e2_m), 9)
chk("e2 discount A=0", (e2_I - 0) * (e2_p / e2_m - 1), 2)
chk("e2 discount A=15", (e2_I - 15) * (e2_p / e2_m - 1), 1)
# direct check of the closed form against p(R - Ru) - A
e2_A = 15
chk("e2 UG identity", e2_p * (e2_R - (e2_I - e2_A) / e2_m) - e2_A, e2_UG(e2_A, e2_m))
e2_m2 = 0.2 * 0.8 + 0.8 * 0.5
chk("e2 m breakdown", e2_m2, 0.56)
chk("e2 mR", e2_m2 * e2_R, 28)
chk("e2 Amin", e2_I - e2_m2 * e2_R, 2)

# --- Ex 3: Berk 16.29 --------------------------------------------------------
e3_N0, e3_Pm, e3_K, e3_C = 100, 13.50, 500, 20
e3_n = e3_K / e3_Pm
chk("e3 new shares", e3_n, 37.037, 1e-3)
chk("e3 total shares", e3_N0 + e3_n, 137.037, 1e-3)
e3_PE = lambda v: (e3_N0 * v + e3_K) / (e3_N0 + e3_n)
e3_PD = lambda v: (e3_N0 * v - e3_C) / e3_N0
chk("e3 equity value low", e3_N0 * 12.50 + e3_K, 1750)
chk("e3 equity value high", e3_N0 * 14.50 + e3_K, 1950)
chk("e3 PE low", e3_PE(12.50), 12.77, 5e-3)
chk("e3 PE low 4dp", e3_PE(12.50), 12.7703, 5e-5)
chk("e3 PD low", e3_PD(12.50), 12.30)
chk("e3 PE high", e3_PE(14.50), 14.23, 5e-3)
chk("e3 PD high", e3_PD(14.50), 14.30)
assert e3_PE(12.50) > e3_PD(12.50) and e3_PE(14.50) < e3_PD(14.50)
chk("e3 distress per share", e3_C / e3_N0, 0.20)
chk("e3 dilution loss high", 14.50 - e3_PE(14.50), 0.27, 5e-3)
chk("e3 shares at 12.50", e3_K / 12.50, 40)
chk("e3 consistency at 12.50", (1250 + 500) / (e3_N0 + e3_K / 12.50), 12.50)
chk("e3 X threshold", e3_N0 * (e3_PE(12.50) - 12.50), 27.03, 5e-3)

# --- Ex 4: GT 19.6 -------------------------------------------------------------
e4_N0, e4_Vin, e4_Vout, e4_K, e4_VP = 100, 1000, 600, 100, 120
chk("e4 NPV", e4_VP - e4_K, 20)
e4_Pi = e4_Vout / e4_N0
chk("e4 issue price", e4_Pi, 6.00)
e4_n = e4_K / e4_Pi
chk("e4 new shares", e4_n, 16.67, 5e-3)
chk("e4 total shares", e4_N0 + e4_n, 116.67, 5e-3)
e4_take = (e4_Vin + e4_VP) / (e4_N0 + e4_n)
chk("e4 value take", e4_Vin + e4_VP, 1120)
chk("e4 P take", e4_take, 9.60)
chk("e4 P pass", e4_Vin / e4_N0, 10.00)
e4_frac = e4_n / (e4_N0 + e4_n)
chk("e4 new holders fraction", e4_frac, 0.142857, 1e-6)
chk("e4 new holders value", e4_frac * 1120, 160)
chk("e4 transfer", e4_frac * 1120 - e4_K, 60)
chk("e4 old holders loss", (e4_frac * 1120 - e4_K) - (e4_VP - e4_K), 40)
chk("e4 loss per share", e4_Vin / e4_N0 - e4_take, 0.40)
chk("e4 threshold price", e4_Vin * e4_K / (e4_N0 * e4_VP), 8.33, 5e-3)
e4_Pi2 = (e4_Vout + e4_VP - e4_K) / e4_N0
chk("e4 alt value with project", e4_Vout + e4_VP, 720)
chk("e4 alt issue price", e4_Pi2, 6.20)
chk("e4 alt new shares", e4_K / e4_Pi2, 16.13, 5e-3)
chk("e4 alt total shares", e4_N0 + e4_K / e4_Pi2, 116.13, 5e-3)
chk("e4 alt P take", 1120 / (e4_N0 + e4_K / e4_Pi2), 9.64, 5e-3)

# --- Ex 5: Ross CQ 17.6 --------------------------------------------------------
e5_Pb, e5_Pa = 28.50, 25
chk("e5 price change", e5_Pa - e5_Pb, -3.50)
chk("e5 return %", 100 * (e5_Pa - e5_Pb) / e5_Pb, -12.28, 5e-3)

# --- Ex 6: Tirole 6.1 (illustration) ------------------------------------------
e6_pH, e6_pL, e6_R, e6_I, e6_BL, e6_BH = 0.8, 0.2, 100, 50, 9, 27
e6_dp = e6_pH - e6_pL
chk("e6 dp", e6_dp, 0.6)
chk("e6 BL/dp", e6_BL / e6_dp, 15)
chk("e6 BH/dp", e6_BH / e6_dp, 45)
chk("e6 (1) left", e6_pH * (e6_R - e6_BH / e6_dp), 44)
chk("e6 (1) right", e6_pH * (e6_R - e6_BL / e6_dp), 68)
chk("e6 (2)", e6_pL * e6_R, 20)
assert e6_pH * (e6_R - e6_BH / e6_dp) < e6_I < e6_pH * (e6_R - e6_BL / e6_dp)
assert e6_pL * e6_R < e6_I
e6_astar = (e6_I / (e6_R - e6_BL / e6_dp) - e6_pL) / e6_dp
chk("e6 alpha* = 11/17", e6_astar, 11 / 17)
chk("e6 alpha* 4dp", e6_astar, 0.6471, 5e-5)
# Pi(alpha*) = 0
chk("e6 Pi(alpha*)", (e6_astar * e6_pH + (1 - e6_astar) * e6_pL) * (e6_R - e6_BL / e6_dp) - e6_I, 0)
e6_a = 0.8
e6_m = e6_a * e6_pH + (1 - e6_a) * e6_pL
chk("e6 m", e6_m, 0.68)
e6_Rb = e6_R - e6_I / e6_m
chk("e6 Rb*", e6_Rb, 26.47, 5e-3)
assert e6_BL / e6_dp <= e6_Rb < e6_BH / e6_dp
e6_pg = e6_pH * (e6_R - e6_Rb) - e6_I
e6_pb = e6_pL * (e6_R - e6_Rb) - e6_I
chk("e6 profit good", e6_pg, 8.82, 5e-3)
chk("e6 profit good closed form", e6_pg, e6_I * (e6_pH - e6_m) / e6_m)
chk("e6 profit bad", e6_pb, -35.29, 5e-3)
chk("e6 profit bad closed form", e6_pb, -e6_I * (e6_m - e6_pL) / e6_m)
chk("e6 average profit", e6_a * e6_pg + (1 - e6_a) * e6_pb, 0)
chk("e6 weighted good", e6_a * e6_pg, 7.06, 5e-3)
chk("e6 weighted bad", (1 - e6_a) * (-e6_pb), 7.06, 5e-3)
chk("e6 good utility", e6_pH * e6_Rb, 21.18, 5e-3)
chk("e6 good SI utility", e6_pH * e6_R - e6_I, 30)
chk("e6 good loss = lender profit", (e6_pH * e6_R - e6_I) - e6_pH * e6_Rb, e6_pg)
chk("e6 bad utility", e6_pL * e6_Rb + e6_BH, 32.29, 5e-3)

# --- Ex 7: Amaro de Matos 6.2.7 #4, #6 (uniform v on [0,2]) --------------------
e7_alpha = 0.36
chk("e7 pi = 1 - alpha (D_U = n)", 1 - e7_alpha, 0.64)
# pi <= pi' for a grid of demands
for e7_DU in (0.5, 1.0, 2.0):
    for e7_DI in (0.0, 0.3, 1.5):
        assert min(1, 1 / (e7_DU + e7_DI)) <= min(1, 1 / e7_DU)
e7_p0 = lambda a: 2 * math.sqrt(1 - a) / (1 + math.sqrt(1 - a))
e7_L = lambda p: p**2 / 4
e7_U = lambda p: (2 - p) ** 2 / 4
chk("e7 L formula", e7_L(0.7), 0.5 * 0.7**2 / 2)  # int_0^p (p-v)/2 dv
chk("e7 U formula", e7_U(0.7), 0.5 * (2 - 0.7) ** 2 / 2)
chk("e7 p0 alpha=0", e7_p0(0), 1.0)
chk("e7 p0 alpha=0.36", e7_p0(0.36), 0.8889, 5e-5)
chk("e7 p0 alpha=0.36 ratio", 1.6 / 1.8, e7_p0(0.36))
chk("e7 p0 alpha=0.64", e7_p0(0.64), 0.75)
chk("e7 p0 alpha=0.64 ratio", 1.2 / 1.6, e7_p0(0.64))
e7_p = e7_p0(e7_alpha)
chk("e7 break-even holds", (1 - e7_alpha) * e7_U(e7_p) - e7_L(e7_p), 0)
chk("e7 U(p0)", e7_U(e7_p), 0.308642, 1e-6)
chk("e7 F(p0)", e7_p / 2, 0.444444, 1e-6)
chk("e7 1-F(p0)", 1 - e7_p / 2, 0.555556, 1e-6)
e7_den = e7_p / 2 + (1 - e7_alpha) * (1 - e7_p / 2)
chk("e7 denominator", e7_den, 0.8)
e7_dp = -e7_U(e7_p) / e7_den
chk("e7 dp0/dalpha", e7_dp, -0.3858, 5e-5)
# compare with derivative of the closed form, and with a finite difference
e7_s = math.sqrt(1 - e7_alpha)
chk("e7 dp0/dalpha closed", -1 / (e7_s * (1 + e7_s) ** 2), e7_dp)
e7_h = 1e-6
chk("e7 dp0/dalpha numeric", (e7_p0(e7_alpha + e7_h) - e7_p0(e7_alpha - e7_h)) / (2 * e7_h), e7_dp, 1e-6)
chk("e7 underpricing", 1 - e7_p, 0.1111, 5e-5)
chk("e7 underpricing = alpha U = Nc/n", 1 - e7_p, e7_alpha * e7_U(e7_p))

# --- Ex 8: Tirole 6.2 ----------------------------------------------------------
# (a) split identity and externality inequality at a generic point
e8_pH, e8_pL, e8_R, e8_I, e8_Rb, e8_H = 0.7, 0.3, 100, 40, 20, 0.6
e8_Ul = e8_H * e8_pH * (e8_R - e8_Rb) + (1 - e8_H) * e8_pL * (e8_R - e8_Rb) - e8_I
e8_split = e8_H * (e8_pH * (e8_R - e8_Rb) - e8_I) + (1 - e8_H) * (e8_pL * (e8_R - e8_Rb) - e8_I)
chk("e8 split identity", e8_split, e8_Ul)
assert e8_Ul >= 0 and e8_pH * (e8_R - e8_Rb) - e8_I > 0  # lending point: positive profit on good
# (b) breakdown example: pL = 0, uniform H
e8_pH, e8_R, e8_I, e8_Bbar = 0.8, 100, 50, 50
e8_H = lambda Rb: min(e8_pH * Rb / e8_Bbar, 1)
e8_U = lambda Rb: e8_H(Rb) * e8_pH * (e8_R - Rb) - e8_I
e8_bound = e8_pH**2 * e8_R**2 / (4 * e8_Bbar)
chk("e8 max repayment", e8_bound, 32)
e8_grid = [e8_R * k / 10000 for k in range(10001)]
chk("e8 grid max of Ul+I", max(e8_U(r) + e8_I for r in e8_grid), e8_bound, 1e-6)
assert all(e8_U(r) < 0 for r in e8_grid)
chk("e8 argmax R/2", e8_R / 2, 50)
chk("e8 Bbar/pH", e8_Bbar / e8_pH, 62.5)
chk("e8 Bbar threshold", e8_pH**2 * e8_R**2 / (4 * e8_I), 32)
chk("e8 creditworthy cutoff", e8_pH * e8_R - e8_I, 30)
chk("e8 creditworthy mass", (e8_pH * e8_R - e8_I) / e8_Bbar, 0.6)
chk("e8 H at R/2", e8_H(50), 0.8)
chk("e8 split good part", 0.8 * (0.8 * 50 - 50), -8)
chk("e8 split bad part", 0.2 * (0 * 50 - 50), -10)
chk("e8 Ul at R/2", e8_U(50), -18)

# ======================================================================
# t3b
# Topic 3 list, exercises 9-15. Run after check_header.py (defines chk, math).
T = 1e-6

# ---- 9. Ratings (Tirole 6.6) ----
e9R, e9I, e9A, e9pH, e9pL, e9b, e9B, e9al = 10, 6, 1, 0.8, 0.4, 0.4, 1.8, 0.3
e9dp = e9pH - e9pL
chk("9 B/dp", e9B / e9dp, 4.5)
chk("9 b/dp", e9b / e9dp, 1.0)
chk("9 P(B)", e9pH * (e9R - e9B / e9dp), 4.4)
chk("9 P(b)", e9pH * (e9R - e9b / e9dp), 7.2)
chk("9 I-A", e9I - e9A, 5)
assert e9pH * (e9R - e9B / e9dp) < e9I - e9A < e9pH * (e9R - e9b / e9dp)
e9mix = e9al * e9pH + (1 - e9al) * e9pL
chk("9 mix", e9mix, 0.52)
chk("9 cond2", e9mix * (e9R - e9b / e9dp), 4.68)
assert e9mix * (e9R - e9b / e9dp) < e9I - e9A
chk("9 pLR+B", e9pL * e9R + e9B, 5.8)
assert e9pL * e9R + e9B < e9I and e9pH * e9R > e9I
e9c0 = e9pL * (e9R - (e9I - e9A) / e9pH) + e9B
e9k = e9pL / e9pH
chk("9 c0", e9c0, 3.3)
chk("9 kappa", e9k, 0.5)
e9r = 1.0
e9qa, e9qb, e9qc = -e9r * (1 - e9k), e9A - e9c0 - e9k * e9r, e9c0 - e9A   # Phi coefficients
chk("9 qa", e9qa, -0.5)
chk("9 qb", e9qb, -2.8)
chk("9 qc", e9qc, 2.3)
e9x = (-e9qb - math.sqrt(e9qb**2 - 4 * e9qa * e9qc)) / (2 * e9qa)
chk("9 xhat", e9x, 0.727038, 1e-6)
chk("9 xhat = -2.8+sqrt(12.44)", -2.8 + math.sqrt(12.44), e9x)
# book's binding no-mimic equation
e9rhs = e9x * (e9A - e9r * e9x) + (1 - e9x) * (e9pL * (e9R - (e9I - e9A + e9r * e9x) / e9pH) + e9B)
chk("9 no-mimic binds", e9rhs, e9A)
e9y = e9r * e9x
chk("9 y closed form", (1 - e9x) * (e9c0 - e9A) / (e9x + (1 - e9x) * e9k), e9y)
chk("9 U_G", e9pH * e9R - e9I + e9A - e9y, 2.272962, 1e-6)
e9RbG = e9R - (e9I - e9A + e9y) / e9pH
chk("9 I-A+rx", e9I - e9A + e9y, 5.727038, 1e-6)
chk("9 RbG", e9RbG, 2.841202, 1e-6)
assert e9RbG >= e9b / e9dp
e9E1, e9E2, e9E3 = e9pH * (e9R - e9b / e9dp) - (e9I - e9A), e9pH * e9R - e9I, e9A
chk("9 E1", e9E1, 2.2)
chk("9 E2", e9E2, 2.0)
chk("9 E3", e9E3, 1.0)
e9yb = min(e9E1, e9E2, e9E3)
e9xb = (e9c0 - e9A - e9k * e9yb) / (e9c0 - e9A + (1 - e9k) * e9yb)
chk("9 xbar", e9xb, 1.8 / 2.8)
chk("9 xbar num", e9xb, 0.642857, 1e-6)
chk("9 rbar", e9yb / e9xb, 1.555556, 1e-6)
chk("9 y sup", (e9c0 - e9A) / e9k, 4.6)
# y(r) increasing: solve Phi=0 at r slightly above/below 1
def e9xhat(r):
    a, b_, c = -r * (1 - e9k), e9A - e9c0 - e9k * r, e9c0 - e9A
    return (-b_ - math.sqrt(b_**2 - 4 * a * c)) / (2 * a)
assert 0.99 * e9xhat(0.99) < 1.01 * e9xhat(1.01) and e9xhat(0.99) > e9xhat(1.01)
chk("9 y(rbar)=ybar", (e9yb / e9xb) * e9xhat(e9yb / e9xb), e9yb)

# ---- 10. Maturity (Tirole 6.10) ----
e10pH, e10qH, e10dp, e10B, e10R, e10rho, e10r, e10IA = 0.8, 0.5, 0.4, 1.2, 10, 4.5, 1, 1.6
chk("10 B/dp", e10B / e10dp, 3)
e10G, e10Bd = e10pH * (e10R - e10B / e10dp), e10qH * (e10R - e10B / e10dp)
chk("10 rho0G", e10G, 5.6)
chk("10 rho0B", e10Bd, 3.5)
assert e10G > e10rho > e10Bd
chk("10 upper", e10r + e10G - e10rho, 2.1)
assert e10r < e10IA < e10r + e10G - e10rho
chk("10 bad hoard", e10r + e10Bd - e10rho, 0)
e10L = e10IA - e10r
chk("10 L", e10L, 0.6)
chk("10 Rn", e10rho / e10pH, 5.625)
chk("10 Rl", e10L / e10pH, 0.75)
chk("10 pH Rb", e10r + e10pH * e10R - e10rho - e10IA, 2.9)
e10Rb = (e10pH * e10R - e10rho - e10L) / e10pH
chk("10 Rb", e10Rb, 3.625)
chk("10 sum", e10Rb + e10rho / e10pH + e10L / e10pH, 10)

# ---- 11. Myers-Majluf objectives (Amaro 3.2.6 #4) ----
e11P, e11S, e11E = 10, 2, 5
def e11new(a): return e11P - e11S - a
def e11old(a): return -e11E + e11E / e11P * (e11S + a)
chk("11 a0", e11P - e11S, 8)
chk("11 new a0", e11new(8), 0)
chk("11 old a0", e11old(8), 0)
chk("11 new a4", e11new(4), 4)
chk("11 old a4", e11old(4), -2)
chk("11 new a12", e11new(12), -4)
chk("11 old a12", e11old(12), 2)
# new-shareholder gain is zero exactly on the line b = P'-(S+a)
chk("11 gain on line", e11E / (e11P + e11E) * (e11E + e11S + 4 + e11new(4)) - e11E, 0)
# E(Z|Z>=c) > c for Z ~ U[0,10]: no interior fixed point
for e11c in (0.0, 3.0, 9.0):
    assert (e11c + 10) / 2 > e11c

# ---- 12. Pecking order, variable investment (Tirole 6.8) ----
e12qH, e12R, e12Bdp, e12A, e12pH = 0.6, 3, 2, 1, 0.8
chk("12 qH(R-B/dp)", e12qH * (e12R - e12Bdp), 0.6)
e12I = e12A / (1 - e12qH * (e12R - e12Bdp))
chk("12 I_SI", e12I, 2.5)
e12U = e12A + (e12qH * e12R - 1) * e12I
chk("12 U_SI direct", e12U, 3)
chk("12 U_SI footnote", (1 + (e12qH * e12R - 1) / (1 - e12qH * (e12R - e12Bdp))) * e12A, 3)
chk("12 ratio", (e12qH * e12R - 1) / (1 - e12qH * (e12R - e12Bdp)), 2)
e12dS = 0.01
e12dF = -e12pH / (1 - e12pH) * e12dS
chk("12 dRF", e12dF, -0.04)
chk("12 dObj", e12pH * e12dS + (1 - e12pH) * e12dF, 0)
chk("12 dM", e12qH * e12dS + (1 - e12qH) * e12dF, -0.01)
chk("12 dM formula", -(e12pH - e12qH) / (1 - e12pH) * e12dS, -0.01)
assert (e12dS - e12dF) > 0          # IC relaxed
# weak monotonic profit identity at a test point with R^F > 0
e12RS, e12RF, e12It, e12q, e12p = 3.0, 0.5, 2.0, 0.6, 0.8
e12RbS = e12Bdp * e12It
e12IA = e12q * (e12RS * e12It - e12RbS) + (1 - e12q) * e12RF * e12It   # = I - A at bad's SI terms
e12Ul = e12p * (e12RS * e12It - e12RbS) + (1 - e12p) * e12RF * e12It - e12IA
chk("12 WMP identity", e12Ul, (e12p - e12q) * ((e12RS - e12Bdp) - e12RF) * e12It)

# ---- 13. Information sharing (Tirole 6.7) ----
e13p, e13q, e13R, e13I, e13d, e13al = 0.8, 0.2, 10, 6, 0.9, 0.3
def e13g(th): return th * e13R - e13I + e13d * th * (e13R - e13I)
chk("13 g(p)", e13g(e13p), 4.88)
chk("13 g(q)", e13g(e13q), -3.28)
chk("13 dp(R-I)", e13d * e13p * (e13R - e13I), 2.88)
chk("13 R+d(R-I)", e13R + e13d * (e13R - e13I), 13.6)
chk("13 alpha bound", (e13I / 13.6 - e13q) / (e13p - e13q), 0.402, 1e-3)
e13m = e13al * e13p + (1 - e13al) * e13q
assert e13m * e13R - e13I + e13d * e13m * (e13R - e13I) < 0
chk("13 pi_ns", e13al * e13g(e13p), 1.464)
chk("13 pi_s", e13al * (e13p * e13R - e13I), 0.6)
chk("13 U_s", e13d * e13al * e13p * (e13R - e13I), 0.864)
chk("13 diff", e13al * e13g(e13p) - e13al * (e13p * e13R - e13I), e13al * e13d * e13p * (e13R - e13I))
e13c = 6
def e13C(a): return e13c * (-a - math.log(1 - a))
e13as = 2.88 / (e13c + 2.88)
chk("13 alpha_s", e13as, 0.324324, 1e-6)
chk("13 FOC", e13c * e13as / (1 - e13as), e13d * e13p * (e13R - e13I))
chk("13 pi_s endo", e13as * (e13p * e13R - e13I), 0.648649, 1e-6)
e13gross = e13d * e13as * e13p * (e13R - e13I)
chk("13 gross U", e13gross, 0.934054, 1e-6)
chk("13 C(as)", e13C(e13as), 0.406307, 1e-6)
chk("13 net U", e13gross - e13C(e13as), 0.527747, 1e-6)
# alpha_s maximises the net utility (grid)
assert all(e13d * a * e13p * (e13R - e13I) - e13C(a) <= e13gross - e13C(e13as) + 1e-12
           for a in [i / 1000 for i in range(1, 1000)])

# ---- 14. Leland-Pyle mean-variance (Amaro 3.2.6 #2) ----
e14b, e14se2, e14sM2, e14cov, e14ex, e14r, e14X0, e14K, e14Em = 2, 0.5, 0.04, 0.06, 0.1, 0.05, 10, 8, 1
e14lam = e14ex / e14sM2 * e14cov
chk("14 lambda", e14lam, 0.15)
chk("14 cov^2/sM2", e14cov**2 / e14sM2, 0.09)
e14su2 = e14se2 - e14cov**2 / e14sM2
chk("14 su2", e14su2, 0.41)
chk("14 b su2", e14b * e14su2, 0.82)
def e14X(a): return e14X0 - e14b * e14su2 * (a + math.log(1 - a))
def e14V(a): return (e14X(a) - e14lam) / (1 + e14r)
def e14B(a): return (e14K - e14Em - (1 - a) * e14V(a)) / a
chk("14 X(.5)", e14X(0.5), 10.158381, 1e-6)
chk("14 V(.5)", e14V(0.5), 9.531791, 1e-6)
chk("14 B(.5)", e14B(0.5), 4.468209, 1e-6)
chk("14 K-Em", e14K - e14Em, 7)
chk("14 V-K+Em", e14V(0.5) - e14K + e14Em, 2.531791, 1e-6)
chk("14 risk term", e14b * e14su2 * 0.25 / (1 + e14r), 0.195238, 1e-6)
e14Bp = (e14V(0.5) - e14K + e14Em - e14b * e14su2 * 0.25 / (1 + e14r)) / 0.25
chk("14 B' formula", e14Bp, 9.346212, 1e-6)
e14h = 1e-6
chk("14 B' numeric", (e14B(0.5 + e14h) - e14B(0.5 - e14h)) / (2 * e14h), e14Bp, 1e-5)
chk("14 X' numeric", (e14X(0.5 + e14h) - e14X(0.5 - e14h)) / (2 * e14h),
    e14b * e14su2 * 0.5 / 0.5, 1e-5)
chk("14 V-B equiv", e14V(0.5) - e14B(0.5), (e14V(0.5) - e14K + e14Em) / 0.5)
# FOC: type Xbar = X(0.5) facing the schedule has dJ/dalpha = 0 at 0.5 (beta optimised)
e14Xbar = e14X(0.5)
def e14J(a):
    beta = (e14ex / e14b - a * e14cov) / e14sM2
    mean = a * (e14Xbar - e14X(a) + e14lam) + beta * e14ex + e14X(a) - e14lam   # (W0-K)(1+r) omitted: constant
    var = a * a * e14se2 + beta * beta * e14sM2 + 2 * a * beta * e14cov
    return mean - e14b / 2 * var
chk("14 FOC dJ/da", (e14J(0.5 + 1e-5) - e14J(0.5 - 1e-5)) / 2e-5, 0, 1e-6)
assert e14J(0.5) > e14J(0.45) and e14J(0.5) > e14J(0.55)
# full-information alpha = 0: with X fixed at Xbar, dJ/da = 0 at a = 0
def e14Jfi(a):
    beta = (e14ex / e14b - a * e14cov) / e14sM2
    mean = a * e14lam + beta * e14ex
    var = a * a * e14se2 + beta * beta * e14sM2 + 2 * a * beta * e14cov
    return mean - e14b / 2 * var
chk("14 FI alpha=0", (e14Jfi(1e-5) - e14Jfi(-1e-5)) / 2e-5, 0, 1e-6)

# ---- 15. Continuum of types (Tirole 6.5), uniform example ----
e15lo, e15hi, e15t, e15R, e15I = 0.1, 0.5, 0.3, 10, 2.5
e15Ep = (e15lo + e15hi) / 2
chk("15 tauR", e15t * e15R, 3)
chk("15 Ep", e15Ep, 0.3)
chk("15 tauR/I", e15t * e15R / e15I, 1.2)
chk("15 bound", (e15hi + e15t) / (e15Ep + e15t), 1.333333, 1e-6)
def e15mm(p): return (p + e15lo) / 2
def e15H(p, t): return t * e15R / e15I * (e15mm(p) + t) - (p + t)
chk("15 lin coef", 1.2 / 2, 0.6)
chk("15 lin const", 1.2 * (0.1 / 2 + 0.3), 0.42)
e15ps = (0.42 - 0.3) / (1 - 0.6)
chk("15 p*", e15ps, 0.3)
chk("15 H(p*)=0", e15H(e15ps, e15t), 0)
e15Rl = e15I / (e15mm(e15ps) + e15t)
chk("15 m-(p*)", e15mm(e15ps), 0.2)
chk("15 Rl", e15Rl, 5)
chk("15 indiff L", (e15ps + e15t) * (e15R - e15Rl), 3)
chk("15 indiff R", e15ps * e15R, 3)
e15F = (e15ps - e15lo) / (e15hi - e15lo)
e15mp = (e15ps + e15hi) / 2
chk("15 F", e15F, 0.5)
chk("15 m+", e15mp, 0.4)
chk("15 Ep decomposition", e15F * e15mm(e15ps) + (1 - e15F) * e15mp, e15Ep)
e15V0 = e15Ep * e15R + e15F * (e15t * e15R - e15I)
e15V1 = (e15mm(e15ps) + e15t) * e15R - e15I
chk("15 V0", e15V0, 3.25)
chk("15 V1", e15V1, 2.5)
chk("15 dV", e15V0 - e15V1, 0.75)
chk("15 dV formula", (1 - e15F) * e15R * (e15mp - e15ps * (e15mm(e15ps) + e15t) / (e15ps + e15t)), 0.75)
chk("15 dV general", (1 - e15F) * (e15mp * e15R - e15V1), 0.75)
e15Hp = e15t * e15R / e15I * 0.5 - 1
e15Ht = e15R / e15I * (e15mm(e15ps) + e15t) + (e15ps - e15mm(e15ps)) / (e15mm(e15ps) + e15t)
chk("15 Hp", e15Hp, -0.4)
chk("15 Ht", e15Ht, 2.2)
chk("15 Ht direct", e15R / e15I * (e15mm(e15ps) + e15t) + e15t * e15R / e15I - 1, 2.2)
chk("15 dp/dt", -e15Ht / e15Hp, 5.5)
def e15pstar(t):   # uniform: H linear in p
    k = t * e15R / e15I
    return (k * (e15lo / 2 + t) - t) / (1 - k / 2)
chk("15 dp/dt numeric", (e15pstar(e15t + 1e-6) - e15pstar(e15t - 1e-6)) / 2e-6, 5.5, 1e-4)
chk("15 volume", e15F * e15I, 1.25)
chk("15 dvolume", e15I * (1 / (e15hi - e15lo)) * 5.5, 34.375)

# ======================================================================
# Deeper solutions (spec C, 2026-11-12): intermediate numbers added to the detailed .tex
chk("d1 gain on under", e1_Q * e1_u, 7000)
chk("d1 loss on over", e1_Q * e1_o, 5000)
chk("d1 shares under", e1_pi * e1_Q, 500)
chk("d1 shares over", e1_pip * e1_Q, 1000)
chk("d2 m parts", 0.5 * 0.8 + 0.5 * 0.7, 0.40 + 0.35)
chk("d2 pR", e2_p * e2_R, 40)
chk("d2 p/m", e2_p / e2_m, 1.066667, 1e-6)
chk("d2 p/m - 1", e2_p / e2_m - 1, 0.066667, 1e-6)
chk("d2 m2 parts", 0.2 * 0.8 + 0.8 * 0.5, 0.16 + 0.40)
chk("d3 PD high numerator", e3_N0 * 14.50 - e3_C, 1430)
chk("d3 PE low - v", e3_PE(12.50) - 12.50, 0.2703, 5e-5)
chk("d3 transfer to old", e3_N0 * (e3_PE(12.50) - 12.50), 27.03, 5e-3)
chk("d3 pooled debt price base", 0.5 * 12.50 + 0.5 * 14.50, 13.50)
chk("d4 fraction 1/7", e4_frac, 1 / 7)
chk("d4 threshold fraction", 100000 / 12000, 8.33, 5e-3)
chk("d4 per-share loss", 40 / e4_N0, 0.40)
chk("d6 10/17 - 1/5", 10 / 17 - 1 / 5, 33 / 85)
chk("d6 alpha* via 33/85", (33 / 85) / 0.6, 11 / 17)
chk("d6 m parts", 0.8 * 0.8 + 0.2 * 0.2, 0.64 + 0.04)
chk("d6 I/m", e6_I / e6_m, 73.53, 5e-3)
chk("d6 good repayment", e6_pH * e6_I / e6_m, 58.82, 5e-3)
chk("d6 bad repayment", e6_pL * e6_I / e6_m, 14.71, 5e-3)
chk("d7 sqrt .64", math.sqrt(0.64), 0.8)
chk("d7 sqrt .36", math.sqrt(0.36), 0.6)
chk("d7 1 - p0", 1 - e7_p0(0.36), 0.1111, 5e-5)
chk("d8 bound numerator", 0.64 * 10000, 6400)
chk("d8 bound", 6400 / 200, 32)
chk("d8 good part", 0.8 * (-10), -8)
chk("d9 mix parts", 0.3 * 0.8 + 0.7 * 0.4, 0.24 + 0.28)
chk("d9 5/0.8", 5 / 0.8, 6.25)
chk("d9 c0 parts", 0.4 * (10 - 6.25), 1.5)
chk("d9 c0", 1.5 + 1.8, 3.3)
chk("d9 coef", 1 - 3.3 - 0.5, -2.8)
chk("d9 disc", 5.6**2 + 4 * 4.6, 49.76)
chk("d9 xhat quadratic", (-5.6 + math.sqrt(49.76)) / 2, 0.727038, 1e-6)
chk("d9 xhat alt", -2.8 + math.sqrt(12.44), 0.727038, 1e-6)
chk("d9 borrow/pH", (5 + 0.727038) / 0.8, 7.158798, 1e-6)
chk("d9 RbG", 10 - 7.158798, 2.841202, 1e-6)
chk("d9 UG", 8 - 6 + 1 - 0.727038, 2.272962, 1e-6)
chk("d9 ybar", min(7.2 - 5, 8 - 6, 1), 1)
chk("d9 xbar", (2.3 - 0.5) / (2.3 + 0.5), 0.642857, 1e-6)
chk("d9 rbar", 1 / ((2.3 - 0.5) / (2.3 + 0.5)), 1.555556, 1e-6)
chk("d10 R - B/dp", 10 - 3, 7)
chk("d10 L", 1.6 - 1, 0.6)
chk("d10 Rb", 2.9 / 0.8, 3.625)
chk("d11 old a4", -5 + 5 / 10 * (2 + 4), -2)
chk("d11 old a12", -5 + 5 / 10 * (2 + 12), 2)
chk("d12 dM parts", 0.6 * 0.01 + 0.4 * (-0.04), 0.006 - 0.016)
chk("d12 I_SI", 1 / (1 - 0.6), 2.5)
chk("d13 m bound", 6 / 13.6, 0.441176, 1e-6)
chk("d13 alpha bound", (6 / 13.6 - 0.2) / 0.6, 0.402, 1e-3)
chk("d13 C'(as) = 2.88", 6 * e13as / (1 - e13as), 2.88)
chk("d13 1 - as", 1 - e13as, 0.675676, 1e-6)
chk("d13 C(as) explicit", 6 * (-0.324324 - math.log(0.675676)), 0.406307, 1e-5)
chk("d14 ln .5", math.log(0.5), -0.693147, 1e-6)
chk("d14 X increment", -0.82 * (0.5 + math.log(0.5)), 0.158381, 1e-6)
chk("d14 X - lambda", e14X(0.5) - e14lam, 10.008381, 1e-6)
chk("d14 (1-a)V", 0.5 * e14V(0.5), 4.765896, 1e-6)
chk("d15 p* solve", 0.12 / 0.4, 0.3)
chk("d15 cut lhs", 1.2 * ((0.3 + 0.1) / 2 + 0.3), 0.3 + 0.3)

# ======================================================================
# Original exercises 16-19 (Stiglitz-Weiss; collateral as a signal).

# --- Ex 16: Stiglitz-Weiss two types ----------------------------------
o16_pL, o16_RL, o16_pH, o16_RH, o16_I, o16_a = 0.8, 150, 0.4, 300, 100, 0.75
o16_Rb = o16_pL * o16_RL
chk("o16 Rbar", o16_Rb, 120)
chk("o16 Rbar H", o16_pH * o16_RH, 120)
chk("o16 var L", o16_pL * (1 - o16_pL) * o16_RL**2, 3600)
chk("o16 var H", o16_pH * (1 - o16_pH) * o16_RH**2, 21600)
chk("o16 MPS P(300)", o16_pL * 0.5, o16_pH)
chk("o16 MPS P(0)", 0.2 + o16_pL * 0.5, 1 - o16_pH)
chk("o16 MPS var add", 3600 + o16_pL * 150**2, 21600)
chk("o16 UL(.2)", o16_Rb - o16_pL * 1.2 * o16_I, 24)
chk("o16 UH(.2)", o16_Rb - o16_pH * 1.2 * o16_I, 72)
o16_rs = o16_Rb / (o16_pL * o16_I) - 1
o16_rm = o16_Rb / (o16_pH * o16_I) - 1
chk("o16 r*", o16_rs, 0.5)
chk("o16 rmax", o16_rm, 2.0)
o16_m = o16_a * o16_pL + (1 - o16_a) * o16_pH
chk("o16 m", o16_m, 0.7)
chk("o16 rho .2", o16_m * 1.2, 0.84)
chk("o16 rho r*", o16_m * (1 + o16_rs), 1.05)
chk("o16 rho .6", o16_pH * 1.6, 0.64)
chk("o16 rho 1", o16_pH * 2.0, 0.80)
chk("o16 rho rmax", o16_pH * (1 + o16_rm), 1.20)
chk("o16 rho rmax = Rbar/I", o16_pH * (1 + o16_rm), o16_Rb / o16_I)
chk("o16 rho just above r*", o16_pH * (1 + o16_rs), 0.60)
chk("o16 drop", (o16_m - o16_pH) * (1 + o16_rs), 0.45)
chk("o16 drop alt", o16_a * (o16_pL - o16_pH) * (1 + o16_rs), 0.45)
o16_rt = o16_m * (1 + o16_rs) / o16_pH - 1
chk("o16 1+rtilde", 1 + o16_rt, 2.625)
chk("o16 rtilde", o16_rt, 1.625)
o16_s = o16_m * (1 + o16_rs) * o16_I / o16_Rb
chk("o16 s", o16_s, 0.875)
chk("o16 equity payoff", (1 - o16_s) * o16_Rb, 15)

# --- Ex 17: Stiglitz-Weiss market ------------------------------------
o17_pL, o17_RL, o17_pH, o17_RH, o17_I, o17_a, o17_N = 0.9, 130, 0.5, 234, 100, 0.75, 1000
def o17_Ls(rho):
    """Deposit supply L^s(rho) = max(0, 1e6 (rho - 0.96))."""
    return max(0.0, 1e6 * (rho - 0.96))
o17_Rb = o17_pL * o17_RL
chk("o17 Rbar", o17_Rb, 117)
chk("o17 Rbar H", o17_pH * o17_RH, 117)
o17_rs = o17_Rb / (o17_pL * o17_I) - 1
o17_rm = o17_Rb / (o17_pH * o17_I) - 1
chk("o17 r*", o17_rs, 0.30)
chk("o17 rmax", o17_rm, 1.34)
o17_m = o17_a * o17_pL + (1 - o17_a) * o17_pH
chk("o17 m", o17_m, 0.80)
o17_rhos = o17_m * (1 + o17_rs)
chk("o17 rho*", o17_rhos, 1.04)
chk("o17 1+rtilde", o17_rhos / o17_pH, 2.08)
chk("o17 rtilde", o17_rhos / o17_pH - 1, 1.08)
chk("o17 D(r*)", o17_N * o17_I, 100000)
chk("o17 Ls(rho*)", o17_Ls(o17_rhos), 80000, 1e-6)
o17_rej = (o17_N * o17_I - o17_Ls(o17_rhos)) / o17_I
chk("o17 rejected", o17_rej, 200, 1e-6)
chk("o17 rejected safe", o17_a * o17_rej, 150, 1e-6)
chk("o17 rejected risky", (1 - o17_a) * o17_rej, 50, 1e-6)
chk("o17 UL(.4)", o17_Rb - o17_pL * 140, -9)
chk("o17 UH(.4)", o17_Rb - o17_pH * 140, 47)
chk("o17 rho(.4)", o17_pH * 1.4, 0.70)
chk("o17 Ls(.70)", o17_Ls(0.70), 0)
chk("o17 D(.4)", (1 - o17_a) * o17_N * o17_I, 25000)
o17_rhoW = 0.96 + 25000 / 1e6
chk("o17 rhoW", o17_rhoW, 0.985)
chk("o17 1+rW", o17_rhoW / o17_pH, 1.97)
o17_rW = o17_rhoW / o17_pH - 1
chk("o17 rW", o17_rW, 0.97)
assert o17_rs < o17_rW <= o17_rm and o17_rhoW < o17_rhos
o17_m2 = 0.9 * o17_pL + 0.1 * o17_pH
chk("o17 m(a=.9)", o17_m2, 0.86)
chk("o17 rho*(a=.9)", o17_m2 * (1 + o17_rs), 1.118)
chk("o17 Ls(a=.9)", o17_Ls(o17_m2 * (1 + o17_rs)), 158000, 1e-6)
chk("o17 clearing rho", 0.96 + 100000 / 1e6, 1.06)
chk("o17 1+r clear", 1.06 / o17_m2, 1.232558, 1e-6)
chk("o17 r clear", 1.06 / o17_m2 - 1, 0.232558, 1e-6)
assert 1.06 / o17_m2 - 1 < o17_rs
o17_pH3 = 0.4
chk("o17 RH3 mean", o17_pH3 * 292.5, 117)
chk("o17 rmax3", o17_Rb / (o17_pH3 * o17_I) - 1, 1.925)
o17_m3 = o17_a * o17_pL + (1 - o17_a) * o17_pH3
chk("o17 m3", o17_m3, 0.775)
o17_rho3 = o17_m3 * (1 + o17_rs)
chk("o17 rho*3", o17_rho3, 1.0075)
chk("o17 Ls3", o17_Ls(o17_rho3), 47500, 1e-6)
chk("o17 unmet3", 100000 - o17_Ls(o17_rho3), 52500, 1e-6)
chk("o17 share rejected3", (100000 - o17_Ls(o17_rho3)) / 100000, 0.525)
chk("o17 drop base", (o17_m - o17_pH) * (1 + o17_rs), 0.39)
chk("o17 drop3", (o17_m3 - o17_pH3) * (1 + o17_rs), 0.4875)
chk("o17 drop3 alt", o17_a * (o17_pL - o17_pH3) * (1 + o17_rs), 0.4875)
chk("o17 1+rW3", 0.985 / o17_pH3, 2.4625)
chk("o17 rW3", 0.985 / o17_pH3 - 1, 1.4625)
assert o17_rs < 0.985 / o17_pH3 - 1 <= o17_Rb / (o17_pH3 * o17_I) - 1 and 0.985 < o17_rho3
chk("o17 safe payoff at r*", o17_Rb - o17_pL * (1 + o17_rs) * o17_I, 0)

# --- Collateral model helpers -----------------------------------------
def col_sep(p, q, I, d):
    """Least-cost separating contract: returns (D, C_G, R_u^G)."""
    D = p * (1 - q) - d * q * (1 - p)
    return D, (p - q) * I / D, I * ((1 - q) - d * (1 - p)) / D

# --- Ex 18: collateral as a separating signal --------------------------
o18_p, o18_q, o18_I, o18_R, o18_a, o18_d = 0.9, 0.6, 60, 120, 0.5, 0.5
chk("o18 RuG sym", o18_I / o18_p, 66.667, 5e-4)
chk("o18 RuB sym", o18_I / o18_q, 100)
chk("o18 UG sym", o18_p * o18_R - o18_I, 48)
chk("o18 UB sym", o18_q * o18_R - o18_I, 12)
o18_Ru20 = (o18_I - (1 - o18_p) * o18_d * 20) / o18_p
chk("o18 Ru C=20", o18_Ru20, 65.556, 5e-4)
chk("o18 0.9Ru = 59", o18_p * o18_Ru20, 59)
chk("o18 U C=20", o18_p * (o18_R - o18_Ru20) - (1 - o18_p) * 20, 47)
chk("o18 U C=20 formula", 48 - (1 - o18_p) * (1 - o18_d) * 20, 47)
o18_m = o18_a * o18_p + (1 - o18_a) * o18_q
chk("o18 m", o18_m, 0.75)
chk("o18 pool Ru", o18_I / o18_m, 80)
chk("o18 pool UG", o18_p * (o18_R - 80), 36)
chk("o18 pool UB", o18_q * (o18_R - 80), 24)
chk("o18 mimic sym", o18_q * (o18_R - o18_I / o18_p), 32)
chk("o18 R - I/p", o18_R - o18_I / o18_p, 53.333, 5e-4)
chk("o18 lender loss", o18_m * o18_I / o18_p, 50)
o18_D, o18_C, o18_Ru = col_sep(o18_p, o18_q, o18_I, o18_d)
chk("o18 D", o18_D, 0.33)
chk("o18 D alt", (o18_p - o18_q) + o18_q * (1 - o18_p) * (1 - o18_d), 0.33)
chk("o18 CG", o18_C, 54.545, 5e-4)
chk("o18 CG slide form", o18_I / (1 + o18_q * (1 - o18_p) * (1 - o18_d) / (o18_p - o18_q)), o18_C)
chk("o18 RuG", o18_Ru, 63.636, 5e-4)
chk("o18 BE parts", o18_p * o18_Ru, 57.273, 5e-4)
chk("o18 BE parts 2", (1 - o18_p) * o18_d * o18_C, 2.727, 5e-4)
chk("o18 BE", o18_p * o18_Ru + (1 - o18_p) * o18_d * o18_C, o18_I)
chk("o18 NM part", o18_q * (o18_R - o18_Ru), 33.818, 5e-4)
chk("o18 NM part 2", (1 - o18_q) * o18_C, 21.818, 5e-4)
chk("o18 NM", o18_q * (o18_R - o18_Ru) - (1 - o18_q) * o18_C, 12)
o18_Us = o18_p * (o18_R - o18_Ru) - (1 - o18_p) * o18_C
chk("o18 R - RuG", o18_R - o18_Ru, 56.364, 5e-4)
chk("o18 0.9(R-RuG)", o18_p * (o18_R - o18_Ru), 50.727, 5e-4)
chk("o18 0.1 CG", (1 - o18_p) * o18_C, 5.455, 5e-4)
chk("o18 Usep", o18_Us, 45.273, 5e-4)
chk("o18 DW", (1 - o18_p) * (1 - o18_d) * o18_C, 2.727, 5e-4)
chk("o18 Usep formula", 48 - (1 - o18_p) * (1 - o18_d) * o18_C, o18_Us)
chk("o18 gain vs pool", o18_Us - 36, 9.273, 5e-4)
chk("o18 good takes bad", o18_p * (o18_R - o18_I / o18_q), 18)
chk("o18 MRS good", (1 - o18_p) / o18_p, 0.111, 5e-4)
chk("o18 MRS bad", (1 - o18_q) / o18_q, 0.667, 5e-4)
assert o18_C <= 60 and o18_Ru < o18_R

# --- Ex 19: separating vs pooling --------------------------------------
o19_p, o19_q, o19_I, o19_R, o19_d = 0.8, 0.7, 50, 100, 0.2
chk("o19 mimic sym", o19_q * (o19_R - o19_I / o19_p), 26.25)
o19_D, o19_C, o19_Ru = col_sep(o19_p, o19_q, o19_I, o19_d)
chk("o19 D", o19_D, 0.212)
chk("o19 CG", o19_C, 23.585, 5e-4)
chk("o19 RuG", o19_Ru, 61.321, 5e-4)
chk("o19 BE p1", o19_p * o19_Ru, 49.057, 5e-4)
chk("o19 BE p2", (1 - o19_p) * o19_d * o19_C, 0.943, 5e-4)
chk("o19 BE", o19_p * o19_Ru + (1 - o19_p) * o19_d * o19_C, o19_I)
chk("o19 NM p1", o19_q * (o19_R - o19_Ru), 27.075, 5e-4)
chk("o19 NM p2", (1 - o19_q) * o19_C, 7.075, 5e-4)
chk("o19 NM", o19_q * (o19_R - o19_Ru) - (1 - o19_q) * o19_C, 20)
o19_DW = (1 - o19_p) * (1 - o19_d) * o19_C
chk("o19 DW", o19_DW, 3.774, 5e-4)
o19_Us = o19_p * o19_R - o19_I - o19_DW
chk("o19 Usep", o19_Us, 26.226, 5e-4)
chk("o19 Usep direct", o19_p * (o19_R - o19_Ru) - (1 - o19_p) * o19_C, o19_Us)
def o19_Up(a):
    """Good type's pooling utility p(R - I/m)."""
    return o19_p * (o19_R - o19_I / (a * o19_p + (1 - a) * o19_q))
chk("o19 m .3", 0.3 * o19_p + 0.7 * o19_q, 0.73)
chk("o19 I/m .3", o19_I / 0.73, 68.493, 5e-4)
chk("o19 R-I/m .3", o19_R - o19_I / 0.73, 31.507, 5e-4)
chk("o19 Upool .3", o19_Up(0.3), 25.205, 5e-4)
chk("o19 m .6", 0.6 * o19_p + 0.4 * o19_q, 0.76)
chk("o19 I/m .6", o19_I / 0.76, 65.789, 5e-4)
chk("o19 R-I/m .6", o19_R - o19_I / 0.76, 34.211, 5e-4)
chk("o19 Upool .6", o19_Up(0.6), 27.368, 5e-4)
assert o19_Up(0.3) < o19_Us < o19_Up(0.6)
o19_x = (1 - o19_p) * (1 - o19_d)
chk("o19 px", o19_p * o19_x, 0.128)
o19_ah = (o19_p - o19_q) / ((o19_p - o19_q) + o19_p * o19_x)
chk("o19 alpha hat", o19_ah, 0.438596, 1e-6)
chk("o19 m(ah)", o19_ah * o19_p + (1 - o19_ah) * o19_q, 0.743860, 1e-6)
chk("o19 I/m(ah)", o19_I / (o19_ah * o19_p + (1 - o19_ah) * o19_q), 67.217, 5e-4)
chk("o19 Upool(ah)", o19_Up(o19_ah), o19_Us)
chk("o19 cond lhs .3", 0.3 * o19_p * o19_x, 0.0384)
chk("o19 cond rhs .3", 0.7 * (o19_p - o19_q), 0.07)
chk("o19 cond lhs .6", 0.6 * o19_p * o19_x, 0.0768)
chk("o19 cond rhs .6", 0.4 * (o19_p - o19_q), 0.04)
chk("o19 D^2", o19_D**2, 0.044944)
chk("o19 dC/dd", (o19_p - o19_q) * o19_I * o19_q * (1 - o19_p) / o19_D**2, 15.575, 5e-4)
chk("o19 dDW/dd", -(1 - o19_p) * (o19_p - o19_q)**2 * o19_I / o19_D**2, -2.225, 5e-4)
o19_h = 1e-7  # finite-difference check of both derivatives
chk("o19 dC/dd numeric", (col_sep(o19_p, o19_q, o19_I, o19_d + o19_h)[1] - o19_C) / o19_h, 15.575, 1e-3)
chk("o19 dDW/dd numeric", ((1 - o19_p) * (1 - o19_d - o19_h) * col_sep(o19_p, o19_q, o19_I, o19_d + o19_h)[1] - o19_DW) / o19_h, -2.225, 1e-3)
for dd, wD, wC, wR, wDW, wU in [(0, 0.24, 20.833, 62.5, 4.167, 25.833),
                                (0.2, 0.212, 23.585, 61.321, 3.774, 26.226),
                                (0.6, 0.156, 32.051, 57.692, 2.564, 27.436)]:
    D_, C_, R_ = col_sep(o19_p, o19_q, o19_I, dd)
    chk(f"o19 D d={dd}", D_, wD)
    chk(f"o19 D lin d={dd}", 0.24 - 0.14 * dd, wD)
    chk(f"o19 C d={dd}", C_, wC, 5e-4)
    chk(f"o19 Ru d={dd}", R_, wR, 5e-4)
    chk(f"o19 Ru num d={dd}", 50 * (0.3 - 0.2 * dd), {0: 15, 0.2: 13, 0.6: 9}[dd])
    chk(f"o19 DW d={dd}", 0.2 * (1 - dd) * C_, wDW, 5e-4)
    chk(f"o19 U d={dd}", 30 - 0.2 * (1 - dd) * C_, wU, 5e-4)
chk("o19 0.24-0.084", 0.24 - 0.084, 0.156)
D1, C1, R1 = col_sep(o19_p, o19_q, o19_I, 1 - 1e-9)
chk("o19 C d->1", C1, 50, 1e-6)
chk("o19 Ru d->1", R1, 50, 1e-6)
o19_dh = 1 - 0.4 * (o19_p - o19_q) / (0.6 * o19_p * (1 - o19_p))
chk("o19 0.04/0.096", 0.04 / 0.096, 0.416667, 1e-6)
chk("o19 delta hat", o19_dh, 0.583333, 1e-6)
chk("o19 Usep(dhat) = Upool(.6)", 30 - (1 - o19_p) * (1 - o19_dh) * col_sep(o19_p, o19_q, o19_I, o19_dh)[1], o19_Up(0.6))
assert 30 - 0.08 * col_sep(o19_p, o19_q, o19_I, 0.6)[1] > o19_Up(0.6)
chk("o19 Ipx", o19_I * o19_p * o19_x, 6.4)
chk("o19 dC/dq", -o19_I * o19_p * o19_x / o19_D**2, -142.40, 5e-3)
chk("o19 dC/dq numeric", (col_sep(o19_p, o19_q + o19_h, o19_I, o19_d)[1] - o19_C) / o19_h, -142.40, 1e-2)
for qq, wD, wC, wDW in [(0.6, 0.296, 33.784, 5.405), (0.75, 0.17, 14.706, 2.353)]:
    D_, C_, _ = col_sep(o19_p, qq, o19_I, o19_d)
    chk(f"o19 D q={qq}", D_, wD)
    chk(f"o19 D alt q={qq}", (o19_p - qq) + qq * o19_x, wD)
    chk(f"o19 C q={qq}", C_, wC, 5e-4)
    chk(f"o19 DW q={qq}", o19_x * C_, wDW, 5e-4)
chk("o19 qR-I q=.6", 0.6 * o19_R - o19_I, 10)
o19_UBp = o19_q * (o19_R - o19_I / 0.73)
chk("o19 UB pool .3", o19_UBp, 22.055, 5e-4)
chk("o19 surplus pool", 0.3 * (o19_p * o19_R - o19_I) + 0.7 * (o19_q * o19_R - o19_I), 23)
chk("o19 surplus pool check", 0.3 * o19_Up(0.3) + 0.7 * o19_UBp, 23)
chk("o19 0.3 Upool", 0.3 * o19_Up(0.3), 7.562, 5e-4)
chk("o19 0.7 UBpool", 0.7 * o19_UBp, 15.438, 5e-4)
chk("o19 loss", 0.3 * o19_DW, 1.132, 5e-4)
chk("o19 surplus sep", 23 - 0.3 * o19_DW, 21.868, 5e-4)
chk("o19 surplus sep check", 0.3 * o19_Us + 0.7 * 20, 23 - 0.3 * o19_DW)
chk("o19 0.3 Usep", 0.3 * o19_Us, 7.868, 5e-4)
chk("o19 good gain", o19_Us - o19_Up(0.3), 1.021, 5e-4)

print(f"PASS {N} checks")
