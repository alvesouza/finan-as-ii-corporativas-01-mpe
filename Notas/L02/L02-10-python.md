---
tags: [notes, lecture-02, python, reference-implementation]
date: 2026-10-24
status: taught
source: "Topic 2A slides 4–105; Ross Fundamentos 9e pp. 297–298 (mine), p. 549 (Exemplo 16.3); Higgins 13e pp. 303, 319 (Polaris); Berk Fundamentals 2e pp. 465–471 (coffee shop)."
---

# L02 · Python — every routine the lecture needs, checked against its own numbers

> Prev: [[L02-09-pitfalls]] · Map: [[L02-00-map]]

**What exists already, and why it is cited rather than imported.**
`Listas/lista-r2-valuation-solutions_check.py` and `Listas/lista-r3-mm-taxes-tradeoff-solutions_check.py`
check every number of the list solutions (run them with `python -I <path>`; each prints its PASS
count). They are flat scripts — every check runs at import, and the hyphenated file names are not
importable — so their `npv` / `root` helpers are re-stated here in a few lines instead. Their
coverage complements this note: lista-r2 #6 (unlevering comparables), #8 (multiple IRRs), #14
(state prices from a traded project); lista-r3 #1 (two-outcome MM), #7 (homemade leverage),
#11 (risky debt in a binomial market). The figures' own checks are in
`Notas/L02/figures/make_figures.py`; the companion's in `Notas/L02/companions/check_companions.py`.

**Run.** Copy the block into a file and run it with `python -I`; it prints `L02 python: all checks
pass` or stops at the first failing `assert`. numpy only.

```python
"""L02 reference implementation. Each routine: purpose, inputs, failure mode in its docstring;
asserts use the slides' (or the cited book's) printed numbers."""
import numpy as np


# ---------- 2A.1-2A.4: present value, NPV, IRR ----------
def npv(r, cfs):
    """NPV at rate r of cash flows cfs[0..T], cfs[0] at t = 0 (eqs. 1.3, 2.4).
    r > -1 required (else division by a non-positive discount factor)."""
    return sum(c / (1 + r) ** t for t, c in enumerate(cfs))


def irr_roots(cfs, lo=-0.99, hi=5.0, n=20000):
    """All IRRs in (lo, hi): sign changes of NPV on a grid, refined by bisection (eq. 2.6).
    Returns [] when the NPV never crosses zero (no IRR) - the caller must handle that.
    A double root (NPV tangent to zero) is missed: grid sign-change method."""
    grid = np.linspace(lo, hi, n)
    vals = [npv(r, cfs) for r in grid]
    roots = []
    for a, b, fa, fb in zip(grid, grid[1:], vals, vals[1:]):
        if fa == 0:
            roots.append(a)
        elif fa * fb < 0:
            for _ in range(100):
                m = (a + b) / 2
                if npv(a, cfs) * npv(m, cfs) <= 0:
                    b = m
                else:
                    a = m
            roots.append((a + b) / 2)
    return roots


assert abs(-15 + 22 / 1.10 - 5) < 1e-12                                    # slide 32
assert np.allclose(irr_roots([-60, 155, -100]), [0.25, 1 / 3], atol=1e-9)  # Ross pp. 297-298
assert round(npv(0.10, [-60, 155, -100]), 2) == -1.74                     # Ross p. 297
assert irr_roots([100, -300, 250]) == []                                   # no IRR (L02-02 s5)
assert np.allclose(irr_roots([-1000, 1500]), [0.5]) and np.allclose(irr_roots([1000, -1500]), [0.5])
assert round(npv(0.10, [-1000, 1500]), 1) == 363.6                         # slide 38
assert round(npv(0.10, [-10, 14.3]), 6) == 3.0 and round(npv(0.10, [-1000, 1210]), 6) == 100.0


def tv_growing(fcf_next, r, g):
    """Growing-perpetuity terminal value FCF_{T+1}/(r-g) (eq. 2.3). Fails (ValueError) if g >= r."""
    if g >= r:
        raise ValueError("g must be below r for the perpetuity to converge")
    return fcf_next / (r - g)


assert abs(tv_growing(1.0, 0.10, 0.02) - npv(0.10, [0] + [1.02 ** k for k in range(3000)])) < 1e-9


# ---------- 2A.2: CAPM, leverage and betas ----------
def capm(rf, beta, rm):
    """Required expected return r_f + beta (E[r_m] - r_f) (eq. 1.4)."""
    return rf + beta * (rm - rf)


def unlever(beta_E, D, E, beta_D=0.0):
    """Asset beta as the value-weighted average (eq. 1.11); D, E market values, D + E > 0."""
    return E / (D + E) * beta_E + D / (D + E) * beta_D


def relever(beta_A, D, E, beta_D=0.0):
    """Equity beta beta_A + (D/E)(beta_A - beta_D) (eq. 1.12); E > 0."""
    return beta_A + D / E * (beta_A - beta_D)


def moments(x, y, prob):
    """Mean of x and Cov(x, y) under state probabilities prob (eq. 1.5)."""
    x, y, prob = map(np.asarray, (x, y, prob))
    return prob @ x, prob @ ((x - prob @ x) * (y - prob @ y))


# the house, slides 12-15
q, rm_s = np.array([0.8, 0.2]), np.array([0.10, -0.05])
Erm, var_m = moments(rm_s, rm_s, q)
assert np.isclose(Erm, 0.07) and np.isclose(var_m, 0.0036)
for debt, rE_print, bE_print in ((20, 0.0825, 1.25), (50, 0.12, 2.0)):
    eq_val = 100 - debt
    rE_s = (100 * (1 + rm_s) - debt * 1.02) / eq_val - 1
    ErE, cov = moments(rE_s, rm_s, q)
    assert np.isclose(ErE, rE_print) and np.isclose(cov / var_m, bE_print)   # slide 14 prints 8% (rounded)
    assert np.isclose(relever(1.0, debt, eq_val), bE_print)

# three comparables, slides 22-23
bA = [unlever(b, d, e) for b, d, e in ((0.75, 0.004, 0.096), (1.0, 2.3, 7.7), (1.08, 0.21, 0.79))]
assert np.allclose(np.round(bA, 2), [0.72, 0.77, 0.85])
assert round(np.mean(bA), 2) == 0.78 and round(100 * capm(0.04, np.mean(bA), 0.124), 2) == 10.56
assert round(unlever(2.05, 7334 - 5898, 5898), 2) == 1.65                  # Higgins p. 319
assert round(100 * capm(0.017, 2.05, 0.017 + 0.064), 1) == 14.8            # Higgins p. 303


# ---------- 2A.6-2A.7: state prices and the entrepreneur ----------
def state_prices(payoffs, prices):
    """State prices p solving payoffs @ p = prices (one row per security, one column per state).
    payoffs must be square and invertible (complete market, N = K); raises LinAlgError otherwise.
    A non-positive entry in the result signals an arbitrage (Amaro Prop. 1.2.1)."""
    p = np.linalg.solve(np.asarray(payoffs, float), np.asarray(prices, float))
    assert (p > 0).all(), "non-positive state price: the securities admit an arbitrage"
    return p


def price(payoff, p):
    """Law of one price: value = sum_s p_s payoff_s (eq. 4.5)."""
    return float(np.dot(payoff, p))


p_ex = state_prices([[1.9, 2.4], [1.05, 1.05]], [2, 1])                    # columns: slump, boom
assert np.allclose(np.round(p_ex, 3), [0.571, 0.381])                     # slides 53-54
assert np.allclose(p_ex / p_ex.sum(), [0.6, 0.4])                          # risk-neutral pi (4.6)

P = state_prices([[0, 2.8], [1.05, 1.05]], [1, 1])                        # [slump p2, boom p1]
p2, p1 = P
assert round(p1, 3) == 0.357 and round(p2, 3) == 0.595                    # slides 65-66
X = np.array([1.05, 3.15])                                                  # slump, boom (slide 55)
QE = np.array([0.5, 0.5])


def claims(F, X=X, P=P, prob=QE):
    """Values and expected returns of debt with face F and equity on payoff X (eqs. 3.1-3.3,
    5.6, 7.4-7.6). Returns dict A, D, E, rA, rD, rE; a return is None when its value is 0."""
    dpay, epay = np.minimum(X, F), np.maximum(X - F, 0)
    A, D, E = price(X, P), price(dpay, P), price(epay, P)
    ret = lambda pay, v: float(prob @ pay) / v - 1 if v > 1e-12 else None
    return dict(A=A, D=D, E=E, rA=ret(X, A), rD=ret(dpay, D), rE=ret(epay, E))


def alpha_equity(cash, X=X, P=P):
    """Share alpha sold to zero-NPV investors who pay `cash` (eq. 5.7)."""
    return cash / price(X, P)


c = claims(1.05)                                                             # slides 68, 71
assert np.allclose([c["A"], c["D"], c["E"], c["rD"], c["rE"], c["rA"]], [1.75, 1, 0.75, 0.05, 0.40, 0.20])
a = alpha_equity(1.0)
assert np.isclose(a, 4 / 7) and np.isclose((1 - a) * price(X, P), 0.75)    # slide 69
c0 = claims(0.0)
assert c0["rD"] is None and np.isclose(c0["rE"], 0.20)                     # slide 72
c4, c5 = claims(0.42), claims(0.525)                                       # slides 78, 80
assert np.isclose(c4["E"], 1.35) and round(100 * c4["rE"], 1) == 24.4
assert np.isclose(c5["E"], 1.25) and np.isclose(c5["rE"], 0.26)
assert round(1.575 / (1 + c4["rE"]), 2) == 1.27                           # slide 79 fallacy: E 1.27
# slide 81: replicate the entrepreneur directly with stock (0, 2.8) and bond (1.05, 1.05)
for target in (np.array([0, 2.1]), 3 / 7 * X):
    xy = np.linalg.solve(np.array([[0, 1.05], [2.8, 1.05]]), target)        # rows: slump, boom
    assert np.isclose(xy.sum(), 0.75)                                       # both prices are 1


# ---------- 2A.8: MM I ----------
def arbitrage_step1(V1, V2, D1, E1, Rf, alpha, X):
    """Slide 87 portfolio when V2 > V1: short alpha of firm 2, buy alpha V2/V1 of firm 1's debt
    and equity. Returns (cost today, payoff per state). Firm 1's debt must be safe: Rf D1 <= min X."""
    k = alpha * V2 / V1
    cost = -alpha * V2 + k * D1 + k * E1
    payoff = -alpha * X + k * Rf * D1 + k * (X - Rf * D1)
    return cost, payoff


cost, pay = arbitrage_step1(1.75, 1.80, 1.0, 0.75, 1.05, 0.1, X)
assert abs(cost) < 1e-12 and (pay > 0).all() and np.allclose(pay, 0.1 * X * (1.80 / 1.75 - 1))


def put_call_value(K, X=X, P=P):
    """C(K) + K/(1+r_f) - P(K) (eq. 6.8); equals price(X) for every K."""
    call = price(np.maximum(X - K, 0), P)
    put = price(np.maximum(K - X, 0), P)
    return call + K * P.sum() - put


assert all(np.isclose(put_call_value(K), 1.75) for K in (0, 0.5, 1.05, 2.1, 3.15, 4.0))
assert np.isclose(claims(2.1)["D"], 2.1 * P.sum() - price(np.maximum(2.1 - X, 0), P))   # eq. 6.6


# ---------- 2A.9-2A.10: MM II, WACC, yield ----------
def mm2_rE(rA, rD, D, E):
    """MM II (eq. 7.2): r_E = r_A + (D/E)(r_A - r_D); E > 0."""
    return rA + D / E * (rA - rD)


def yield_vs_rD(F, D, p_def, C):
    """(y, r_D) for one-period debt of face F and value D (eqs. 7.10-7.11); C recovery in default."""
    return F / D - 1, (F * (1 - p_def) + C * p_def) / D - 1


for F in np.linspace(0.01, 3.14, 300):                                      # both regions
    cl = claims(F)
    assert np.isclose(cl["rE"], mm2_rE(cl["rA"], cl["rD"], cl["D"], cl["E"]))
    assert np.isclose(cl["E"] / cl["A"] * cl["rE"] + cl["D"] / cl["A"] * cl["rD"], 0.20)  # WACC fixed
    if F > 1.05:
        assert np.isclose(cl["rE"], 0.40)                                   # flat region (7.6)
cr = claims(2.1)
y, rD = yield_vs_rD(2.1, cr["D"], 0.5, 1.05)
assert np.isclose(rD, cr["rD"]) and round(100 * y, 2) == 52.73 and round(100 * rD, 2) == 14.55 and y > rD
assert round(100 * mm2_rE(0.12, 0.08, 0.2, 0.8), 6) == 13 and round(100 * mm2_rE(0.12, 0.08, 1, 1), 6) == 16  # Ross p. 549
assert np.isclose(mm2_rE(0.15, 0.05, 15000, 15000), 0.25)                   # Berk p. 471
assert np.isclose((34500 - 6300) / 24000 - 1, 0.175)                       # Berk p. 469
print("L02 python: all checks pass")
```

---

## What each block settles

| Block | Settles | Note |
|---|---|---|
| `npv`, `irr_roots`, `tv_growing` | (2.3)–(2.6); two IRRs for the mine, none for $+100,-300,+250$; lending vs. borrowing | [[L02-02-cash-flows-npv-irr]] |
| `capm`, `unlever`, `relever`, `moments` | (1.4)–(1.12); the house's 8.25% / 1.25 and 12% / 2; the comparables' 10.56% | [[L02-01-present-value-capm-betas]] |
| `state_prices`, `price` | (4.1)–(4.6); 0.381 / 0.571 and $\pi=(0.6,0.4)$; 0.357 / 0.595 | [[L02-04-complete-markets-state-prices]] |
| `claims`, `alpha_equity` | every entrepreneur table (slides 68–80) and the slide-81 replication | [[L02-05-entrepreneur-example]] |
| `arbitrage_step1`, `put_call_value` | (6.1)–(6.8): zero cost, positive payoff; $V(K)=1.75$ for every $K$ | [[L02-06-mm1-arbitrage-put-call]] |
| `mm2_rE`, `yield_vs_rD` | (7.2) in both regions, WACC fixed at 20%, flat 40%, $y=52.73\%>r_D=14.55\%$ | [[L02-07-mm2-wacc-cost-of-debt]] |

## Links

- Interactive version of `claims`: [The State-Price Balance Sheet](companions/companion-mm-state-prices.html).
- Figures built from the same expressions: `figures/make_figures.py` (run
  `python -I Notas/L02/figures/make_figures.py`).
- Rules: [[../../rules/02_valuation|rules/02]] · [[../../rules/03_benchmark_mm|rules/03]].
