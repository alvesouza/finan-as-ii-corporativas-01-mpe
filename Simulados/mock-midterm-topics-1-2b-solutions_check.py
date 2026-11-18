"""Check every number printed in mock-midterm-topics-1-2b-solutions.tex.

Run: python -I Simulados/mock-midterm-topics-1-2b-solutions_check.py
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


def annuity(r, T):
    """Present value of 1 per year for T years at rate r (first payment in one year)."""
    return (1 - (1 + r) ** -T) / r


# ---------------------------------------------------------------- Q1.1 Berk 2.24 ($ billion)
mc = {"AA": 1.7, "BA": 2.2}
debt = {"AA": 11.1, "BA": 4.7}
cash = {"AA": 4.6, "BA": 2.6}
rev = {"AA": 23.8, "BA": 13.1}
ev = {k: mc[k] + debt[k] - cash[k] for k in mc}
check(mc["AA"] / rev["AA"], 0.0714, 5e-5)
check(mc["BA"] / rev["BA"], 0.1679, 5e-5)
check(ev["AA"], 8.2, 1e-9)
check(ev["BA"], 4.3, 1e-9)
check(ev["AA"] / rev["AA"], 0.3445, 5e-5)
check(ev["BA"] / rev["BA"], 0.3282, 5e-5)
check(mc["BA"] / rev["BA"] / (mc["AA"] / rev["AA"]), 2.35, 5e-3)  # P/S ratio of ratios

# ---------------------------------------------------------------- Q1.2 Berk 9.13 ($ million)
tax = 0.35
yrs = {1: dict(R=125, C=40, Dep=25, dNWC=2, CX=30), 2: dict(R=160, C=60, Dep=36, dNWC=8, CX=40)}
printed = {1: dict(EBIT=60, tx=21, NI=39, FCF=32), 2: dict(EBIT=64, tx=22.4, NI=41.6, FCF=29.6)}
for t, y in yrs.items():
    ebit = y["R"] - y["C"] - y["Dep"]
    ni = ebit * (1 - tax)
    fcf = ni + y["Dep"] - y["CX"] - y["dNWC"]
    alt = (y["R"] - y["C"]) * (1 - tax) + tax * y["Dep"] - y["CX"] - y["dNWC"]
    check(ebit, printed[t]["EBIT"], 1e-9)
    check(ebit * tax, printed[t]["tx"], 1e-9)
    check(ni, printed[t]["NI"], 1e-9)
    check(fcf, printed[t]["FCF"], 1e-9)
    check(alt, printed[t]["FCF"], 1e-9)
check(tax * 25, 8.75, 1e-9)
check(tax * 36, 12.6, 1e-9)

# ---------------------------------------------------------------- Q1.3 Berk 16.19-16.21 ($ million)
r, I, N0 = 0.08, 50, 5
VU = 10 / r
check(VU, 125, 1e-9)
check(VU - I, 75, 1e-9)                 # NPV
P_eq = VU / (N0 + I / 15)               # fixed point P = 15
check(P_eq, 15, 1e-9)
check((VU - I) / N0, 15, 1e-9)
check(I / 15, 3.3333, 5e-5)             # new shares (million)
tc = 0.40
VL = VU + tc * I
check(tc * I, 20, 1e-9)
check(VL, 145, 1e-9)
check((VL - I) / N0, 19, 1e-9)
VU_d = 9 / r
check(VU_d, 112.5, 1e-9)
check(VU_d + tc * I, 132.5, 1e-9)
check((VU_d + tc * I - I) / N0, 16.5, 1e-9)
check((10 - 9) / r, 12.5, 1e-9)         # PV of distress costs

# ---------------------------------------------------------------- Q1.4 Berk 17.11-17.13 ($ million)
cashT, rT = 100, 0.07
check(cashT * rT, 7, 1e-9)
tcK = 0.35
check(cashT * rT * (1 - tcK), 4.55, 1e-9)
check(cashT * rT * (1 - tcK) / rT, 65, 1e-9)
check(cashT - cashT * rT * (1 - tcK) / rT, 35, 1e-9)
td = 0.15
check(cashT * rT * (1 - td), 5.95, 1e-9)
check(cashT * rT * (1 - td) / rT, 85, 1e-9)
check(cashT * (1 - td), 85, 1e-9)

# ---------------------------------------------------------------- Q2 previous-year midterm
rf, mrp, tau = 0.05, 0.10, 0.30
bE_c, de_c = 1.65, 0.10
bU = bE_c / (1 + de_c)                  # beta_D = 0, beta_ITS = beta_U
check(bU, 1.5, 1e-12)
rU = rf + bU * mrp
check(rU, 0.20, 1e-12)
check(rf + bE_c * mrp, 0.215, 1e-12)
check(rU + de_c * (rU - rf), 0.215, 1e-12)
check(1 / 1.1, 0.9091, 5e-5)
check(0.1 / 1.1, 0.0909, 5e-5)

# (b) all equity
a20 = annuity(rU, 5)
check(a20, 2.9906, 5e-5)
VU2 = 250 * a20
check(VU2, 747.65, 5e-3)
check(VU2 - 750, -2.35, 5e-3)
check(750 / VU2, 1.0031, 5e-5)

# (c) D/E = 0.5
de = 0.5
rE = rU + de * (rU - rf)
check(rE, 0.275, 1e-12)
check(bU * (1 + de), 2.25, 1e-12)

# (d) WACC
DV = de / (1 + de)
wacc = (1 - DV) * rE + DV * rf * (1 - tau)
check(wacc, 0.195, 1e-12)
check(rU - DV * tau * rf, 0.195, 1e-12)
check((1 - DV) * rE, 0.183333, 5e-7)
check(DV * rf * (1 - tau), 0.011667, 5e-7)
a195 = annuity(wacc, 5)
check(a195, 3.0238, 5e-5)
VL = [250 * annuity(wacc, 5 - t) if t < 5 else 0.0 for t in range(6)]
check(VL[0], 755.95, 5e-3)
check(VL[0] - 750, 5.95, 5e-3)

# (e) balance sheet at t = 0
D0, E0 = DV * VL[0], (1 - DV) * VL[0]
check(D0, 251.98, 5e-3)
check(E0, 503.97, 5e-3)
outside = 750 - D0
check(outside, 498.02, 5e-3)
check(outside / E0, 0.9882, 5e-5)
check(1 - outside / E0, 0.0118, 5e-5)
check(E0 - outside, 5.95, 5e-3)

# (f) debt schedule, tax shields, PV at r_U
D = [DV * v for v in VL]
for t, p in enumerate([251.98, 217.79, 176.92, 128.09, 69.74, 0.0]):
    check(D[t], p, 5e-3)
for t, p in enumerate([755.95, 653.37, 530.77, 384.27, 209.21, 0.0]):
    check(VL[t], p, 5e-3)
ITS = [tau * rf * D[t - 1] for t in range(1, 6)]
for t, p in enumerate([3.78, 3.27, 2.65, 1.92, 1.05]):
    check(ITS[t], p, 5e-3)
pv = [ITS[t - 1] / (1 + rU) ** t for t in range(1, 6)]
for t, p in enumerate([3.15, 2.27, 1.54, 0.93, 0.42]):
    check(pv[t], p, 5e-3)
PVITS = sum(pv)
check(PVITS, 8.30, 5e-3)
check(VL[0] - VU2, 8.30, 5e-3)
check(VU2 + PVITS, 755.95, 5e-3)
check(VU2 - 750 + PVITS, 5.95, 5e-3)    # APV = NPV(d)
# exact identity, not just to rounding
assert abs(VU2 + PVITS - VL[0]) < 1e-9
n += 1

print(f"PASS {n} checks")
