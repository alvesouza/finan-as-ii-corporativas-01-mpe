"""Scenes group 5 (Act IV: the fixed-investment model) for aula-01-what-is-corporate-finance."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scenes_common import *
# ---- scenes ----

from video_explainer import label_near

# Parts of a Stack line written as {{...}} get their role colour: insider terms BLUE,
# outsider terms TEAL. Only exact parts are tinted, never a whole line that merely contains one.
_G5_INK = {"R_b": INS, "B": INS, "R_l": OUT, r"\mathcal P": OUT}


def _g5_tint(m):
    """Colour the {{...}} parts of a MathTex by role; returns m."""
    for part in m.submobjects:
        c = _G5_INK.get(getattr(part, "tex_string", "").strip())
        if c is not None:
            part.set_color(c)
    return m


def _g5_line(s, tex, colour=FOCUS, transform=False):
    """Stack.add / Stack.transform with role tinting of the {{...}} parts of the new line.
    For transform the tint goes on Transform's target, which is built here for that reason."""
    if not transform:
        anims = s.add(tex, colour=colour)
        _g5_tint(s.group[-1])
        return anims
    new = _g5_tint(s._place(eq(tex, size=s.size, colour=colour), len(s.group) - 1))
    return [Transform(s.group[-1], new)]


_G5_PARAMS = [("I", "investment", "100"),
              ("A", "her own assets (net worth)", "10"),
              ("I - A", "what she must borrow", "90"),
              ("R", "income on success (zero on failure)", "160"),
              ("p_H", "success probability if she behaves", "0.8"),
              ("p_L", "success probability if she shirks", "0.4"),
              ("B", "her private benefit from shirking", "20"),
              (r"\Delta p", "gain in success probability from behaving", "0.4")]


def _g5_params(n):
    """The parameter table with its first n rows filled; the symbol column is MathTex."""
    w, rh = [1.6, 6.6, 1.6], 0.5
    rows = [("", m, v) for _, m, v in _G5_PARAMS[:n]] + [("", "", "")] * (8 - n)
    grid = table(["symbol", "meaning", "value"], rows, col_widths=w, row_height=rh,
                 font_size=20, cell_colours={(6, 1): INS, (6, 2): INS})
    for r, (sym, _, _) in enumerate(_G5_PARAMS[:n], start=1):
        grid.add(MathTex(sym, font_size=28, color=INS if sym == "B" else WHITE)
                 .move_to([-sum(w) / 2 + w[0] / 2, rh * 9 / 2 - rh * (r + 0.5), 0]))
    return grid


def _g5_timeline(n):
    """Fig. 3.1: four dated events, the first n labelled."""
    xs = [-4.5, -1.5, 1.5, 4.5]
    labels = [("loan agreement", WHITE), ("investment", WHITE),
              ("moral hazard\n(unseen)", INS), ("outcome;\nmoney shared", WHITE)]
    g = VGroup(Arrow(LEFT * 5.8, RIGHT * 5.8, buff=0, color=GREY, stroke_width=3))
    for x, (txt, c) in list(zip(xs, labels))[:n]:
        tick = Line(UP * 0.18, DOWN * 0.18, color=c).move_to([x, 0, 0])
        g.add(tick, label_near(tick, note(txt, colour=c, size=24), DOWN, buff=0.3))
    return g


def _g5_axes(xr):
    """Axes for U_b against A; y runs 0..35 so the jump to 28 has headroom."""
    ax, panel = axes_panel(xr, [0, 35, 7], width=8.6, height=3.7)
    panel.add(MathTex("A", font_size=30, color=GREY).next_to(ax.x_axis, RIGHT, buff=0.2))
    panel.add(MathTex("U_b", font_size=30, color=INS).next_to(ax.y_axis, UP, buff=0.15))
    return ax, panel


def _g5_step(ax, abar, xmin, xmax):
    """(3.6): U_b = 0 below the threshold, p_H R - I = 28 from it on. Parts: lo, jump, hi,
    open dot, closed dot, threshold label -- same structure for every abar, so Transform
    between two of them moves the cliff."""
    lo = Line(ax.c2p(xmin, 0), ax.c2p(abar, 0), color=INS, stroke_width=6)
    jump = DashedLine(ax.c2p(abar, 0), ax.c2p(abar, 28), color=MUTED)
    hi = Line(ax.c2p(abar, 28), ax.c2p(xmax, 28), color=INS, stroke_width=6)
    hole = Circle(radius=0.08, color=INS, stroke_width=4).set_fill(BLACK, 1) \
        .move_to(ax.c2p(abar, 0))
    shut = Dot(ax.c2p(abar, 28), color=INS, radius=0.09)
    lab = label_near(Dot(ax.c2p(abar, 0), radius=0.01),
                     eq(rf"\bar A = {abar}", size=28), DOWN, buff=0.28)
    return VGroup(lo, jump, hi, hole, shut, lab)


def _g5_founder(ax, x, funded=False):
    """The founder: RED on the zero segment while rationed, GREEN on the 28 segment."""
    c = KEEP if funded else BROKEN
    d = Dot(ax.c2p(x, 28 if funded else 0), color=c, radius=0.12)
    return VGroup(d, label_near(d, eq(f"A = {x}", size=28, colour=c), UP, buff=0.15))


def _g5_npv(ax, xmax):
    """The height of the jump, labelled once above the right end of the upper segment."""
    return label_near(Dot(ax.c2p(xmax, 28), radius=0.01),
                      eq(r"p_H R - I = 28", size=28, colour=INS), UP, buff=0.2)


def _g5_chart(xr, abar=12, fx=10, funded=False):
    """The whole step chart as one group: (ax, group, step, founder)."""
    ax, panel = _g5_axes(xr)
    step = _g5_step(ax, abar, xr[0], xr[1])
    who = _g5_founder(ax, fx, funded)
    return ax, VGroup(panel, step, who, _g5_npv(ax, xr[1])), step, who


def _g5_pie():
    """R = 160 carved: BLUE R_b >= 50 kept by her, TEAL the 110 investors can be promised."""
    a = TAU * 50 / 160
    pie = VGroup(Sector(radius=1.5, angle=a, start_angle=PI / 2, color=INS, fill_opacity=0.85),
                 Sector(radius=1.5, angle=TAU - a, start_angle=PI / 2 + a, color=OUT,
                        fill_opacity=0.85))
    keys = VGroup(
        VGroup(eq(r"R_b \ge 50", size=34, colour=INS), note("she must keep", colour=INS))
        .arrange(RIGHT, buff=0.3),
        VGroup(eq(r"R - \frac{B}{\Delta p} = 110", size=34, colour=OUT),
               note("all investors can\nbe promised", colour=OUT)).arrange(RIGHT, buff=0.3),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    return VGroup(pie, keys).arrange(DOWN, buff=0.45)


class BeatSetup(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatSetup")
        b.step(st.show("title", title("Act IV: the fixed-investment model (Tirole, section 3.2)")),
               t=0.8, hold=2)
        b.step(st.show("note", note("Holmström and Tirole: the workhorse model of credit "
                                    "rationing")), t=0.7, hold=3)
        b.step(st.show("note", note("notation: R is now the income on success, "
                                    "not total revenue")), t=0.7, hold=3)
        b.step(st.show("title", title("The parameters, in thousands of reais")), t=0.8, hold=1)
        b.step(st.show("main", _g5_params(2)), t=1.0, hold=3)
        b.step(st.show("main", _g5_params(3)), t=0.8, hold=2)
        b.step(st.show("main", _g5_params(4)), t=0.8, hold=3)
        b.step(st.show("note", note("after the money is raised, she chooses how to behave")),
               t=0.7, hold=2)
        b.step(st.show("main", _g5_params(6)), t=0.8, hold=4)
        b.step(st.show("main", _g5_params(7)), t=0.8, hold=3)
        b.step(st.show("note", note("an easier life, a pet project, a friend hired as "
                                    "supplier -- and investors cannot see her choice",
                                    colour=INS)), t=0.7, hold=4)
        b.step(st.show("main", _g5_params(8)), t=0.8, hold=3)
        b.step(st.show("title", title("The timeline (Fig. 3.1)")), t=0.8, hold=1)
        b.step(st.show("main", _g5_timeline(1)), t=0.9, hold=2)
        b.step(st.show("main", _g5_timeline(2)), t=0.7, hold=2)
        b.step(st.show("main", _g5_timeline(3)), t=0.7, hold=2)
        b.step(st.show("main", _g5_timeline(4)), t=0.7, hold=2)
        b.step(st.show("note", note("risk-neutral  |  interest rate zero  |  limited "
                                    "liability  |  competitive lenders")), t=0.8, hold=4)
        b.step(st.show("note", note("no insurance motive, no discounting -- and if it can "
                                    "be financed at all, she gets all the surplus")),
               t=0.8, hold=6)
        s = Stack(st, size=40, rows=2)
        b.step(st.show("title", title("Two assumptions, checked with our numbers")),
               t=0.8, hold=1)
        b.step(s.add(r"(3.1)\quad p_H R - I = 128 - 100 = 28 > 0", colour=KEEP), t=1.1,
               hold=4)
        b.step(_g5_line(s, r"(3.2)\quad p_L R - I + {{B}} = 64 - 100 + 20 = -16 < 0"),
               t=1.1, hold=5)
        b.step([s.group[0].animate.set_color(KEEP)] +
               st.show("note", note("investors want her to behave. Can they make her?",
                                    colour=FOCUS)), t=0.8, hold=3)
        b.run()


class BeatIncentive(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatIncentive")
        b.step(st.show("title", title("The contract: a sharing rule")), t=0.8, hold=1)
        b.step(st.show("main", _g5_tint(eq(r"\text{success: } {{R_b}} + {{R_l}} = R"
                                           r"\qquad \text{failure: } 0", size=46))),
               t=1.1, hold=3)
        b.step(st.show("note", note("b for borrower, l for lenders. On failure there is "
                                    "nothing -- and she cannot be made to pay")), t=0.8, hold=4)
        s = Stack(st, size=34, rows=6)
        b.step(st.show("title", title("Her incentive constraint")), t=0.8, hold=1)
        b.step(_g5_line(s, r"p_H\,{{R_b}} \;\ge\; p_L\,{{R_b}} + {{B}}"
                           r"\qquad (\text{IC}_b)"), t=1.2, hold=5)
        b.step(st.show("note", note("behaving must pay her at least as much as "
                                    "misbehaving")), t=0.7, hold=3)
        b.step(_g5_line(s, r"(\Delta p)\,{{R_b}} \;\ge\; {{B}}"), t=1.1, hold=3)
        b.step(_g5_line(s, r"{{R_b}} \;\ge\; \frac{B}{\Delta p}"), t=1.1, hold=2)
        b.step(_g5_line(s, r"{{R_b}} \;\ge\; \frac{B}{\Delta p} = \frac{20}{0.4} = 50",
                        transform=True), t=1.1, hold=3)
        b.step(st.show("note", note("she must keep at least 50 of the success income -- "
                                    "or shirking pays her better", colour=INS)),
               t=0.8, hold=5)
        b.step(st.show("note", note("why not fine her on failure? Limited liability: "
                                    "failure leaves nothing to take")), t=0.8, hold=5)
        b.step(st.show("note", note("the only lever is the reward on success -- the floor "
                                    "at zero makes incentives expensive")), t=0.8, hold=5)
        b.step(_g5_line(s, r"{{R_l}} \;\le\; R - \frac{B}{\Delta p} = 160 - 50 = 110"),
               t=1.2, hold=4)
        b.step(st.show("note", note("the most lenders can be promised on success")),
               t=0.7, hold=2)
        b.step(_g5_line(s, r"{{\mathcal P}} \equiv p_H\left(R - \frac{B}{\Delta p}\right)"),
               t=1.2, hold=3)
        b.step(_g5_line(s, r"{{\mathcal P}} \equiv p_H\left(R - \frac{B}{\Delta p}\right)"
                           r" = 0.8 \times 110 = 88", transform=True), t=1.1, hold=3)
        b.step(st.show("note", note("pledgeable income: paid only on success, with "
                                    "probability 0.8", colour=OUT)), t=0.7, hold=3)
        b.step(_g5_line(s, r"p_H R = 128 \quad\text{vs}\quad {{\mathcal P}} = 88"),
               t=1.1, hold=3)
        b.step(_g5_line(s, r"p_H R - {{\mathcal P}} = 128 - 88 = 40 = \frac{p_H B}{\Delta p}",
                        transform=True), t=1.2, hold=4)
        b.step(st.show("note", note("the agency rent: what must stay with her for the "
                                    "project to work at all", colour=INS)), t=0.8, hold=4)
        b.step(st.show("title", title("Of 128 expected, only 88 can be promised to anyone "
                                      "else", colour=FOCUS)), t=0.8, hold=4)
        b.run()


class BeatThreshold(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatThreshold")
        s = Stack(st, size=34, rows=6)
        b.step(st.show("title", title("The lenders' question")), t=0.8, hold=1)
        b.step(st.show("note", note("they put in I - A, and get back at most the pledgeable "
                                    "income", colour=OUT)), t=0.7, hold=3)
        b.step(_g5_line(s, r"{{\mathcal P}} \;\ge\; I - A \qquad (\text{IR}_l)"),
               t=1.1, hold=3)
        b.step(st.show("note", note("individual rationality for the lenders")), t=0.7, hold=2)
        b.step(s.add(r"p_H\left(R - \frac{B}{\Delta p}\right) \;\ge\; I - A"), t=1.1, hold=3)
        b.step(s.add(r"A \;\ge\; I - p_H R + \frac{p_H B}{\Delta p}"), t=1.1, hold=4)
        b.step(s.add(r"A \;\ge\; \bar A \equiv \frac{p_H B}{\Delta p} - (p_H R - I)"
                     r"\qquad (3.3)"), t=1.2, hold=3)
        b.step(st.show("note", note("the agency rent, minus the net present value")),
               t=0.7, hold=3)
        b.step(s.add(r"\bar A = 40 - 28 = 12"), t=1.0, hold=3)
        b.step(s.add(r"A = 10"), t=0.8, hold=2)
        b.step(_g5_line(s, r"A = 10 \;<\; \bar A = 12", colour=BROKEN, transform=True),
               t=1.0, hold=2)
        b.step(st.show("note", note("the lenders' constraint fails: she is turned down",
                                    colour=BROKEN)), t=0.7, hold=3)
        b.step(st.show("title", title("Two ways to see one gap")), t=0.8, hold=1)
        b.step(st.show("main", VGroup(
            eq(r"I - A = 90 \;>\; \mathcal P = 88 \qquad \text{short by } 2", size=42,
               colour=FOCUS),
            eq(r"\bar A = 12 \;>\; A = 10 \qquad \text{short by } 2", size=42,
               colour=FOCUS)).arrange(DOWN, buff=0.6)), t=1.2, hold=5)
        b.step(st.show("title", title("The threshold can be negative")) + st.clear("note"),
               t=0.8, hold=1)
        b.step(st.show("main", eq(r"p_H R - I = 50 \;\Rightarrow\; \bar A = 40 - 50 = -10",
                                  size=44, colour=FOCUS)), t=1.1, hold=3)
        b.step(st.show("note", note("a founder with nothing would be funded. Tirole assumes "
                                    "it positive: value created < rent")), t=0.8, hold=4)
        b.step(st.show("title", title("Read the threshold as a sentence")), t=0.8, hold=1)
        b.step(st.show("main", eq(r"\bar A = \underbrace{\frac{p_H B}{\Delta p}}"
                                  r"_{\text{rent she must keep}} - "
                                  r"\underbrace{(p_H R - I)}_{\text{value created}}",
                                  size=46, colour=FOCUS)), t=1.2, hold=5)
        b.step(st.show("note", note("“one only lends to the rich”", colour=FOCUS,
                                    size=32)), t=0.8, hold=4)
        b.run()


class BeatRicherFounder(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatRicherFounder")
        s = Stack(st, size=34, rows=6)
        b.step(st.show("title", title("A richer sister: same project, A = 20")), t=0.8, hold=2)
        b.step(st.show("note", note("20 is above 12, so she should be funded. Write the "
                                    "contract and check")), t=0.7, hold=3)
        b.step(s.add(r"I - A = 100 - 20 = 80"), t=1.0, hold=2)
        b.step(_g5_line(s, r"p_H\,{{R_l}} = 80 \;\Rightarrow\; {{R_l}} = \frac{80}{0.8} = 100"),
               t=1.2, hold=4)
        b.step(_g5_line(s, r"{{R_b}} = R - {{R_l}} = 160 - 100 = 60"), t=1.1, hold=3)
        b.step(_g5_line(s, r"{{R_b}} = 60 \;\ge\; \frac{B}{\Delta p} = 50 \;\checkmark"
                           r"\qquad (\text{IC}_b)", colour=KEEP), t=1.2, hold=3)
        b.step(st.show("note", note("she behaves: the contract is self-enforcing",
                                    colour=KEEP)), t=0.7, hold=2)
        b.step(s.add(r"U_b = 0.8 \times 60 - 20 = 48 - 20 = 28 = p_H R - I"), t=1.2, hold=4)
        b.step(st.show("note", note("lenders break even, so all the value created is hers")),
               t=0.7, hold=3)
        b.step(s.add(r"(1+\iota)\times 80 = 100 \;\Rightarrow\; 1+\iota = 1.25"),
               t=1.1, hold=4)
        b.step(_g5_line(s, r"1+\iota = \frac{100}{80} = 1.25 = \frac{1}{p_H} "
                           r"= \frac{1}{0.8}", transform=True), t=1.1, hold=3)
        b.step(st.show("note", note("25 per cent: pure default premium for the 20 per cent "
                                    "chance of failure")), t=0.8, hold=4)
        b.step(st.show("note", note("no penalty for being watched, no extra interest for "
                                    "the moral hazard")), t=0.8, hold=4)
        b.step(st.show("title", title("Above the threshold it costs her nothing; below it, "
                                      "everything")), t=0.8, hold=3)
        b.step(st.show("note", note("not a smooth premium -- a cliff", colour=FOCUS,
                                    size=30)), t=0.8, hold=3)
        b.run()


class BeatComparativeStatics(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatComparativeStatics")
        s = Stack(st, size=34, rows=5)
        b.step(st.show("title", title("Who gets funded? What moves the threshold?")),
               t=0.8, hold=2)
        b.step(s.add(r"\bar A = \frac{p_H B}{\Delta p} - (p_H R - I) \qquad (3.3)",
                     colour=WHITE), t=1.1, hold=3)
        b.step(s.add(r"\frac{\partial \bar A}{\partial B} = \frac{p_H}{\Delta p} "
                     r"= \frac{0.8}{0.4} = 2"), t=1.1, hold=3)
        b.step(st.show("note", note("one more thousand of private benefit: the threshold "
                                    "rises by two thousand", colour=INS)), t=0.7, hold=3)
        b.step(s.add(r"\frac{\partial \bar A}{\partial R} = -p_H = -0.8"), t=1.0, hold=2)
        b.step(st.show("note", note("less than one for one: only the success state pays")),
               t=0.7, hold=2)
        b.step(s.add(r"\frac{\partial \bar A}{\partial I} = 1"), t=0.9, hold=1)
        b.step(st.show("note", note("every extra real of investment must be found by "
                                    "somebody")), t=0.7, hold=2)
        b.step(s.add(r"\frac{p_H B}{\Delta p} = \frac{B}{\Delta p \,/\, p_H}"), t=1.1, hold=3)
        b.step(st.show("note", note("the likelihood ratio: the more success reveals about "
                                    "behaviour, the lower the threshold")), t=0.8, hold=4)
        b.step(st.show("title", title("Read across the four lines")), t=0.8, hold=1)
        b.step(st.show("main", table(
            ["funding is easier when ...", "the class that studies it"],
            [("insiders have more of their own money", "Class 7: borrowing capacity"),
             ("insiders can divert less", "Class 8: governance"),
             ("the project is more valuable or cheaper", "Classes 2-3: valuation"),
             ("outcomes reveal more about behaviour", "Class 13: monitoring")],
            col_widths=[6.4, 5.0], row_height=0.66, font_size=21)), t=1.2, hold=5)
        b.step(st.show("note", note("Class 7, the determinants of borrowing capacity: this "
                                    "list, one item at a time")), t=0.7, hold=3)
        b.run()


class BeatStep(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatStep")
        xr = [0, 30, 5]
        ax, panel = _g5_axes(xr)
        b.step(st.show("title", title("What she gets, against how much she has")),
               t=0.8, hold=1)
        b.step(st.show("main", panel), t=0.9, hold=3)
        step = _g5_step(ax, 12, xr[0], xr[1])
        lo, jump, hi, hole, shut, lab = step
        st.add_to("main", lo)
        b.step([Create(lo)], t=1.0, hold=3)
        st.add_to("main", VGroup(jump, hi, hole, shut))
        b.step([Create(jump), Create(hi), FadeIn(hole), FadeIn(shut)], t=1.3, hold=2)
        top = _g5_npv(ax, xr[1])
        b.step(st.add_to("main", top), t=0.7, hold=2)
        b.step(st.add_to("main", lab) +
               st.show("note", note("(3.6): zero below the threshold, the whole NPV from it "
                                    "on")), t=0.8, hold=3)
        who = _g5_founder(ax, 10)
        b.step(st.add_to("main", who), t=0.8, hold=3)
        b.step(st.show("note", note("two units left of the jump. Same project, same value "
                                    "-- she loses all of it", colour=BROKEN)), t=0.8, hold=4)
        b.step(st.show("note", note("investors keep their 90; the economy is 28 poorer. "
                                    "Credit rationing is inefficient")), t=0.8, hold=6)
        b.step(st.show("title", title("Two motions: move the dot, or move the cliff")),
               t=0.8, hold=1)
        b.step([Transform(who, _g5_founder(ax, 16, funded=True))] +
               st.show("note", note("more wealth of her own: the dot crosses the jump",
                                    colour=KEEP)), t=1.2, hold=2)
        b.step([Transform(who, _g5_founder(ax, 10))], t=1.0, hold=1)
        b.step([Transform(step, _g5_step(ax, 14, xr[0], xr[1]))] +
               st.show("note", note("raise B from 20 to 21: the jump moves right by two",
                                    colour=INS)), t=1.2, hold=2)
        b.step([Transform(step, _g5_step(ax, 12, xr[0], xr[1]))], t=1.0, hold=1)
        b.step([Transform(step, _g5_step(ax, 4, xr[0], xr[1])),
                Transform(who, _g5_founder(ax, 10, funded=True))] +
               st.show("note", note("success more informative (Δp 0.4 to 0.5): rent 32, "
                                    "threshold 4")), t=1.3, hold=3)
        b.step([Transform(step, _g5_step(ax, 12, xr[0], xr[1])),
                Transform(who, _g5_founder(ax, 10))], t=1.0, hold=1)
        b.step(st.show("note", note("investor protection limits what insiders can take: "
                                    "it lowers B")), t=0.8, hold=4)
        b.step(st.show("note", note("courts, disclosure, Novo Mercado, a cross-listing: "
                                    "the jump moves left, firms like hers get funded")),
               t=0.8, hold=5)
        b.run()


class BeatMMRecovered(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatMMRecovered")
        xr = [-30, 30, 10]
        ax, chart, step, who = _g5_chart(xr)
        b.step(st.show("title", title("One last move: shrink B to zero")), t=0.8, hold=2)
        b.step(st.show("main", chart), t=1.0, hold=3)
        b.step(st.show("note", note("threshold = agency rent - NPV; as B goes to zero, the "
                                    "rent goes to zero")), t=0.7, hold=2)
        b.step([Transform(step, _g5_step(ax, -8, xr[0], xr[1]))] +
               st.show("title", eq(r"B = 10:\quad \bar A = 20 - 28 = -8", size=36)),
               t=1.2, hold=1)
        b.step([Transform(step, _g5_step(ax, -18, xr[0], xr[1]))] +
               st.show("title", eq(r"B = 5:\quad \bar A = 10 - 28 = -18", size=36)),
               t=1.2, hold=1)
        b.step([Transform(step, _g5_step(ax, -28, xr[0], xr[1]))] +
               st.show("title", eq(r"\bar A = \frac{p_H \cdot 0}{\Delta p} - 28 = -28",
                                   size=36, colour=FOCUS)), t=1.4, hold=3)
        b.step([Transform(who, _g5_founder(ax, 10, funded=True))] +
               st.show("note", note("the jump is left of zero: every founder is funded, "
                                    "even one with nothing", colour=KEEP)), t=1.2, hold=4)
        b.step(st.show("note", note("nothing to gain from misbehaving: all expected income "
                                    "is pledgeable")), t=0.7, hold=4)
        b.step(st.show("title", title("Modigliani and Miller, recovered as a special case",
                                      colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("main", table(
            ["the lenders' claim", "on success", "on failure"],
            [("debt: repay 110", "110", "0"), ("equity: a share of the income", "110", "0")],
            col_widths=[5.4, 2.6, 2.6], row_height=0.7, font_size=22,
            cell_colours={(0, 1): OUT, (1, 1): OUT})) +
               st.show("title", title("Two outcomes: debt and equity are the same claim "
                                      "(section 3.2.3)")), t=1.1, hold=5)
        b.step(st.show("note", note("the model says how much can be promised in total, "
                                    "not which security")), t=0.8, hold=4)
        b.step(st.show("main", _g5_chart(xr, -28, 10, True)[1]), t=1.0, hold=2)
        b.step(st.show("title", title("One assumption separates the two worlds",
                                      colour=FOCUS)) +
               st.show("note", note("behaviour in the contract: financing irrelevant. "
                                    "Not in it: financing is the whole problem")),
               t=0.9, hold=5)
        b.run()


class BeatClose(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClose")
        b.step(st.show("title", title("The picture to keep")), t=0.8, hold=1)
        b.step(st.show("main", _g5_chart([0, 30, 5])[1]), t=1.0, hold=3)
        b.step(st.show("main", side_by_side(_g5_chart([0, 30, 5])[1], _g5_pie(),
                                            ratio=0.66)), t=1.2, hold=4)
        b.step(st.show("note", note("MM: the step sits left of zero. Corporate finance: it "
                                    "does not.", colour=FOCUS, size=28)), t=0.8, hold=5)
        b.step(st.show("note", note("Classes 2-3: valuation prices the pie")), t=0.6, hold=2)
        b.step(st.show("note", note("Classes 4-5: MM finished -- taxes and default costs")),
               t=0.6, hold=2)
        b.step(st.show("note", note("Classes 6-8: this model -- borrowing capacity, debt "
                                    "overhang, control rights")), t=0.6, hold=3)
        b.step(st.show("note", note("Liquidity: the pie needs more money midway")),
               t=0.6, hold=2)
        b.step(st.show("note", note("Asymmetric information: the lender does not know how "
                                    "big the pie is")), t=0.6, hold=2)
        b.step(st.show("note", note("Activism and takeovers: who watches the insider")),
               t=0.6, hold=2)
        b.step(st.show("note", note("The last classes: every founder in an economy near "
                                    "the jump at once")), t=0.6, hold=2)
        b.step(st.show("note", note("Practice: Tirole, exercises 3.1-3.3, p. 144 (answers "
                                    "at the back)")), t=0.7, hold=3)
        b.step(st.show("note", note("First, redo it with B = 15: minimum stake, pledgeable "
                                    "income, threshold -- funded?", colour=FOCUS)),
               t=0.7, hold=5)
        b.step(st.show("note", note("Ten against twelve. Two thousand reais of something "
                                    "that is not money.", colour=FOCUS, size=28)),
               t=0.8, hold=5)
        b.run()
