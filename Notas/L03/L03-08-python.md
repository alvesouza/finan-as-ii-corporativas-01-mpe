---
tags: [notes, lecture-03, python, reference-implementation, trade-off, wacc, apv]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 2–51, 54–63; numbers checked against the slides and Ross Fundamentos 9e pp. 551–553, 588; Berk Fundamentals 2e pp. 476, 503–507"
---

# L03 · Python — the lecture's routines, each with self-checks

> Prev: [[L03-07-pitfalls]] · Next: [[L03-00-map]] · Map: [[L03-00-map]]

Four blocks, run in order in one session (`python -I`, numpy/scipy only). Each ends with `assert`s
against the slides' or the books' own numbers; a broken routine fails loudly. Figures are built
separately by `figures/make_figures.py`; the companion's JavaScript is checked against an independent
Python copy in `companions/check_companions.py`.

**Reused, not rebuilt:** the numerical check of the R3 list's solutions,
`Listas/lista-r3-mm-taxes-tradeoff-solutions_check.py` (192 checks: tax shields, APV, Hamada,
two-state trade-off, Miller's $G_L$), is run as is in §5. It is a flat script with no importable
routines, so the valuation routines below are written fresh.

---

## 1 · Tax shields, WACC and APV (notes 01–02)

`v_its` implements slide 13's three policies ([[L03-01-tax-shield-mm-taxes]] (14)–(16), with the
$1+r_D$ correction); the checks reproduce slides 2–3, 14–15, 28–32 and 63, Ross's firm L and Berk's
Example 16.4.

```python
import sys
sys.stdout.reconfigure(encoding="utf-8")


def its(tau, r_d, debt):
    """Interest tax shield of one period, slide 3: ITS = tau * r_D * D."""
    return tau * r_d * debt


def v_its(tau, r_d, debt, policy, r_u=None, g=0.0):
    """PV of interest tax shields, slide 13 (note 01 eqs. 14-16).

    policy: "constant" (fixed debt level, r_ITS = r_D), "continuous" (target D/E rebalanced
    continuously, r_ITS = r_U) or "annual" (target D/E reset once a year). r_u, g are needed
    for the two target-ratio policies; raises ValueError if r_u <= g.
    """
    if policy == "constant":
        return tau * debt
    if r_u is None or r_u <= g:
        raise ValueError("target-ratio shields need r_U > g")
    cont = tau * r_d * debt / (r_u - g)
    return cont if policy == "continuous" else cont * (1 + r_u) / (1 + r_d)


def wacc_after_tax(e_v, r_e, r_d, tau):
    """Slide 16: r_WACC = E/V r_E + D/V r_D (1 - tau)."""
    return e_v * r_e + (1 - e_v) * r_d * (1 - tau)


def annuity(r, n):
    """PV of 1 per period for n periods at rate r."""
    return (1 - (1 + r) ** -n) / r


# Slides 2-3 (Berk Table 16.2): taxes 525 vs 647.5, ITS 122.5
assert abs(0.35 * 1850 - 0.35 * 1500 - its(0.35, 1.0, 350)) < 1e-9
# Slides 14-15: V_L = 800, P = 0.8, N = 625, gain 200
vl = 600 + v_its(0.40, 0.05, 500, "constant")
P = vl / 1000
assert abs(vl - 800) < 1e-9 and abs(500 / P - 625) < 1e-9 and abs((P - 0.6) * 1000 - 200) < 1e-9
# Ross pp. 551-553: V_L = 7,300, R_E = 10.22%, WACC 9.589%
E = 7000 + 0.30 * 1000 - 1000
r_e = 0.10 + (0.10 - 0.08) * 1000 / E * (1 - 0.30)
assert abs(E - 6300) < 1e-9 and round(100 * r_e, 2) == 10.22
assert abs(wacc_after_tax(E / 7300, r_e, 0.08, 0.30) - 0.10 * (1 - 0.30 * 1000 / 7300)) < 1e-12
# Slides 28-31: WACC 11.5%, V_L = 100,000 both ways; slide 32: 98,945
r_u, r_d, tau, g = 0.12, 0.05, 0.40, 0.04
r_e = r_u + (0.25 / 0.75) * (r_u - r_d)                  # note 01 (13): 14.333%
w = wacc_after_tax(0.75, r_e, r_d, tau)
assert abs(w - 0.115) < 1e-12 and abs(w - (r_u - tau * r_d * 0.25)) < 1e-12   # note 02 (1) = (4)
vu = 7500 / (r_u - g)
assert abs(7500 / (w - g) - 100000) < 1e-6 and abs(vu - 93750) < 1e-6
assert abs(vu + v_its(tau, r_d, 25000, "continuous", r_u, g) - 100000) < 1e-6
assert abs(v_its(tau, r_d, 25000, "annual", r_u, g) - 6666.6667) < 1e-3
loan = its(tau, r_d, 60000) * annuity(r_d, 5)
assert round(loan) == 5195 and round(vu + loan) == 98945
# Berk Example 16.4 (p. 476): 42 million a year for 10 years at 6% -> 309 million
assert round(42 * annuity(0.06, 10)) == 309
# Slide 63: r_D = 33.33% but the shield follows the coupon rate 50/525
r_D, rbar = 700 / 525 - 1, 50 / 525
assert abs(r_D - 1 / 3) < 1e-12 and abs((r_D - 0.35 * rbar) - 0.30) < 1e-12
print("section 1 OK")
```

## 2 · The appendix identity, numerically

Section 1 already checks that the after-tax WACC (note 02 (1)) equals $r_U-\tau r_DD/V$ (note 02
(4)) and that discounting at it gives the APV value — the content of the appendix derivation
(note 02 (14)–(20)) in the constant-ratio case.

## 3 · The static trade-off with any density (note 04)

`TradeOff` integrates slides 42–44 numerically for any $h$, so it does **not** rely on the uniform
closed forms used by the figures and the companion — it is the independent path. The checks:
$K^*=\bar X-C/\tau$ and $V(K^*)=81.6327$ for the uniform calibration, $E+D=V$, identity (8),
FOC root = grid argmax, the two landmarks, a symmetric triangular density with the signs of (13)–(14),
and the volatility caveat of note 04 §6.

```python
import numpy as np
from scipy import integrate, optimize, stats


class TradeOff:
    """Slides 41-45: one-period trade-off with any density h on [x_lo, x_hi].

    pdf, cdf: callables for h and H; tau: tax rate paid only if solvent; c: fixed default
    cost (slide assumes c < x_lo); rf: investors' required return. All values are at t = 0.
    """

    def __init__(self, pdf, cdf, x_lo, x_hi, tau, c, rf):
        self.h, self.H, self.lo, self.hi = pdf, cdf, x_lo, x_hi
        self.tau, self.c, self.rf = tau, c, rf

    def _int(self, f, a, b):
        a, b = max(a, self.lo), min(b, self.hi)
        return integrate.quad(lambda x: f(x) * self.h(x), a, b)[0] if b > a else 0.0

    def v_u(self):                       # eq. (2)
        return (1 - self.tau) * self._int(lambda x: x, self.lo, self.hi) / (1 + self.rf)

    def equity(self, K):                 # eq. (4)
        return (1 - self.tau) * self._int(lambda x: x - K, K, self.hi) / (1 + self.rf)

    def debt(self, K):                   # eq. (5)
        return (self._int(lambda x: x - self.c, self.lo, K)
                + K * (1 - self.H(min(max(K, self.lo), self.hi)))) / (1 + self.rf)

    def value(self, K):                  # eq. (6)
        Kc = min(max(K, self.lo), self.hi)
        s = self._int(lambda x: x, self.lo, K) + K * (1 - self.H(Kc))
        return self.v_u() + (self.tau * s - self.c * self.H(Kc)) / (1 + self.rf)

    def foc(self, K):                    # eq. (10) times (1 + rf)
        return self.tau * (1 - self.H(K)) - self.c * self.h(K)

    def k_star(self):
        """Root of (11) on (x_lo, x_hi); corner x_lo if the FOC is already negative there."""
        a, b = self.lo + 1e-9, self.hi - 1e-9
        if self.c == 0:
            return self.hi
        if self.foc(a) <= 0:
            return self.lo
        return optimize.brentq(self.foc, a, b)


def uniform(lo=50.0, hi=150.0, tau=0.35, c=20.0, rf=0.05):
    u = stats.uniform(loc=lo, scale=hi - lo)
    return TradeOff(u.pdf, u.cdf, lo, hi, tau, c, rf)


m = uniform()
ks = m.k_star()
assert abs(ks - (150 - 20 / 0.35)) < 1e-7                                  # eq. (16)
assert abs(m.value(ks) - 81.6327) < 1e-4 and abs(m.v_u() - 61.9048) < 1e-4
assert abs(m.debt(ks) - 71.5258) < 1e-4 and abs(m.equity(ks) - 10.1069) < 1e-4
assert abs(m.debt(ks) + m.equity(ks) - m.value(ks)) < 1e-9                 # E + D = V
assert abs(m.value(ks) - (m.v_u() + m.tau * m.debt(ks)
                          - (1 - m.tau) * m.c * m.H(ks) / (1 + m.rf))) < 1e-9   # eq. (8)
grid = np.linspace(0, 180, 1801)
assert abs(grid[np.argmax([m.value(k) for k in grid])] - ks) < 0.1         # FOC = grid argmax
assert abs(m.value(50) - 78.5714) < 1e-4 and abs(m.value(160) - 76.1905) < 1e-4
assert uniform(c=0).k_star() == 150 and uniform(c=40).k_star() == 50       # landmarks / corner

# A non-uniform h: symmetric triangular on [50, 150]; comparative statics (13)-(14) numerically
def tri(tau=0.35, c=20.0):
    t = stats.triang(c=0.5, loc=50, scale=100)
    return TradeOff(t.pdf, t.cdf, 50, 150, tau, c, 0.05)

k0 = tri().k_star()
assert 50 < k0 < 150 and abs(tri().foc(k0)) < 1e-9
assert tri(tau=0.40).k_star() > k0 > tri(c=25.0).k_star()                  # dK*/dtau > 0, dK*/dC < 0

# Note 04 section 6 caveat: mean 100, widths 20, 100, 140 (C < X_lo holds) -> value gains 30.00, 19.73, 18.17
for w_, gain in [(20, 30.00), (100, 19.73), (140, 18.17)]:
    mw = uniform(lo=100 - w_ / 2, hi=100 + w_ / 2)
    assert round(mw.value(mw.k_star()) - mw.v_u(), 2) == gain
print("section 3 OK: K* uniform", round(ks, 4), "triangular", round(k0, 4))
```

## 4 · Dividend irrelevance (note 05)

Prices per share (slide 50, (1)) and share counts (sources = uses, (2)) depend on each other, so the
routine solves them jointly; the value $n_0P_0$ comes out equal to (6) for five random payout plans
with the investment plan fixed.

```python
import numpy as np

rng = np.random.default_rng(0)


def firm_value_by_payout(X, I, div, delta, n0=1.0, iters=500):
    """Slides 49-51, deterministic: V_0 = n_0 P_0 for a given dividend plan.

    X, I, div: arrays for t = 1..T of cash flow, investment and TOTAL dividends paid to the
    shares outstanding at t-1; the gap div_t + I_t - X_t is raised by issuing (or bought back
    by repurchasing) shares at the ex-dividend price P_t, eq. (2). The firm is liquidated at T,
    so P_T = 0 and div_T must equal X_T - I_T. Prices P_t = delta (d_{t+1} + P_{t+1}), eq. (1),
    and share counts depend on each other, so they are solved by fixed-point iteration.
    """
    T = len(X)
    assert abs(div[-1] - (X[-1] - I[-1])) < 1e-12, "nothing can be raised at P_T = 0"
    raised = div + I - X                      # index k <-> period k+1
    P = np.ones(T + 1)
    P[T] = 0.0
    n = np.full(T + 1, n0)
    for _ in range(iters):
        for t in range(1, T):                 # n_t = n_{t-1} + raised_t / P_t
            n[t] = n[t - 1] + raised[t - 1] / P[t]
        n[T] = n[T - 1]
        for t in range(T - 1, -1, -1):        # eq. (1), per-share dividend d_{t+1} = div / n_t
            P[t] = delta * (div[t] / n[t] + P[t + 1])
    return n[0] * P[0]


X = np.array([10.0, 12, 9, 15, 11, 14])
I = np.array([4.0, 6, 2, 8, 3, 0])
delta = 1 / 1.08
target = sum(delta ** (i + 1) * (X[i] - I[i]) for i in range(len(X)))       # eq. (6)
for _ in range(5):
    div = rng.uniform(0.6, 1.4, len(X)) * (X - I)
    div[-1] = X[-1] - I[-1]
    assert abs(firm_value_by_payout(X, I, div, delta) - target) < 1e-9
# Ross Wharton (p. 588): 173.55 under both policies
assert round(100 / 1.1 + 100 / 1.21, 2) == round(110 / 1.1 + 89 / 1.21, 2) == 173.55
# Berk Genron (pp. 503-507): 42 under the three policies
assert abs(2 + 4.80 / 0.12 - 42) < 1e-9 and abs(48 / (10 - 20 / 42) / 0.12 - 42) < 1e-9
assert abs(48 / (10 + 28 / 42) * (1 + 1 / 0.12) - 42) < 1e-9
print("section 4 OK: V_0 =", round(target, 4), "for every payout policy")
```

## 5 · The R3 list's own check (reuse)

```python
import runpy
# run from the repository root
runpy.run_path("Listas/lista-r3-mm-taxes-tradeoff-solutions_check.py")   # prints "PASS 192 checks"
```

---

## Links

Map: [[L03-00-map]] · Formulas: [[L03-06-formulas]] · Pitfalls: [[L03-07-pitfalls]] ·
Figures: `figures/make_figures.py` · Companion check: `companions/check_companions.py` ·
List R3: [[../../Listas/lista-r3-mm-taxes-tradeoff|Lista R3]].
