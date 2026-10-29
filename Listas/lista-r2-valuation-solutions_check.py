"""Check every number printed in lista-r2-valuation-solutions.tex.

Run: python -I Listas/lista-r2-valuation-solutions_check.py
Prints "PASS <n> checks" or stops at the first failing assert.
Tolerance: |computed - printed| <= half a unit in the last printed digit
(passed explicitly to each check as `tol`).
"""

n = 0


def check(value, printed, tol):
    """Assert that `value` rounds to the number printed in the solutions.

    value   -- number computed here from the statement's data.
    printed -- number as displayed in the .tex.
    tol     -- half a unit of the last printed digit.
    """
    global n
    assert abs(value - printed) <= tol, (value, printed, tol)
    n += 1


def npv(r, cfs):
    """NPV of cash flows cfs[0..T] (cfs[0] at t = 0) at rate r."""
    return sum(c / (1 + r) ** t for t, c in enumerate(cfs))


def root(f, lo, hi):
    """Bisection root of f on [lo, hi]; f(lo) and f(hi) must differ in sign."""
    assert f(lo) * f(hi) < 0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def annuity(r, T):
    """Present value of 1 per period for T periods at rate r."""
    return (1 - (1 + r) ** -T) / r


# 1. Berk 8.2
check(80000 / 1.09, 73394.50, 0.005)
check(30000 / 1.09**2, 25250.40, 0.005)
check(npv(0.09, [-100000, 80000, 30000]), -1355.10, 0.005)

# 2. Berk 12.24
rf, rm = 0.04, 0.10
rI, rB = rf + 1.6 * (rm - rf), rf + 1.0 * (rm - rf)
check(rI, 0.136, 5e-5)
check(rB, 0.100, 5e-5)
bP = 0.6 * 1.6 + 0.4 * 1.0
check(bP, 1.36, 5e-5)
check(rf + bP * (rm - rf), 0.1216, 5e-5)
check(0.6 * rI + 0.4 * rB, 0.1216, 5e-5)

# 3. Berk 9.18
check(-(115000 + 30000 + 5000), -150000, 0.5)

# 4. Berk 13.4
D, E, A = 400, 600, 1000
debt_pay = D * 1.05
check(debt_pay, 420, 1e-9)
eq_hi, eq_lo = 1200 - debt_pay, 960 - debt_pay
check(eq_hi, 780, 1e-9)
check(eq_lo, 540, 1e-9)
check((eq_hi + eq_lo) / 2, 660, 1e-9)
rE4 = (eq_hi + eq_lo) / 2 / E - 1
check(rE4, 0.10, 1e-9)
check((1200 + 960) / 2, 1080, 1e-9)
rA4 = (1200 + 960) / 2 / A - 1
check(rA4, 0.08, 1e-9)
check(0.4 * 0.05 + 0.6 * rE4, 0.08, 1e-9)

# 5. Higgins 8.7
kE5 = 0.06 + 0.75 * 0.063
check(kE5, 0.10725, 5e-7)
E5, D5 = 30.0, 10.0
check(E5 + D5, 40, 1e-9)
check((1 - 0.4) * 0.0768, 0.04608, 5e-7)
kw5 = ((1 - 0.4) * 0.0768 * D5 + kE5 * E5) / (D5 + E5)
check(kw5, 0.0919575, 5e-9)
check(0.04608 * 10, 0.4608, 5e-6)
check(0.10725 * 30, 3.2175, 5e-6)
check(0.4608 + 3.2175, 3.6783, 5e-6)

# 6. Grinblatt 11.10-11.13 (seven decimals displayed)
t7 = 5e-8
bL, bN = 0.90 / 1.90, 0.85 / 1.70
check(bL, 0.4736842, t7)
check(bN, 0.5000000, t7)
check(bL + bN, 0.9736842, t7)
bA6 = (bL + bN) / 2
check(bA6, 0.4868421, t7)
rA6 = 0.08 + bA6 * (0.14 - 0.08)
check(bA6 * 0.06, 0.0292105, t7)
check(rA6, 0.1092105, t7)
check(rA6 - 0.05, 0.0592105, t7)
V6 = 300 / (rA6 - 0.05)
check(V6, 5066.67, 0.005)
check(300 / 0.0592105, 5066.67, 0.005)  # displayed arithmetic
bE_H = bA6 * 2
check(bE_H, 0.9736842, t7)
check(bE_H * 0.06, 0.0584211, t7)
rE_H = 0.08 + bE_H * 0.06
check(rE_H, 0.1384211, t7)
check(0.5 * rE_H, 0.0692105, t7)
check(0.5 * 0.08 + 0.5 * rE_H, 0.1092105, t7)
bGM = 1.20 / 1.40
check(bGM, 0.8571429, t7)
check(bGM * 0.06, 0.0514286, t7)
check(0.08 + bGM * 0.06, 0.1314286, t7)
check(0.08 + bGM * 0.06 - 0.05, 0.0814286, t7)
V_GM = 300 / (0.08 + bGM * 0.06 - 0.05)
check(V_GM, 3684.21, 0.005)
check(300 / 0.0814286, 3684.21, 0.005)
check((V6 - V_GM) / 1000, 1.4, 0.05)  # "about $1.4 billion"

# 7. Berk 8.26
A7 = [-100, 25, 30, 40, 50]
B7 = [-100, 50, 40, 30, 20]
check(npv(0.11, A7), 9.055, 5e-4)
check(npv(0.11, B7), 12.620, 5e-4)
irrA = root(lambda r: npv(r, A7), 0.0, 0.5)
irrB = root(lambda r: npv(r, B7), 0.0, 0.5)
check(irrA, 0.1470, 5e-5)
check(irrB, 0.1780, 5e-5)
diff7 = [a - b for a, b in zip(A7, B7)]
assert diff7 == [0, -25, -10, 10, 30]
cross = root(lambda r: npv(r, diff7), 1e-4, 0.5)
check(cross, 0.0557, 5e-5)
check(npv(cross, A7), 24.86, 5e-3)
check(npv(cross, B7), 24.86, 5e-3)

# 8. Berk 8.17 (millions)
def npv8(r):
    return -5 + annuity(r, 10) - 0.1 / r


check(annuity(0.06, 10), 7.36009, 5e-6)
check(0.1 / 0.06, 1.66667, 5e-6)
check(npv8(0.06), 0.69342, 5e-6)
check(annuity(0.02, 10), 8.98259, 5e-6)
check(0.1 / 0.02, 5.0, 5e-6)
check(npv8(0.02), -1.01741, 5e-6)
check(annuity(0.11, 10), 5.88923, 5e-6)
check(0.1 / 0.11, 0.90909, 5e-6)
check(npv8(0.11), -0.01986, 5e-6)
irr8a = root(npv8, 0.02, 0.06)
irr8b = root(npv8, 0.06, 0.11)
check(irr8a, 0.0275, 5e-5)
check(irr8b, 0.1088, 5e-5)

# 9. Berk 13.20
rE9 = 0.03 + 0.26 * 0.06
check(rE9, 0.0456, 5e-7)
w9 = 0.89 * rE9 + 0.11 * 0.048 * (1 - 0.35)
check(0.89 * rE9, 0.040584, 5e-7)
check(0.11 * 0.048 * 0.65, 0.003432, 5e-7)
check(w9, 0.044016, 5e-7)
rU9 = 0.89 * rE9 + 0.11 * 0.048
check(rU9, 0.045864, 5e-7)
check(0.11 * 0.35 * 0.048, 0.001848, 5e-7)
check(rU9 - 0.11 * 0.35 * 0.048, 0.044016, 5e-7)
check((0.048 - 0.03) / 0.06, 0.30, 5e-7)
w_cs = 0.96 * (0.03 + 0.61 * 0.06) + 0.04 * 0.048 * 0.65
check(0.03 + 0.61 * 0.06, 0.0666, 5e-7)
check(w_cs, 0.065184, 5e-7)

# 10. Higgins 8.16 (millions)
kw10 = 0.5 * 0.08 * (1 - 0.25) + 0.5 * 0.14
check(0.5 * 0.08 * 0.75, 0.03, 1e-12)
check(kw10, 0.10, 1e-12)
check(1 / 10, 0.10, 1e-12)
int_at = 5 * 0.08 * (1 - 0.25)
check(int_at, 0.3, 1e-12)
check(1 - int_at, 0.7, 1e-12)
check((1 - int_at) / 5, 0.14, 1e-12)

# 11. Berk 9.25 (thousands)
tau11 = 2625 / 7500
check(tau11, 0.35, 1e-12)
ebit11 = 30000 - 18000 - 1000 - 2500
check(ebit11, 8500, 1e-9)
check(ebit11 * tau11, 2975, 1e-9)
uni11 = ebit11 * (1 - tau11)
check(uni11, 5525, 1e-9)
fcf11 = uni11 + 2500
check(fcf11, 8025, 1e-9)
check(fcf11 + 10000, 18025, 1e-9)
check(-25000 - 10000, -35000, 1e-9)
cfs11 = [-35000] + [fcf11] * 9 + [fcf11 + 10000]
check(annuity(0.14, 10), 5.216116, 5e-7)
check(fcf11 * annuity(0.14, 10), 41859.33, 0.005)
check(1.14**10, 3.707221, 5e-7)
check(10000 / 1.14**10, 2697.44, 0.005)
check(npv(0.14, cfs11), 9556.77, 0.005)
check(npv(0.14, cfs11) + 35000, 44556.77, 0.005)

# 12. Higgins 9.11 ($ millions)
fcf12 = [-52, 76, 92, 112]
pv_terms = [c / 1.11 ** (t + 1) for t, c in enumerate(fcf12)]
for v, p in zip(pv_terms, [-46.847, 61.683, 67.270, 73.778]):
    check(v, p, 5e-4)
pv12 = sum(pv_terms)
check(pv12, 155.884, 5e-4)
check(1.11**4, 1.518070, 5e-7)
tv_a = 200 * (1 - 0.4) / 0.11
check(200 * 0.6, 120, 1e-9)
check(tv_a, 1090.909, 5e-4)
check(tv_a / 1.11**4, 718.616, 5e-4)
fmv_a = pv12 + tv_a / 1.11**4
check(fmv_a, 874.500, 5e-4)
check((fmv_a - 250) / 40, 15.61, 5e-3)
fcf26 = 200 * 1.05 * (1 - 0.4) - 30 - 15
check(200 * 1.05, 210, 1e-9)
check(210 * 0.6, 126, 1e-9)
check(fcf26, 81, 1e-9)
tv_c = fcf26 / (0.11 - 0.05)
check(tv_c, 1350, 1e-9)
check(tv_c / 1.11**4, 889.287, 5e-4)
fmv_c = pv12 + tv_c / 1.11**4
check(fmv_c, 1045.171, 5e-4)
check((fmv_c - 250) / 40, 19.88, 5e-3)
ni25 = (200 - 0.10 * 250) * (1 - 0.4)
check(200 - 25, 175, 1e-9)
check(ni25, 105, 1e-9)
check(12 * ni25, 1260, 1e-9)
tv_d = 12 * ni25 + 250
check(tv_d, 1510, 1e-9)
check(tv_d / 1.11**4, 994.684, 5e-4)
fmv_d = pv12 + tv_d / 1.11**4
check(fmv_d, 1150.568, 5e-4)
check((fmv_d - 250) / 40, 22.51, 5e-3)
check((fmv_d - 250) / 40, 22.514, 5e-4)

# 13. Ross 10.31 (dollars)
units = [3200, 4300, 3900, 2800]
dep = [1.4e6, 1.4e6, 1.4e6, 0.0]
check(4.2e6 / 3, 1.4e6, 1e-6)
sales = [u * 780 for u in units]
for v, p in zip(sales, [2496000, 3354000, 3042000, 2184000]):
    check(v, p, 0.5)
ebit13 = [0.85 * s - 425000 - d for s, d in zip(sales, dep)]
for v, p in zip([0.85 * s for s in sales], [2121600, 2850900, 2585700, 1856400]):
    check(v, p, 0.5)
for v, p in zip(ebit13, [296600, 1025900, 760700, 1431400]):
    check(v, p, 0.5)
ni13 = [e * 0.66 for e in ebit13]
for v, p in zip(ni13, [195756, 677094, 502062, 944724]):
    check(v, p, 0.5)
ocf13 = [x + d for x, d in zip(ni13, dep)]
for v, p in zip(ocf13, [1595756, 2077094, 1902062, 944724]):
    check(v, p, 0.5)
salv = 400000 * (1 - 0.34)
check(400000 * 0.34, 136000, 0.5)
check(salv, 264000, 0.5)
cf0 = -4.2e6 - 1.5e6 - 125000
check(cf0, -5825000, 0.5)
cf4 = ocf13[3] + 1.6e6 + salv + 125000
check(cf4, 2933724, 0.5)
cfs13 = [cf0] + ocf13[:3] + [cf4]
pv13 = [c / 1.13**t for t, c in enumerate(cfs13)][1:]
for v, p in zip(pv13, [1412173.45, 1626669.28, 1318224.38, 1799307.87]):
    check(v, p, 0.005)
npv13 = npv(0.13, cfs13)
check(npv13, 331374.98, 0.005)
# Robustness: US 3-year MACRS (33.33, 44.45, 14.81, 7.41 percent) instead of straight line.
macrs = [0.3333, 0.4445, 0.1481, 0.0741]
assert abs(sum(macrs) - 1) < 1e-12
dep_m = [m * 4.2e6 for m in macrs]
ocf_m = [(0.85 * s - 425000 - d) * 0.66 + d for s, d in zip(sales, dep_m)]
npv_m = npv(0.13, [cf0] + ocf_m[:3] + [ocf_m[3] + 1.6e6 + salv + 125000])
check(npv_m, 337231.54, 0.005)

# 14. Amaro 1.2.6 #5
s = 1 / 1.01
check(s, 0.990099, 5e-7)
psi1 = (6.7 - 5 * s) / 5
psi2 = s - psi1
check(5 * s, 4.950495, 5e-7)
check(6.7 - 5 * s, 1.749505, 5e-7)
check(psi1, 0.349901, 5e-7)
check(psi2, 0.640198, 5e-7)
assert psi1 > 0 and psi2 > 0
check(1.01 * psi1 + 1.01 * psi2, 1.0, 1e-12)
check(10 * psi1 + 5 * psi2, 6.7, 1e-12)
V2 = -2 * psi1 + 4 * psi2
check(-2 * psi1, -0.699802, 5e-7)
check(4 * psi2, 2.560792, 5e-7)
check(V2, 1.860990, 5e-7)
check(6.7 - 5, 1.7, 1e-12)
check(V2 - 2, -0.139010, 5e-7)
# replication of project 2 with a units of project 1 and b units of the bond
a = (-2 - 4) / (10 - 5)
b = (4 - 5 * a) / 1.01
check(a, -1.2, 1e-12)
check(b, 9.900990, 5e-7)
check(a * 6.7 + b, 1.860990, 5e-7)
q1, q2 = 1.01 * psi1, 1.01 * psi2
check(q1, 0.3534, 5e-5)
check(q2, 0.6466, 5e-5)

# ---- further displayed intermediate values ----
# 1.
check(80000 / 1.09 + 30000 / 1.09**2, 98644.90, 0.005)
# 2.
check(1.6 * 0.06, 0.096, 1e-12)
check(1.36 * 0.06, 0.0816, 1e-12)
check(0.6 * 0.136, 0.0816, 1e-12)
check(0.6 * 1.6, 0.96, 1e-12)
# 4.
check(0.5 * 780, 390, 1e-12)
check(0.5 * 540, 270, 1e-12)
check(660 / 600, 1.10, 1e-12)
check(0.5 * 1200 + 0, 600, 1e-12)
check(0.5 * 960, 480, 1e-12)
check(0.4 * 0.05, 0.02, 1e-12)
check(0.6 * 0.10, 0.06, 1e-12)
# 5.
check(0.75 * 0.063, 0.04725, 1e-12)
# 7.
for c, t, p in [(25, 1, 22.5225), (30, 2, 24.3487), (40, 3, 29.2477), (50, 4, 32.9365),
                (50, 1, 45.0450), (40, 2, 32.4649), (30, 3, 21.9357), (20, 4, 13.1746)]:
    check(c / 1.11**t, p, 5e-5)
coef = [-25, -10, 10, 30]  # -25x^3 - 10x^2 + 10x + 30
assert sum(1 for a, b in zip(coef, coef[1:]) if a * b < 0) == 1
x = 1 + cross
check(-25 * x**3 - 10 * x**2 + 10 * x + 30, 0.0, 1e-9)
# 8.
check(npv8(irr8a), 0.0, 1e-9)
check(npv8(irr8b), 0.0, 1e-9)
for r in (0.0275, 0.06, 0.1088):  # r N(r) = 0.9 - (1+r)^-10 - 5r
    check(r * npv8(r), 0.9 - (1 + r) ** -10 - 5 * r, 1e-12)
# 9.
check(0.26 * 0.06, 0.0156, 1e-12)
check(0.11 * 0.048, 0.00528, 1e-12)
check((w_cs - w9) * 100, 2.1, 0.05)  # "about 2.1 points"
check(0.96 * 0.0666, 0.063936, 5e-7)
check(0.04 * 0.048 * 0.65, 0.001248, 5e-7)
# 10.
check(0.5 * 0.14, 0.07, 1e-12)
# 11.
check(30000 - 18000 - 1000 - 2500, 8500, 1e-9)
check((npv(0.14, cfs11) + 35000) / 1000, 44.56, 0.005)
check(41859.33 + 2697.44 - 35000, 9556.77, 0.005)
# 12.
check(fmv_a - 250, 624.500, 5e-4)
check(fmv_c - 250, 795.171, 5e-4)
check(fmv_d - 250, 900.568, 5e-4)
shares = [tv_a / 1.11**4 / fmv_a, tv_c / 1.11**4 / fmv_c, tv_d / 1.11**4 / fmv_d]
check(min(shares), 0.82, 0.005)
check(max(shares), 0.86, 0.005)
check(126 - 45, 81, 1e-12)
# 13.
for v, p in zip([0.15 * s for s in sales], [374400, 503100, 456300, 327600]):
    check(v, p, 0.5)
for v, p in zip([0.34 * e for e in ebit13], [100844, 348806, 258638, 486676]):
    check(v, p, 0.5)
check(-4.2e6 - 1.5e6 - 125000, -5825000, 0.5)
check(1.5e6 - 1.6e6 / 1.13**4, 519000, 500)  # "about $519,000"
assert all(e > 0 for e in ebit13)
# 14.
check(1.01 * 5 - 1.01 * 10, -5.05, 1e-12)
check(10 * 0.349901, 3.49901, 5e-6)
check(5 * 0.640198, 3.20099, 5e-6)
check(-1.2 * 6.7, -8.04, 1e-12)
check(10 / 1.01, 9.900990, 5e-7)
check(4 - 5 * a, 10, 1e-12)

print(f"PASS {n} checks")
