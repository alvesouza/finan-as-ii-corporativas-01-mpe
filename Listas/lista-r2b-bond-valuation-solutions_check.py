"""Numeric checks for Listas/lista-r2b-bond-valuation-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-r2b-bond-valuation-solutions_check.py  -> PASS <n> checks
Every number printed in the two solution files is asserted here. Tolerances are absolute and
match the decimals printed (5e-3 for cents, 5e-5 for rates shown to 0.01%, 5e-7 for factors
shown to six decimals) unless stated otherwise.
"""

N = 0


def chk(label, got, want, tol):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a boolean condition (orderings, signs); count the check."""
    global N
    assert cond, label
    N += 1


def ann(r, n):
    """Annuity factor [1 - (1+r)^-n]/r: PV of 1 per period for n periods at rate r per period."""
    return (1 - (1 + r) ** -n) / r


def price(c, face, r, n):
    """Price of a level-coupon bond: coupon c per period, face paid at n, yield r per period."""
    return c * ann(r, n) + face / (1 + r) ** n


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


C, R, F6, F7 = 5e-3, 5e-5, 5e-7, 5e-4  # cents, rate to 0.01%, factor to 6 dp, 4-dp ratio

# --- Ex 1: Berk 6.4, zero-coupon yields
prices = [95.51, 91.05, 86.38, 81.65, 76.51]
ratio = [1.047011, 1.098298, 1.157675, 1.224740, 1.307019]
gross = [1.047011, 1.047997, 1.050015, 1.051988, 1.055009]
ytm1 = [0.0470, 0.0480, 0.0500, 0.0520, 0.0550]
y = []
for n, (p, q, g, t) in enumerate(zip(prices, ratio, gross, ytm1), 1):
    chk(f"1 100/P_{n}", 100 / p, q, F6)
    chk(f"1 (100/P)^(1/{n})", (100 / p) ** (1 / n), g, F6)
    chk(f"1 YTM_{n}", (100 / p) ** (1 / n) - 1, t, 5e-4)
    y.append((100 / p) ** (1 / n) - 1)
ok("1 curve upward sloping", all(a < b for a, b in zip(y, y[1:])))

# --- Ex 2: Higgins 5.5, holding-period return
chk("2 coupon", 0.06 * 1000, 60, 1e-9)
chk("2 price change", 940 - 1050, -110, 1e-9)
chk("2 HPR", (60 + 940 - 1050) / 1050, -0.0476, 5e-5)

# --- Ex 3: Ross 7.6, seasoned semiannual bond
chk("3 coupon per half-year", 69 / 2, 34.5, 1e-9)
chk("3 rate per half-year", 0.074 / 2, 0.037, 1e-12)
chk("3 1.037^20", 1.037 ** 20, 2.068117, F6)
chk("3 annuity factor", ann(0.037, 20), 13.958605, F6)
chk("3 discount factor", 1 / 1.037 ** 20, 0.483532, F6)
chk("3 PV coupons", 34.5 * ann(0.037, 20), 481.57, C)
chk("3 PV face", 1000 / 1.037 ** 20, 483.53, C)
chk("3 price", price(34.5, 1000, 0.037, 20), 965.10, C)

# --- Ex 5: illustration of promised yield vs expected return (one-year zero)
chk("5 promised yield", 100 / 90 - 1, 0.1111, 5e-5)
chk("5 expected payoff", 0.95 * 100 + 0.05 * 40, 97, 1e-9)
chk("5 expected return", 97 / 90 - 1, 0.0778, 5e-5)

# --- Ex 6: Berk 6.24, credit spreads
chk("6 AAA price", 100 / 1.032, 96.90, C)
chk("6 AAA spread", 3.2 - 3.1, 0.1, 1e-9)
chk("6 BBB spread", 4.2 - 3.1, 1.1, 1e-9)
chk("6 B spread", 4.9 - 3.1, 1.8, 1e-9)

# --- Ex 7: Berk 6.16-6.18, GMAC bond over time
chk("7 a10 at 6%", ann(0.06, 10), 7.360087, F6)
chk("7 v10 at 6%", 1 / 1.06 ** 10, 0.558395, F6)
chk("7 PV coupons", 70 * ann(0.06, 10), 515.21, C)
chk("7 PV face", 1000 / 1.06 ** 10, 558.39, C)
P0 = price(70, 1000, 0.06, 10)
chk("7 P0", P0, 1073.60, C)
chk("7 P before coupon", P0 * 1.06, 1138.02, C)
chk("7 a9 at 6%", ann(0.06, 9), 6.801692, F6)
chk("7 v9 at 6%", 1 / 1.06 ** 9, 0.591898, F6)
chk("7 9-year PV coupons", 70 * ann(0.06, 9), 476.12, C)
chk("7 9-year PV face", 1000 / 1.06 ** 9, 591.90, C)
P1 = price(70, 1000, 0.06, 9)
chk("7 P after coupon", P1, 1068.02, C)
chk("7 before = 70 + after", 70 + P1, P0 * 1.06, 1e-9)
chk("7 drop over the year", P0 - P1, 5.58, C)
chk("7 interest at 6% on P0", 0.06 * P0, 64.42, C)

# --- Ex 8: Berk 6.10, spot-rate pricing
chk("8 1.0055^2", 1.0055 ** 2, 1.011030, F6)
chk("8 1.0065^3", 1.0065 ** 3, 1.019627, F6)
pv8 = [20 / 1.005, 20 / 1.0055 ** 2, 1020 / 1.0065 ** 3]
for k, w in zip(pv8, [19.90, 19.78, 1000.37]):
    chk("8 PV term", k, w, C)
P8 = sum(pv8)
chk("8 price", P8, 1040.05, C)
y8 = bisect(lambda r: 20 / (1 + r) + 20 / (1 + r) ** 2 + 1020 / (1 + r) ** 3 - P8, 1e-6, 0.05)
chk("8 YTM APR", 2 * y8, 0.01295, 5e-6)
ok("8 YTM between 1.1% and 1.3%", 0.011 < 2 * y8 < 0.013)

# --- Ex 9: Ross 7.19, coupon for a new issue at par
y9 = bisect(lambda r: price(40, 1000, r, 40) - 930, 1e-4, 0.2)
chk("9 semiannual yield", y9, 0.043736, F6)
chk("9 APR", 2 * y9, 0.0875, 5e-5)
chk("9 annuity factor", ann(y9, 40), 18.738512, F6)
chk("9 discount factor", 1 / (1 + y9) ** 40, 0.180460, F6)
chk("9 PV coupons", 40 * ann(y9, 40), 749.54, C)
chk("9 PV face", 1000 / (1 + y9) ** 40, 180.46, C)
chk("9 EAR", (1 + y9) ** 2 - 1, 0.0894, 5e-5)
chk("9 trial 9% APR", price(40, 1000, 0.045, 40), 907.99, C)
chk("9 trial 8.5% APR", price(40, 1000, 0.0425, 40), 952.31, C)

# --- Ex 10: Berk 6.26, HMK
chk("10 a5 at 6.3%", ann(0.063, 5), 4.178207, F6)
chk("10 v5 at 6.3%", 1 / 1.063 ** 5, 0.736773, F6)
P10 = price(65, 1000, 0.063, 5)
chk("10 PV coupons", 65 * ann(0.063, 5), 271.58, C)
chk("10 PV face", 1000 / 1.063 ** 5, 736.77, C)
chk("10 price AA", P10, 1008.36, C)
chk("10 bonds needed", 10e6 / P10, 9917.13, C)
chk("10 principal", round(10e6 / P10) * 1000, 9917000, 1e-9)
chk("10 proceeds", round(10e6 / P10) * P10, 9999870.56, C)
chk("10 par at 6.5%", price(65, 1000, 0.065, 5), 1000, 1e-9)
y10 = bisect(lambda r: price(65, 1000, r, 5) - 959.54, 0.01, 0.2)
chk("10 implied yield", y10, 0.0750, 5e-6)
chk("10 a5 at 7.5%", ann(0.075, 5), 4.045885, F6)
chk("10 v5 at 7.5%", 1 / 1.075 ** 5, 0.696559, F6)
chk("10 PV coupons 7.5%", 65 * ann(0.075, 5), 262.98, C)
chk("10 PV face 7.5%", 1000 / 1.075 ** 5, 696.56, C)
chk("10 price at 7.5%", price(65, 1000, 0.075, 5), 959.54, C)

# --- Ex 11: Berk 6.21-6.22, sensitivity
rows = {"A": (0, 15, 417.27, 481.02, 0.1528), "B": (0, 10, 558.39, 613.91, 0.0994),
        "C": (40, 15, 805.76, 896.20, 0.1123), "D": (80, 10, 1147.20, 1231.65, 0.0736)}
chg = {}
for k, (c, n, p6, p5, d) in rows.items():
    a6, a5 = price(c, 1000, 0.06, n), price(c, 1000, 0.05, n)
    chk(f"11 {k} P(6%)", a6, p6, C)
    chk(f"11 {k} P(5%)", a5, p5, C)
    chk(f"11 {k} change", a5 / a6 - 1, d, 5e-5)
    chg[k] = a5 / a6 - 1
chk("11 a15 6%", ann(0.06, 15), 9.712249, F6)
chk("11 a15 5%", ann(0.05, 15), 10.379658, F6)
chk("11 a10 5%", ann(0.05, 10), 7.721735, F6)
chk("11 v15 6%", 1 / 1.06 ** 15, 0.417265, F6)
chk("11 v15 5%", 1 / 1.05 ** 15, 0.481017, F6)
chk("11 v10 5%", 1 / 1.05 ** 10, 0.613913, F6)
ok("11 ranking A > C > B > D", chg["A"] > chg["C"] > chg["B"] > chg["D"])


def duration(c, n, r=0.06):
    """Macaulay duration (years) of an annual-coupon bond with face 1000 at yield r."""
    p = price(c, 1000, r, n)
    return sum(t * (c + (1000 if t == n else 0)) / (1 + r) ** t for t in range(1, n + 1)) / p


chk("11 D_A", duration(0, 15), 15.00, C)
chk("11 D_B", duration(0, 10), 10.00, C)
chk("11 D_C", duration(40, 15), 11.11, C)
chk("11 D_D", duration(80, 10), 7.45, C)

# --- Ex 12: Ross 7.31, bonds M and N
r = 0.035
chk("12 a16", ann(r, 16), 12.094117, F6)
chk("12 a12", ann(r, 12), 9.663334, F6)
chk("12 1.035^12", (1 + r) ** 12, 1.511069, F6)
chk("12 1.035^28", (1 + r) ** 28, 2.620172, F6)
chk("12 1.035^40", (1 + r) ** 40, 3.959260, F6)
chk("12 value at 12 of 1100 annuity", 1100 * ann(r, 16), 13303.53, C)
chk("12 value at 28 of 1400 annuity", 1400 * ann(r, 12), 13528.67, C)
pv1 = 1100 * ann(r, 16) / (1 + r) ** 12
pv2 = 1400 * ann(r, 12) / (1 + r) ** 28
pv3 = 20000 / (1 + r) ** 40
chk("12 PV block 1", pv1, 8804.05, C)
chk("12 PV block 2", pv2, 5163.27, C)
chk("12 PV face", pv3, 5051.45, C)
chk("12 price M", pv1 + pv2 + pv3, 19018.78, C)
chk("12 price N", pv3, 5051.45, C)
chk("12 periods", 12 + 16 + 12, 40, 0)

# --- Ex 13: G&T 10A.3, bootstrap
par = [0.045, 0.05, 0.0525, 0.0525]
dfs = []
want_d = [0.956938, 0.906812, 0.857153, 0.814397]
want_s = [0.0450, 0.0501, 0.0527, 0.0527]
want_s4 = [0.045000, 0.050126, 0.052723, 0.052667]
want_A = [0.956938, 1.863750, 2.720903, 3.535300]
want_ay = [0.0450, 0.0484, 0.0505, 0.0513]
want_ay4 = [0.045000, 0.048356, 0.050460, 0.051296]
want_strip = [100.0, 95.215311, 90.215311, 85.715260]
for t, cpar in enumerate(par, 1):
    cc = 100 * cpar
    stripped = 100 - cc * sum(dfs)
    chk(f"13 stripped value {t}", stripped, want_strip[t - 1], F6)
    d = stripped / (100 + cc)
    dfs.append(d)
    chk(f"13 d_{t}", d, want_d[t - 1], F6)
    s = d ** (-1 / t) - 1
    chk(f"13 spot {t} (2dp)", s, want_s[t - 1], 5e-5)
    chk(f"13 spot {t} (4dp)", s, want_s4[t - 1], F6)
    A = sum(dfs)
    chk(f"13 annuity PV {t}", A, want_A[t - 1], F6)
    ay = bisect(lambda q: ann(q, t) - A, 1e-6, 0.5)
    chk(f"13 annuity yield {t} (2dp)", ay, want_ay[t - 1], 5e-5)
    chk(f"13 annuity yield {t} (4dp)", ay, want_ay4[t - 1], F6)
chk("13 5 x d1", 5 * dfs[0], 4.784689, F6)
chk("13 5.25 x (d1+d2)", 5.25 * (dfs[0] + dfs[1]), 9.784689, F6)
chk("13 5.25 x (d1+d2+d3)", 5.25 * sum(dfs[:3]), 14.284740, F6)
chk("13 check 2-yr par bond", 5 * dfs[0] + 105 * dfs[1], 100, 1e-9)
chk("13 check 4-yr par bond", 5.25 * sum(dfs[:3]) + 105.25 * dfs[3], 100, 1e-9)

# --- Ex 14: Ross 7.32, implied call value
w = (12 - 8.25) / (12 - 6.5)
chk("14 weight on 6.5%", w, 0.681818, F6)
chk("14 weight on 12%", 1 - w, 0.318182, F6)
chk("14 synthetic coupon", w * 6.5 + (1 - w) * 12, 8.25, 1e-9)
ask = [106 + 12 / 32, 103 + 16 / 32, 134 + 31 / 32]
bid = [106 + 10 / 32, 103 + 14 / 32, 134 + 25 / 32]
chk("14 ask 6.5", ask[0], 106.375, 1e-12)
chk("14 ask 8.25", ask[1], 103.5, 1e-12)
chk("14 ask 12", ask[2], 134.96875, 1e-12)
chk("14 w x ask 6.5", w * ask[0], 72.5284, 5e-5)
chk("14 (1-w) x ask 12", (1 - w) * ask[2], 42.9446, 5e-5)
syn = w * ask[0] + (1 - w) * ask[2]
chk("14 synthetic ask", syn, 115.4730, 5e-5)
chk("14 call value % of face (ask)", syn - ask[1], 11.9730, 5e-5)
chk("14 call value per 1000 (ask)", 10 * (syn - ask[1]), 119.73, C)
synb = w * bid[0] + (1 - w) * bid[2]
chk("14 bid 6.5", bid[0], 106.3125, 1e-12)
chk("14 bid 8.25", bid[1], 103.4375, 1e-12)
chk("14 bid 12", bid[2], 134.78125, 1e-12)
chk("14 synthetic bid", synb, 115.3707, 5e-5)
chk("14 call value per 1000 (bid)", 10 * (synb - bid[1]), 119.33, C)

# --- Ex 15: G&T 7.3, risky bond on a tree
pi0 = (100 * 1.04 - 90) / (120 - 90)
piU = (120 * 1.04 - 110) / (300 - 110)
piD = (90 * 1.04 - 50) / (110 - 50)
chk("15 pi0", pi0, 0.466667, F6)
chk("15 piU", piU, 0.077895, F6)
chk("15 piD", piD, 0.726667, F6)
chk("15 pi0 numerator", 100 * 1.04 - 90, 14, 1e-9)
chk("15 piU numerator", 120 * 1.04 - 110, 14.8, 1e-9)
chk("15 piD numerator", 90 * 1.04 - 50, 43.6, 1e-9)
VU = 105 / 1.04
VD = (piD * 105 + (1 - piD) * 50) / 1.04
chk("15 VU", VU, 100.9615, 5e-5)
chk("15 piD x 105", piD * 105, 76.30, C)
chk("15 (1-piD) x 50", (1 - piD) * 50, 13.6667, 5e-5)
chk("15 VD numerator", piD * 105 + (1 - piD) * 50, 89.9667, 5e-5)
chk("15 VD", VD, 86.5064, 5e-5)
chk("15 pi0 x VU", pi0 * VU, 47.1154, 5e-5)
chk("15 (1-pi0) x VD", (1 - pi0) * VD, 46.1368, 5e-5)
chk("15 expected date-1 value of final payment", pi0 * VU + (1 - pi0) * VD, 93.2521, 5e-5)
chk("15 PV final payment", (pi0 * VU + (1 - pi0) * VD) / 1.04, 89.6655, 5e-5)
chk("15 PV coupon", 5 / 1.04, 4.8077, 5e-5)
V0 = 5 / 1.04 + (pi0 * VU + (1 - pi0) * VD) / 1.04
chk("15 bond value", V0, 94.47, C)
chk("15 cum-coupon route", (pi0 * (VU + 5) + (1 - pi0) * (VD + 5)) / 1.04, V0, 1e-9)
chk("15 cum-coupon numerator", pi0 * (VU + 5) + (1 - pi0) * (VD + 5), 98.2521, 5e-5)
yy = bisect(lambda q: 5 / (1 + q) + 105 / (1 + q) ** 2 - V0, 0, 0.5)
chk("15 promised yield per period", yy, 0.0810, 5e-5)
chk("15 promised yield APR", 2 * yy, 0.1621, 5e-5)
chk("15 promised yield EAR", (1 + yy) ** 2 - 1, 0.1686, 5e-5)
riskfree = 5 / 1.04 + 105 / 1.04 ** 2
chk("15 default-free twin", riskfree, 101.89, C)
chk("15 1.04^2", 1.04 ** 2, 1.0816, 1e-12)
qDD = (1 - pi0) * (1 - piD)
chk("15 q_DD", qDD, 0.145778, F6)
chk("15 expected shortfall at 2", 55 * qDD, 8.0178, 5e-5)
chk("15 PV expected shortfall", 55 * qDD / 1.04 ** 2, 7.4129, 5e-5)
chk("15 twin minus risky", riskfree - V0, 55 * qDD / 1.04 ** 2, 1e-9)
chk("15 spread per period (pp)", 100 * (yy - 0.04), 4.10, C)
qUU = pi0 * piU
qUD = pi0 * (1 - piU) + (1 - pi0) * piD
chk("15 q_UU", qUU, 0.036351, F6)
chk("15 q_UD", qUD, 0.817871, F6)
chk("15 q sum", qUU + qUD + qDD, 1, 1e-12)
chk("15 RN expected one-period return at U", 105 / VU - 1, 0.04, 1e-12)
chk("15 105/1.0816", 105 / 1.0816, 97.0784, 5e-5)
chk("15 asset return up at 0", 120 / 100 - 1, 0.20, 1e-12)
chk("15 asset return down at 0", 90 / 100 - 1, -0.10, 1e-12)
chk("15 asset return up at U", 300 / 120 - 1, 1.50, 1e-12)
chk("15 asset return down at U", 110 / 120 - 1, -0.083, 5e-4)

# --- extra numbers quoted in the text of the solutions
chk("2 capital loss only", (940 - 1050) / 1050, -0.105, 5e-4)
chk("3 1 - v", 1 - 1 / 1.037 ** 20, 0.516468, F6)
chk("3 discount = PV of shortfall", (37 - 34.5) * ann(0.037, 20), 1000 - price(34.5, 1000, 0.037, 20), 1e-9)
chk("3 discount", (37 - 34.5) * ann(0.037, 20), 34.90, C)
ok("8 flat 1.3% price lower", price(20, 1000, 0.0065, 3) < P8)
chk("10 AA minus BB price", P10 - price(65, 1000, 0.075, 5), 48.82, C)
chk("11 C coupons 6%", 40 * ann(0.06, 15), 388.49, C)
chk("11 C coupons 5%", 40 * ann(0.05, 15), 415.19, C)
chk("11 D coupons 6%", 80 * ann(0.06, 10), 588.81, C)
chk("11 D coupons 5%", 80 * ann(0.05, 10), 617.74, C)
chk("12 M minus N", pv1 + pv2, 13967.33, C)
chk("13 1/1.048356", 1 / 1.048356, 0.953874, F6)
chk("13 1/1.048356^2", 1 / 1.048356 ** 2, 0.909876, F6)
chk("13 sum", 1 / 1.048356 + 1 / 1.048356 ** 2, 1.863751, F6)
chk("14 0.681818 x 6.5", w * 6.5, 4.431818, F6)
chk("14 0.318182 x 12", (1 - w) * 12, 3.818182, F6)
chk("14 call % of face (bid)", synb - bid[1], 11.9332, 5e-5)
chk("10 AA proceeds per bond = price", P10, 1008.36, C)

print(f"PASS {N} checks")
