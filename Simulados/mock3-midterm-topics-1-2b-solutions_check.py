"""Check every number printed in mock3-midterm-topics-1-2b-solutions.tex.

Run: python -I Simulados/mock3-midterm-topics-1-2b-solutions_check.py
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


# ---------------------------------------------------------------- Q2.1 Berk 16.2 ($ million)
VU = 2 / 0.50                       # $2m buys 50% of the unlevered equity
check(VU, 4, 1e-9)
E_lev = VU - 1                      # MM: V_L = V_U, debt 1
check(E_lev, 3, 1e-9)
frac = 1 / E_lev                    # fraction of equity sold for the extra $1m
check(frac, 0.3333, 5e-5)
check(0.5 * VU, 2, 1e-9)            # your stake, case (a)
check((1 - frac) * E_lev, 2, 1e-9)  # your stake, case (b)
# expected payoff of the venture implies the probability of success (MM fixes nothing else)
check(VU / 30, 0.1333, 5e-5)

# ---------------------------------------------------------------- Q2.2 Berk 16.4
interest = 0.10 * 5000
check(interest, 500, 1e-9)
for fcf, div_xyz in [(800, 300), (1000, 500)]:
    check(fcf - interest, div_xyz, 1e-9)
    # (b) 10% of XYZ equity + 10% of XYZ debt = 10% of ABC equity
    check(0.1 * (fcf - interest) + 0.1 * interest, 0.1 * fcf, 1e-9)
    # (c) borrow $500 at 10% (interest $50), buy 10% of ABC equity = 10% of XYZ equity
    check(0.1 * fcf - 0.10 * 500, 0.1 * div_xyz, 1e-9)
check(0.1 * 5000, 500, 1e-9)

# ---------------------------------------------------------------- Q2.3 Berk 13.21 ($ billion)
rE = 0.045 + 1.21 * 0.05
check(rE, 0.1055, 5e-5)
E, D = 67, 0.7
V = E + D
check(V, 67.7, 1e-9)
check(E / V, 0.9897, 5e-5)
check(D / V, 0.0103, 5e-5)
check(0.06 * (1 - 0.35), 0.039, 1e-9)
wacc_c = E / V * rE + D / V * 0.06 * (1 - 0.35)
check(wacc_c, 0.1048, 5e-5)
wacc_s = (0.12 - 0.40 * wacc_c) / 0.60
check(wacc_s, 0.1301, 5e-5)

# ---------------------------------------------------------------- Q2.4 Berk 16.6
rU, dv, rD = 0.092, 0.05, 0.06
de = dv / (1 - dv)
check(de, 0.0526, 5e-5)
rE6 = rU + de * (rU - rD)
check(rE6, 0.0937, 5e-5)
check(rE6 * (1 - dv) + rD * dv, 0.092, 1e-12)  # WACC unchanged

# ---------------------------------------------------------------- Q3.1 Berk 16.7-16.8 ($ million)
ebit, intr, t = 325, 125, 0.40
ni = (ebit - intr) * (1 - t)
check(ni, 120, 1e-9)
check(ni + intr, 245, 1e-9)
ni_u = ebit * (1 - t)
check(ni_u, 195, 1e-9)
check(ni + intr - ni_u, 50, 1e-9)
check(t * intr, 50, 1e-9)
check(1 * (1 - 0.35), 0.65, 1e-9)
check(20.75 - 0.65, 20.10, 1e-9)

# ---------------------------------------------------------------- Q3.2 Berk 16.9, 16.12
d_ms = 0.13 * 300
check(d_ms, 39, 1e-9)
check(0.35 * d_ms, 13.65, 1e-9)
its6 = 0.35 * 0.06 * 10
check(its6, 0.21, 1e-9)
check(its6 / 0.06, 3.5, 1e-9)
its5 = 0.35 * 0.05 * 10
check(its5, 0.175, 1e-9)
check(its5 / 0.05, 3.5, 1e-9)

# ---------------------------------------------------------------- Q3.3 Berk 16.13-16.15
pre_r = 2 / 3 * 0.12 + 1 / 3 * 0.07
check(pre_r, 0.1033, 5e-5)
post_r = 2 / 3 * 0.12 + 1 / 3 * 0.07 * (1 - 0.35)
check(post_r, 0.0952, 5e-5)
E14, D14 = 30 * 15, 150
check(E14, 450, 1e-9)
check(E14 + D14, 600, 1e-9)
pre14 = 0.75 * 0.10 + 0.25 * 0.05
check(pre14, 0.0875, 5e-5)
post14 = 0.75 * 0.10 + 0.25 * 0.05 * (1 - 0.35)
check(post14, 0.0831, 5e-5)
dv15 = 0.65 / 1.65
check(dv15, 0.3939, 5e-5)
cut = 0.40 * 0.07 * dv15
check(cut, 0.0110, 5e-5)

# ---------------------------------------------------------------- Q3.4 Berk 17.3-17.5 ($ million)
cap = 1 * 20
check(cap - 0.1 * 20, 18, 1e-9)
check((cap - 0.1 * 20) / 0.9, 20, 1e-9)
cash1, assets1, eq0, eq1 = 50 - 20, 500 - 20, 500 - 200, 500 - 200 - 20
check(cash1, 30, 1e-9)
check(assets1, 480, 1e-9)
check(eq0, 300, 1e-9)
check(eq1, 280, 1e-9)
check(200 / eq0, 0.667, 5e-4)
check(200 / eq1, 0.714, 5e-4)
check(200 / 500, 0.40, 1e-9)
check(200 / assets1, 0.417, 5e-4)
check(20 * 0.10, 2, 1e-9)

print(f"PASS {n} checks")
