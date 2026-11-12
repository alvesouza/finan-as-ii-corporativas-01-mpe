"""Numerical check of lista-r4-moral-hazard-financing-capacity-solutions.tex.

Covers the exercises written for this list: 1, 3, 7, 8, 12, 13, 14, 15. The other seven
positions (2, 4, 5, 6, 9, 10, 11) are pasted from lista-topic4-moral-hazard-overhang-solutions.tex
and are checked in lista-topic4-moral-hazard-overhang-solutions_check.py.

Every number printed in the PDF is recomputed from the exercise data (or from the stated
illustration parameters) and compared with the value as displayed. Tolerance: half a unit
in the last displayed decimal (``dec``), so a display that rounds wrongly fails. Symbolic
results are checked numerically at parameter points that satisfy each exercise's assumptions.

Run: python -I Listas/lista-r4-moral-hazard-financing-capacity-solutions_check.py
     -> prints "PASS <n> checks".
"""
import math

n = 0


def chk(got, printed, dec):
    """Assert that `got` rounds to `printed` when shown with `dec` decimals."""
    global n
    assert abs(got - printed) <= 0.5 * 10 ** (-dec) + 1e-9, (got, printed, dec)
    n += 1


def ok(cond):
    """Assert a qualitative (sign / ordering) result."""
    global n
    assert cond
    n += 1


# --- Shared illustration parameters (Tirole binary-effort model) ---------------------------
pH, pL, Rv, Bv = 0.8, 0.4, 1.5, 0.3          # variable-investment illustration (Ex 7, 8, 13)
dp = pH - pL
rho1 = pH * Rv
rho0 = pH * (Rv - Bv / dp)

# 1. Ross Q7 -- incentive stake in the Tirole illustration (I=100, R=150, B=30)
chk(30 / dp, 75, 0)
chk(75 / 150, 0.5, 2)

# 3. Berk 16.24 -- two-state illustration, risk neutral, r = 0
e_fib = 0.5 * 110 + 0.5 * 0
chk(e_fib, 55, 0)
chk(e_fib - 50, 5, 0)
V_up, V_dn = 100 + 110, 100 + 0
chk(V_up, 210, 0); chk(V_dn, 100, 0)
chk(0.5 * V_up + 0.5 * V_dn, 155, 0)
F = 120
chk(150 - F, 30, 0)
D1 = 0.5 * min(V_up, F) + 0.5 * min(V_dn, F)
E1 = 0.5 * max(V_up - F, 0) + 0.5 * max(V_dn - F, 0)
chk(D1, 110, 0); chk(E1, 45, 0)
chk(E1 - 30, 15, 0); chk(D1 - 120, -10, 0)
chk(E1 - 30, (e_fib - 50) - (D1 - 120), 0)
# negative-NPV variant: fibre pays 90 or 0
e_b = 0.5 * 90
chk(e_b, 45, 0); chk(e_b - 50, -5, 0)
chk(0.5 * 190 + 0.5 * 100, 145, 0)
D2 = 0.5 * min(190, F) + 0.5 * min(100, F)
E2 = 0.5 * max(190 - F, 0) + 0.5 * max(100 - F, 0)
chk(D2, 110, 0); chk(E2, 35, 0); chk(E2 - 30, 5, 0)
# riskless debt F = 80: no transfer
F3 = 80
chk(0.5 * min(V_up, F3) + 0.5 * min(V_dn, F3) - F3, 0, 0)
chk(0.5 * (V_up - F3) + 0.5 * (V_dn - F3) - (150 - F3), 5, 0)

# 7. Tirole 3.8
chk(rho1, 1.2, 1); chk(Bv / dp, 0.75, 2); chk(rho0, 0.6, 1)
chk(pL * Rv + Bv, 0.9, 1); ok(pL * Rv + Bv < 1 < rho1)
k = 1 / (1 - rho0)
chk(k, 2.5, 1); chk(k * 10, 25, 0); chk((rho1 - 1) * 25, 5, 0)
b = lambda c: Bv / (1 + 20 * c)


def kc(c):
    """Equity multiplier with monitoring, book's (and our) formula."""
    return 1 / (1 - rho0 + c + pH / dp * (b(c) - Bv))


f = lambda c: (rho1 - 1 - c) * kc(c)
# the two forms of the denominator coincide
for c in (0.0, 0.03, 0.075, 0.15):
    chk(1 + c - pH * (Rv - b(c) / dp), 1 - rho0 + c + pH / dp * (b(c) - Bv), 12)
cs = 0.075
u = 1 + 20 * cs
chk(u, 2.5, 1)
chk(24 * u, 60, 0)
chk(b(cs), 0.12, 2)
Dn = 1 - rho0 + cs + pH / dp * (b(cs) - Bv)
chk(Dn, 0.115, 3)
chk(rho1 - 1 - cs, 0.125, 3)
chk(kc(cs), 8.6957, 4)
chk(f(cs), 1.0870, 4)
chk(f(0), 0.5, 1)
# FOC holds at c* and c* is the global max on a fine grid where D > 0
bp = -20 * Bv / u ** 2
chk(bp, -0.96, 2)
chk(-Dn - (rho1 - 1 - cs) * (1 + pH / dp * bp), 0, 12)
grid = [i / 100000 for i in range(0, 20000)]
ok(max(grid, key=f) == cs)
I7 = kc(cs) * 10
chk(I7, 86.96, 2); chk(f(cs) * 10, 10.87, 2)
Rb7, Rm7 = b(cs) / dp, cs / dp
chk(Rb7, 0.3, 1); chk(Rm7, 0.1875, 4)
chk(pH / dp - 1, pL / dp, 12)
Im7 = (pH / dp - 1) * cs * I7
chk(Im7, 6.52, 2)
chk(I7 - 10 - Im7, 70.43, 2)
chk(pH * (Rv - Rb7 - Rm7) * I7, 70.43, 2)
chk(pH * (Rv - Rb7 - Rm7) * I7, I7 - 10 - Im7, 9)

# 8. Tirole 3.13 (i): I=100, R=150, pH=.8, pL=.4, B=30
I8, R8, B8 = 100, 150, 30
V8 = pH * R8 - I8
P8 = pH * (R8 - B8 / dp)
Abar = I8 - P8
Ahat = pH * B8 / dp
chk(V8, 20, 0); chk(B8 / dp, 75, 0); chk(P8, 60, 0); chk(Abar, 40, 0); chk(Ahat, 60, 0)
chk(pL * R8 + B8 - I8, -10, 0)
chk(Ahat - Abar, V8, 9)


def lender(A):
    """Monopoly lender's contract in the fixed model: (R_b, U_b, U_l)."""
    if A >= I8:
        return None, V8, 0.0
    Rb = max(B8 / dp, A / pH)
    Ul = pH * (R8 - Rb) - (I8 - A)
    if Ul < 0:
        return None, 0.0, 0.0
    return Rb, pH * Rb - A, Ul


Rb, Ub, Ul = lender(50)
chk(50 / pH, 62.5, 1); chk(Rb, 75, 0); chk(Ub, 10, 0); chk(Ul, 10, 0); chk(Ub + Ul, V8, 9)
Rb, Ub, Ul = lender(70)
chk(Rb, 87.5, 1); chk(Ub, 0, 0); chk(pH * (R8 - Rb), 50, 0); chk(Ul, 20, 0)
ok(lender(39.9)[1] == 0 and lender(40)[1] == 20 and lender(100)[1] == 20)
chk(lender(55)[1], Ahat - 55, 9)
# (ii)
mu = 1 - (rho1 - 1) * dp / (pH * Bv)
lam = (rho1 - 1) / Bv
ok(lam > 0 and mu > 0)
chk(pH * Bv / dp, 0.6, 1)
Imon = 10 / (pH * Bv / dp)
chk(Imon, 16.667, 3); chk((rho1 - 1) * Imon, 3.3333, 4)
ok(Imon < 10 / (1 - rho0))
# Lagrange multipliers: lambda = mu = 0.6667 in the illustration
chk(lam, 0.6667, 4); chk(mu, 0.6667, 4)

# 12. Tirole 3.5: R(I) = 4 sqrt(I), pH = .5, B/dp = 3
p12, bd = 0.5, 3.0
Rf = lambda I: 4 * math.sqrt(I)
Rp = lambda I: 2 / math.sqrt(I)
Istar = 1.0
chk(p12 * Rp(Istar), 1, 9)
Pl = lambda I: p12 * (Rf(I) - bd * I)
chk(Pl(Istar), 0.5, 1)
Astar = Istar - Pl(Istar)
chk(Astar, 0.5, 1)


def I12(A):
    """Constrained investment: larger root of 2.5 I - 2 sqrt(I) = A."""
    if A >= Astar:
        return Istar
    s = (2 + math.sqrt(4 + 10 * A)) / 5
    return s * s


def v12(A):
    """Gross shadow value of assets."""
    if A >= Astar:
        return 1.0
    return p12 * bd / (1 - p12 * Rp(I12(A)) + p12 * bd)


for A, Iv, Dv, vv, Ipv in ((0.0, 0.64, 1.25, 1.2, 0.8),
                           (0.2, 0.791918, 1.376276, 1.089898, 0.726599),
                           (0.5, 1.0, 1.5, 1.0, 0.666667)):
    I_ = I12(A)
    chk(I_, Iv, 6)
    chk(Pl(I_), I_ - A, 9)                       # breakeven binds
    D_ = 1 - p12 * Rp(I_) + p12 * bd
    chk(D_, Dv, 6); chk(v12(A), vv, 6); chk(1 / D_, Ipv, 6)
chk(math.sqrt(I12(0.2)), 0.889898, 6); chk(p12 * Rp(I12(0.2)), 1.123724, 6)
chk(p12 * bd, 1.5, 1)
# v(A) equals 1 + d(net utility)/dA by finite differences, and decreases
h = 1e-6
for A in (0.05, 0.2, 0.4):
    U = lambda a: a + p12 * Rf(I12(a)) - I12(a)
    chk((U(A + h) - U(A - h)) / (2 * h), v12(A), 5)
    # book's net derivative 1/[(pH B/dp)/(pH R' - 1) - 1] = v - 1
    chk(1 / ((p12 * bd) / (p12 * Rp(I12(A)) - 1) - 1), v12(A) - 1, 9)
ok(v12(0.0) > v12(0.2) > v12(0.45) > v12(0.5) == 1.0)

# 13. Tirole 4.10
A13 = 10
ratio = pH / (pH + pL)
chk(ratio, 2 / 3, 9)
rho0p = pH * (Rv - ratio * Bv / dp)
chk(rho0p, 0.8, 1); chk(ratio * Bv / dp, 0.5, 1)
chk(rho0p - rho0, pH * (Bv / dp) * pL / (pH + pL), 12)
I_pf = A13 / (1 - rho0); I_cp = A13 / (1 - rho0p)
chk(I_pf, 25, 0); chk((rho1 - 1) * I_pf, 5, 0)
chk(I_cp, 50, 0); chk((rho1 - 1) * I_cp, 10, 0)
R2 = Bv * I_cp / ((pH + pL) * dp)
chk(R2, 31.25, 2)
m = pH ** 2 * R2
chk(m, 20, 0)
chk(pH * Rv * I_cp, 60, 0); chk(pH * Rv * I_cp - m, I_cp - A13, 9)
chk(pH * dp * R2, 10, 0); chk(Bv * I_cp / 2, 7.5, 1)
chk((pH ** 2 - pL ** 2) * R2, 15, 0); chk(Bv * I_cp, 15, 0)
Rbi = Bv * 12.5 / dp
chk(Rbi, 9.375, 3); chk(pH * (Rv * 12.5 - Rbi), 7.5, 1); chk(12.5 - 5, 7.5, 1)
# likelihood ratios: LR2 > LR1 > 0 > LR0 at the illustration point and a few others
for a, bb in ((0.8, 0.4), (0.6, 0.5), (0.95, 0.1)):
    LR2 = 1 - (bb / a) ** 2
    LR1 = 1 - bb * (1 - bb) / (a * (1 - a))
    LR0 = 1 - ((1 - bb) / (1 - a)) ** 2
    ok(LR2 > LR1 and LR0 < 0)
chk(1 - (pL / pH) ** 2, 0.75, 2)
chk(1 - pL * (1 - pL) / (pH * (1 - pH)), -0.5, 1)

# 14. Tirole 3.20
R14, I14 = 0.9, 0.3
ok(math.sqrt(2 * I14) < R14 < 1)
chk(math.sqrt(2 * I14), 0.774597, 6)
chk(R14 ** 2 / 2 - I14, 0.105, 3)
A1 = I14 - R14 ** 2 / 4
chk(R14 ** 2 / 4, 0.2025, 4); chk(A1, 0.0975, 4)
chk(3 * R14 ** 2 / 8, 0.30375, 5); chk(3 * R14 ** 2 / 8 - I14, 0.00375, 5)


def rb(R, x):
    """Largest root of r (R - r) = x."""
    return (R + math.sqrt(R * R - 4 * x)) / 2


def Vf(R, I, A):
    """NPV with continuous effort, investment I, cash A (financed region)."""
    if A >= I:
        return R * R / 2 - I
    r = rb(R, I - A)
    return r * R - r * r / 2 - I


r = rb(R14, I14 - 0.2)
chk(math.sqrt(R14 ** 2 - 0.4), 0.640312, 6)
chk(r, 0.7701562, 7)
V02 = Vf(R14, I14, 0.2)
chk(R14 * r, 0.6931406, 7); chk(r * r / 2, 0.2965703, 7); chk(V02, 0.0965703, 7)
Vp = (R14 - r) / (2 * r - R14)
chk(R14 - r, 0.129844, 6); chk(Vp, 0.202782, 6)
Vpp = -R14 / (2 * r - R14) ** 3
chk(Vpp, -3.4282, 4)
chk((Vf(R14, I14, 0.2 + h) - Vf(R14, I14, 0.2 - h)) / (2 * h), Vp, 5)
chk((Vf(R14, I14, 0.2 + 1e-4) - 2 * V02 + Vf(R14, I14, 0.2 - 1e-4)) / 1e-8, Vpp, 2)
chk((Vf(R14, I14, I14) - Vf(R14, I14, I14 - 1e-7)) / 1e-7, 0, 3)   # V'(I) = 0
# utility identity U_b = R_b^2/2 - A equals the NPV
chk(r * r / 2 - 0.2, V02, 9)
# A2 formula when 3R^2/8 < I (check at I = 0.35 > 0.30375)
Ib = 0.35
s = math.sqrt(R14 ** 2 - 2 * Ib)
A2 = R14 ** 2 - Ib - R14 * s
chk(Vf(R14, Ib, A2), 0, 9)
ok(A2 > Ib - R14 ** 2 / 4)
# (iii) pooling: R = 0.9, A = 0.08, I_L = 0.25, I_H in {0.285, 0.30}
A14, IL = 0.08, 0.25
for IH in (0.285, 0.30):
    ok(IL - A14 < R14 ** 2 / 4 < IH - A14 and 3 * R14 ** 2 / 8 > IH
       and R14 ** 2 / 2 > IL + IH - 2 * A14 and math.sqrt(2 * IH) < R14)
chk(IL - A14, 0.17, 2)
chk(math.sqrt(R14 ** 2 - 4 * 0.17), 0.360555, 6)
chk(rb(R14, 0.17), 0.6302776, 7); chk(R14 * rb(R14, 0.17), 0.5672498, 7); chk(rb(R14, 0.17) ** 2 / 2, 0.1986249, 7)
no_pool = Vf(R14, IL, A14)
chk(no_pool, 0.1186249, 7); chk(no_pool / 2, 0.059312, 6)
chk(IL - 2 * A14, 0.09, 2)
chk(rb(R14, 0.09), 0.7854102, 7)
chk(R14 * rb(R14, 0.09), 0.706869, 6); chk(rb(R14, 0.09) ** 2 / 2, 0.3084346, 7); chk(R14 * rb(R14, 0.09), 0.7068692, 7)
only = Vf(R14, IL, min(2 * A14, IL))
chk(only, 0.1484346, 7); chk(only / 2, 0.074217, 6)
ok(only / 2 > no_pool / 2)
res = {}
for IH, Ib_, x, rv, a, bq, vv in ((0.285, 0.2675, 0.1875, 0.5724745, 0.5152270, 0.1638635, 0.0838635),
                                  (0.30, 0.275, 0.195, 0.5366025, 0.4829423, 0.1439711, 0.0639711)):
    chk((IL + IH) / 2, Ib_, 4); chk(Ib_ - A14, x, 4)
    rr = rb(R14, x)
    chk(rr, rv, 7); chk(R14 * rr, a, 7); chk(rr * rr / 2, bq, 7)
    both = Vf(R14, Ib_, A14)
    chk(both, vv, 7)
    # equal stakes: each project's own breakeven with A_L, A_H
    AL, AH = A14 - (IH - IL) / 2, A14 + (IH - IL) / 2
    chk(rr * (R14 - rr), IL - AL, 9); chk(rr * (R14 - rr), IH - AH, 9)
    # book's expression (lucky firm's NPV) exceeds the per-entrepreneur value by (IH-IL)/2
    chk(Vf(R14, IL, AL) - both, (IH - IL) / 2, 9)
    res[IH] = both
chk((0.285 - IL) / 2, 0.0175, 4); chk((0.30 - IL) / 2, 0.025, 3)
ok(res[0.285] > only / 2 and res[0.30] < only / 2)
# FOC of the pooled program gives equal stakes: R_b = R(1+lam)/(1+2lam) solves both FOCs
for lam_ in (0.1, 1.0, 5.0):
    rr = R14 * (1 + lam_) / (1 + 2 * lam_)
    chk(R14 - rr + lam_ * (R14 - 2 * rr), 0, 12)

# 15. Tirole 3.21
# (i) fixed model, epsilon uniform on [-20, 20]; Abar = 40, V = 20
Fu = lambda x: min(max((x + 20) / 40, 0), 1)       # P(eps < x)
for A0, hedge, prob, gamble in ((50, 70, 0.75, 65), (30, 30, 0.25, 35)):
    h_ = A0 + (V8 if A0 >= Abar else 0)
    pr = 1 - Fu(Abar - A0)
    chk(h_, hedge, 0); chk(pr, prob, 2); chk(A0 + V8 * pr, gamble, 0)
ok(65 < 70 and 35 > 30)
chk(30 - 20, 10, 0)
# (ii) continuous effort: R = 0.9, I = 0.3, A0 = 0.2, eps = +-0.05
ok(I14 - 0.2 < R14 ** 2 / 4 and I14 - 0.15 < R14 ** 2 / 4)
chk(rb(R14, 0.15), 0.6791288, 7); chk(rb(R14, 0.05), 0.8405125, 7)
chk(math.sqrt(0.81 - 0.6), 0.458258, 6); chk(math.sqrt(0.81 - 0.2), 0.781025, 6)
V015, V025 = Vf(R14, I14, 0.15), Vf(R14, I14, 0.25)
chk(R14 * rb(R14, 0.15), 0.6112159, 7); chk(rb(R14, 0.15) ** 2 / 2, 0.2306080, 7)
chk(R14 * rb(R14, 0.05), 0.7564612, 7); chk(rb(R14, 0.05) ** 2 / 2, 0.3532306, 7)
chk(V015, 0.0806080, 7); chk(V025, 0.1032306, 7)
chk((V015 + V025) / 2, 0.0919193, 7)
ok((V015 + V025) / 2 < V02)
# book's dV/dA = R/(2Rb-R) differs from the correct (R-Rb)/(2Rb-R)
chk(R14 / (2 * r - R14), 1.405564, 6)
# (iii) B(I) = 0.3 I + 0.1 g(I); phi(I) = 0.4 I + 0.2 g(I)
chk(rho1, 1.2, 1); chk(pH / dp, 2, 0)
chk(1 - rho1 + pH / dp * 0.3, 0.4, 1); chk(pH / dp * 0.1, 0.2, 1)
Ilin = lambda A: A / 0.4
Icvx = lambda A: (-0.4 + math.sqrt(0.16 + 0.8 * A)) / 0.4
Iccv = lambda A: ((-0.2 + math.sqrt(0.04 + 1.6 * A)) / 0.8) ** 2
B3 = {'lin': lambda I: 0.3 * I, 'cvx': lambda I: 0.3 * I + 0.1 * I * I,
      'ccv': lambda I: 0.3 * I + 0.1 * math.sqrt(I)}
for key, If in (('lin', Ilin), ('cvx', Icvx), ('ccv', Iccv)):
    for A in (5, 10, 15):
        I_ = If(A)
        chk(pH * (Rv * I_ - B3[key](I_) / dp), I_ - A, 9)      # breakeven binds
vals = {}
for key, If, nums in (('lin', Ilin, (12.5, 25.0, 37.5, 25.0)),
                      ('cvx', Icvx, (4.0990, 6.1414, 7.7178, 5.9084)),
                      ('ccv', Iccv, (10.8528, 22.6219, 34.5606, 22.7067))):
    lo, mid, hi = If(5), If(10), If(15)
    chk(lo, nums[0], 4); chk(mid, nums[1], 4); chk(hi, nums[2], 4)
    chk((lo + hi) / 2, nums[3], 4)
    vals[key] = ((lo + hi) / 2, mid)
ok(abs(vals['lin'][0] - vals['lin'][1]) < 1e-12)
ok(vals['cvx'][0] < vals['cvx'][1])
ok(vals['ccv'][0] > vals['ccv'][1])
chk((rho1 - 1) * (vals['cvx'][1] - vals['cvx'][0]), 0.0466, 4)
chk((rho1 - 1) * (vals['ccv'][0] - vals['ccv'][1]), 0.0170, 4)
# (iv) R(I) = 2 sqrt(I), A0 = 1, eps = +-0.5
chk(2 * math.sqrt(1), 2, 0)
chk(2 * math.sqrt(0.5), 1.414214, 6); chk(2 * math.sqrt(1.5), 2.449490, 6)
chk((2 * math.sqrt(0.5) + 2 * math.sqrt(1.5)) / 2, 1.931852, 6)
# (v) random financing at date 0 vs gambling, A0 = 30
x = 30 / Abar
chk(x, 0.75, 2); chk(30 + x * V8, 45, 0)
chk((1 - Fu(Abar - 30)) * Abar, 10, 0)
chk(30 + (1 - Fu(Abar - 30)) * V8, 35, 0)

print(f"PASS {n} checks")
