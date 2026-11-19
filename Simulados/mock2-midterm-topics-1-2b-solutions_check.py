"""Check every number printed in mock2-midterm-topics-1-2b-solutions.tex.

Run: python -I Simulados/mock2-midterm-topics-1-2b-solutions_check.py
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


# ---------------------------------------------------------------- Q2.1 Berk 13.1, 13.3 ($ million)
D, E, P = 100, 6 * 50, 20
V = D + E + P
check(E, 300, 0)
check(V, 420, 0)
check(E / V, 0.7143, 5e-5)
check(D / V, 0.2381, 5e-5)
check(P / V, 0.0476, 5e-5)
E3, D3 = 1 * 50, 20 * 1.01
check(E3, 50, 0)
check(D3, 20.2, 1e-9)
check(E3 + D3, 70.2, 1e-9)
check(E3 / (E3 + D3), 0.7123, 5e-5)
check(D3 / (E3 + D3), 0.2877, 5e-5)
check(1 + 30, 31, 0)                     # book equity, not used

# ---------------------------------------------------------------- Q2.2 Berk 13.18-13.19 ($ million)
pv15 = 15 / (0.15 - 0.04)
check(pv15, 136.36, 5e-3)
check(pv15 - 100, 36.36, 5e-3)
pv12 = 15 / (0.12 - 0.04)
check(pv12, 187.5, 5e-2)
check(pv12 - 100, 87.5, 5e-2)

# ---------------------------------------------------------------- Q2.3 Berk 13.15
rE = 1 / 20 + 0.04
rP = 2 / 28
rD = 0.065
check(rE, 0.09, 1e-12)
check(rP, 0.0714, 5e-5)
Em, Pm, Lm = 5 * 20, 1 * 28, 20
A = Em + Pm + Lm
check(Em, 100, 0)
check(Pm, 28, 0)
check(A, 148, 0)
wacc = Em / A * rE + Pm / A * rP + Lm / A * rD * (1 - 0.35)
check(Em / A, 0.6757, 5e-5)
check(Pm / A, 0.1892, 5e-5)
check(Lm / A, 0.1351, 5e-5)
check(Em / A * rE, 0.0608, 5e-5)
check(Pm / A * rP, 0.0135, 5e-5)
check(Lm / A * rD * 0.65, 0.0057, 5e-5)
check(rD * 0.65, 0.04225, 5e-6)
check(wacc, 0.0800, 5e-5)

# ---------------------------------------------------------------- Q2.4 Berk 16.3 ($ million)
EX = 0.8 * 50 + 0.2 * 20
VU = EX / 1.10
check(EX, 44, 1e-9)
check(VU, 40, 1e-9)
Dv = 20 / 1.05
Ev = VU - Dv
check(Dv, 19.05, 5e-3)
check(Ev, 20.95, 5e-3)
EpayL = 0.8 * 30 + 0.2 * 0
check(EpayL, 24, 1e-9)
check(EpayL / Ev - 1, 0.1455, 5e-5)
check(0.10 + Dv / Ev * (0.10 - 0.05), 0.1455, 5e-5)  # MM II cross-check
check(Dv / Ev, 0.9091, 5e-5)
check(20 / VU - 1, -0.50, 1e-12)
check(50 / VU - 1, 0.25, 1e-12)
check(0 / Ev - 1, -1.0, 1e-12)
check(30 / Ev - 1, 0.4318, 5e-5)

# ---------------------------------------------------------------- Q3.1 Berk 16.10
tau, rf = 0.40, 0.05
EU = 1000 * (1 - tau) / rf
check(1000 * (1 - tau), 600, 1e-9)
check(EU, 12000, 1e-6)
NI = (1000 - 500) * (1 - tau)
check(NI, 300, 1e-9)
EL, DL = NI / rf, 500 / rf
check(EL, 6000, 1e-6)
check(DL, 10000, 1e-6)
check(EL + DL, 16000, 1e-6)
check(EL + DL - EU, 4000, 1e-6)
check((EL + DL - EU) / DL, 0.40, 1e-12)
check(tau * DL, 4000, 1e-6)
check(tau * 500, 200, 1e-9)
check(1000 - tau * (1000 - 500), 800, 1e-9)   # total paid to investors with debt
check(tau * 500 / rf, 4000, 1e-6)

# ---------------------------------------------------------------- Q3.2 Berk 16.16-16.17
VU16 = 5 / 0.15
check(VU16, 33.33, 5e-3)
check(0.35 * 19.05, 6.67, 5e-3)
check(VU16 + 0.35 * 19.05, 40.00, 5e-3)
rU, rD17, t17, dv = 0.15, 0.09, 0.35, 0.5
rE17 = (rU - dv * rD17) / (1 - dv)
check(rE17, 0.21, 1e-12)
w17 = (1 - dv) * rE17 + dv * rD17 * (1 - t17)
check(w17, 0.13425, 5e-6)
check(rU - t17 * rD17 * dv, 0.13425, 5e-6)
check(t17 * rD17 * dv, 0.01575, 5e-6)
check(rD17 * (1 - t17), 0.0585, 5e-5)

# ---------------------------------------------------------------- Q3.3 Berk 16.23 ($ million)
rU23 = 0.05 + 1.10 * (0.15 - 0.05)
check(rU23, 0.16, 1e-12)
VU23 = 16 / rU23
check(VU23, 100, 1e-9)
VFCF = 15 / rU23
check(VFCF, 93.75, 1e-9)
check(0.35 * 40, 14, 1e-9)
VL23 = VFCF + 0.35 * 40
check(VL23, 107.75, 1e-9)
check(VU23 - VFCF, 6.25, 1e-9)           # PV of lost FCF = PV(distress)
check(0.35 * 40 - (VU23 - VFCF), 7.75, 1e-9)

# ---------------------------------------------------------------- Q3.4 Berk 17.9
check(2 * (1 - 0.20), 1.60, 1e-12)
check(2 * 0.8 / 0.12, 13.33, 5e-3)
check(2 / 0.12, 16.67, 5e-3)
check(2 / 0.12 - 2 * 0.8 / 0.12, 3.33, 5e-3)
check((2 / 0.12) / (1.6 / 0.12) - 1, 0.25, 1e-12)

print(f"PASS {n} checks")
