---
tags: [notes, lecture-01, python, reference-implementation]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 21, 24–25, 39, 48, 50, 58; Higgins 13e pp. 25, 27–28, 55–57; Berk 2e pp. 31, 37, 39; Ross Fundamentos pp. 38–41; reuses Listas/lista-r1-accounting-capital-structure-solutions_check.py"
---

# Topic 1 · Python — every routine, checked against the slides' and books' numbers

> **Claim.** The accounting review is arithmetic on identities, so its reference implementation is
> a set of small functions, one per numbered equation, each followed by `assert`s on the source's
> own printed numbers. The block below runs in about a second. It re-derives every worked case of
> notes 01–06, then **runs the existing Lista R1 checker** instead of re-implementing its 15 exercises.

Prev: [[L01-08-pitfalls]] · Next: — · Map: [[L01-00-map]]

**Run.** Save the block as a file and run it from the repo root with `python -I <file>` (standard
library only; `cwd` must be the repo root, for the Lista R1 checker path). The verification run of
2026-10-24 printed:

```
L01 python: all asserts pass; Lista R1 checker: PASS 163 checks
```

**What is reused, and why the rest is new.** `Listas/lista-r1-accounting-capital-structure-solutions_check.py`
is a flat script of checks on the list's 15 exercises (Higgins 1.4 … Ross 2.25–2.26), with no functions
to import. So it is **executed** (last section), not copied. Its item 8 already asserts the leverage
bridge (5.20) on Higgins 2.7's numbers. The lecture's own examples (GPA, Starbucks, GM, slide 48,
slide 50) are in no existing script, so the functions below are new. Figures use their own copies of the
same expressions in [figures/make_figures.py](figures/make_figures.py), and the companion is checked by
[companions/check_companions.py](companions/check_companions.py).

| Section of the code | Equations | Note |
|---|---|---|
| balance sheet | (1.1), (2.4), (3.4)–(3.8) | [[L01-02-balance-sheet-items]], [[L01-03-book-vs-market-leverage]] |
| income statement | (4.2)–(4.5), (4.8) | [[L01-04-income-statement]] |
| ratios, DuPont, ROIC | (5.6)–(5.23) | [[L01-05-ratios-dupont-roic]] |
| cash flows | (6.1), (6.5)–(6.13) | [[L01-06-cash-flows-fcf]] |

## The reference implementation

```python
"""L01 reference implementation: every routine the accounting review needs, checked against the
slides' and books' own numbers. Run from the repo root: python -I <this file>."""
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")


def close(a, b, tol):
    """True if |a - b| <= tol; tol is half a unit of the last printed decimal."""
    return abs(a - b) <= tol


# ---- balance sheet: identity (1.1), NWC (2.4), ratios (3.3)-(3.8) -------------------------
def nwc(ca, cl):
    """Net working capital, eq. (2.4)."""
    return ca - cl


def current_ratio(ca, cl):
    """Eq. (3.7)."""
    return ca / cl


def quick_ratio(ca, inv, cl):
    """Eq. (3.8): current assets other than inventory over current liabilities."""
    return (ca - inv) / cl


def enterprise_value(mcap, debt, cash):
    """Eq. (3.6): market equity + debt - cash."""
    return mcap + debt - cash


GPA = dict(ca=17641, nca=35654, ta=53295, cash=8711, inv=6536, ap=11424, cl=18483, ncl=18005,
           tl=36488, e=16807)                                     # slide 21, BRL m
SBUX = dict(ca=8358, nca=21611, ta=29968, cash=5028, inv=1472, cl=7884, ncl=29989, tl=37872,
            e=-7904, debt=493 + 750 + 14674, mcap=122600)       # slides 24-25, USD m

assert GPA["ca"] + GPA["nca"] == GPA["ta"] == GPA["tl"] + GPA["e"]       # (1.1)
assert SBUX["tl"] + SBUX["e"] == SBUX["ta"]                              # (1.1), residual -7,904
assert nwc(GPA["ca"], GPA["cl"]) == -842 and nwc(SBUX["ca"], SBUX["cl"]) == 474
assert close(current_ratio(GPA["ca"], GPA["cl"]), 0.954, 5e-4)
assert close(quick_ratio(GPA["ca"], GPA["inv"], GPA["cl"]), 0.601, 5e-4)
assert close(current_ratio(SBUX["ca"], SBUX["cl"]), 1.060, 5e-4)
assert close(quick_ratio(SBUX["ca"], SBUX["inv"], SBUX["cl"]), 0.873, 5e-4)
assert close(GPA["ap"] / GPA["cl"], 0.6181, 5e-5)                        # suppliers' share, note 02 §6
assert SBUX["debt"] == 15917
assert enterprise_value(SBUX["mcap"], SBUX["debt"], SBUX["cash"]) == 133489
assert close(enterprise_value(36, 118.7, 23.2), 131.5, 5e-2)            # Berk Global, p. 31
assert close(SBUX["tl"] / SBUX["mcap"], 0.309, 5e-4)                     # market D/E, total liabilities
assert close(118.7 / 22.2, 5.3, 5e-2) and close(118.7 / 36, 3.3, 5e-2)  # Berk p. 31, book vs market D/E

# ---- income statement (4.2)-(4.5), operating leverage (4.8) -------------------------------
def income_statement(sales, cogs, opex, noi, interest, taxes):
    """Eqs. (4.2)-(4.5): returns gross profit, operating income, EBIT, pre-tax income, NI."""
    gp = sales - cogs
    oi = gp - opex
    ebit = oi + noi
    ebt = ebit - interest
    return dict(gp=gp, oi=oi, ebit=ebit, ebt=ebt, ni=ebt - taxes)


def dol(fixed, oi):
    """Eq. (4.8): elasticity of operating income to sales, 1 + F/OI (v and F constant)."""
    return 1 + fixed / oi


gm = income_statement(108673 + 13812, 97539 + 11274, 7038, 2559, 1098, 1774)   # slide 39
assert (gm["gp"], gm["oi"], gm["ebit"], gm["ebt"], gm["ni"]) == (13672, 6634, 9193, 8095, 6321)
tau_gm = 1774 / gm["ebt"]
assert close(tau_gm, 0.21915, 5e-6)
assert close(dol(7038, 6634), 2.061, 5e-4)
assert close(((0.9 * 13672 - 7038) - 6634) / 6634, -0.2061, 5e-5)       # 10% sales fall, note 04 §4

# ---- ratios (5.3)-(5.10), DuPont (5.14), ROIC bridge (5.16)-(5.22) -------------------------
S = 122485
assert close(gm["gp"] / S, 0.1116, 5e-5) and close(gm["oi"] / S, 0.0542, 5e-5)
assert close(gm["ni"] / S, 0.0516, 5e-5)
assert close(gm["ebit"] / 1098, 8.37, 5e-3)                               # coverage (5.10)
assert gm["ebit"] + 12815 == 22008                                        # EBITDA (5.9)
assert close(414 - 0.10 * 1434, 270.6, 5e-2)                              # economic earnings (5.6)
assert close(18.5 / (186.7 / 365), 36.2, 5e-2)                            # AR days (5.7), Berk p. 37


def dupont(margin, turnover, leverage):
    """Eq. (5.14): ROE = margin x turnover x leverage."""
    return margin * turnover * leverage


for name, (roe, m, t, lev) in {"Google": (14.8, 21.6, 0.54, 1.27), "JPMorgan": (8.5, 18.6, 0.04, 11.44),
                               "Hyundai Motor": (15.9, 10.3, 0.65, 2.36), "Chevron": (14.4, 9.7, 0.87, 1.7)}.items():
    assert close(dupont(m, t, lev), roe, 0.15), name                     # slide 48: inputs are rounded
assert close(dupont(3.6, 2.4, 2.6), 22.5, 5e-2) and close(dupont(7.7, 1.7, 2.4), 31.4, 5e-2)  # Berk Ex. 2.3


def returns(ebit, debt, equity, rd, tau):
    """Statement route: (5.17), then ROE (5.11), ROA (5.12) with assets = D + E, ROIC (5.16)."""
    ni = (ebit - rd * debt) * (1 - tau)
    return dict(ni=ni, roe=ni / equity, roa=ni / (debt + equity), roic=ebit * (1 - tau) / (debt + equity))


def roe_bridge(roic, de, rd, tau):
    """Eq. (5.20): ROE = ROIC + (D/E)(ROIC - r_D(1 - tau))."""
    return roic + de * (roic - rd * (1 - tau))


for tau, roe_a, roe_b in ((0.40, 0.18, 0.072), (0.25, 0.225, 0.09)):     # slide 50; Higgins 13e pp. 55-56
    a, b = returns(120, 900, 100, 0.10, tau), returns(120, 0, 1000, 0.10, tau)
    assert close(a["roe"], roe_a, 1e-12) and close(b["roe"], roe_b, 1e-12)
    assert close(a["roe"], roe_bridge(a["roic"], 9, 0.10, tau), 1e-12)   # both routes agree
    assert close(a["roic"], b["roic"], 1e-12)                            # ROIC is financing-neutral
    assert close(a["roa"], a["roic"] - 0.9 * 0.10 * (1 - tau), 1e-12)    # (5.21)
assert close(returns(120, 900, 100, 0.12, 0.40)["roe"], 0.072, 1e-12)    # zero spread: flat
assert close(returns(120, 900, 100, 0.16, 0.40)["roe"], -0.144, 1e-12)   # negative spread
d1 = returns(130, 900, 100, 0.10, 0.40)["roe"] - returns(120, 900, 100, 0.10, 0.40)["roe"]
d0 = 130 * 0.6 / 1000 - 120 * 0.6 / 1000
assert close(d1 / d0, 10.0, 1e-9)                                         # (5.22): swing 1 + D/E
assert close(588 * (1 - 107 / 521) / (142 + 1294 + 1434), 0.163, 5e-4)   # Polaris ROIC, p. 55
assert close(95.28 / 6.69, 14.2, 5e-2)                                    # Polaris P/E (5.23), p. 57

# ---- cash flows (6.1), (6.5)-(6.13) -------------------------------------------------------
cfo = 6321 + 12815 - 1341 + 42 - 104 - 1063                               # (6.1), slide 58
cfi = -5300 - 16204 + 11941 - 12263
cff = 277 + 78527 - 72663 + 492 - 669 - 412
assert (cfo, cfi, cff) == (16670, -21826, 5552)
assert cfo + cfi + cff - 222 == 174 and 22943 + 174 == 23117


def fcf(ebit, tau, dep, capex, dnwc):
    """Eq. (6.6): unlevered free cash flow."""
    return ebit * (1 - tau) + dep - capex - dnwc


def fcfe(fcf_, interest, tau, net_borrowing):
    """Eq. (6.7): FCF minus after-tax interest plus net borrowing."""
    return fcf_ - interest * (1 - tau) + net_borrowing


dnwc = 1341 - 42 + 104
f = fcf(9193, tau_gm, 12815, 5300, dnwc)
fe = fcfe(f, 1098, tau_gm, 277 + 78527 - 72663)
assert dnwc == 1403 and close(f, 13290.4, 0.05) and close(fe, 18574.0, 0.05)
assert close(f - 1098 * (1 - tau_gm), 6321 + 12815 - 5300 - dnwc, 1e-9)  # (6.8)

# Ross, Brasil S/A (pp. 38-41): (6.11)-(6.13)
tau_r = 212 / (694 - 70)
f_r = fcf(694, tau_r, 65, 130, 330)
cf_d, cf_e = 70 - 46, 103 - 40
assert close(f_r, 63.22, 5e-3) and close(tau_r * 70, 23.78, 5e-3)
assert close(f_r + tau_r * 70, 87, 1e-9) and cf_d + cf_e == 87          # (6.11), (6.13)
assert close(fcfe(f_r, 70, tau_r, 46), cf_e, 1e-9)                      # (6.7) reproduces Ross's 63

# ---- reuse: the list's own checker ----------------------------------------------------------
root = pathlib.Path.cwd()
chk = root / "Listas" / "lista-r1-accounting-capital-structure-solutions_check.py"
out = subprocess.run([sys.executable, "-I", str(chk)], capture_output=True, text=True, check=True).stdout
assert out.startswith("PASS"), out
print("L01 python: all asserts pass;", "Lista R1 checker:", out.strip())
```

## Links

- The notes each section checks: [[L01-01-balance-sheet-view]] (Ross identity), [[L01-02-balance-sheet-items]],
  [[L01-03-book-vs-market-leverage]], [[L01-04-income-statement]], [[L01-05-ratios-dupont-roic]],
  [[L01-06-cash-flows-fcf]]; every equation listed in [[L01-07-formulas]].
- Reused checker: `Listas/lista-r1-accounting-capital-structure-solutions_check.py` (solutions:
  [PDF](../../Listas/lista-r1-accounting-capital-structure-solutions.pdf)).
- Code conventions: [[../../rules/lang-python|rules/lang-python]].
