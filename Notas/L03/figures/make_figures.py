"""Figures for L03 (Topic 2B: taxes, bankruptcy costs and the static trade-off).

Run from anywhere:  python -I Notas/L03/figures/make_figures.py
Writes L03-*.png beside this file. Every curve is the slides' exact expression; numbers are
the slides' own (Aula/Topic2B.pdf, slide numbers cited) except the trade-off calibration,
which the slides leave free (uniform h, declared below and in the companion footer).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt

# Slides 28-31 project: rU 12%, rD 5%, tau 40%, g 4%, D/V 25%, FCF1 7,500.
RU, RD, TAU, G = 0.12, 0.05, 0.40, 0.04
# Trade-off page calibration (slides 41-45 give no numbers): X ~ U[50, 150], tau 35%
# (the rate of slides 2 and 33), C = 20 < X_lo, rf = 5% (the debt rate of slide 32).
XLO, XHI, TT, CC, RF = 50.0, 150.0, 0.35, 20.0, 0.05


def trade_off(K, xlo=XLO, xhi=XHI, tau=TT, c=CC, rf=RF):
    """Slides 42-44 with uniform h on [xlo, xhi]: returns (V_U, PV tax shield, PV distress, V).

    Tax-shield bracket tau*(int_xlo^K x h dx + K[1-H(K)]); distress C*H(K); both / (1+rf).
    """
    K = np.asarray(K, float)
    w = xhi - xlo
    Kc = np.clip(K, xlo, xhi)
    H = (Kc - xlo) / w
    shield = np.where(K <= xlo, tau * K,
                      tau * ((Kc ** 2 - xlo ** 2) / (2 * w) + Kc * (xhi - Kc) / w))
    vu = (1 - tau) * (xlo + xhi) / 2 / (1 + rf)
    pv_t, pv_c = shield / (1 + rf), c * H / (1 + rf)
    return vu, pv_t, pv_c, vu + pv_t - pv_c


def k_star(xlo=XLO, xhi=XHI, tau=TT, c=CC):
    """FOC tau[1-H(K*)] = C h(K*) with uniform h: K* = xhi - C/tau, never below xlo (slide 45)."""
    if tau == 0:
        return xlo                         # any K <= xlo is optimal; report the top of the set
    return max(xlo, xhi - c / tau)


def mm_taxes():
    """Slides 14-15: V_U = 600, 1000 shares, tau = 40%, debt-financed repurchase."""
    D = np.linspace(0, 600, 200)
    VL = 600 + TAU * D                    # V_L = V_U + tau D (slide 8)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.0))
    a1.plot(D, VL, color=C["main"], label="$V_L=V_U+\\tau D$")
    a1.axhline(600, color=C["ref"], ls="--", lw=1.2, label="$V_U=600$ (MM, no taxes)")
    a1.plot(D, VL - D, color=C["hi"], label="equity $E=V_L-D$")
    a1.plot(500, 800, "o", color=C["good"], ms=8)
    a1.annotate("$D=500$: $V_L=800$, $E=300$", (500, 800), xytext=(-150, 14),
                textcoords="offset points", color=C["good"])
    a1.vlines(500, 600, 800, color=C["good"], ls=":", lw=1.4)
    a1.text(510, 690, "$V_{ITS}=200$", color=C["good"])
    a1.set(xlabel="perpetual safe debt $D$", ylabel="value",
           title="MM I with corporate taxes", xlim=(0, 600), ylim=(0, 900))
    a1.legend(loc="lower left")
    P = (600 + TAU * D) / 1000            # P = V_L / initial shares (slide 15)
    a2.plot(D, P, color=C["main"])
    a2.axhline(0.6, color=C["ref"], ls="--", lw=1.2)
    a2.text(10, 0.605, "$P_0=0.6$", color=C["ref"], va="bottom")
    a2.plot(500, 0.8, "o", color=C["good"], ms=8)
    a2.annotate("$P=0.8$, $N=625$ repurchased", (500, 0.8), xytext=(-170, 10),
                textcoords="offset points", color=C["good"])
    a2.set(xlabel="perpetual safe debt $D$", ylabel="share price",
           title="Share price after announcement: $(V_U+\\tau D)/1000$", xlim=(0, 600))
    save(fig, "L03-mm-taxes")
    return float(np.interp(500, D, VL)), 500 / 0.8


def its_policies():
    """Slide 13 closed forms, V_ITS / D against g, at the slide-28 calibration."""
    g = np.linspace(0, 0.10, 200)
    cont = TAU * RD / (RU - g)                          # continuously adjusted D/E
    ann = cont * (1 + RU) / (1 + RD)                    # annually adjusted (slide prints 1+r_g)
    fig, ax = plt.subplots()
    ax.axhline(TAU, color=C["warn"], label="constant debt level: $\\tau$")
    ax.plot(g, ann, color=C["hi"], label="target $D/E$, annual: $\\frac{\\tau r_D}{r_U-g}\\frac{1+r_U}{1+r_D}$")
    ax.plot(g, cont, color=C["main"], label="target $D/E$, continuous: $\\frac{\\tau r_D}{r_U-g}$")
    ax.axvline(G, color=C["ref"], ls=":", lw=1.2)
    for y, col in [(TAU * RD / (RU - G), C["main"]), (TAU * RD / (RU - G) * 1.12 / 1.05, C["hi"])]:
        ax.plot(G, y, "o", color=col)
    ax.annotate("$g=4\\%$: 0.250 (6,250 on $D$=25,000)", (G, 0.25), xytext=(12, -22),
                textcoords="offset points", color=C["main"])
    ax.annotate("0.267", (G, 0.2667), xytext=(-36, 8), textcoords="offset points", color=C["hi"])
    ax.set(xlabel="growth rate $g$ of unlevered FCF", ylabel="$V_{ITS}/D$",
           title="How risky the shield is decides what it is worth ($r_U$=12%, $r_D$=5%, $\\tau$=40%)",
           xlim=(0, 0.10), ylim=(0, 0.75))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{100 * v:.0f}%"))
    ax.legend(loc="upper left", fontsize=9.5)
    save(fig, "L03-its-policies")
    return TAU * RD / (RU - G)


def wacc_taxes():
    """Slides 12, 16-18 (continuous rebalancing, safe debt): r_E, r_D(1-tau), r_WACC vs D/V."""
    w = np.linspace(0, 0.90, 300)
    rE = RU + w / (1 - w) * (RU - RD)                    # slide 12: r_ITS = r_U
    wacc = RU - TAU * RD * w                             # slide 18, continuous case
    fig, ax = plt.subplots()
    ax.plot(w, 100 * rE, color=C["warn"], label="equity $r_E=r_U+\\frac{D}{E}(r_U-r_D)$")
    ax.axhline(100 * RU, color=C["ref"], ls="--", lw=1.2, label="$r_U$ = pre-tax WACC")
    ax.plot(w, 100 * wacc, color=C["good"], label="after-tax WACC $r_U-\\tau r_D\\frac{D}{V}$")
    ax.axhline(100 * RD, color=C["main"], ls=":", lw=1.4, label="debt $r_D$")
    ax.axhline(100 * RD * (1 - TAU), color=C["main"], label="after-tax debt $r_D(1-\\tau)$")
    ax.axvline(0.25, color=C["ref"], ls=":", lw=1)
    ax.plot([0.25, 0.25], [100 * (RU + (RU - RD) / 3), 100 * (RU - TAU * RD * 0.25)], "o", color=C["ink"])
    ax.annotate("$D/V$=25%: $r_E$=14.33%", (0.25, 14.333), xytext=(8, 8), textcoords="offset points")
    ax.annotate("WACC 11.5%", (0.25, 11.5), xytext=(8, -16), textcoords="offset points", color=C["good"])
    ax.set(xlabel="debt-to-value $D/(D+E)$", ylabel="cost of capital (%)", ylim=(0, 40), xlim=(0, 0.9),
           title="After-tax WACC falls with leverage; $r_U$ does not move")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{100 * v:.0f}%"))
    ax.legend(loc="upper left", fontsize=9.5)
    save(fig, "L03-wacc-taxes")
    return 100 * (RU - TAU * RD * 0.25)


def apv_vs_wacc():
    """Slides 28-32: constant D/V (both methods 100,000) vs a fixed 60,000 loan (98,945)."""
    vu = 7500 / (RU - G)                                 # 93,750
    its_c = 25000 * RD * TAU / (RU - G)                  # 6,250
    ann = (1 - 1.05 ** -5) / 0.05
    its_f = 60000 * RD * TAU * ann                       # 1,200 x 4.3295 = 5,195
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.0), gridspec_kw={"width_ratios": [1.1, 1]})
    x = [0, 1, 2]
    a1.bar(0, 7500 / (0.115 - G), color=C["main"], width=0.6)
    a1.bar([1, 2], [vu, vu], color=C["ref"], width=0.6, label="$V_U$ = 93,750")
    a1.bar(1, its_c, bottom=vu, color=C["good"], width=0.6, label="$V_{ITS}$, constant $D/V$: 6,250")
    a1.bar(2, its_f, bottom=vu, color=C["warn"], width=0.6, label="$V_{ITS}$, fixed loan: 5,195")
    for xi, v in zip(x, [100000, vu + its_c, vu + its_f]):
        a1.text(xi, v + 1200, f"{v:,.0f}", ha="center")
    a1.axhline(60000, color=C["ink"], lw=1, ls="--")
    a1.text(2.35, 61000, "investment 60,000", ha="right", fontsize=9)
    a1.set_xticks(x, ["WACC at 11.5%", "APV, $D/V$=25%", "APV, 60,000 loan"])
    a1.set(ylabel="$V_L$", ylim=(0, 112000), title="Same project, three valuations")
    a1.legend(loc="lower center", fontsize=9, frameon=True, framealpha=0.92)
    t = np.arange(1, 11)
    a2.bar(t - 0.2, 500 * 1.04 ** (t - 1), width=0.4, color=C["good"], label="$D/V$ = 25%: $500(1.04)^{t-1}$")
    a2.bar(t + 0.2, np.where(t <= 5, 1200.0, 0.0), width=0.4, color=C["warn"], label="loan: 1,200 for 5 years")
    a2.set(xlabel="year $t$", ylabel="interest tax shield $\\tau r_D D_{t-1}$",
           title="The shield streams being valued", xticks=t)
    a2.legend(loc="upper right", fontsize=9)
    save(fig, "L03-apv-vs-wacc")
    return 7500 / (0.115 - G), vu + its_c, vu + its_f


def trade_off_value():
    """Slides 42-45: V(K) = V_U + [tau(int x h + K(1-H)) - C H(K)]/(1+rf), uniform h."""
    K = np.linspace(0, 180, 1801)
    vu, pv_t, pv_c, v = trade_off(K)
    ks = k_star()
    vs = float(trade_off(ks)[3])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.2))
    a1.axhline(vu, color=C["ref"], ls="--", lw=1.2, label=f"$V_U$ = {vu:.2f}")
    a1.plot(K, vu + pv_t, color=C["main"], lw=1.6, label="$V_U$ + PV tax shield (C = 0)")
    a1.plot(K, v, color=C["good"], label="$V(K)$ with C = 20")
    a1.fill_between(K, v, vu + pv_t, color=C["warn"], alpha=0.15, label="PV expected distress $CH(K)/(1+r_f)$")
    a1.axvspan(0, XLO, color=C["grid"], alpha=0.5, lw=0)
    a1.text(3, 56, "safe debt\n$K\\leq 50$ (lowest $X$)", fontsize=9, color=C["ref"])
    a1.plot(ks, vs, "o", color=C["good"], ms=8)
    a1.annotate(f"$K^*$ = {ks:.2f}, $V$ = {vs:.2f}", (ks, vs), xytext=(-30, 14),
                textcoords="offset points", color=C["good"])
    a1.set(xlabel="debt repayment $K$", ylabel="firm value", xlim=(0, 180), ylim=(55, 100),
           title="The static trade-off: $V(K)$")
    a1.legend(loc="upper left", fontsize=8.8)
    w = XHI - XLO
    H = np.clip((K - XLO) / w, 0, 1)
    h = np.where((K > XLO) & (K < XHI), 1 / w, 0.0)
    a2.plot(K, TT * (1 - H) / (1 + RF), color=C["main"], label="marginal tax benefit $\\tau[1-H(K)]/(1+r_f)$")
    a2.plot(K, CC * h / (1 + RF), color=C["warn"], label="marginal distress cost $C\\,h(K)/(1+r_f)$")
    a2.axvline(ks, color=C["good"], ls=":", lw=1.4)
    a2.text(ks + 2, 0.30, "$K^*=150-C/\\tau$", color=C["good"])
    a2.set(xlabel="debt repayment $K$", ylabel="per unit of $K$", xlim=(0, 180), ylim=(0, 0.4),
           title="Slide 45: marginal benefit = marginal cost")
    a2.legend(loc="upper right", fontsize=8.8)
    save(fig, "L03-trade-off")
    return ks, vs, float(K[np.argmax(v)])


def trade_off_statics():
    """Slide 45: K* rises with tau and falls with C (uniform h on [50, 150])."""
    taus = np.linspace(0.001, 0.5, 500)
    cs = np.linspace(0, 49, 491)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.0))
    for c, col in [(10, C["main"]), (20, C["good"]), (35, C["warn"])]:
        a1.plot(100 * taus, [k_star(tau=t, c=c) for t in taus], color=col, label=f"$C$ = {c}")
    a1.axhline(XLO, color=C["ref"], ls="--", lw=1)
    a1.text(1, XLO - 6, "corner $K^*=50$ (lowest $X$: safe debt)", color=C["ref"], fontsize=9)
    a1.set(xlabel="tax rate $\\tau$ (%)", ylabel="$K^*$", ylim=(40, 155), title="$K^*$ rises with $\\tau$")
    a1.legend(loc="upper left")
    for t, col in [(0.25, C["main"]), (0.35, C["good"]), (0.45, C["warn"])]:
        a2.plot(cs, [k_star(tau=t, c=c) for c in cs], color=col, label=f"$\\tau$ = {100 * t:.0f}%")
    a2.axhline(XHI, color=C["ref"], ls="--", lw=1)
    a2.text(1, XHI + 1.5, "$C=0$: $K^*=150$ (highest $X$: whole tax bill shielded)", color=C["ref"], fontsize=9)
    a2.axhline(XLO, color=C["ref"], ls="--", lw=1)
    a2.set(xlabel="fixed default cost $C$", ylim=(40, 160), title="$K^*$ falls with $C$")
    a2.legend(loc="center right")
    save(fig, "L03-trade-off-statics")
    return k_star(tau=0.25, c=35), k_star(tau=0.45, c=0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    apply()
    vl, n = mm_taxes()
    assert abs(vl - 800) < 1e-9 and abs(n - 625) < 1e-9                    # slides 14-15
    assert abs(its_policies() - 0.25) < 1e-12                               # 6,250 / 25,000
    assert abs(wacc_taxes() - 11.5) < 1e-9                                  # slide 29
    w, a, f = apv_vs_wacc()
    assert abs(w - 100000) < 1e-6 and abs(a - 100000) < 1e-6               # slides 29-31
    assert round(f) == 98945                                                # slide 32
    ks, vs, kgrid = trade_off_value()
    assert abs(ks - (150 - 20 / 0.35)) < 1e-12 and abs(kgrid - ks) < 0.1   # FOC = grid argmax
    assert abs(vs - 81.63265306) < 1e-6
    lo, hi = trade_off_statics()
    assert lo == XLO and hi == XHI                                          # the two corners
    print("L03 figures written:", sorted(p.name for p in pathlib.Path(__file__).parent.glob("L03-*.png")))
