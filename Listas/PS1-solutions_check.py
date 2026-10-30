"""Check every number printed in PS1-solutions.tex and PS1-solutions-short.tex.

Run: python -I Listas/PS1-solutions_check.py
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
    """Present value of 1 per year for T years at rate r."""
    return (1 - (1 + r) ** -T) / r


# Exercise 2 (thousands of dollars).
tau = 2625 / 7500
check(tau, 0.35, 1e-12)
ebit = 30000 - 18000 - 1000 - 2500
check(ebit, 8500, 0)
check(ebit * tau, 2975, 1e-9)
nopat = ebit * (1 - tau)
check(nopat, 5525, 1e-9)
fcf = nopat + 2500
check(fcf, 8025, 1e-9)
check((30000 - 18000 - 1000) * (1 - tau) + tau * 2500, 8025, 1e-9)
cfs2 = [-25000 - 10000] + [fcf] * 9 + [fcf + 10000]
check(cfs2[0], -35000, 0)
check(cfs2[-1], 18025, 1e-9)
a14 = annuity(0.14, 10)
check(1.14**10, 3.707221, 5e-7)
check(1.14**-10, 0.269744, 5e-7)
check(a14, 5.216116, 5e-7)
check(fcf * a14, 41859.33, 0.005)
check(10000 * 1.14**-10, 2697.44, 0.005)
v2 = npv(0.14, cfs2)
check(v2, 9556.77, 0.005)
check(fcf * a14 + 10000 * 1.14**-10, 44556.77, 0.005)
check(root(lambda r: npv(r, cfs2), 0.01, 1.0), 0.202, 5e-4)
# Bridge from the consultants' net income to the NPV.
check(4875 * a14, 25428.56, 0.005)
check(1000 * (1 - tau) * a14, 3390.48, 0.005)
check(2500 * a14, 13040.29, 0.005)
check(10000 - 10000 * 1.14**-10, 7302.56, 0.005)
check(4875 * a14 + 1000 * (1 - tau) * a14 + 2500 * a14 - 25000
      - (10000 - 10000 * 1.14**-10), v2, 1e-9)
# Exercise 1(a): same totals, different timing.
check(sum(cfs2), 55250, 1e-9)
check(10 * nopat, 55250, 1e-9)
check(nopat * a14, 28819.04, 0.005)
check(nopat * a14 - v2, 19262, 0.5)

# Exercise 1(b): two-year deferred-tax example.
check(50 * 0.7 + 50, 85, 1e-12)
check(85 / 1.1, 77.2727, 5e-5)
check(85 / 1.1**2, 70.2479, 5e-5)
check(npv(0.1, [0, 85, 85]), 147.5207, 5e-5)
check(100 / 1.1, 90.9091, 5e-5)
check(70 / 1.1**2, 57.8512, 5e-5)
check(npv(0.1, [0, 100, 70]), 148.7603, 5e-5)
check(npv(0.1, [0, 100, 70]) - npv(0.1, [0, 85, 85]), 1.2397, 5e-5)
check(15 / 1.1 - 15 / 1.1**2, 1.2397, 5e-5)

# Exercise 3 (dollars).
t3 = 0.45
bv = 110000 - 10000
check(bv, 100000, 0)
tax_sale = t3 * (50000 - bv)
check(tax_sale, -22500, 1e-9)
sale = 50000 - tax_sale
check(sale, 72500, 1e-9)
check(-150000 + sale, -77500, 1e-9)
dfcf = 20000 * (1 - t3) + t3 * (15000 - 10000)
check(dfcf, 13250, 1e-9)
a10 = annuity(0.10, 10)
check(1.1**10, 2.593742, 5e-7)
check(1.1**-10, 0.385543, 5e-7)
check(a10, 6.144567, 5e-7)
check(dfcf * a10, 81415.51, 0.005)
cfs3 = [-150000 + sale] + [dfcf] * 10
check(npv(0.10, cfs3), 3915.51, 0.005)
check(root(lambda r: npv(r, cfs3), 0.01, 1.0), 0.112, 5e-4)
keep = (20000 * (1 - t3) + t3 * 10000) * a10
new = (40000 * (1 - t3) + t3 * 15000) * a10
check(keep, 95240.79, 0.005)
check(new, 176656.30, 0.005)
check(new - 77500, 99156.30, 0.005)
check(new - 77500 - keep, 3915.51, 0.005)
check(-100000 + dfcf * a10, -18584.49, 0.005)

print(f"PASS {n} checks")
