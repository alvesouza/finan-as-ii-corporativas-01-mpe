"""Check every number printed in lista-r5b-trade-credit-working-capital-solutions.tex.

Run: python -I Listas/lista-r5b-trade-credit-working-capital-solutions_check.py
Each printed value is recomputed from the statement data and compared with the value shown
in the PDF. Tolerance: half a unit in the last printed decimal (e.g. 44.59 -> 5e-3), so the
assert fails if the displayed rounding is wrong. Prints "PASS <n> checks".
"""

n = 0


def ok(computed, printed, decimals):
    """Assert `computed` rounds to `printed` at `decimals` places (tolerance 0.5e-decimals)."""
    global n
    tol = 0.5 * 10 ** (-decimals) + 1e-9
    assert abs(computed - printed) <= tol, (computed, printed)
    n += 1


Y = 365  # days in a year, all books


def ear(rate, days):
    """Effective annual rate of `rate` earned over a period of `days` days."""
    return (1 + rate) ** (Y / days) - 1


# 1. Berk 19.3 Westerly
inv1 = 15_000 / (80_000 / Y); ok(80_000 / Y, 219.18, 2); ok(inv1, 68.44, 2)
ar1 = 30_000 / (100_000 / Y); ok(100_000 / Y, 273.97, 2); ok(ar1, 109.50, 2)
ap1 = 40_000 / (80_000 / Y); ok(ap1, 182.50, 2)
ok(inv1 + ar1, 177.94, 2)
ccc1 = inv1 + ar1 - ap1; ok(ccc1, -4.56, 2)

# 2. Ross 18.6 Mediadora
ainv = (9_780 + 11_380) / 2; ok(ainv, 10_580, 0)
aar = (4_108 + 4_938) / 2; ok(aar, 4_523, 0)
aap = (7_636 + 7_927) / 2; ok(aap, 7_781.5, 1)
tinv = 56_384 / ainv; ok(tinv, 5.3293, 4)
tar = 89_804 / aar; ok(tar, 19.8550, 4)
tap = 56_384 / aap; ok(tap, 7.2459, 4)
dinv = Y / tinv; ok(dinv, 68.49, 2)
dar = Y / tar; ok(dar, 18.38, 2)
dap = Y / tap; ok(dap, 50.37, 2)
oc2 = dinv + dar; ok(oc2, 86.87, 2)
cc2 = oc2 - dap; ok(cc2, 36.50, 2)

# 3. Ross 20.1 cash discount
inv3 = 400 * 125; ok(inv3, 50_000, 0)
disc3 = 0.01 * inv3; ok(disc3, 500, 0)
ok(inv3 - disc3, 49_500, 0)
r3 = disc3 / (inv3 - disc3); ok(r3 * 100, 1.0101, 4)
ok(30 - 10, 20, 0)
ok(Y / 20, 18.25, 2)
ok(ear(r3, 20) * 100, 20.13, 2)
ok(r3 * Y / 20 * 100, 18.43, 2)  # simple-interest APR, for the pitfall

# 4. Ross 20.3 Kyoto Boy
pmr = 0.65 * 10 + 0.35 * 30; ok(0.65 * 10, 6.5, 1); ok(0.35 * 30, 10.5, 1); ok(pmr, 17, 0)
ms4 = 1_300 * 1_700; ok(ms4, 2_210_000, 0)
as4 = 12 * ms4; ok(as4, 26_520_000, 0)
ds4 = as4 / Y; ok(ds4, 72_657.53, 2)
ar4 = ds4 * pmr; ok(ar4, 1_235_178.08, 2)
ok(ms4 * pmr / 30, 1_252_333.33, 2)  # 30-day-month alternative

# 5. Berk 19.17 HVHS
dc5 = 8_000_000 / Y; ok(dc5, 21_917.81, 2)
dio5 = 2_000_000 / dc5; ok(dio5, 91.25, 2)
inv5 = 73 * dc5; ok(inv5, 1_600_000, 0)
ok(2_000_000 - inv5, 400_000, 0)
ok(91.25 - 73, 18.25, 2)
ok(18.25 * dc5, 400_000, 0)

# 6. Berk 19.6 Greek Connection ($ thousands)
ok(2_000 + 3_950 + 1_300, 7_250, 0); ok(1_500 + 1_000 + 1_220, 3_720, 0)
nwc6 = 7_250 - 3_720; ok(nwc6, 3_530, 0)
onwc6 = 3_950 + 1_300 - 1_500 - 1_220; ok(onwc6, 2_530, 0)
ds6 = 32_000 / Y; ok(ds6, 87.671, 3)
dc6 = 20_000 / Y; ok(dc6, 54.795, 3)
ar6 = 3_950 / ds6; ok(ar6, 45.05, 2)
inv6 = 1_300 / dc6; ok(inv6, 23.73, 2)
ap6 = 1_500 / dc6; ok(ap6, 27.38, 2)
ccc6 = inv6 + ar6 - ap6; ok(ccc6, 41.40, 2)
ccc6c = inv6 + 30 - ap6; ok(ccc6c, 26.35, 2)
ok(ccc6 - ccc6c, 15.05, 2)
ar6c = 30 * ds6; ok(ar6c, 2_630.14, 2)
ok(3_950 - ar6c, 1_319.86, 2)

# 7. Berk 19.14 terms 3/15, net 40
r7 = 3 / 97; ok(r7 * 100, 3.0928, 4)
ok(Y / 25, 14.6, 1); ok(Y / 35, 10.4286, 4)
ea7 = ear(r7, 25); ok(ea7 * 100, 56.00, 2)
eb7 = ear(r7, 35); ok(eb7 * 100, 37.39, 2)
ok(r7 * Y / 25 * 100, 45.15, 2)  # APR (pitfall)

# 8. Higgins 2.13 Toyota vs Apple
ti = 2_434_918 / (24_522_364 / Y); ok(ti, 36.24, 2)
tr = 8_709_065 / (29_929_992 / Y); ok(tr, 106.21, 2)
tp = 2_434_180 / (24_522_364 / Y); ok(tp, 36.23, 2)
ai = 4_061 / (169_559 / Y); ok(ai, 8.74, 2)
ar = 16_120 / (274_515 / Y); ok(ar, 21.43, 2)
apd = 42_296 / (169_559 / Y); ok(apd, 91.05, 2)
ok(24_522_364 / Y, 67_184.56, 2); ok(29_929_992 / Y, 82_000.0, 1)
ok(169_559 / Y, 464.55, 2); ok(274_515 / Y, 752.10, 2)
oct_ = ti + tr; ok(oct_, 142.45, 2)
oca = ai + ar; ok(oca, 30.18, 2)
ok(oct_ - tp, 106.22, 2)
ok(oca - apd, -60.87, 2)
ok(16_120 + 4_061 - 42_296, -22_115, 0)  # Apple trade working capital, $ million
ok(8_709_065 + 2_434_918 - 2_434_180, 8_709_803, 0)

# 9. Berk 20.8 Hand-to-Mouth
rA = 2 / 98; ok(rA * 100, 2.0408, 4)
eA = ear(rA, 20); ok(eA * 100, 44.59, 2)
LB = 10_100 / 0.95; ok(LB, 10_631.58, 2)
ok(0.05 * LB, 531.58, 2)
iB = 0.12 / 12 * LB; ok(iB, 106.32, 2)
payB = LB + iB - 0.05 * LB; ok(payB, 10_206.32, 2)
rB = payB / 10_000 - 1; ok(rB * 100, 2.0632, 4)
eB = ear(rB, 30); ok(eB * 100, 28.21, 2)
ok((1 + rB) ** 12 * 100 - 100, 27.77, 2)
LC = 10_000 / 0.99; ok(LC, 10_101.01, 2)
ok(0.01 * LC, 101.01, 2)
iC = 0.15 / 12 * LC; ok(iC, 126.26, 2)
payC = LC + iC; ok(payC, 10_227.27, 2)
rC = payC / 10_000 - 1; ok(rC * 100, 2.2727, 4)
eC = ear(rC, 30); ok(eC * 100, 31.45, 2)
ok((1 + rC) ** 12 * 100 - 100, 30.95, 2)
ok(Y / 30, 12.1667, 4)
assert eB < eC < eA; n += 1

# 10. Ross 20.9 Pecas Aereas ($ million per engine)
v, P, pi, R = 1.6, 1.87, 1 / 200, 0.029
ok(pi, 0.005, 3)
ok((1 - pi) * P, 1.86065, 5)
pv10 = (1 - pi) * P / (1 + R); ok(pv10, 1.808212, 6)
npv10 = -v + pv10; ok(npv10, 0.208212, 6)
ok(8 * npv10, 1.665695, 6)
ok(v * (1 + R), 1.6464, 4)
q10 = v * (1 + R) / P; ok(q10, 0.880428, 6)
ok(1 - q10, 0.119572, 6)
ok((P - v), 0.27, 2)
ok((1 - pi) * (P - v), 0.26865, 5)
pv10c = (1 - pi) * (P - v) / R; ok(pv10c, 9.263793, 6)
npv10c = -v + pv10c; ok(npv10c, 7.663793, 6)
ok(8 * npv10c, 61.310345, 6)
ok(v * R, 0.0464, 4)
q10c = v * R / (P - v); ok(q10c, 0.171852, 6)
ok(1 - q10c, 0.828148, 6)

# 11. Ross 18.15 Lince ($ million)
S = [210, 180, 245, 280]; S5 = 240
ok(45 / 90, 0.5, 1); ok(36 / 90, 0.4, 1)
coll = [68 + 0.5 * S[0]] + [0.5 * S[i - 1] + 0.5 * S[i] for i in (1, 2, 3)]
for c, p in zip(coll, [173, 195, 212.5, 262.5]):
    ok(c, p, 1)
ok(0.5 * S[3], 140, 0)  # receivables at year end
purch = [0.45 * x for x in (S[1], S[2], S[3], S5)]
for c, p in zip(purch, [81, 110.25, 126, 108]):
    ok(c, p, 2)
p0 = 0.45 * S[0]; ok(p0, 94.5, 1)
prev = [p0] + purch[:3]
pay = [0.4 * prev[i] + 0.6 * purch[i] for i in range(4)]
for c, p in zip(pay, [86.4, 98.55, 119.7, 115.2]):
    ok(c, p, 2)
for a, b, p in zip([0.4 * x for x in prev], [0.6 * x for x in purch],
                   [(37.8, 48.6), (32.4, 66.15), (44.1, 75.6), (50.4, 64.8)]):
    ok(a, p[0], 2); ok(b, p[1], 2)
wages = [0.25 * x for x in S]
for c, p in zip(wages, [52.5, 45, 61.25, 70]):
    ok(c, p, 2)
capex = [0, 80, 0, 0]
disb = [pay[i] + wages[i] + 12 + capex[i] for i in range(4)]
for c, p in zip(disb, [150.9, 235.55, 192.95, 197.2]):
    ok(c, p, 2)
net = [coll[i] - disb[i] for i in range(4)]
for c, p in zip(net, [22.1, -40.55, 19.55, 65.3]):
    ok(c, p, 2)
cash = 64; ends = []
for x in net:
    cash += x; ends.append(cash)
for c, p in zip(ends, [86.1, 45.55, 65.1, 130.4]):
    ok(c, p, 2)
for c, p in zip([e - 30 for e in ends], [56.1, 15.55, 35.1, 100.4]):
    ok(c, p, 2)
# (b) plan: keep 30, invest surplus at 2%/qtr, borrow at 3%/qtr (none needed)
inv = 0.0; begin_cash = 64; incs, buys, sells, invb, inve = [], [], [], [], []
for x in net:
    inc = 0.02 * inv
    flow = begin_cash + x + inc - 30
    invb.append(inv)
    incs.append(inc)
    buys.append(max(flow, 0)); sells.append(max(-flow, 0))
    inv += flow; inve.append(inv)
    assert inv >= 0  # no borrowing ever needed
    begin_cash = 30
n += 1
for c, p in zip(incs, [0, 1.122, 0.33344, 0.73111]):
    ok(c, p, 5)
for c, p in zip(buys, [56.1, 0, 19.88344, 66.03111]):
    ok(c, p, 5)
ok(sells[1], 39.428, 3)
for c, p in zip(inve, [56.1, 16.672, 36.55544, 102.58655]):
    ok(c, p, 5)
tot_inc = sum(incs); ok(tot_inc, 2.18655, 5)
ok(-tot_inc, -2.18655, 5)

# 12. Grinblatt 17.5 BCD
ts12 = 1_000 * 0.12 * 0.40; ok(1_000 * 0.12, 120, 0); ok(ts12, 48, 0)
sc12 = 0.02 * 1_500; ok(sc12, 30, 0)
sca12 = sc12 * (1 - 0.40); ok(sca12, 18, 0)
ok(ts12 - sca12, 30, 0)
ok(ts12 - sc12, 18, 0)
ok(1_000 * 0.40, 400, 0)          # PV tax shield, perpetual debt
ok(sca12 / 0.12, 150, 0)          # PV of supplier cost at 12%
ok(400 - 150, 250, 0)

# 13. Berk 19.15 IMC ($ million)
i09 = 6_200 / (52_000 / Y); ok(i09, 43.52, 2)
r09 = 2_800 / (60_000 / Y); ok(r09, 17.03, 2)
p09 = 3_600 / (52_000 / Y); ok(p09, 25.27, 2)
c09 = i09 + r09 - p09; ok(c09, 35.28, 2)
i10 = 6_600 / (61_000 / Y); ok(i10, 39.49, 2)
r10 = 6_900 / (75_000 / Y); ok(r10, 33.58, 2)
p10 = 4_600 / (61_000 / Y); ok(p10, 27.52, 2)
c10 = i10 + r10 - p10; ok(c10, 45.55, 2)
ok(c10 - c09, 10.26, 2)
ok(52_000 / Y, 142.47, 2); ok(60_000 / Y, 164.38, 2)
ok(61_000 / Y, 167.12, 2); ok(75_000 / Y, 205.48, 2)
ok(r09 * 75_000 / Y, 3_500, 0)
ok(6_900 - r09 * 75_000 / Y, 3_400, 0)
ok(i09 * 61_000 / Y, 7_273.08, 2)
ok(30 * 61_000 / Y, 5_013.70, 2)
ok(30 * 61_000 / Y - 4_600, 413.70, 2)
ok(30 * 52_000 / Y - 3_600, 673.97, 2)
ok(i10 - i09, -4.03, 2); ok(r10 - r09, 16.55, 2); ok(p10 - p09, 2.26, 2)
ok((c10 - c09) * 75_000 / Y, 2_109, 0)

# 14. Ross 20.14 + 20.18 Senna
cost0 = 91 * 3_850 + 47 * (3_940 - 3_850); ok(91 * 3_850, 350_350, 0); ok(cost0, 354_580, 0)
ok(47 * 90, 4_230, 0)
ok((94 - 47) * 3_940, 185_180, 0); ok((91 - 47) * 3_850, 169_400, 0)
inc0 = (94 - 47) * 3_940 - (91 - 47) * 3_850; ok(inc0, 15_780, 0)
ok(inc0 / 0.025, 631_200, 0)
ok(-cost0 + inc0 / 0.025, 276_620, 0)
cost18 = 91 * 3_850 + 47 * (4_100 - 3_850); ok(47 * 250, 11_750, 0); ok(cost18, 362_100, 0)
need = 0.025 * cost18; ok(need, 9_052.5, 1)
ok(169_400 + need, 178_452.5, 1)
m18 = (169_400 + need) / 4_100; ok(m18, 43.525, 3)
p18 = 47 + m18; ok(p18, 90.525, 3)
npv18 = -cost18 + ((p18 - 47) * 4_100 - 169_400) / 0.025; ok(npv18, 0, 6)

# 15. Higgins 3.13 + 3.14 Toys-4-Kids ($ thousands)
S = [300, 375, 3_200, 5_000]; A = sum(S); ok(A, 8_875, 0)
t = 0.40; ok(188 / 470, t, 2)
# seasonal (book table, unrounded)
cogs_s = [0.70 * x for x in S]
pbt_s = [S[i] - cogs_s[i] - 560 for i in range(4)]
pat_s = [(1 - t) * x for x in pbt_s]
ok(sum(pat_s), 253.5, 1)
eq_s = []; e = 3_000
for x in pat_s:
    e += x; eq_s.append(e)
for c, p in zip(eq_s, [2_718, 2_449.5, 2_689.5, 3_253.5]):
    ok(c, p, 1)
ok(2_960 - (225 + 500 + 1_000), 1_235, 0)
efr_s = []
for i in range(4):
    assets = 200 + 0.75 * S[i] + 500 + 1_000
    le = 0.10 * S[i] + t * pbt_s[i] + 400 + eq_s[i]
    efr_s.append(assets - le)
ok(efr_s[0], -1_035, 0); ok(efr_s[1], -727, 0)  # negative -> excess cash
ok(efr_s[2], 530.5, 1); ok(efr_s[3], 920.5, 1)
# level production
cogs = [0.65 * x for x in S]
for c, p in zip(cogs, [195, 243.75, 2_080, 3_250]):
    ok(c, p, 2)
ac = sum(cogs); ok(ac, 5_768.75, 2)
qp = ac / 4; ok(qp, 1_442.1875, 4)
inv = 500; invs = []
for c in cogs:
    inv = inv + qp - c; invs.append(inv)
for c, p in zip(invs, [1_747.1875, 2_945.625, 2_307.8125, 500]):
    ok(c, p, 4)
gp = [S[i] - cogs[i] for i in range(4)]
for c, p in zip(gp, [105, 131.25, 1_120, 1_750]):
    ok(c, p, 2)
pbt = [g - 560 for g in gp]
for c, p in zip(pbt, [-455, -428.75, 560, 1_190]):
    ok(c, p, 2)
tax = [t * x for x in pbt]
for c, p in zip(tax, [-182, -171.5, 224, 476]):
    ok(c, p, 2)
pat = [x - y for x, y in zip(pbt, tax)]
for c, p in zip(pat, [-273, -257.25, 336, 714]):
    ok(c, p, 2)
ok(sum(pat), 519.75, 2)
ok(sum(pat) - sum(pat_s), 266.25, 2)
ok(0.05 * A, 443.75, 2); ok(0.05 * A * (1 - t), 266.25, 2)
apl = 0.10 * A / 4; ok(A / 4, 2_218.75, 2); ok(apl, 221.875, 3)
eq = []; e = 3_000
for x in pat:
    e += x; eq.append(e)
for c, p in zip(eq, [2_727, 2_469.75, 2_805.75, 3_519.75]):
    ok(c, p, 2)
ar = [0.75 * x for x in S]
ta, le, efr = [], [], []
for i in range(4):
    ta.append(200 + ar[i] + invs[i] + 1_000)
    le.append(apl + tax[i] + 400 + eq[i])
    efr.append(ta[i] - le[i])
for c, p in zip(ta, [3_172.1875, 4_426.875, 5_907.8125, 5_450]):
    ok(c, p, 4)
for c, p in zip(le, [3_166.875, 2_920.125, 3_651.625, 4_617.625]):
    ok(c, p, 3)
for c, p in zip(efr, [5.3125, 1_506.75, 2_256.1875, 832.375]):
    ok(c, p, 4)
for c, p in zip([apl + x for x in tax], [39.875, 50.375, 445.875, 697.875]):
    ok(c, p, 3)
ok(efr[3] - efr_s[3], -88.125, 3)
ok((1_000 + 3_519.75) - 0, 4_519.75, 2)
d = [efr[0] - 0, efr[1] - 0, efr[2] - efr_s[2], efr[3] - efr_s[3]]
for c, p in zip(d, [5.3125, 1_506.75, 1_725.6875, -88.125]):
    ok(c, p, 4)
avg = sum(d) / 4; ok(sum(d), 3_149.625, 3); ok(avg, 787.40625, 5)
ok(0.05 * A / avg * 100, 56.36, 2)
for c, p in zip([invs[i] - 500 for i in range(4)], [1_247.1875, 2_445.625, 1_807.8125, 0]):
    ok(c, p, 4)
ok(efr[2] / (ar[2] + invs[2]), 0.4792, 4)
ok(ar[2] + invs[2], 4_707.8125, 4)
ok(efr[1] / (ar[1] + invs[1]), 0.4669, 4)
ok(ar[1] + invs[1], 3_226.875, 3)

# extra figures quoted in the prose
ok(56_384 / Y, 154, 0)                         # Ex 2 daily COGS
ok(2_000_000 / (20_000_000 / Y), 36.5, 1)      # Ex 5 pitfall (sales basis)
ok(3_950 / (20_000 / Y), 72, 0)                # Ex 6 pitfall (COGS basis)
ok((1.87 - 1.6) / 0.029, 9.31, 2)              # Ex 10 value of a customer per engine
ok(200 + 225 + 500 + 1_000, 1_925, 0)          # Ex 15 base Q1 assets at minimum cash
ok(225 + 500 + 1_000, 1_725, 0)
ok(476 - 376, 100, 0)                          # Ex 15 higher accrued taxes in Q4
ok(500 - 221.875, 278.125, 3)

print(f"PASS {n} checks")
