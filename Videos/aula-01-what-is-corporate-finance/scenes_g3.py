"""Scenes group 3 (Act II: the Modigliani-Miller benchmark) for aula-01-what-is-corporate-finance."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scenes_common import *
# ---- scenes ----


def _g3_tag(stack):
    """Colour the trailing '(n)' tag of the live line MUTED (its last three glyphs)."""
    stack.group[-1][0][-3:].set_color(MUTED)


def _g3_table_rows(columns, rows, **kw):
    """A table shown with only its first row filled, plus the later rows' cells.

    Returns (first, later): `first` goes to st.show("main", ...); each VGroup in `later`
    is revealed with st.add_to("main", ...). Both tables share one geometry, so the later
    cells land exactly in the empty cells of `first`.
    """
    n = len(columns)
    full = Stage.fit(table(columns, rows, **kw), "main")
    first = Stage.fit(table(columns, [rows[0]] + [("",) * n] * (len(rows) - 1), **kw), "main")
    texts = [m for m in full if isinstance(m, Text)]
    later = [VGroup(*texts[n * (r + 1):n * (r + 2)]) for r in range(1, len(rows))]
    return first, later


def _g3_pie_cut(centre, debt_angle, r=1.8):
    """Debt slice centred at the top, equity the rest; returns (debt, equity, label points)."""
    top = PI / 2
    debt = Sector(radius=r, angle=debt_angle * DEGREES, start_angle=top - debt_angle * DEGREES / 2,
                  arc_center=centre, fill_color=OUT, fill_opacity=0.85, stroke_width=0)
    equity = Sector(radius=r, angle=TAU - debt_angle * DEGREES,
                    start_angle=top + debt_angle * DEGREES / 2,
                    arc_center=centre, fill_color=TEAL_A, fill_opacity=0.35, stroke_width=0)
    thin = debt_angle < 180
    debt_pt = centre + UP * r * (0.7 if thin else 0.45)
    eq_pt = centre + DOWN * r * (0.45 if thin else 0.75)
    return debt, equity, debt_pt, eq_pt


class BeatPie(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPie")
        b.step(st.show("title", title("Modigliani and Miller, 1958")), t=0.8, hold=2)
        b.step(st.show("note", note("Tirole: \"striking and somewhat counterintuitive\"")),
               t=0.7, hold=3)
        claim = VGroup(Text("total value of the firm", font_size=36),
                       Text("= value of all claims on its income", font_size=30, color=MUTED),
                       Text("is independent of how it is financed", font_size=36, color=FOCUS)
                       ).arrange(DOWN, buff=0.35)
        b.step(st.show("main", claim), t=0.8, hold=4)
        b.step(st.show("note", note("debt, equity, collateral, seniority, dividends: "
                                    "they only decide who gets which slice")), t=0.7, hold=5)

        # the pie, carved thin-debt, then re-carved thick-debt -- same circle, same radius
        r = 1.8
        rim = Circle(radius=r, color=WHITE, stroke_width=3)
        d1, e1, dp1, ep1 = _g3_pie_cut(ORIGIN, 50, r)
        ld = Text("debt", font_size=22, color=WHITE).move_to(dp1)
        le = Text("equity", font_size=22, color=WHITE).move_to(ep1)
        pie = VGroup(d1, e1, rim, ld, le)
        b.step(st.show("left", pie), t=1.2, hold=4)
        c = rim.get_center()
        d2, e2, dp2, ep2 = _g3_pie_cut(c, 310, r)
        b.step([Transform(d1, d2), Transform(e1, e2),
                ld.animate.move_to(dp2), le.animate.move_to(ep2)], t=1.5, hold=3)
        b.step(st.show("note", note("\"the size of the pie is unaffected by the way it is "
                                    "carved\"", colour=WHITE)), t=0.7, hold=4)

        # the assumptions, one per step
        items = ["complete markets", "no transaction costs", "no taxes",
                 "no bankruptcy costs", "decisions are contractible"]
        head = Text("under these conditions", font_size=26, color=MUTED)
        rows = [Text(i, font_size=28, color=FOCUS if k == 4 else WHITE)
                for k, i in enumerate(items)]
        Stage.fit(VGroup(head, *rows).arrange(DOWN, aligned_edge=LEFT, buff=0.38), "right")
        b.step(st.add_to("right", VGroup(head, rows[0])), t=0.6, hold=2)
        for k in range(1, 4):
            b.step(st.add_to("right", rows[k]), t=0.5, hold=2)
        b.step(st.add_to("right", rows[4]), t=0.6, hold=3)
        b.step(st.show("note", note("nobody can change the size of the pie by changing "
                                    "what they do")), t=0.7, hold=4)
        b.step(st.show("note", note("NOT needed: risk neutrality -- value each state of the "
                                    "world at its own state price")), t=0.7, hold=6)
        b.step(st.show("note", note("every unit of income goes to somebody, and markets "
                                    "let investors undo any split")), t=0.7, hold=5)
        b.step(st.show("title", title("A detonator", colour=FOCUS)), t=0.8, hold=2)
        b.step(st.show("note", note("a benchmark whose assumptions \"needed to be relaxed\" "
                                    "-- every later class relaxes one")), t=0.7, hold=5)
        b.step(st.show("note", note("first, prove it -- twice, as Tirole does on p. 78")),
               t=0.7, hold=3)
        b.run()


class BeatValueAdditivity(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatValueAdditivity")
        s = Stack(st, size=34, rows=6)
        b.step(st.show("title", title("Proof 1: value additivity (Tirole, p. 78)")),
               t=0.8, hold=2)
        b.step(st.show("note", eq(r"R:\ \text{the firm's random total income}",
                                  size=32, colour=MUTED)), t=0.7, hold=4)
        b.step(st.show("note", eq(r"D:\ \text{face value of debt} \qquad "
                                  r"\text{risk-neutral: a claim is worth its expected payoff}",
                                  size=30, colour=MUTED)), t=0.7, hold=4)
        b.step(st.show("note", eq(r"E\left(\cdot\right):\ \text{expectation, round brackets "
                                  r"(}E\text{ alone would read as equity)}",
                                  size=30, colour=MUTED)), t=0.7, hold=3)
        b.step(s.add(r"\text{equity pays } \max\left(0,\, R-D\right)"), t=1.2, hold=6)
        b.step(st.show("note", note("limited liability: when R falls short of D, "
                                    "shareholders get zero")), t=0.6, hold=2)
        b.step(s.add(r"\text{debt pays } \min\left(R,\, D\right)"), t=1.2, hold=6)
        b.step(s.add(r"R \ge D:\quad \left(R-D\right) + D = R"), t=1.2, hold=5)
        b.step(s.add(r"R < D:\quad 0 + R = R"), t=1.2, hold=4)
        b.step(s.add(r"\max\left(0,\, R-D\right) + \min\left(R,\, D\right) = R"
                     r"\quad \text{in every state}"), t=1.4, hold=5)
        b.step(st.show("note", note("the face value has cancelled out of the sum, state by "
                                    "state")), t=0.6, hold=3)
        b.step(s.add(r"V_E + V_D = E\left(\max\left(0,\, R-D\right)\right) "
                     r"+ E\left(\min\left(R,\, D\right)\right) = E\left(R\right)"),
               t=1.4, hold=5)
        b.step(s.collapse(r"V_E + V_D = E\left(R\right) \qquad \text{independent of } D"),
               t=1.2, hold=4)
        b.step(st.show("note", note("choose any leverage you like: the pie does not change")),
               t=0.6, hold=3)
        b.step(st.show("note", note("so the firm may as well issue one claim: "
                                    "100 per cent equity")), t=0.7, hold=4)
        b.step(st.show("title", title("Try it with numbers")), t=0.7, hold=1)
        b.step(st.show("note", eq(r"R \in \{0,\ 200\},\ \text{each with probability } "
                                  r"\tfrac12 \quad\Rightarrow\quad E\left(R\right) = 100",
                                  size=32, colour=WHITE)), t=0.8, hold=3)
        first, later = _g3_table_rows(
            ["face value D", "debt pays", "equity pays", "total"],
            [("80", "0 or 80: worth 40", "0 or 120: worth 60", "100"),
             ("150", "0 or 150: worth 75", "0 or 50: worth 25", "100")],
            col_widths=[2.4, 3.6, 3.6, 1.6], row_height=0.8, font_size=24,
            cell_colours={(0, 3): KEEP, (1, 3): KEEP})
        b.step(st.show("main", first), t=1.0, hold=8)
        b.step(st.add_to("main", later[0]), t=0.8, hold=8)
        b.step(st.show("note", note("the slices moved; the pie did not", colour=KEEP)),
               t=0.7, hold=3)
        b.step(st.show("title", title("Not an economic argument: an accounting identity")),
               t=0.8, hold=3)
        b.step(st.show("note", note("in the real world some income goes to nobody -- "
                                    "it is never produced", colour=BROKEN)), t=0.7, hold=4)
        b.run()


class BeatPayoutIrrelevance(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPayoutIrrelevance")
        s = Stack(st, size=32, rows=8)
        b.step(st.show("title", title("Proof 2: dividends do not matter (Tirole, p. 78)")),
               t=0.8, hold=3)
        b.step(st.show("note", eq(r"t = 0, 1, 2, \dots \qquad R_t\ \text{revenue} \qquad "
                                  r"I_t\ \text{investment} \qquad n_t\ \text{shares outstanding}",
                                  size=30, colour=MUTED)), t=0.8, hold=4)
        b.step(st.show("note", eq(r"d_t\ \text{dividend per share} \qquad "
                                  r"P_t\ \text{price, just after the dividend} \qquad "
                                  r"\beta\ \text{discount factor}",
                                  size=30, colour=MUTED)), t=0.8, hold=4)
        b.step(st.show("note", note("line one: the arbitrage condition -- price = discounted "
                                    "next dividend plus next price")), t=0.6, hold=5)
        b.step(s.add(r"P_t = \beta E\left(d_{t+1} + P_{t+1}\right) \quad (1)"), t=1.3, hold=4)
        _g3_tag(s)
        b.step(st.show("note", note("line two: the cash identity -- money in = money out")),
               t=0.6, hold=2)
        b.step(s.add(r"R_t + P_t\left(n_t - n_{t-1}\right) = n_{t-1} d_t + I_t \quad (2)"),
               t=1.3, hold=5)
        _g3_tag(s)
        b.step(st.show("note", note("in: revenue + new shares sold.  out: dividends on the "
                                    "old shares + investment")), t=0.6, hold=4)
        b.step(s.add(r"V_t \equiv n_t P_t"), t=1.0, hold=3)
        b.step(st.show("note", eq(r"\text{multiply (1) by } n_t", size=30, colour=MUTED)),
               t=0.6, hold=1)
        b.step(s.add(r"V_t = \beta E\left(n_t d_{t+1} + n_t P_{t+1}\right)"), t=1.3, hold=4)
        b.step(st.show("note", eq(r"\text{the step that matters: (2) at } t+1, "
                                  r"\text{ solved for total dividends}",
                                  size=30, colour=MUTED)), t=0.6, hold=2)
        b.step(s.add(r"n_t d_{t+1} = R_{t+1} + P_{t+1}\left(n_{t+1} - n_t\right) - I_{t+1}"),
               t=1.3, hold=5)
        b.step(st.show("note", note("substitute into line four")), t=0.6, hold=1)
        b.step(s.add(r"V_t = \beta E\left(R_{t+1} + P_{t+1}\left(n_{t+1} - n_t\right) "
                     r"- I_{t+1} + n_t P_{t+1}\right)"), t=1.4, hold=3)
        b.step(s.transform(r"V_t = \beta E\left(R_{t+1} - I_{t+1} + n_{t+1} P_{t+1}\right)"),
               t=1.4, hold=4)
        b.step(s.add(r"V_t = \beta E\left(R_{t+1} - I_{t+1} + V_{t+1}\right)"), t=1.3, hold=5)
        b.step(st.show("note", eq(r"\text{repeat for } V_{t+1},\ V_{t+2},\ \dots"
                                  r"\ \text{ by induction}", size=30, colour=MUTED)),
               t=0.6, hold=2)
        b.step(s.add(r"V_t = E\left({\textstyle\sum_{\tau \ge 1}} \beta^{\tau} "
                     r"\left(R_{t+\tau} - I_{t+\tau}\right)\right)"), t=1.4, hold=4)
        b.step(s.collapse(r"V_t = E\left(\sum_{\tau \ge 1} \beta^{\tau} "
                          r"\left(R_{t+\tau} - I_{t+\tau}\right)\right)"), t=1.2, hold=3)
        b.step(st.show("note", note("survived: revenue and investment -- the real side of "
                                    "the firm", colour=KEEP)), t=0.6, hold=4)
        b.step(st.show("note", note("disappeared: the dividend and the number of shares",
                                    colour=BROKEN)), t=0.6, hold=4)
        b.step(st.show("note", note("pay out more today, issue shares to fund the same "
                                    "investment:\nthe new holders' claim offsets the old "
                                    "holders' cash")), t=0.6, hold=6)
        b.step(st.show("title", title("Value depends only on \"real characteristics\"",
                                      colour=WHITE)), t=0.8, hold=3)
        b.step(st.show("note", note("assuming investment policy does not change when payout "
                                    "policy does", colour=FOCUS)), t=0.6, hold=4)
        b.run()


class BeatPuzzle(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatPuzzle")
        s = Stack(st, size=40, rows=3)
        b.step(st.show("title", title("Our founder, through Modigliani-Miller")), t=0.8, hold=3)
        b.step(s.add(r"I = 100, \qquad E\left(\text{return}\right) = 128"), t=1.0, hold=3)
        b.step(s.add(r"\text{NPV} = 128 - 100 = +28 > 0"), t=1.0, hold=3)
        b.step(st.show("note", note("offer investors any claim worth 90 in expectation -- "
                                    "debt or equity, it does not matter")), t=0.6, hold=4)
        b.step(st.show("note", note("investors break even; she keeps 28")), t=0.6, hold=2)
        anims = s.add(r"\Rightarrow\ \text{funded}", colour=BROKEN)
        box = SurroundingRectangle(s.group[-1], color=BROKEN, buff=0.18)
        b.step(anims + st.add_to("main", box), t=1.0, hold=3)
        cross = Cross(VGroup(s.group[-1], box), stroke_color=BROKEN, stroke_width=8)
        b.step(st.add_to("main", cross), t=0.8, hold=3)
        b.step(st.show("title", title("Our wrong first attempt", colour=BROKEN)), t=0.7, hold=2)
        b.step(st.show("note", note("nothing in either proof was mistaken -- a premise we "
                                    "used without noticing was")), t=0.6, hold=4)
        quote = Text("\"Whenever managerial decisions cannot be perfectly specified\n"
                     "contractually, the incentives given to those who pick those\n"
                     "decisions affect the firm's income -- the size of the pie --\n"
                     "and therefore the split of the pie matters.\"",
                     font_size=30, slant=ITALIC, line_spacing=1.1)
        b.step(st.show("main", quote), t=1.2, hold=6)
        b.step(st.show("note", note("Tirole, the key sentence of the chapter")), t=0.6, hold=3)
        b.step(st.show("note", note("value additivity treated R as given -- the same "
                                    "whatever the split")), t=0.6, hold=3)
        b.step(st.show("note", eq(r"\text{but her effort decides whether } R = 160 "
                                  r"\text{ or } 0, \text{ and her effort depends on her slice}",
                                  size=30, colour=WHITE)), t=0.6, hold=4)
        b.step(st.show("title", title("What outsiders can do -- each one a chapter")),
               t=0.7, hold=1)
        first, later = _g3_table_rows(
            ["remedy", "why it is not free"],
            [("covenants", "can use only public, hence coarse, information"),
             ("incentives", "costly: a large slice no longer pays investors"),
             ("monitoring", "partly a public good: undersupplied")],
            col_widths=[2.8, 7.6], row_height=0.85, font_size=24)
        b.step(st.show("main", first), t=1.0, hold=5)
        b.step(st.add_to("main", later[0]), t=0.7, hold=5)
        b.step(st.add_to("main", later[1]), t=0.7, hold=5)
        b.step(st.show("note", note("none is free, so the split of the pie always costs "
                                    "something")), t=0.6, hold=3)
        b.step(st.show("note", note("the size of the pie depends on how it is carved",
                                    colour=FOCUS, size=30)), t=0.8, hold=4)
        b.step(st.show("title", title("Do the data agree that financing matters?")),
               t=0.7, hold=3)
        b.run()
