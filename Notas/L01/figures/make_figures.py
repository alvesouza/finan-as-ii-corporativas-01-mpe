"""Figures for L01 (Topic 1, accounting review).

Run from the repo root:  python -I Notas/L01/figures/make_figures.py
Writes L01-*.png beside this file. Every number is the slides' (Aula/Topic1.pdf, slide
numbers in comments) or a book's (printed pages, Livros/book-registry.json offsets).
Ends with assert checks on at least one plotted number per figure.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import PercentFormatter  # noqa: E402

apply()


def roe(de, roic, rd, tau):
    """L01-05 eq. (5.20): ROE = ROIC + (D/E)(ROIC - r_D(1-tau)). Rates as decimals."""
    return roic + np.asarray(de, float) * (roic - rd * (1 - tau))


def roe_leverage():
    """Slide 50 (Higgins two-firm example): EBIT 120, D+E = 1000, tau 40%, r_D 10%."""
    ebit, cap, tau = 120.0, 1000.0, 0.40
    roic = ebit * (1 - tau) / cap                      # 0.072, slide 50
    de = np.linspace(0, 10, 201)
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    cases = [(0.08, C["good"], "$r_D$ = 8%: after-tax 4.8% < ROIC"),
             (0.10, C["main"], "$r_D$ = 10% (slide): after-tax 6.0%"),
             (0.12, C["ref"], "$r_D$ = 12%: after-tax 7.2% = ROIC (flat)"),
             (0.14, C["warn"], "$r_D$ = 14%: after-tax 8.4% > ROIC")]
    for rd, col, lab in cases:
        ax.plot(de, 100 * roe(de, roic, rd, tau), color=col, lw=2.6 if rd == 0.10 else 1.8, label=lab)
    w = de / (1 + de)                                  # D/(D+E)
    roa = roic - w * 0.10 * (1 - tau)                  # NI/(D+E), assets = D+E in the example
    ax.plot(de, 100 * roa, color=C["main"], ls="--", lw=1.4, label="ROA at $r_D$ = 10%")
    ax.axhline(100 * roic, color=C["hi"], ls=":", lw=1.4)
    ax.text(10, 100 * roic + 0.5, "ROIC = 7.2%", color=C["hi"], ha="right")
    ax.plot(9, 18, "o", color=C["main"], ms=8)
    ax.annotate("Company A: D/E = 9, ROE = 18%", (9, 18), xytext=(-190, 8), textcoords="offset points",
                color=C["main"])
    ax.plot(0, 7.2, "o", color=C["good"], ms=8)
    ax.annotate("Company B: D/E = 0, ROE = 7.2%", (0, 7.2), xytext=(8, -26), textcoords="offset points",
                color=C["good"])
    ax.plot(9, 1.8, "o", mfc="white", mec=C["main"], ms=7)
    ax.annotate("A's ROA = 1.8%", (9, 1.8), xytext=(-40, 10), textcoords="offset points", color=C["main"])
    ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
    ax.set(xlabel="book debt-to-equity ratio $D/E$", ylabel="return on book equity",
           title="Leverage moves ROE by the spread ROIC $-\\,r_D(1-\\tau)$; ROIC does not move",
           xlim=(-0.2, 10), ylim=(-3, 26))
    ax.legend(loc="upper left", fontsize=8.8)
    save(fig, "L01-roe-leverage")
    return roic, float(roe(9, roic, 0.10, tau)), float(roa[180])


# Slide 48 (Higgins 10e, 2013): ROE, net margin, asset turnover, financial leverage.
DUPONT_2013 = {"Google": (14.8, 21.6, 0.54, 1.27), "JPMorgan": (8.5, 18.6, 0.04, 11.44),
               "Hyundai Motor": (15.9, 10.3, 0.65, 2.36), "Chevron": (14.4, 9.7, 0.87, 1.7)}
# Higgins 13e Table 2.1, p. 40 (2020): same columns.
DUPONT_2020 = {"Alphabet": (18.1, 22.1, 0.57, 1.44), "Citigroup": (6.1, 12.4, 0.04, 12.56),
               "Diageo": (20.8, 12.0, 0.35, 4.92), "Kroger": (27.0, 2.0, 2.72, 5.08),
               "Microsoft": (37.4, 31.0, 0.47, 2.55), "Norfolk Southern": (13.6, 20.6, 0.26, 2.57),
               "Novartis": (14.3, 16.6, 0.37, 2.33), "Polaris": (28.9, 5.8, 1.44, 3.43),
               "Target": (30.2, 4.7, 1.83, 3.55), "Wendy's": (21.4, 6.8, 0.34, 9.17)}


def dupont():
    """Eq. (5.15): ROA = margin x turnover (left); ROE = ROA x leverage (right). Iso-curves are exact."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.8))
    t = np.geomspace(0.02, 5, 200)
    for roa_ in (1, 2, 5, 10, 15):                     # log-log: iso-ROA curves are straight lines
        a1.plot(t, roa_ / t, color=C["grid"] if roa_ != 10 else C["ref"], lw=1.2, zorder=0)
        a1.text(roa_ / 36, 36, f"ROA {roa_}%", fontsize=7.5, color=C["ref"], ha="left", va="top", rotation=-38)
    lev = np.geomspace(1, 20, 200)
    for roe_ in (5, 10, 15, 20, 30):
        a2.plot(lev, roe_ / lev, color=C["grid"] if roe_ != 15 else C["ref"], lw=1.2, zorder=0)
        x = min(14, roe_ / 0.5)
        a2.text(x, roe_ / x, f"ROE {roe_}%", fontsize=7.5, color=C["ref"], ha="left", va="bottom", rotation=-38)
    off1 = {"Google": (6, -12), "Alphabet": (6, 4), "Target": (6, -10), "Chevron": (6, -13)}
    off2 = {"JPMorgan": (-62, 4), "Citigroup": (6, -10), "Polaris": (6, -11), "Target": (6, 4), "Alphabet": (6, 4), "Google": (6, -13), "Hyundai Motor": (-92, -3)}
    for data, col, ms, fs in ((DUPONT_2020, C["ref"], 5, 7.2), (DUPONT_2013, C["main"], 8, 8.8)):
        for name, (r, m, at, fl) in data.items():
            a1.plot(at, m, "o", color=col, ms=ms)
            a1.annotate(name, (at, m), xytext=off1.get(name, (5, 3)), textcoords="offset points", fontsize=fs,
                        color=col)
            a2.plot(fl, m * at, "o", color=col, ms=ms)
            a2.annotate(name, (fl, m * at), xytext=off2.get(name, (5, 3)), textcoords="offset points",
                        fontsize=fs, color=col)
    a1.set(xscale="log", yscale="log", xlabel="asset turnover, sales / assets (log)",
           ylabel="net profit margin, % (log)", title="ROA = margin × turnover", xlim=(0.03, 5), ylim=(1.5, 40))
    a2.set(xscale="log", yscale="log", xlabel="financial leverage, assets / equity (log)", ylabel="ROA, % (log)",
           title="ROE = ROA × leverage", xlim=(1, 20), ylim=(0.4, 20))
    for a in (a1, a2):
        a.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:g}"))
        a.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:g}"))
    a1.plot([], [], "o", color=C["main"], label="slide 48 (2013)")
    a1.plot([], [], "o", color=C["ref"], ms=5, label="Higgins 13e Table 2.1 (2020)")
    a1.legend(loc="lower left", fontsize=8.5)
    save(fig, "L01-dupont")
    return {k: v[1] * v[2] * v[3] for k, v in DUPONT_2013.items()}


# GM 2020, slides 39 and 58 (USD millions).
GM = dict(ebit=9193, interest=1098, pretax=8095, taxes=1774, ni=6321, da=12815, ar=-1341, ap=42,
          inv=-104, other_op=-1063, cfo=16670, capex=5300, st_debt=277, issue=78527, repay=72663)


def gm_fcf():
    """Eqs. (6.6)-(6.9) on GM 2020: returns the bridge values (USD millions)."""
    g = GM
    tau = g["taxes"] / g["pretax"]                     # 0.21915 effective rate
    nopat = g["ebit"] * (1 - tau)
    dnwc = -(g["ar"] + g["ap"] + g["inv"])             # 1341 - 42 + 104 = 1403
    fcf = nopat + g["da"] - g["capex"] - dnwc
    at_int = g["interest"] * (1 - tau)
    net_borrow = g["st_debt"] + g["issue"] - g["repay"]
    fcfe = fcf - at_int + net_borrow
    return dict(tau=tau, nopat=nopat, dnwc=dnwc, fcf=fcf, at_int=at_int, net_borrow=net_borrow, fcfe=fcfe)


def fcf_bridge():
    """Waterfall EBIT -> NOPAT -> FCF -> FCFE for GM 2020 (slides 39, 58, 60-61)."""
    b = gm_fcf()
    steps = [("EBIT", GM["ebit"], "total"), ("− τ·EBIT", -GM["ebit"] * b["tau"], "step"),
             ("NOPAT\nEBIT(1−τ)", b["nopat"], "total"), ("+ D&A", GM["da"], "step"),
             ("− capex", -GM["capex"], "step"), ("− ΔNWC", -b["dnwc"], "step"),
             ("FCF", b["fcf"], "total"), ("− interest\n×(1−τ)", -b["at_int"], "step"),
             ("+ net\nborrowing", b["net_borrow"], "step"), ("FCFE", b["fcfe"], "total")]
    fig, ax = plt.subplots(figsize=(10.4, 4.6))
    level = 0.0
    for i, (lab, v, kind) in enumerate(steps):
        if kind == "total":
            ax.bar(i, v, color=C["main"], width=0.62)
            level = v
            ax.text(i, v + 300, f"{v:,.0f}", ha="center", fontsize=9, color=C["main"], fontweight="semibold")
        else:
            lo = level + min(v, 0)
            ax.bar(i, abs(v), bottom=lo, color=C["good"] if v > 0 else C["warn"], width=0.62)
            ax.text(i, level + max(v, 0) + 300, f"{v:+,.0f}", ha="center", fontsize=9,
                    color=C["good"] if v > 0 else C["warn"])
            level += v
    ax.set_xticks(range(len(steps)), [s[0] for s in steps], fontsize=8.8)
    ax.set(ylabel="USD millions", ylim=(0, 25000),
           title=f"GM 2020: from EBIT to free cash flow (τ = {100 * b['tau']:.2f}% effective)")
    save(fig, "L01-fcf-bridge")
    return b


# Starbucks, slide 24 (27/12/2020, USD millions) and slide 25 (market cap 122.6 bn on Dec 28).
SBUX = dict(cash=5028, ar=888, inv=1472, oca=970, ca=8358, nca=21611, ta=29968, cl=7884, ncl=29989,
            tl=37872, equity=-7904, st_debt=493, cur_ltd=750, ltd=14674, lease_cur=1268, lease_lt=7755,
            ap=1051, mcap=122600)
# GPA, slide 21 (31/12/2020, BRL millions).
GPA = dict(cash=8711, ar=686, inv=6536, oca=1708, ca=17641, nca=35654, ta=53295, ap=11424, cl=18483,
           ncl=18005, tl=36488, equity=16807, borrow_cur=2309, borrow_lt=6842)


def book_vs_market():
    """Slides 24-25, 30: book vs market equity and the enterprise-value build (eq. 3.6)."""
    s = SBUX
    debt = s["st_debt"] + s["cur_ltd"] + s["ltd"]       # interest-bearing debt 15,917
    ev = s["mcap"] + debt - s["cash"]                   # 133,489
    leases = s["lease_cur"] + s["lease_lt"]             # 9,023
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw=dict(width_ratios=[1, 1.25]))
    labs = ["book assets", "total liabilities", "book equity", "market cap"]
    vals = [s["ta"], s["tl"], s["equity"], s["mcap"]]
    cols = [C["ref"], C["ref"], C["warn"], C["good"]]
    a1.bar(range(4), np.array(vals) / 1000, color=cols, width=0.6)
    for i, v in enumerate(vals):
        a1.text(i, v / 1000 + (3 if v > 0 else -9), f"{v / 1000:,.1f}", ha="center", color=cols[i],
                fontweight="semibold")
    a1.axhline(0, color=C["ink"], lw=1)
    a1.set_xticks(range(4), labs, fontsize=9)
    a1.set(ylabel="USD billions", ylim=(-16, 135), title="Starbucks 2020: book says −7.9, market says 122.6")
    a1.set_ylim(-22, 135)
    steps = [("market cap", s["mcap"], "total"), ("+ debt", debt, "step"), ("− cash", -s["cash"], "step"),
             ("EV", ev, "total"), ("+ lease\nliabilities", leases, "step"), ("EV incl.\nleases", ev + leases, "total")]
    level = 0.0
    for i, (lab, v, kind) in enumerate(steps):
        if kind == "total":
            a2.bar(i, v / 1000, color=C["main"] if i < 4 else C["hi"], width=0.6)
            level = v
            a2.text(i, v / 1000 + 2, f"{v / 1000:,.1f}", ha="center", fontsize=9,
                    color=C["main"] if i < 4 else C["hi"], fontweight="semibold")
        else:
            lo = level + min(v, 0)
            a2.bar(i, abs(v) / 1000, bottom=lo / 1000, color=C["good"] if v > 0 else C["warn"], width=0.6)
            a2.text(i, (level + max(v, 0)) / 1000 + 2, f"{v / 1000:+,.1f}", ha="center", fontsize=9,
                    color=C["good"] if v > 0 else C["warn"])
            level += v
    a2.set_xticks(range(len(steps)), [x[0] for x in steps], fontsize=8.8)
    a2.set(ylim=(0, 160), title="Enterprise value = market equity + debt − cash")
    save(fig, "L01-book-vs-market")
    return debt, ev, ev + leases


def balance_sheets():
    """Slides 21 and 24 as common-size stacks: A = L + E, NWC sign, negative book equity."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), sharey=True)
    for ax, (name, d, unit) in zip(axes, (("GPA 2020", GPA, "BRL"), ("Starbucks 2020", SBUX, "USD"))):
        ta = d["ta"]
        left = [("cash", d["cash"], C["good"]), ("receivables", d["ar"], C["hi"]),
                ("inventories", d["inv"], "#c49a1c"), ("other current", d["oca"], C["grid"]),
                ("non-current assets", d["nca"], C["ref"])]
        right = [("trade / accounts payable", d["ap"], "#d98b5f"),
                 ("other current liabilities", d["cl"] - d["ap"], "#f0c8ad"),
                 ("non-current liabilities", d["ncl"], C["main"])]
        bottom = 0.0
        for lab, v, col in left:
            ax.bar(0, 100 * v / ta, bottom=bottom, color=col, width=0.55, edgecolor="white")
            if v / ta > 0.04:
                ax.text(0, bottom + 50 * v / ta, f"{lab}\n{100 * v / ta:.1f}%", ha="center", va="center", fontsize=8)
            bottom += 100 * v / ta
        bottom = 0.0
        for lab, v, col in right:
            ax.bar(1, 100 * v / ta, bottom=bottom, color=col, width=0.55, edgecolor="white")
            if v / ta > 0.04:
                ax.text(1, bottom + 50 * v / ta, f"{lab}\n{100 * v / ta:.1f}%", ha="center", va="center", fontsize=8,
                    color="white" if col == C["main"] else C["ink"])
            bottom += 100 * v / ta
        e = 100 * d["equity"] / ta
        if e > 0:
            ax.bar(1, e, bottom=bottom, color=C["good"], width=0.55, edgecolor="white")
            ax.text(1, bottom + e / 2, f"equity\n{e:.1f}%", ha="center", va="center", fontsize=8, color="white")
        else:
            ax.bar(1, e, bottom=0, color=C["warn"], width=0.55, hatch="//", edgecolor="white")
            ax.text(1, e / 2, f"equity {e:.1f}%", ha="center", va="center", fontsize=8, color="white")
        ax.axhline(100, color=C["ink"], lw=0.8, ls=":")
        ax.axhline(0, color=C["ink"], lw=1)
        nwc = d["ca"] - d["cl"]
        ax.set_xticks([0, 1], ["assets", "liabilities + equity"])
        ax.set_title(f"{name}: NWC = {nwc:+,} {unit} m")
    axes[0].set(ylabel="% of total assets", ylim=(-32, 130))
    save(fig, "L01-balance-sheets")
    return GPA["ca"] - GPA["cl"], SBUX["ca"] - SBUX["cl"], 100 * SBUX["equity"] / SBUX["ta"]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    roic, roe_a, roa_a = roe_leverage()
    assert abs(roic - 0.072) < 1e-12 and abs(roe_a - 0.18) < 1e-12 and abs(roa_a - 0.018) < 1e-12  # slide 50
    prod = dupont()
    assert abs(prod["Google"] - 14.8) < 0.05 and abs(prod["JPMorgan"] - 8.5) < 0.05     # slide 48
    assert abs(prod["Hyundai Motor"] - 15.9) < 0.15                                    # inputs rounded on the slide
    b = fcf_bridge()
    assert abs(b["fcf"] - 13290.4) < 0.1 and abs(b["fcfe"] - 18574.0) < 0.1 and b["net_borrow"] == 6141
    assert abs((b["fcf"] - b["at_int"]) - (GM["ni"] + GM["da"] - GM["capex"] - b["dnwc"])) < 1e-6  # eq. (6.8)
    debt, ev, ev_l = book_vs_market()
    assert debt == 15917 and ev == 133489 and ev_l == 142512
    nwc_gpa, nwc_sbux, e_share = balance_sheets()
    assert nwc_gpa == -842 and nwc_sbux == 474 and abs(e_share + 26.37) < 0.01
    assert GPA["ca"] + GPA["nca"] == GPA["ta"] and GPA["tl"] + GPA["equity"] == GPA["ta"]  # slide 21
    assert SBUX["tl"] + SBUX["equity"] == SBUX["ta"]                                     # slide 24
    print("L01 figures: 5 written, all asserts pass")
