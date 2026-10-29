"""Figures for L02 (Topic 2A: valuation, the NPV rule and the frictionless benchmark).

Run:  python -I Notas/L02/figures/make_figures.py
Writes L02-*.png beside this file. Every curve is the model's exact expression; every number
is the slides' (Aula/Topic2A.pdf, slide numbers in comments) or a cited book page
(Ross *Fundamentos* 9e, printed pages). Ends with assert checks on the plotted numbers.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

sys.stdout.reconfigure(encoding="utf-8")
apply()

# ---- the entrepreneur economy (slides 55-56, 65-66) ----
XS, XB = 1.05, 3.15          # project payoff: slump, boom (slide 55)
P1 = 1 / 2.8                 # boom state price, slide 65: 0.357
P2 = 1 / 1.05 - 1 / 2.8      # slump state price, slide 66: 0.595
Q = 0.5                      # probability of each state (slide 55)
RF = 0.05                    # bond 1 -> 1.05 (slide 56)


def sml_comparables():
    """Slides 22-23: rf 4%, E[rm] 12.4%; equity vs asset betas of three comparables."""
    rf, rm = 0.04, 0.124
    bE = np.array([0.75, 1.00, 1.08])
    D = np.array([0.004, 2.3, 0.21])
    E = np.array([0.096, 7.7, 0.79])
    bA = E / (D + E) * bE                     # beta_D = 0 -> beta_A = E/(D+E) beta_E (slide 23)
    bbar = bA.mean()
    r = rf + bbar * (rm - rf)
    fig, ax = plt.subplots()
    b = np.linspace(0, 1.3, 50)
    ax.plot(b, rf + b * (rm - rf), color=C["main"], label="SML: $r_f+\\beta(E[\\tilde r_m]-r_f)$")
    for i, name in enumerate("ABC"):
        ax.annotate("", (bA[i], rf + bA[i] * (rm - rf)), (bE[i], rf + bE[i] * (rm - rf)),
                    arrowprops=dict(arrowstyle="->", color=C["ref"], lw=1.2))
        ax.plot(bE[i], rf + bE[i] * (rm - rf), "o", mfc="white", mec=C["warn"], ms=8)
        ax.plot(bA[i], rf + bA[i] * (rm - rf), "o", color=C["main"], ms=6)
        ax.annotate(name, (bE[i], rf + bE[i] * (rm - rf)), xytext=(6, -14),
                    textcoords="offset points", color=C["warn"])
    ax.plot(bbar, r, "s", color=C["good"], ms=9)
    ax.annotate(f"project: $\\bar\\beta_A$ = {bbar:.2f}, r = {100 * r:.2f}%", (bbar, r),
                xytext=(-190, 22), textcoords="offset points", color=C["good"],
                arrowprops=dict(arrowstyle="-", color=C["good"], lw=0.8))
    ax.plot([], [], "o", mfc="white", mec=C["warn"], label="equity beta $\\beta_E$ (levered, observed)")
    ax.plot([], [], "o", color=C["main"], label="asset beta $\\beta_A$ (unlevered)")
    ax.axhline(rf, color=C["ref"], lw=1, ls="--")
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.set(xlabel="systematic risk $\\beta$", ylabel="expected return",
           title="Unlevering three comparables onto the SML (slides 22-23)", xlim=(0, 1.3))
    ax.legend(loc="upper left")
    save(fig, "L02-sml-comparables")
    return bA, bbar, r


def npv_profile():
    """(a) Ross Fundamentos 9e p. 297-298 mine: -60, +155, -100 -> IRRs 25% and 33 1/3%.
    (b) Slide 38: project A (-1000, +1500) vs B (+1000, -1500), both IRR 50%."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
    r = np.linspace(0, 0.6, 400)
    mine = -60 + 155 / (1 + r) - 100 / (1 + r) ** 2
    a1.plot(r, mine, color=C["main"])
    a1.axhline(0, color=C["ref"], lw=1)
    a1.fill_between(r, mine, 0, where=mine > 0, color=C["good"], alpha=0.2)
    for irr in (0.25, 1 / 3):
        a1.plot(irr, 0, "o", color=C["warn"], ms=7)
    a1.annotate("IRR 25%", (0.25, 0), xytext=(-60, 16), textcoords="offset points", color=C["warn"])
    a1.annotate("IRR 33.3%", (1 / 3, 0), xytext=(6, 16), textcoords="offset points", color=C["warn"])
    a1.plot(0.10, -60 + 155 / 1.1 - 100 / 1.21, "o", color=C["hi"])
    a1.annotate("NPV(10%) = -1.74", (0.10, -1.74), xytext=(8, -16), textcoords="offset points", color=C["hi"])
    a1.xaxis.set_major_formatter(PercentFormatter(1.0))
    a1.set(xlabel="discount rate r", ylabel="NPV", ylim=(-6, 1.5),
           title="Multiple IRRs: -60, +155, -100 (Ross p. 297)")
    nA = -1000 + 1500 / (1 + r)
    a2.plot(r, nA, color=C["good"], label="A: invest 1000, receive 1500")
    a2.plot(r, -nA, color=C["warn"], label="B: borrow 1000, repay 1500")
    a2.axhline(0, color=C["ref"], lw=1)
    a2.plot(0.5, 0, "o", color=C["ink"])
    a2.annotate("both IRRs = 50%", (0.5, 0), xytext=(-40, 20), textcoords="offset points")
    a2.plot([0.1, 0.1], [-1000 + 1500 / 1.1, 1000 - 1500 / 1.1], "o", color=C["hi"])
    a2.annotate("+363.6", (0.1, 363.6), xytext=(8, 4), textcoords="offset points", color=C["hi"])
    a2.annotate("-363.6", (0.1, -363.6), xytext=(8, -12), textcoords="offset points", color=C["hi"])
    a2.xaxis.set_major_formatter(PercentFormatter(1.0))
    a2.set(xlabel="discount rate r", title="Lending vs. borrowing (slide 38)")
    a2.legend(loc="upper right", fontsize=9)
    save(fig, "L02-npv-profile")
    return mine, nA


def payoffs():
    """Slides 44-45: debt min(A, F), equity max(A - F, 0); F = 1.05 and the project's two
    outcomes 1.05 / 3.15 (slides 55, 58)."""
    F = 1.05
    A = np.linspace(0, 4, 400)
    fig, ax = plt.subplots()
    ax.plot(A, A, color=C["ref"], lw=1, ls="--", label="assets $\\tilde A$ (45°)")
    ax.plot(A, np.minimum(A, F), color=C["main"], label="debt $\\min(\\tilde A,F)$")
    ax.plot(A, np.maximum(A - F, 0), color=C["warn"], label="equity $\\max(\\tilde A-F,0)$ = call")
    for x, lab in ((XS, "slump"), (XB, "boom")):
        ax.plot([x, x], [0, x], color=C["grid"], lw=1)
        ax.plot(x, min(x, F), "o", color=C["main"])
        ax.plot(x, max(x - F, 0), "o", color=C["warn"])
        ax.annotate(f"{lab}: D {min(x, F):.2f}, E {max(x - F, 0):.2f}", (x, max(x - F, 0)),
                    xytext=(6, 10 if lab == "boom" else 14), textcoords="offset points", fontsize=9.5)
    ax.axvline(F, color=C["hi"], lw=1, ls=":")
    ax.annotate("F = 1.05: default to the left", (F, 2.6), xytext=(6, 0), textcoords="offset points",
                color=C["hi"])
    ax.set(xlabel="value of the firm's assets at maturity, $\\tilde A$", ylabel="payoff at t = 1",
           title="Debt is concave, equity is a call (slides 44-45)", xlim=(0, 4), ylim=(0, 4))
    ax.legend(loc="upper left")
    save(fig, "L02-payoffs")
    return F


def state_prices():
    """Slides 56, 60-69: the state-price plane. Price = p2*(slump payoff) + p1*(boom payoff);
    the stock (0, 2.8) and the bond (1.05, 1.05) both cost 1, so they sit on one iso-price line."""
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    x = np.linspace(0, 4, 50)
    for price, col, lw in ((0.5, C["ref"], 0.8), (1.0, C["main"], 1.8), (1.75, C["good"], 1.8)):
        y = (price - P2 * x) / P1
        ax.plot(x, y, color=col, lw=lw)
        ax.lines[-1].set_label(f"iso-price line: {price:g}")
    pts = [((0, 2.8), "stock, price 1", C["main"], (8, 4)),
           ((1.05, 1.05), "bond, price 1", C["main"], (8, 6)),
           ((1.05, 3.15), "project, price 1.75", C["good"], (8, 4)),
           ((0, 1), "cc 1 (boom), $p_1$ = 0.357", C["hi"], (8, -14)),
           ((1, 0), "cc 2 (slump), $p_2$ = 0.595", C["hi"], (6, 8)),
           ((0, 2.1), "entrepreneur, debt: 0.75", C["warn"], (8, -4))]
    for (xs, yb), lab, col, off in pts:
        ax.plot(xs, yb, "o", color=col, ms=7)
        ax.annotate(lab, (xs, yb), xytext=off, textcoords="offset points", color=col, fontsize=9.5)
    ax.set(xlabel="payoff in the slump state", ylabel="payoff in the boom state",
           title="Pricing by state prices (slides 56-69)", xlim=(0, 3.3), ylim=(0, 4.2))
    ax.legend(loc="upper right", fontsize=9)
    ax.set_aspect("equal")
    save(fig, "L02-state-prices")
    return P1 * XB + P2 * XS


def mm2():
    """Slides 73-77, 99-100: r_E, r_D, r_A against D/E in the entrepreneur economy, extended past
    the safe region (face F > 1.05) with exact state-price values: D(F) = p1 min(3.15,F) +
    p2 min(1.05,F), E = 1.75 - D, returns from 50/50 expected payoffs."""
    F = np.linspace(1e-4, 3.15 - 1e-3, 2000)
    Dv = P1 * np.minimum(XB, F) + P2 * np.minimum(XS, F)
    A = P1 * XB + P2 * XS
    Ev = A - Dv
    rD = Q * (np.minimum(XB, F) + np.minimum(XS, F)) / Dv - 1
    rE = Q * (np.maximum(XB - F, 0) + np.maximum(XS - F, 0)) / Ev - 1
    rA = Q * (XB + XS) / A - 1
    de = Dv / Ev
    fig, ax = plt.subplots()
    m = de <= 6
    ax.axvspan(0, 1 / 0.75, color=C["good"], alpha=0.08)
    ax.axvspan(1 / 0.75, 6, color=C["warn"], alpha=0.06)
    ax.plot(de[m], rE[m], color=C["main"], label="$r_E$ (equity)")
    ax.plot(de[m], rD[m], color=C["warn"], label="$r_D$ (debt)")
    ax.axhline(rA, color=C["good"], label="$r_A=r_{WACC}$ = 20%")
    for d, lab, off in ((0.4, "D = 0.4: 24.4%", (8, -14)), (0.5, "D = 0.5: 26%", (-24, 10)),
                        (1.0, "D = 1: 40%", (-20, 10))):
        e = A - d
        ax.plot(d / e, rA + d / e * (rA - RF), "o", color=C["main"])
        ax.annotate(lab, (d / e, rA + d / e * (rA - RF)), xytext=off, textcoords="offset points",
                    fontsize=9)
    ax.text(0.15, 0.075, "safe debt: $r_D$ = 5%,\n$r_E$ linear in D/E", fontsize=9, color=C["good"])
    ax.text(2.2, 0.02, "risky debt (F > 1.05): $r_D$ rises,\n$r_E$ flat at 40%", fontsize=9, color=C["warn"])
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.set(xlabel="market debt-to-equity ratio D/E", ylabel="expected return",
           title="MM II in the entrepreneur economy (slides 75-77, 100)", xlim=(0, 6), ylim=(0, 0.45))
    ax.legend(loc="center right")
    save(fig, "L02-mm2")
    return F, Dv, Ev, rD, rE, rA


bA, bbar, r = sml_comparables()
mine, nA = npv_profile()
Fpay = payoffs()
Aval = state_prices()
F, Dv, Ev, rD, rE, rA = mm2()

# ---- checks against the printed numbers ----
assert np.allclose(bA.round(2), [0.72, 0.77, 0.85])                       # slide 23
assert round(bbar, 2) == 0.78 and round(100 * r, 2) == 10.56              # slide 23
assert abs(-60 + 155 / 1.25 - 100 / 1.25 ** 2) < 1e-9                     # Ross p. 298
assert abs(-60 + 155 / (4 / 3) - 100 / (4 / 3) ** 2) < 1e-9
assert round(-60 + 155 / 1.1 - 100 / 1.21, 2) == -1.74                    # Ross p. 297 table
assert round(-1000 + 1500 / 1.1, 1) == 363.6                              # slide 38
assert np.allclose((min(XB, Fpay), max(XB - Fpay, 0)), (1.05, 2.1))       # slide 58
assert round(P1, 3) == 0.357 and round(P2, 3) == 0.595                    # slides 65-66
assert abs(Aval - 1.75) < 1e-12 and abs(2.1 * P1 - 0.75) < 1e-12          # slide 68
safe = F <= XS
assert np.allclose(rD[safe], RF)                                          # safe region
assert np.allclose(rE[~safe], 0.40)                                       # flat region, slide 100
assert np.allclose(rE, rA + Dv / Ev * (rA - rD))                          # MM II identity
assert abs(rA - 0.20) < 1e-12                                             # slide 71
print("L02 figures written; all checks pass.")
