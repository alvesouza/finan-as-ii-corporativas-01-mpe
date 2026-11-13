"""Numeric checks for Listas/lista-r2c-financial-planning-forecasting-solutions.tex and -solutions-short.tex.

Run: python -I Listas/lista-r2c-financial-planning-forecasting-solutions_check.py  -> PASS <n> checks
Default tolerance 1e-6 absolute. Values printed rounded in the PDFs are checked with the
tolerance of their rounding (0.5 of the last printed digit, stated per call).
"""

N = 0


def chk(label, got, want, tol=1e-6):
    """Assert |got - want| <= tol (absolute); count the check."""
    global N
    assert abs(got - want) <= tol, f"{label}: got {got!r}, want {want!r} (tol {tol})"
    N += 1


def ok(label, cond):
    """Assert a boolean condition; count the check."""
    global N
    assert cond, label
    N += 1


# --- Ex 1: Berk 18.1
chk("1 COGS share", 72000 / 100000, 0.72)
chk("1 COGS forecast", 0.72 * 110000, 79200)

# --- Ex 2: Higgins 3.1 + 3.4 (illustrations)
chk("2 cash after plug", 100 + 40, 140)
chk("2 balance after plug", 900 + 140, 1040)
chk("2a AR up 50 -> EFN up 50", (1000 + 50 - 1040) - (1000 - 1040), 50)

# --- Ex 3: Ross 4.1 + 4.2
s, c = 23000 * 1.15, 16700 * 1.15
chk("3 sales", s, 26450)
chk("3 costs", c, 19205)
chk("3 NI", s - c, 7245)
chk("3 assets", 15800 * 1.15, 18170)
chk("3 debt", 5200 * 1.15, 5980)
chk("3 equity", 10600 * 1.15, 12190)
chk("3 equity change", 12190 - 10600, 1590)
chk("3 dividends plug", 7245 - 1590, 5655)
chk("3 equity if no dividend", 10600 + 7245, 17845)
chk("3.2 dividends", 0.5 * 7245, 3622.5)
chk("3.2 equity", 10600 + 3622.5, 14222.5)
chk("3.2 L&E", 5200 + 14222.5, 19422.5)
chk("3.2 EFN", 18170 - 19422.5, -1252.5)

# --- Ex 4: Berk 18.16
chk("4a ROA", 50000 / 400000, 0.125)
chk("4b ROE", 50000 / 250000, 0.20)
chk("4c SGR 40% payout", 0.20 * 0.6, 0.12)

# --- Ex 5: Higgins 3.5
chk("5a NFA", 2000 + 500 - 260, 2240)
chk("5b equity", 2950 + 156 * 0.5, 3028)
chk("5c TA", 2750 + 2240, 4990)
chk("5c L&E", 1155 + 500 + 3028, 4683)
chk("5c EFN", 4990 - 4683, 307)

# --- Ex 6: Berk 18.2 + 18.3
chk("6 retained", 50000 * 0.9, 45000)
chk("6 equity end", 300000 + 45000, 345000)
chk("6 liabilities end", 120000 + 10000, 130000)
chk("6 L&E", 130000 + 345000, 475000)
chk("6 NNF", 500000 - 475000, 25000)
chk("6.3 nondebt liab beg", 120000 - 100000, 20000)
chk("6.3 nondebt liab end", 20000 + 10000, 30000)
chk("6.3 D+E end", 500000 - 30000, 470000)
chk("6.3 D/E", 100000 / 300000, 1 / 3)
chk("6.3 E end", 470000 * 3 / 4, 352500)
chk("6.3 D end", 470000 / 4, 117500)
chk("6.3 equity issue", 352500 - 345000, 7500)
chk("6.3 debt issue", 117500 - 100000, 17500)
chk("6.3 sum", 7500 + 17500, 25000)

# --- Ex 7: Ross 4.9-4.11
b7 = 7736 / 12936
chk("7 retention", b7, 0.598021, 5e-7)
chk("7 payout", 5200 / 12936, 0.401979, 5e-7)
s, c = 38000 * 1.2, 18400 * 1.2
chk("7.9 sales", s, 45600)
chk("7.9 costs", c, 22080)
chk("7.9 EBT", s - c, 23520)
chk("7.9 tax", 0.34 * 23520, 7996.8)
chk("7.9 NI", 23520 - 7996.8, 15523.2)
chk("7.9 NI = 1.2 x", 12936 * 1.2, 15523.2)
chk("7.9 dividends", 15523.2 * (1 - b7), 6240)
chk("7.9 addition RE", 15523.2 * b7, 9283.2)
for name, v, pct in [("cash", 3050, 8.03), ("AR", 6900, 18.16), ("inv", 7600, 20.00),
                     ("CA", 17550, 46.18), ("FA", 34500, 90.79), ("TA", 52050, 136.97),
                     ("AP", 1300, 3.42)]:
    chk(f"7.10 {name} % of sales", 100 * v / 38000, pct, 5e-3)
s, c = 38000 * 1.15, 18400 * 1.15
chk("7.11 sales", s, 43700)
chk("7.11 costs", c, 21160)
chk("7.11 EBT", s - c, 22540)
chk("7.11 tax", 0.34 * 22540, 7663.6)
chk("7.11 NI", 22540 - 7663.6, 14876.4)
chk("7.11 dividends", 14876.4 * (1 - b7), 5980)
chk("7.11 addition RE", 14876.4 * b7, 8896.4)
chk("7.11 cash", 3050 * 1.15, 3507.5)
chk("7.11 AR", 6900 * 1.15, 7935)
chk("7.11 inv", 7600 * 1.15, 8740)
chk("7.11 CA", 3507.5 + 7935 + 8740, 20182.5)
chk("7.11 FA", 34500 * 1.15, 39675)
chk("7.11 TA", 20182.5 + 39675, 59857.5)
chk("7.11 AP", 1300 * 1.15, 1495)
chk("7.11 CL", 1495 + 6800, 8295)
chk("7.11 RE", 3950 + 8896.4, 12846.4)
chk("7.11 equity", 15000 + 12846.4, 27846.4)
chk("7.11 L&E", 8295 + 25000 + 27846.4, 61141.4)
chk("7.11 EFN", 59857.5 - 61141.4, -1283.9)

# --- Ex 8: Berk 18.8-18.11 (Global, $ millions)
g = 1.08
s, c, d = 186.7 * g, 175.1 * g, 1.2 * g
chk("8 sales", s, 201.636)
chk("8a costs", c, 189.108)
chk("8b dep", d, 1.296)
chk("8 dep % sales", 100 * 1.2 / 186.7, 0.6427, 5e-5)
chk("8 EBITDA", s - c, 12.528)
chk("8 EBIT", s - c - d, 11.232)
chk("8 pretax", 11.232 - 7.7, 3.532)
tr = 0.7 / 2.7
chk("8 tax rate", tr, 0.259259, 5e-7)
chk("8 tax", 3.532 * tr, 0.915704, 5e-7)
ni8 = 3.532 * (1 - tr)
chk("8c NI", ni8, 2.616296, 5e-7)
chk("8d cash", 23.2 * g, 25.056)
chk("8e AR", 18.5 * g, 19.98)
chk("8f inv", 15.3 * g, 16.524)
chk("8 CA", 57 * g, 61.56)
chk("8g PPE", 113.1 * g, 122.148)
chk("8 TA", 170.1 * g, 183.708)
chk("8h AP", 34.7 * g, 37.476)
chk("9 retained", 0.5 * ni8, 1.308148, 5e-7)
e9 = 22.2 + 0.5 * ni8
chk("9 equity", e9, 23.508148, 5e-7)
le = 37.476 + 113.2 + e9
chk("10 L&E", le, 174.184148, 5e-7)
chk("10 NNF", 183.708 - le, 9.523852, 5e-7)
need = 183.708 - 37.476 - 113.2 - 22.2 - 9
chk("11 min retained", need, 1.832)
chk("11 retention min", need / ni8, 0.700227, 5e-7)
chk("11 payout max", 1 - need / ni8, 0.299773, 5e-7)
chk("11 dividends max", ni8 - need, 0.784296, 5e-7)
chk("11 gap", 9.523852 - 9, 0.523852, 1e-6)

# --- Ex 9: Berk 18.17-18.19
sales = [74889, 88369, 103247, 119793, 138167, 158546]
ni = [6941, 7600, 8807, 11141, 13739, 16627]
beq = [69275, 74134, 76948, 83252, 90156, 97729]
div = [2082, 4786, 2503, 4237, 6167, 8313]
growth = [100 * (sales[k] / sales[k - 1] - 1) for k in range(1, 6)]
for k, w in zip(range(5), [18.00, 16.84, 16.03, 15.34, 14.75]):
    chk(f"9.17 sales growth {2011 + k}", growth[k], w, 5e-3)
sgr = [100 * (ni[k] - div[k]) / beq[k] for k in range(1, 6)]
for k, w in zip(range(5), [3.80, 8.19, 8.29, 8.40, 8.51]):
    chk(f"9.17 SGR {2011 + k}", sgr[k], w, 5e-3)
roe = [100 * ni[k] / beq[k] for k in range(1, 6)]
for k, w in zip(range(5), [10.25, 11.45, 13.38, 15.24, 17.01]):
    chk(f"9.17 ROE (max SGR) {2011 + k}", roe[k], w, 5e-3)
ok("9.17 growth > SGR every year", all(growth[k] > sgr[k] for k in range(5)))
ok("9.17 growth > ROE 2011-2014 only", all(growth[k] > roe[k] for k in range(4)) and growth[4] < roe[4])
chk("9.17 retained 2011", 7600 - 4786, 2814)
chk("9.17 2010 SGR at 30% payout", 100 * 6941 / 69275 * 0.7, 7.01, 5e-3)
chk("9.17 D/E 2010", 100 * 4500 / 74134, 6.07, 5e-3)
chk("9.17 D/E 2011", 100 * 24500 / 76948, 31.84, 5e-3)
chk("9.18 SGR", 0.12 * 0.75, 0.09)
chk("9.18 retained", 600000 * 0.12 * 0.75, 54000)
chk("9.18 new debt", 400000 * 0.09, 36000)
chk("9.18 D/E check", (400000 + 36000) / (600000 + 54000), 400000 / 600000)
chk("9.19 ROA", 20000 / 400000, 0.05)
chk("9.19 retention", 15000 / 20000, 0.75)
chk("9.19 IGR", 0.05 * 0.75, 0.0375)
chk("9.19 assets", 400000 * 1.0375, 415000)
chk("9.19 equity", 300000 + 15000, 315000)
chk("9.19 D/E new", 100000 / 315000, 0.31746, 5e-6)
chk("9.19 D/E old", 100000 / 300000, 0.33333, 5e-6)

# --- Ex 10: Higgins 4.8 (g* = P R A T)
P = [5.5, 6.4, 6.6, 7.0, 7.0]
A = [1.6, 1.6, 1.6, 1.6, 1.5]
T = [1.7, 1.7, 1.9, 1.8, 1.9]
gs = [p * a * t for p, a, t in zip(P, A, T)]
for k, w in zip(range(5), [14.96, 17.408, 20.064, 20.16, 19.95]):
    chk(f"10a g* {2009 + k}", gs[k], w, 1e-9)
actual = [18.1, 24.2, 38.4, 24.6, 27.1]
ok("10b actual > g* every year", all(a > s for a, s in zip(actual, gs)))
chk("10b gap 2011", 38.4 - 20.064, 18.336, 1e-9)
chk("10d P = 8%", 8.0 * 1.5 * 1.9, 22.8, 1e-9)
chk("10d T = 2.4", 7.0 * 1.5 * 2.4, 25.2, 1e-9)
chk("10d both", 8.0 * 1.5 * 2.4, 28.8, 1e-9)
ok("10d both exceeds actual 27.1", 28.8 > 27.1)

# --- Ex 11: Ross 4.25-4.27 (Turismo da Onca)
tr11, p11 = 60550 / 173000, 33735 / 112450
chk("11 tax rate", tr11, 0.35)
chk("11 payout", p11, 0.30)


def onca(g):
    """Pro forma income lines of Turismo da Onca at sales growth g (interest fixed)."""
    s = 929000 * (1 + g)
    cst, oth = 723000 * (1 + g), 19000 * (1 + g)
    ebit = s - cst - oth
    ebt = ebit - 14000
    tax = tr11 * ebt
    ni = ebt - tax
    return s, cst, oth, ebit, ebt, tax, ni, p11 * ni, ni - p11 * ni


s, cst, oth, ebit, ebt, tax, ni11, dv, add = onca(0.2)
chk("11 sales", s, 1114800)
chk("11 costs", cst, 867600)
chk("11 other", oth, 22800)
chk("11 EBIT", ebit, 224400)
chk("11 EBT", ebt, 210400)
chk("11 tax", tax, 73640)
chk("11 NI", ni11, 136760)
chk("11 div", dv, 41028)
chk("11 add RE", add, 95732)
chk("11 cash", 25300 * 1.2, 30360)
chk("11 AR", 40700 * 1.2, 48840)
chk("11 inv", 86900 * 1.2, 104280)
chk("11 CA", 152900 * 1.2, 183480)
chk("11 FA", 413000 * 1.2, 495600)
chk("11 TA", 183480 + 495600, 679080)
chk("11 AP", 68000 * 1.2, 81600)
chk("11 CL", 81600 + 17000, 98600)
chk("11 RE", 182900 + 95732, 278632)
chk("11 equity", 140000 + 278632, 418632)
chk("11 L&E", 98600 + 158000 + 418632, 675232)
chk("11.25 EFN", 679080 - 675232, 3848)
chk("11.26 full-capacity sales", 929000 / 0.8, 1161250)
ok("11.26 projected sales below capacity", 1114800 < 1161250)
chk("11.26 TA", 183480 + 413000, 596480)
chk("11.26 EFN", 596480 - 675232, -78752)
de = (85000 + 158000) / 322900
chk("11.27 D/E", de, 0.752555, 5e-7)
D = de * 418632
chk("11.27 total debt allowed", D, 315043.59, 5e-3)
chk("11.27 L&E", 418632 + D, 733675.59, 5e-3)
chk("11.27 EFN", 679080 - 418632 - D, -54595.59, 5e-3)
chk("11.27 spontaneous+old liabilities", 81600 + 17000 + 158000, 256600)
chk("11.27 extra borrowing room", D - 256600, 58443.59, 5e-3)
chk("11.27 decomposition", 3848 - 58443.59, -54595.59, 5e-3)

# --- Ex 12: Higgins 3.9 (and 3.8)


def rande(base_sales, eq0, g, cogs, ca, sga=0.11, ltd=560, cpltd=100, cl=0.144, nfa=270,
          floor=False):
    """2023 forecast of R&E Supplies; EFN solved from the circular interest equation in closed form."""
    s = base_sales * (1 + g)
    gp = s * (1 - cogs)
    ga = sga * s
    ta = ca * s + nfa
    cls = cl * s
    keep = 0.75 * (1.0 if floor else 0.5)   # (1 - tax) x retention
    k = ta - cls - ltd - eq0 - keep * (gp - ga - 0.1 * (ltd + cpltd))
    x = k / (1 - keep * 0.1)
    i = 0.1 * (ltd + cpltd + x)
    ebt = gp - ga - i
    eat = 0.75 * ebt
    dv = 0 if floor else 0.5 * eat
    add = eat - dv
    return dict(s=s, cogs=s * cogs, gp=gp, sga=ga, i=i, ebt=ebt, tax=0.25 * ebt, eat=eat,
                div=dv, add=add, ca=ca * s, ta=ta, cl=cls, eq=eq0 + add,
                le=cls + ltd + eq0 + add, x=x, k=k)


# 2022 row from Table 3.5 (unrounded spreadsheet values)
r22 = rande(20613, 1730, 0.25, 0.86, 0.29, sga=0.12, ltd=660, cpltd=100, cl=0.145, nfa=280)
chk("12 2022 sales", r22["s"], 25766.25)
chk("12 2022 EFN (Table 3.5)", r22["x"], 1518, 0.5)
chk("12 2022 interest", r22["i"], 228, 0.5)
chk("12 2022 add RE", r22["add"], 107.81, 5e-3)
chk("12 2022 equity", r22["eq"], 1837.81, 5e-3)
chk("12 2022 EFN 2dp", r22["x"], 1518.30, 5e-3)
s22, e22 = r22["s"], r22["eq"]
ra = rande(s22, e22, 0.30, 0.86, 0.29)
for key, w in [("s", 33496.13), ("cogs", 28806.67), ("gp", 4689.46), ("sga", 3684.57),
               ("ca", 9713.88), ("ta", 9983.88), ("cl", 4823.44)]:
    chk(f"12a {key}", ra[key], w, 5e-3)
chk("12a K", ra["k"], 2410.54, 5e-3)
chk("12a EFN", ra["x"], 2504.46, 5e-3)
chk("12a interest", ra["i"], 316.45, 5e-3)
chk("12a EBT", ra["ebt"], 688.44, 5e-3)
chk("12a tax", ra["tax"], 172.11, 5e-3)
chk("12a EAT", ra["eat"], 516.33, 5e-3)
chk("12a div", ra["div"], 258.16, 5e-3)
chk("12a equity", ra["eq"], 2095.975, 1e-3)
chk("12a L&E", ra["le"], 7479.42, 5e-3)
chk("12a EFN = TA - L&E", ra["ta"] - ra["le"], ra["x"], 1e-6)
chk("12a book 2,504", ra["x"], 2504, 0.5)
chk("12a vs 2022", ra["x"] - r22["x"], 986.16, 5e-3)
rb = rande(s22, e22, 0.30, 0.84, 0.29)
chk("12b gp", rb["gp"], 5359.38, 5e-3)
chk("12b K", rb["k"], 2159.32, 5e-3)
chk("12b EFN", rb["x"], 2243.45, 5e-3)
chk("12b book 2,243", rb["x"], 2243, 0.5)
chk("12b change", rb["x"] - ra["x"], -261.01, 5e-3)
chk("12b change %", 100 * (rb["x"] / ra["x"] - 1), -10.42, 5e-3)
rc = rande(s22, e22, -0.05, 0.88, 0.35)
for key, w in [("s", 24477.94), ("cogs", 21540.59), ("gp", 2937.35), ("sga", 2692.57),
               ("ca", 8567.28), ("ta", 8837.28), ("cl", 3524.82)]:
    chk(f"12c {key}", rc[key], w, 6e-3)
chk("12c K", rc["k"], 2847.60, 5e-3)
chk("12c EFN", rc["x"], 2958.55, 5e-3)
chk("12c interest", rc["i"], 361.85, 5e-3)
chk("12c EBT", rc["ebt"], -117.08, 5e-3)
chk("12c EAT", rc["eat"], -87.81, 5e-3)
chk("12c div (mechanical)", rc["div"], -43.90, 5e-3)
chk("12c book 2,959", rc["x"], 2959, 0.5)
chk("12c change %", 100 * (rc["x"] / ra["x"] - 1), 18.13, 5e-3)
rf = rande(s22, e22, -0.05, 0.88, 0.35, floor=True)
chk("12c EFN with zero dividend", rf["x"], 3006.01, 5e-3)
chk("12c EAT with zero dividend", rf["eat"], -91.37, 5e-3)

# --- Ex 13: Ross 4.31-4.33 (identities checked at the chapter's Hoffman numbers)
V, A_, NI_, b = 500.0, 500.0, 66.0, 2 / 3
ML = NI_ / V
for gg in (0.0, 0.05, 0.25):
    efn_direct = A_ * gg - ML * V * b * (1 + gg)
    efn_formula = -ML * V * b + (A_ - ML * V * b) * gg
    chk(f"13 NAF identity g={gg}", efn_direct, efn_formula, 1e-9)
roa = NI_ / A_
igr = ML * V * b / (A_ - ML * V * b)
chk("13 IGR = ROA b/(1-ROA b)", igr, roa * b / (1 - roa * b), 1e-12)
chk("13 Hoffman IGR", 100 * igr, 9.65, 5e-3)
P_ = 250.0
sgr = (1 + (A_ - P_) / P_) * ML * V * b / (A_ - (1 + (A_ - P_) / P_) * ML * V * b)
roe_ = NI_ / P_
chk("13 SGR = ROE b/(1-ROE b)", sgr, roe_ * b / (1 - roe_ * b), 1e-12)
chk("13 Hoffman SGR", 100 * sgr, 21.36, 5e-3)
Pb, NIx, bx = 80.0, 20.0, 0.6
Pe = Pb + bx * NIx
re_ = NIx / Pe
chk("13.33 end ROE formula = beg ROE x b", re_ * bx / (1 - re_ * bx), NIx / Pb * bx, 1e-12)
chk("13.33 ross example 15%", NIx / Pb * bx, 0.15, 1e-12)
Ab = 100.0
Ae = Ab + bx * NIx
ra_ = NIx / Ae
chk("13.33 end ROA formula = beg ROA x b", ra_ * bx / (1 - ra_ * bx), NIx / Ab * bx, 1e-12)
chk("13.33 ross example IGR 12%", NIx / Ab * bx, 0.12, 1e-12)

# --- Ex 14: Ross 4.28-4.29


def efn25(gg):
    """NAF of Problem 25 (no new debt or equity) at growth gg."""
    return 565900 * (1 + gg) - (68000 * (1 + gg) + 17000 + 158000 + 322900 + onca(gg)[8])


def efn27(gg):
    """NAF of Problem 27 (constant total-debt/equity) at growth gg."""
    return 565900 * (1 + gg) - (322900 + onca(gg)[8]) * (1 + de)


keep = (1 - p11) * (1 - tr11)
chk("14 keep factor", keep, 0.455)
chk("14 slope 25", 565900 - 68000 - keep * 187000, 412815)
chk("14 const 25", 17000 + 158000 + 322900 - keep * 14000, 491530)
for gg, w, a in [(0.15, -16792.75, 91477.75), (0.20, 3848.0, 95732.0), (0.25, 24488.75, 99986.25)]:
    chk(f"14.28 EFN g={gg}", efn25(gg), w, 1e-6)
    chk(f"14.28 add RE g={gg}", onca(gg)[8], a, 1e-6)
g28 = 491530 / 412815 - 1
chk("14.28 zero-NAF growth", 100 * g28, 19.07, 5e-3)
chk("14.28 efn at root", efn25(g28), 0, 1e-6)
roa14 = 112450 / 565900
chk("14.28 ROA", 100 * roa14, 19.87, 5e-3)
chk("14.28 ROA b", 0.7 * roa14, 0.139097, 5e-7)
chk("14.28 formula IGR", 100 * 0.7 * roa14 / (1 - 0.7 * roa14), 16.16, 5e-3)
chk("14.28 formula = 78715/(565900-78715)", 78715 / (565900 - 78715), 0.7 * roa14 / (1 - 0.7 * roa14), 1e-12)
chk("14.28 with spontaneous AP only", 100 * 78715 / (565900 - 68000 - 78715), 18.78, 5e-3)
slope27 = 565900 - (1 + de) * keep * 187000
const27 = (1 + de) * (322900 - keep * 14000)
chk("14.29 (1+D/E)", 1 + de, 1.752555, 5e-7)
chk("14.29 slope", slope27, 416783.86, 5e-3)
chk("14.29 const", const27, 554736.22, 5e-3)
for gg, w, a in [(0.20, -54595.59, 95732.0), (0.30, -12917.21, 104240.5), (0.35, 7921.99, 108494.75)]:
    chk(f"14.29 EFN g={gg}", efn27(gg), w, 5e-3)
    chk(f"14.29 add RE g={gg}", onca(gg)[8], a, 1e-6)
g29 = const27 / slope27 - 1
chk("14.29 zero-NAF growth", 100 * g29, 33.10, 5e-3)
chk("14.29 efn at root", efn27(g29), 0, 1e-6)
roe14 = 112450 / 322900
chk("14.29 ROE", 100 * roe14, 34.83, 5e-3)
chk("14.29 ROE b", 0.7 * roe14, 0.243775, 5e-7)
chk("14.29 formula SGR", 100 * 0.7 * roe14 / (1 - 0.7 * roe14), 32.24, 5e-3)
chk("14.29 formula via (1+D/E)78715", (1 + de) * 78715 / (565900 - (1 + de) * 78715),
    0.7 * roe14 / (1 - 0.7 * roe14), 1e-12)
chk("14.29 (1+D/E) x 78715", (1 + de) * 78715, 137952.36, 5e-3)

# --- Ex 15: Berk 18.12-18.15 and 18.20-18.22 (KMS, 0.25%/yr share growth, $000s)
mkt = [10000, 10500, 11025, 11576, 12155, 12763]
shr = [0.10, 0.1025, 0.105, 0.1075, 0.11, 0.1125]
prc = [74.89, 76.51, 78.04, 79.60, 81.19, 82.82]
vol = [m * q for m, q in zip(mkt, shr)]
for k, w in enumerate([1000, 1076.25, 1157.625, 1244.42, 1337.05, 1435.8375]):
    chk(f"15.12 volume {2010 + k}", vol[k], w, 1e-6)
ok("15.12 first year above 1100 is 2012", vol[1] <= 1100 < vol[2])
interest = [306, 306, 306, 1666, 1666, 1666]
chk("15.13 coupon on 4,500", 0.068 * 4500, 306)
chk("15.13 coupon on 24,500", 0.068 * 24500, 1666)
its = [0.35 * i for i in interest]
chk("15.13 ITS small", its[1], 107.1)
chk("15.13 ITS large", its[3], 583.1)
sales15 = [74889] + [vol[k] * prc[k] for k in range(1, 6)]
for k, w in enumerate([74889, 82343.9, 90341.1, 99055.8, 108555.1, 118916.1]):
    chk(f"15.14 sales {2010 + k}", sales15[k], w, 0.05)
dep = [5492, 5443, 7398, 7459, 7513, 7561]
cost15 = [58413] + [0.78 * x for x in sales15[1:]]
ebitda = [x - y for x, y in zip(sales15, cost15)]
ebit = [x - y for x, y in zip(ebitda, dep)]
pti = [x - y for x, y in zip(ebit, interest)]
tax15 = [0.35 * x for x in pti]
ni15 = [x - y for x, y in zip(pti, tax15)]
for k, w in enumerate([58413, 64228.2, 70466.0, 77263.5, 84673.0, 92754.5]):
    chk(f"15.14 costs {2010 + k}", cost15[k], w, 0.05)
for k, w in enumerate([16476, 18115.7, 19875.0, 21792.3, 23882.1, 26161.5]):
    chk(f"15.14 EBITDA {2010 + k}", ebitda[k], w, 0.05)
for k, w in enumerate([10984, 12672.7, 12477.0, 14333.3, 16369.1, 18600.5]):
    chk(f"15.14 EBIT {2010 + k}", ebit[k], w, 0.05)
for k, w in enumerate([10678, 12366.7, 12171.0, 12667.3, 14703.1, 16934.5]):
    chk(f"15.14 pretax {2010 + k}", pti[k], w, 0.05)
for k, w in enumerate([3737.3, 4328.3, 4259.9, 4433.5, 5146.1, 5927.1]):
    chk(f"15.14 tax {2010 + k}", tax15[k], w, 0.05)
for k, w in enumerate([6940.7, 8038.3, 7911.2, 8233.7, 9557.0, 11007.4]):
    chk(f"15.14 NI {2010 + k}", ni15[k], w, 0.05)
cash = [11982] + [0.16 * x for x in sales15[1:]]
ar = [14229] + [0.19 * x for x in sales15[1:]]
inv = [14978] + [0.20 * x for x in sales15[1:]]
ap = [11982] + [0.16 * x for x in sales15[1:]]
tca = [a + b_ + c_ for a, b_, c_ in zip(cash, ar, inv)]
nwc = [x - y for x, y in zip(tca, ap)]
dnwc = [nwc[k] - nwc[k - 1] for k in range(1, 6)]
for k, w in enumerate([11982, 13175.0, 14454.6, 15848.9, 17368.8, 19026.6]):
    chk(f"15.15 cash/AP {2010 + k}", cash[k], w, 0.05)
for k, w in enumerate([14229, 15645.3, 17164.8, 18820.6, 20625.5, 22594.1]):
    chk(f"15.15 AR {2010 + k}", ar[k], w, 0.05)
for k, w in enumerate([14978, 16468.8, 18068.2, 19811.2, 21711.0, 23783.2]):
    chk(f"15.15 inv {2010 + k}", inv[k], w, 0.05)
for k, w in enumerate([41189, 45289.1, 49687.6, 54480.7, 59705.3, 65403.8]):
    chk(f"15.15 TCA {2010 + k}", tca[k], w, 0.05)
for k, w in enumerate([29207, 32114.1, 35233.0, 38631.8, 42336.5, 46377.3]):
    chk(f"15.15 NWC {2010 + k}", nwc[k], w, 0.05)
for k, w in enumerate([2907.1, 3118.9, 3398.8, 3704.7, 4040.8]):
    chk(f"15.15 dNWC {2011 + k}", dnwc[k], w, 0.05)
chk("15.15 NWC share of sales", 0.16 + 0.19 + 0.20 - 0.16, 0.39)
capex = [5000, 5000, 25000, 8000, 8000, 8000]
ati = [0.65 * i for i in interest]
chk("15.20 after-tax interest small", ati[1], 198.9)
chk("15.20 after-tax interest large", ati[3], 1082.9)
uni = [x + y for x, y in zip(ni15, ati)]
for k in range(6):
    chk(f"15.20 unlevered NI = 0.65 EBIT {2010 + k}", uni[k], 0.65 * ebit[k], 1e-6)
for k, w in enumerate([8237.2, 8110.1, 9316.6, 10639.9, 12090.3]):
    chk(f"15.20 unlevered NI {2011 + k}", uni[k + 1], w, 0.05)
fcf = [uni[k] + dep[k] - dnwc[k - 1] - capex[k] for k in range(1, 6)]
for k, w in enumerate([5773.1, -12610.8, 5376.9, 6448.2, 7610.6]):
    chk(f"15.20 FCF {2011 + k}", fcf[k], w, 0.05)
cv = 8.5 * ebitda[5]
chk("15.21 CV", cv, 222373.0, 0.05)
pv_fcf = [fcf[k] / 1.1 ** (k + 1) for k in range(5)]
for k, w in enumerate([5248.3, -10422.2, 4039.7, 4404.2, 4725.6]):
    chk(f"15.22 PV FCF {2011 + k}", pv_fcf[k], w, 0.05)
chk("15.22 sum PV FCF", sum(pv_fcf), 7995.6, 0.05)
chk("15.22 discount factor 1.1^5", 1.1 ** 5, 1.61051, 1e-9)
chk("15.22 PV CV", cv / 1.1 ** 5, 138076.2, 0.05)
pv_its = [its[k + 1] / 1.068 ** (k + 1) for k in range(5)]
for k, w in enumerate([100.3, 93.9, 478.7, 448.2, 419.6]):
    chk(f"15.22 PV ITS {2011 + k}", pv_its[k], w, 0.05)
chk("15.22 sum PV ITS", sum(pv_its), 1540.7, 0.05)
v15 = sum(pv_fcf) + cv / 1.1 ** 5 + sum(pv_its)
chk("15.22 firm value", v15, 147612.5, 0.05)
chk("15.22 vs chapter", 200974 - v15, 53361.5, 0.05)
chk("15.22 chapter at 8.5x", 4096 + 8.5 * 34880 / 1.1 ** 5 + 1958, 190144.8, 0.05)
chk("15.22 CV share of value", 100 * (cv / 1.1 ** 5) / v15, 93.54, 5e-3)

# --- Numbers quoted in intuitions, pitfalls and the Ex 14 plot
chk("4 leverage link", 12.5 * (400000 / 250000), 20)
chk("5 asset growth", 4990 - 4500, 490)
chk("5 payables growth", 1155 - 1050, 105)
chk("5 gap", 490 - 105 - 78, 307)
chk("7 asset need at 15%", 0.15 * 52050, 7807.5)
chk("7 payables add", 1495 - 1300, 195)
chk("7 net margin", 100 * 12936 / 38000, 34.0, 5e-2)
chk("8 new assets", 183.708 - 170.1, 13.608)
chk("8 dividend cut", 1.308148 - 0.784296, 0.523852, 1e-6)
chk("10 margin rise", 8.0 / 7.0 - 1, 0.142857, 5e-7)
chk("10 leverage rise", 2.4 / 1.9 - 1, 0.263158, 5e-7)
chk("10 joint rise", 28.8 / 19.95 - 1, 0.443609, 5e-7)
chk("11 idle capacity value", 495600 - 413000, 82600)
chk("11 utilization", 1114800 / 1161250, 0.96)
chk("12 interest on EFR", 0.0375 * ra["x"], 93.92, 5e-3)
chk("13 Ross end ROE", 20 / 92, 0.2174, 5e-5)
chk("13 pitfall end ROE in simple formula", 100 * 0.6 * 20 / 92, 13.0, 5e-2)
chk("13 pitfall beg ROE in [4.3]", 100 * 0.15 / 0.85, 17.6, 5e-2)
chk("14 slope per point 28", 412815 / 100, 4128.15)
chk("14 slope per point 29", slope27 / 100, 4167.84, 5e-3)
for gg, w in [(0.10, -37.4335), (0.40, 86.411)]:
    chk(f"14 plot 28 g={gg}", efn25(gg) / 1000, w, 5e-4)
for gg, w in [(0.10, -96.2741), (0.40, 28.7616)]:
    chk(f"14 plot 29 g={gg}", efn27(gg) / 1000, w, 5e-4)
chk("15 CV share of value", 100 * 138076.2 / 147612.5, 93.54, 5e-3)
chk("15 gap vs chapter at 8.5x", 190144.8 - 147612.5, 42532.3, 0.05)

print(f"PASS {N} checks")
