"""Check every number printed in lista-r1-accounting-capital-structure-solutions.tex.

Run: python -I Listas/lista-r1-accounting-capital-structure-solutions_check.py
Each printed value is recomputed from the statement data and compared with the value shown
in the PDF. Tolerance: half a unit in the last printed decimal (e.g. 0.3305 -> 5e-5), so the
assert fails if the displayed rounding is wrong. Prints "PASS <n> checks".
"""

n = 0


def ok(computed, printed, decimals):
    """Assert `computed` rounds to `printed` at `decimals` places (tolerance 0.5e-decimals)."""
    global n
    tol = 0.5 * 10 ** (-decimals) + 1e-9
    assert abs(computed - printed) <= tol, (computed, printed)
    n += 1


# 1. Higgins 1.4
ok(500_000 - 300_000, 200_000, 0)
ok(-0.40 * 80, -32, 0)
ok(0.60 * 80, 48, 0)
ok(80 - 32, 48, 0)
ok(60 - 60, 0, 0)
ok(-10_000 * 24, -240_000, 0)

# 2. Berk 2.12
S, C, SGA, RD, D, tau = 10, 6, 0.5, 1, 1, 0.35
GP = S - C; ok(GP, 4, 0); ok(GP / S, 0.40, 2)
OI = GP - SGA - RD - D; ok(OI, 1.5, 1); ok(OI / S, 0.15, 2)
NI = OI * (1 - tau); ok(NI, 0.975, 3); ok(NI / S, 0.0975, 4)

# 3. Berk 2.31
I, D, tau = 40, 10, 0.40
ok(-D * (1 - tau), -6, 0)
ok(tau * D, 4, 0)
ok(-I + tau * D, -36, 0)
ok(4 * (-D * (1 - tau)), -24, 0)
ok((-I + tau * D) + 3 * tau * D, -24, 0)

# 4. Berk 2.8
MC = 10.3 * 38; ok(MC, 391.4, 1)
ok(MC / 117, 3.345, 3)
ok(467 / 117, 3.991, 3)
ok(467 / MC, 1.193, 3)
ok(MC + 467 - 16, 842.4, 1)

# 5. Higgins 2.3 (b) counterexample
ok(-10 / 100, -0.10, 2); ok(-10 / 50, -0.20, 2)

# 6. Berk 2.21
ok(500 / 400, 1.25, 2); ok(80 / 40, 2.00, 2)
ok(500 / 300, 1.667, 3); ok(80 / 35, 2.286, 3)
ok(100 / 50, 2.00, 2); ok(8 / 7, 1.143, 3)
ok(1 / 8, 0.125, 3); ok(50 / 100, 0.50, 2)

# 7. Berk 2.27
EM = 44 / 18; ok(EM, 2.4444, 4)
ok(0.035 * 1.8 * EM, 0.1540, 4)
ok(1.8 * 44, 79.2, 1); ok(0.035 * 79.2, 2.772, 3); ok(2.772 / 18, 0.154, 3)
ok(0.04 * 1.8 * EM, 0.1760, 4)
ok(1.8 * 1.20, 2.16, 2)
ok(0.04 * 2.16 * EM, 0.2112, 4)
ok(79.2 * 1.2, 95.04, 2); ok(0.04 * 95.04, 3.8016, 4); ok(3.8016 / 18, 0.2112, 4)
ok(0.04 / 0.035, 1.143, 3); ok((0.04 / 0.035) * 1.2, 1.371, 3)

# 8. Higgins 2.7
r, t = 0.07, 0.30
for ebit, d, e, intr, ebt, ni, roe, roa, roic in [
    (450, 290, 910, 20.3, 429.7, 300.79, 0.3305, 0.2507, 0.2625),
    (470, 1490, 370, 104.3, 365.7, 255.99, 0.6919, 0.1376, 0.1769),
]:
    ok(r * d, intr, 1); ok(ebit - r * d, ebt, 1)
    NI = (ebit - r * d) * (1 - t); ok(NI, ni, 2)
    ok(NI / e, roe, 4); ok(NI / (d + e), roa, 4)
    ROIC = ebit * (1 - t) / (d + e); ok(ROIC, roic, 4)
    ok(ROIC + (ROIC - r * (1 - t)) * d / e, roe, 4)   # leverage identity (e8-lev)
    ok(100 * NI / e, round(100 * roe, 1), 1); ok(100 * NI / (d + e), round(100 * roa, 1), 1)
ok(r * (1 - t), 0.049, 3); ok(1490 / 370, 4.03, 2); ok(290 / 910, 0.32, 2)
ok(100 * 0.2625, 26.25, 2); ok(100 * 470 * 0.7 / 1860, 17.7, 1)
ok(1200, 290 + 910, 0); ok(1860, 1490 + 370, 0)

# 9. Ross 2.14
EBIT = 196_000 - 104_000 - 6_800 - 9_100; ok(EBIT, 76_100, 0)
OCF = EBIT + 9_100 - 21_455; ok(OCF, 63_745, 0)
CFC = 14_800 - (-7_300); ok(CFC, 22_100, 0)
CFS = 10_400 - 5_700; ok(CFS, 4_700, 0)
CFA = CFC + CFS; ok(CFA, 26_800, 0)
NCS = 27_000 + 9_100; ok(NCS, 36_100, 0)
ok(OCF - NCS - CFA, 845, 0)

# 10. Higgins 1.11
ok(782 - (87 - 57), 752, 0)
ok(502 + (29 - 39), 492, 0)
capex = (482 - 404) + 61; ok(capex, 139, 0)
ok((135 - 86) + capex, 188, 0)
ok(142 + 61 - (87 - 57) - (29 - 39) + (44 - 39), 188, 0)

# 11. Ross 2.21
EBIT = 22_800 - 16_050 - 4_050; ok(EBIT, 2_700, 0)
EBT = EBIT - 1_830; ok(EBT, 870, 0)
tax = 0.34 * EBT; ok(tax, 295.80, 2)
ok(EBT - tax, 574.20, 2)
OCF = EBIT + 4_050 - tax; ok(OCF, 6_454.20, 2)
NCS = (16_800 - 13_650) + 4_050; ok(NCS, 7_200, 0)
ok(5_930 - 3_150, 2_780, 0); ok(4_800 - 2_700, 2_100, 0)
dNWC = (5_930 - 3_150) - (4_800 - 2_700); ok(dNWC, 680, 0)
CFA = OCF - NCS - dNWC; ok(CFA, -1_425.80, 2)
ok(NCS + dNWC, 7_880, 0)
CFC = 1_830 - 0; ok(CFC, 1_830, 0)
CFS = CFA - CFC; ok(CFS, -3_255.80, 2)
ok(1_300 - CFS, 4_555.80, 2)

# 12. Berk *2.19 (Table 2.3, p. 34)
ok(10.4 / 186.7, 0.0557, 4)
ok(36 / 2.0, 18, 0); ok(18 * 2.0 / 3.6, 10, 0)
S1 = 186.7 * 1.15; ok(S1, 214.705, 3)
EBIT1 = 0.045 * S1; ok(EBIT1, 9.6617, 4)
tau09 = 0.6 / 2.5; ok(tau09, 0.24, 2)
EBT1 = EBIT1 - 7.7; ok(EBT1, 1.9617, 4)
NI1 = EBT1 * (1 - tau09); ok(NI1, 1.4909, 4)
ok(NI1 / 3.6, 0.41414, 5)
ok(18 * NI1 / 3.6, 7.45, 2)
tau10 = 0.7 / 2.7; ok(tau10, 0.25926, 5); ok(1 - tau10, 0.74074, 5)
NI1b = EBT1 * (1 - tau10); ok(NI1b, 1.4531, 4)
ok(18 * NI1b / 3.6, 7.27, 2)
ok(EBIT1 / 10.4 - 1, -0.071, 3)
ok(EBT1 / 2.7 - 1, -0.27, 2)
ok(1 - 0.045 / 0.0557, 0.19, 2)   # "margin down by a fifth" (about 19%)

# 13. Berk *2.23
NI0 = 0.80 * 6_500; ok(NI0, 5_200, 0)
dNI = -500 * (1 - 0.35); ok(dNI, -325, 0)
ok(dNI / 6_500, -0.05, 2); ok(0.80 + dNI / 6_500, 0.75, 2)
dN = 900 / 18; ok(dN, 50, 0)
EPSb = NI0 / (6_500 + dN); ok(EPSb, 0.7939, 4)
ok(EPSb - 0.80, -0.0061, 4)
ok(900 - 325, 575, 0)

# 14. Higgins 2.11
S = 365 * 1_100_000 / 34; ok(S, 11_808_824, 0)
AR = 71 * S / 365; ok(AR, 2_297_059, 0)
CA = 1_100_000 + AR + 1_900_000; ok(CA, 5_297_059, 0)
ok(8_000_000 - CA, 2_702_941, 0)
COGS = 5 * 1_900_000; ok(COGS, 9_500_000, 0)
AP = 36 * COGS / 365; ok(AP, 936_986, 0)
CL = CA / 2.6; ok(CL, 2_037_330, 0)
ok(CL - AP, 1_100_344, 0)
TL = 0.75 * 8_000_000; ok(TL, 6_000_000, 0)
ok(TL - CL, 3_962_670, 0)
ok(8_000_000 - TL, 2_000_000, 0)
ok(CL + (TL - CL) + (8_000_000 - TL), 8_000_000, 0)

# 15. Ross 2.25-2.26
EBIT8 = 7_233 - 2_487 - 591 - 1_038; ok(EBIT8, 3_117, 0)
EBT8 = EBIT8 - 485; ok(EBT8, 2_632, 0)
tax8 = 0.34 * EBT8; ok(tax8, 894.88, 2)
NI8 = EBT8 - tax8; ok(NI8, 1_737.12, 2)
ok(NI8 - 882, 855.12, 2)
EBIT9 = 8_085 - 2_942 - 515 - 1_085; ok(EBIT9, 3_543, 0)
EBT9 = EBIT9 - 579; ok(EBT9, 2_964, 0)
tax9 = 0.34 * EBT9; ok(tax9, 1_007.76, 2)
NI9 = EBT9 - tax9; ok(NI9, 1_956.24, 2)
RE9 = NI9 - 1_011; ok(RE9, 945.24, 2)
CA8 = 3_792 + 5_021 + 8_927; ok(CA8, 17_740, 0)
TA8 = CA8 + 31_805; ok(TA8, 49_545, 0)
CL8 = 3_984 + 732; ok(CL8, 4_716, 0)
E8 = TA8 - CL8 - 12_700; ok(E8, 32_129, 0)
CA9 = 4_041 + 5_892 + 9_555; ok(CA9, 19_488, 0)
TA9 = CA9 + 33_921; ok(TA9, 53_409, 0)
CL9 = 4_025 + 717; ok(CL9, 4_742, 0)
E9 = TA9 - CL9 - 15_435; ok(E9, 33_232, 0)
OCF = EBIT9 + 1_085 - tax9; ok(OCF, 3_620.24, 2)
NCS = (33_921 - 31_805) + 1_085; ok(NCS, 3_201, 0)
ok(CA9 - CL9, 14_746, 0); ok(CA8 - CL8, 13_024, 0)
dNWC = (CA9 - CL9) - (CA8 - CL8); ok(dNWC, 1_722, 0)
CFA = OCF - NCS - dNWC; ok(CFA, -1_302.76, 2)
ok(15_435 - 12_700, 2_735, 0)
CFC = 579 - (15_435 - 12_700); ok(CFC, -2_156, 0)
nne = (E9 - E8) - RE9; ok(nne, 157.76, 2)
CFS = 1_011 - nne; ok(CFS, 853.24, 2)
ok(CFC + CFS, CFA, 2)
ok(NCS + dNWC, 4_923, 0)

print(f"PASS {n} checks")
