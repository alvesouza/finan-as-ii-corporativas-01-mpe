"""Numerical check of lista-r3-mm-taxes-tradeoff-solutions.tex.

Every number printed in the solutions PDF is recomputed here from the exercise data and
compared with the value as displayed. Tolerance: half a unit in the last displayed decimal
place (``dec`` argument), so a display that rounds wrongly fails. Proof exercises (13-15)
are checked by evaluating the derived identities at arbitrary parameter values.

Run: python -I Listas/lista-r3-mm-taxes-tradeoff-solutions_check.py  -> prints "PASS <n> checks".
"""

n = 0


def chk(got, printed, dec):
    """Assert that `got` rounds to `printed` when shown with `dec` decimals."""
    global n
    assert abs(got - printed) <= 0.5 * 10 ** (-dec) + 1e-9, (got, printed, dec)
    n += 1


# 1. Berk 16.1
ecf = 0.5 * 130_000 + 0.5 * 180_000
chk(ecf, 155_000, 0)
pv = ecf / 1.20
chk(pv, 129_166.67, 2)
chk(pv - 100_000, 29_166.67, 2)
repay = 100_000 * 1.10
chk(repay, 110_000, 0)
chk(130_000 - repay, 20_000, 0)
chk(180_000 - repay, 70_000, 0)
el = pv - 100_000
chk(0.5 * 20_000 + 0.5 * 70_000, 45_000, 0)
chk(45_000 / el - 1, 0.542857, 6)
chk(100_000 / el, 3.428571, 6)
chk(0.20 + (100_000 / el) * (0.20 - 0.10), 0.542857, 6)

# 2. Berk 17.7 (millions)
v = 500 * 15
chk(v, 7_500, 0)
chk(250 / 500, 0.50, 2)
chk((v - 250) / 500, 14.50, 2)
rep = 250 / 15
chk(rep, 16.6667, 4)
chk(500 - rep, 483.3333, 4)
chk((v - 250) / (500 - rep), 15.00, 2)

# 3. Ross 16.14
vu = 92_000 * (1 - 0.35) / 0.15
chk(92_000 * (1 - 0.35), 59_800, 0)
chk(vu, 398_666.67, 2)
chk(0.35 * 0.09 * 60_000, 1_890, 0)
chk(1_890 / 0.09, 21_000, 0)
chk(0.35 * 60_000, 21_000, 0)
vl = vu + 0.35 * 60_000
chk(vl, 419_666.67, 2)
chk(vl - 60_000, 359_666.67, 2)

# 4. Higgins 8.23
ts = 1_000_000 * 0.08 * 0.40
chk(ts, 32_000, 0)
f = [1 / 1.08 ** t for t in (1, 2, 3)]
chk(f[0], 0.925926, 6)
chk(f[1], 0.857339, 6)
chk(f[2], 0.793832, 6)
chk(sum(f), 2.577097, 6)
pvts = ts * sum(f)
chk(pvts, 82_467.10, 2)
chk(500_000 + pvts, 582_467.10, 2)
chk(500_000 + pvts, 582_467, 0)  # book's printed answer, p. 425

# 5. Berk 16.5
ra = 0.12 + 0.50 * (0.12 - 0.06)
chk(ra, 0.15, 4)
rb = 0.12 + 1.50 * (0.12 - 0.08)
chk(rb, 0.18, 4)
chk((1 / 1.5) * ra + (0.5 / 1.5) * 0.06, 0.12, 4)
chk((1 / 2.5) * rb + (1.5 / 2.5) * 0.08, 0.12, 4)

# 6. Berk 16.11 (millions)
bal = [100, 75, 50, 25]
shields = [0.40 * 0.10 * b for b in bal]
for s, p in zip(shields, [4, 3, 2, 1]):
    chk(s, p, 4)
for b, p in zip(bal, [10, 7.5, 5, 2.5]):
    chk(0.10 * b, p, 4)
terms = [s / 1.10 ** (t + 1) for t, s in enumerate(shields)]
for x, p in zip(terms, [3.636364, 2.479339, 1.502630, 0.683013]):
    chk(x, p, 6)
chk(sum(terms), 8.301346, 6)

# 7. Ross 16.18
chk(72_000 / 1_200_000, 0.06, 4)
chk(400_000 - 72_000, 328_000, 0)
chk(400_000 / 2_500_000, 0.16, 4)
cost_c = 0.05 * 1_632_000
inc_c = 0.05 * 328_000
chk(cost_c, 81_600, 0)
chk(inc_c, 16_400, 0)
chk(inc_c / cost_c, 0.2010, 4)
chk(0.05 * 2_500_000, 125_000, 0)
chk(0.05 * 400_000, 20_000, 0)
borrow = 125_000 - cost_c
chk(borrow, 43_400, 0)
chk(0.06 * borrow, 2_604, 0)
inc_w = 20_000 - 0.06 * borrow
chk(inc_w, 17_396, 0)
chk(inc_w / cost_c, 0.2132, 4)
chk(inc_w - inc_c, 996, 0)
chk(0.05 * 1_200_000, 60_000, 0)
chk(0.06 * 60_000, 3_600, 0)
chk(20_000 - 3_600, 16_400, 0)
chk(125_000 - 60_000, 65_000, 0)
chk(cost_c - 65_000, 16_600, 0)
chk(1_632_000 + 1_200_000, 2_832_000, 0)
chk(2_832_000 - 2_500_000, 332_000, 0)
chk(0.05 * 332_000, 16_600, 0)
chk(0.06 * 16_600, 996, 0)
chk(2_500_000 - 1_200_000, 1_300_000, 0)
chk(328_000 / 1_300_000, 0.2523, 4)
chk(0.16 + (1.2 / 1.3) * (0.16 - 0.06), 0.2523, 4)

# 8. Berk 16.22 (millions)
chk(0.30 * 20, 6, 4)
chk(5.50 * 10, 55, 4)
chk((55 + 6) / 10, 6.10, 2)
chk(5.75 * 10 - 55, 2.5, 4)
chk(6 - 2.5, 3.5, 4)

# 9. Grinblatt & Titman 13.15-13.16
re = 0.08 + 1.2 * (0.13 - 0.08)
chk(re, 0.14, 4)
wacc = 0.5 * re + 0.5 * 0.08 * (1 - 0.40)
chk(wacc, 0.094, 4)
bua = 1.2 / (1 + (1 - 0.40) * 1)
chk(bua, 0.75, 4)
rua = 0.08 + bua * 0.05
chk(rua, 0.1175, 4)
chk(rua * (1 - 0.40 * 0.5), 0.094, 4)
chk(100 - 0.40 * 50, 80, 4)
chk(0.40 * 25, 10, 4)
v2 = 80 + 0.40 * 25
chk(v2, 90, 4)
chk(v2 - 25, 65, 4)
chk(50 - 0.40 * 25, 40, 4)
chk(25 / 90, 0.277778, 6)
chk(1 - 0.40 * 25 / 90, 0.888889, 6)
w2 = rua * (1 - 0.40 * 25 / 90)
chk(w2, 0.104444, 6)
be2 = bua * (1 + 0.6 * 25 / 65)
chk(1 + 0.6 * 25 / 65, 1.230769, 6)
chk(be2, 0.923077, 6)
re2 = 0.08 + be2 * 0.05
chk(re2, 0.126154, 6)
chk((65 / 90) * re2, 0.091111, 6)
chk((25 / 90) * 0.08 * 0.6, 0.013333, 6)
chk((65 / 90) * re2 + (25 / 90) * 0.08 * 0.6, 0.104444, 6)
chk(rua * (1 - 0.40 * 0.25), 0.105750, 6)

# 10. Grinblatt & Titman 16.2
chk(210 * (1 - 1 / 3), 140, 4)
chk(66 * (1 - 1 / 3), 44, 4)
vu10 = 0.5 * (140 + 44) / 1.1
chk(vu10, 920 / 11, 12)
chk(vu10, 83.6364, 4)
d10 = 44 / 1.1
chk(d10, 40, 4)
chk(0.05 * d10, 2, 4)
chk(44 + 2, 46, 4)
chk(140 + 2 - 44, 98, 4)
chk(46 - 44, 2, 4)
e10 = 0.5 * (98 + 2) / 1.1
chk(e10, 500 / 11, 12)
chk(e10, 45.4545, 4)
chk(e10 + d10, 940 / 11, 12)
chk(e10 + d10, 85.4545, 4)
chk(2 / 1.1, 20 / 11, 12)
chk(2 / 1.1, 1.8182, 4)
chk(vu10 + 2 / 1.1, 940 / 11, 12)
# (e) face 70: D = 0.5*(70 + 24 + 0.05 D)/1.1, shown with 5 decimals
de = 47 / 1.075
chk(0.5 * (70 + 24), 47, 4)
chk(1.1 - 0.025, 1.075, 4)
chk(de, 43.72093, 5)
chk(0.05 * de, 2.18605, 5)
chk(24 + 0.05 * de, 26.18605, 5)
chk(70 + 0.05 * de, 72.18605, 5)
ee = 0.5 * (70 + 0.05 * de) / 1.1
chk(ee, 32.81184, 5)
chk(de + ee, 76.53277, 5)
chk(43.72093 + 32.81184, 76.53277, 5)
chk(vu10, 83.63636, 5)
chk(0.05 * de / 1.1, 1.98732, 5)
chk(0.5 * 20 / 1.1, 9.09091, 5)
chk(83.63636 + 1.98732 - 9.09091, 76.53277, 5)
chk(0.05 * 70 / 1.1, 3.18182, 5)
chk(vu10 + 0.05 * 70 / 1.1 - 0.5 * 20 / 1.1, 77.72727, 5)
chk(83.63636 + 3.18182 - 9.09091, 77.72727, 5)

# 11. Grinblatt & Titman 14.2-14.3 (rf = 0, q = 1/2)
chk(0.5 * 210 + 0.5 * 80, 145, 4)
chk(145 - 50, 95, 4)
chk(95 / 100, 0.95, 4)
chk(0.5 * 50 + 0.5 * 40, 45, 4)
chk(2 * 45, 90, 4)
chk(145 + 45 - 90, 100, 4)
chk(100 / 100, 1.00, 4)
chk(45 / 1.00, 45, 4)
chk(100 - 45, 55, 4)
chk(145 - 90, 55, 4)
chk(0.5 * 110, 55, 4)
chk(0.2 * 160, 32, 4)
chk(0.2 * 30, 6, 4)
chk(0.5 * 32 + 0.5 * 6, 19, 4)
chk(0.2 * 55, 11, 4)
chk(20 - 11, 9, 4)
chk(0.2 * 45, 9, 4)
chk(11 * 2 + 0.2 * 50, 32, 4)
chk(0.2 * 40, 8, 4)
chk(0.5 * 32 + 0.5 * 8, 20, 4)
chk(20 - 19, 1, 4)
chk(0.2 * 5, 1, 4)
beta = 6 / 80
chk(beta, 0.075, 4)
nsh = (32 - 100 * beta) / 2
chk(nsh, 12.25, 4)
chk(nsh * 1.00 + beta * 90, 19.00, 4)
chk(beta * 90, 6.75, 4)
chk(50 + 95, 145, 4)
chk(90 + 55, 145, 4)

# 12. Berk 16.18 (millions)
chk(20 * 7.50, 150, 4)
chk(0.40 * 50, 20, 4)
chk(150 + 50 + 20, 220, 4)
chk(220 - 50, 170, 4)
chk(170 / 20, 8.50, 4)
rep12 = 50 / 8.50
chk(rep12, 5.882353, 6)
chk(20 - rep12, 14.117647, 6)
chk(150 + 20, 170, 4)
chk(170 - 50, 120, 4)
chk(120 / (20 - rep12), 8.50, 4)

# 13. Ross 16.19: identity WACC = R_U (1 - T_C D/V) at arbitrary values, then Ex. 3 data
for ebit, ru, rd, tc, d in [(92_000, 0.15, 0.09, 0.35, 60_000), (500, 0.11, 0.05, 0.3, 1_200)]:
    vu_ = ebit * (1 - tc) / ru
    v_ = vu_ + tc * d
    e_ = v_ - d
    re_ = (ebit - rd * d) * (1 - tc) / e_
    chk(re_, ru + (ru - rd) * (d / e_) * (1 - tc), 12)
    chk((e_ / v_) * re_ + (d / v_) * rd * (1 - tc), ru * (1 - tc * d / v_), 12)
chk(21_000 / vl, 0.05003971, 8)
w13 = 0.15 * (1 - 21_000 / vl)
chk(w13, 0.14249404, 8)
chk(0.14249404 * 419_666.67, 59_800.00, 2)
chk((92_000 - 0.09 * 60_000) * 0.65, 56_290, 0)
chk(56_290 / (vl - 60_000), 0.156506, 6)
chk(60_000 / (vl - 60_000), 0.166821, 6)
chk(0.15 + (0.15 - 0.09) * (60_000 / (vl - 60_000)) * 0.65, 0.156506, 6)
chk((vl - 60_000) / vl * 0.156506 + 60_000 / vl * 0.09 * 0.65, 0.142494, 6)

# 14. Amaro 2.2.7 #1: replicating portfolio reproduces the levered payoff; G_L special cases
for X, r, B, tc, ts_, tb in [(10.0, 0.06, 40.0, 0.34, 0.15, 0.30), (3.0, 0.1, 7.0, 0.4, 0.0, 0.0)]:
    L = B * (1 - tc) * (1 - ts_) / (1 - tb)
    levered = (X - r * B) * (1 - tc) * (1 - ts_)
    homemade = X * (1 - tc) * (1 - ts_) - r * L * (1 - tb)
    chk(homemade, levered, 12)
g0 = (1 - (1 - 0.4) * (1 - 0.0) / (1 - 0.0)) * 7.0
chk(g0, 0.4 * 7.0, 12)  # no personal taxes: tau_c B
chk((1 - (1 - 0.4) * (1 - 0.25) / (1 - 0.55)) * 7.0, 0.0, 12)  # Miller: (1-tb)=(1-tc)(1-ts)

# 15. Amaro 2.1.5 #3-#4: replication costs and the no-arbitrage band
for X, r, B, tau, su in [(12.0, 0.08, 50.0, 0.3, 90.0), (5.0, 0.05, 20.0, 0.0, 60.0)]:
    # holding alpha=1 of l's equity vs u's equity plus personal borrowing (1-tau)B
    chk((X - r * B) * (1 - tau), X * (1 - tau) - r * (1 - tau) * B, 12)
    # u's equity vs l's equity plus (1-tau) of l's debt
    chk(X * (1 - tau), (X - r * B) * (1 - tau) + (1 - tau) * r * B, 12)
rbar, rlow, r, B = 0.09, 0.07, 0.08, 50.0
Lb = r * B / rbar   # borrow so that rbar*L = r*B
Ll = r * B / rlow   # lend so that rlow*L = r*B
chk(rbar * Lb, r * B, 12)
chk(rlow * Ll, r * B, 12)
chk(B - Lb, B * (rbar - r) / rbar, 12)
chk(Ll - B, B * (r - rlow) / rlow, 12)

print(f"PASS {n} checks")
