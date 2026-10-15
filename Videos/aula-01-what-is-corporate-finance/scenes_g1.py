"""Scenes group 1 (Act 0 + Act I, first half) for aula-01-what-is-corporate-finance."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scenes_common import *
# ---- scenes ----


def _g1_person(colour, label, size=20):
    """A drawn figure (head + body) with a caption underneath."""
    head = Circle(radius=0.26, color=colour, fill_opacity=0.35)
    body = RoundedRectangle(width=0.9, height=0.75, corner_radius=0.2, color=colour,
                            fill_opacity=0.35).next_to(head, DOWN, buff=0.08)
    cap = Text(label, font_size=size, color=colour).next_to(body, DOWN, buff=0.15)
    return VGroup(head, body, cap)


# ------------------------------------------------------------------ Act 0

class BeatOpen(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatOpen")
        head, w, e = ["", "thousand reais"], [3.7, 2.0], ("", "")
        r1 = ("investment", "100")
        r2 = ("expected return 0.8 × 160", "128")
        r3 = ("value created", "+28")
        r4 = ("her own money", "10")
        r5 = ("needed from outside", "90")
        cc = {(2, 1): KEEP, (3, 1): INS, (4, 1): OUT}

        def tab(*rows):
            rows = list(rows) + [e] * (5 - len(rows))
            return table(head, rows, col_widths=w, font_size=20, cell_colours=cc)

        crowd = VGroup(_g1_person(OUT, "a bank"), _g1_person(OUT, "an angel"),
                       _g1_person(OUT, "her uncle, a dentist")).arrange(RIGHT, buff=0.45)
        Stage.fit(crowd, "right")
        noes = VGroup(*[Text("no", font_size=30, color=BROKEN).next_to(p, DOWN, buff=0.3)
                        for p in crowd])

        b.step(st.show("title", title("A founder in Campinas")), t=0.8, hold=2)
        b.step(st.show("left", tab(r1)), t=0.9, hold=3)
        b.step(st.show("left", tab(r1, r2)), t=0.9, hold=5)
        b.step(st.show("left", tab(r1, r2, r3)), t=0.9, hold=4)
        b.step(st.show("note", note("nobody disputes that number")), t=0.6, hold=2)
        b.step(st.show("left", tab(r1, r2, r3, r4)), t=0.9, hold=2)
        b.step(st.show("left", tab(r1, r2, r3, r4, r5)), t=0.9, hold=2)
        b.step(st.add_to("right", crowd[0]), t=0.6, hold=1)
        b.step(st.add_to("right", crowd[1]), t=0.6, hold=1)
        b.step(st.add_to("right", crowd[2]), t=0.6, hold=2)
        b.step(st.show("note", note("every one agrees: it is a good project")), t=0.6, hold=2)
        b.step(st.add_to("right", noes), t=0.8, hold=4)
        b.step(st.show("title", title("A famous theorem says this cannot happen")),
               t=0.8, hold=4)
        b.step(st.show("note", note("a project that creates value always finds money; "
                                    "only the price is in question")), t=0.7, hold=4)
        b.step(st.show("note", note("either the theorem is wrong, or something about her "
                                    "is not in the theorem")), t=0.7, hold=4)
        b.step(st.show("title", title("Short by exactly 2 thousand", colour=FOCUS)),
               t=0.8, hold=4)
        b.step(st.show("note", note("of something that is not money", colour=FOCUS)),
               t=0.7, hold=3)
        b.step(st.show("title", title("That missing something is corporate finance")),
               t=0.8, hold=3)
        b.run()


# ------------------------------------------------------------------ Act I

class BeatTwoSides(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTwoSides")
        firm = VGroup(Rectangle(width=2.6, height=1.6, color=WHITE),
                      Text("the firm", font_size=26))
        ins = _g1_person(INS, "insiders").move_to(LEFT * 4.6)
        out = _g1_person(OUT, "outsiders").move_to(RIGHT * 4.6)
        money_a = Arrow(RIGHT * 3.6 + UP * 1.5, LEFT * 3.6 + UP * 1.5, color=OUT, buff=0)
        money = VGroup(money_a, Text("money", font_size=22, color=OUT)
                       .next_to(money_a, UP, buff=0.12))
        prom_a = Arrow(LEFT * 3.6 + DOWN * 1.5, RIGHT * 3.6 + DOWN * 1.5, color=INS, buff=0)
        prom = VGroup(prom_a, Text("promises: a share of income, repayments, a board seat",
                                   font_size=20, color=INS).next_to(prom_a, DOWN, buff=0.12))
        agent = Text("the agent", font_size=20, color=INS).next_to(ins, UP, buff=0.2)
        princ = Text("the principal", font_size=20, color=OUT).next_to(out, UP, buff=0.2)
        diagram = VGroup(firm, ins, out, money, prom, agent, princ)
        Stage.fit(diagram, "main")

        head, w, e = ["asymmetry", "the insider's edge", "our founder"], [3.2, 4.5, 4.6], \
            ("", "", "")
        a1, a2, a3 = (("adverse selection", "knows quality before signing"),
                      ("hidden knowledge", "knows the income earned"),
                      ("moral hazard", "acts where nobody can see"))
        f1, f2, f3 = ("is her market real?", "could report less success",
                      "days on the project, or not?")

        def tab(rows, cc=None):
            rows = list(rows) + [e] * (3 - len(rows))
            return table(head, rows, col_widths=w, font_size=20, cell_colours=cc)

        b.step(st.show("title", title("Two sides of one firm")), t=0.8, hold=2)
        b.step(st.add_to("main", firm), t=0.7, hold=1)
        b.step(st.add_to("main", ins), t=0.7, hold=2)
        b.step(st.add_to("main", out), t=0.7, hold=2)
        b.step(st.add_to("main", money), t=0.8, hold=1)
        b.step(st.add_to("main", prom), t=0.8, hold=4)
        b.step(st.show("note", note("Arrow-Debreu: complete markets, no taxes, no transaction "
                                    "costs, everyone knows everything")), t=0.7, hold=5)
        b.step(st.show("note", note("it “said little about the firms' financial choices "
                                    "and about their governance”")), t=0.7, hold=4)
        b.step(st.show("note", note("what the firm does is in the contract: "
                                    "nothing to govern", colour=BROKEN)), t=0.7, hold=4)
        b.step(st.show("title", title("Corporate finance refuses that assumption")),
               t=0.8, hold=2)
        b.step(st.show("note", note("insiders know what outsiders do not, and do what "
                                    "outsiders cannot see")), t=0.7, hold=3)
        b.step(st.add_to("main", princ), t=0.6, hold=2)
        b.step(st.add_to("main", agent), t=0.6, hold=2)
        b.step(st.show("title", title("Three kinds of asymmetry")), t=0.8, hold=1)
        b.step(st.show("main", tab([a1 + ("",)])), t=0.9, hold=4)
        b.step(st.show("main", tab([a1 + ("",), a2 + ("",)])), t=0.9, hold=3)
        b.step(st.show("main", tab([a1 + ("",), a2 + ("",), a3 + ("",)])), t=0.9, hold=4)
        b.step(st.show("title", title("Put our founder into each")), t=0.8, hold=1)
        b.step(st.show("main", tab([a1 + (f1,), a2 + ("",), a3 + ("",)])), t=0.9, hold=3)
        b.step(st.show("main", tab([a1 + (f1,), a2 + (f2,), a3 + ("",)])), t=0.9, hold=3)
        b.step(st.show("main", tab([a1 + (f1,), a2 + (f2,), a3 + (f3,)])), t=0.9, hold=3)
        b.step(st.show("note", note("the same hesitation, different timing: before, after, "
                                    "in between")), t=0.7, hold=4)
        b.step(st.show("main", tab([a1 + (f1,), a2 + (f2,), a3 + (f3,)],
                                   {(2, 0): FOCUS, (2, 1): FOCUS, (2, 2): FOCUS})),
               t=0.9, hold=2)
        b.step(st.show("note", note("this one turns our founder down", colour=FOCUS)),
               t=0.7, hold=3)
        b.run()


class BeatBerleMeans(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBerleMeans")
        dots = VGroup(*[Dot(radius=0.07, color=OUT) for _ in range(60)]) \
            .arrange_in_grid(rows=6, cols=10, buff=0.22).move_to(LEFT * 3.4)
        crowd = VGroup(dots, Text("tens of thousands of shareholders", font_size=20,
                                  color=OUT).next_to(dots, DOWN, buff=0.3))
        arrow = Arrow(ORIGIN, RIGHT * 2.4, color=MUTED, buff=0).next_to(dots, RIGHT, buff=0.45)
        ctl = Text("control", font_size=20, color=MUTED).next_to(arrow, UP, buff=0.1)
        mgr = _g1_person(INS, "one manager, owning almost none").next_to(arrow, RIGHT, buff=0.3)
        Stage.fit(VGroup(crowd, arrow, ctl, mgr), "main")
        s = Stack(st, size=34, rows=4)
        defn = VGroup(
            Text("Corporate governance:", font_size=30, color=WHITE),
            Text("the ways in which the suppliers of finance to corporations",
                 font_size=26, color=OUT),
            Text("“assure themselves of getting a return on their investment”",
                 font_size=28, color=OUT)).arrange(DOWN, buff=0.35)

        b.step(st.show("title", title("Berle and Means, 1932")), t=0.8, hold=2)
        b.step(st.show("note", note("the separation of ownership and control")), t=0.6, hold=2)
        # a copy: show() recentres its mobject, and the original must stay where the
        # arrow, label and manager were laid out against it (step "diagram" below)
        b.step(st.show("main", crowd.copy()), t=0.9, hold=4)
        b.step(st.show("note", note("the effort would be theirs; the gain shared with "
                                    "everybody")), t=0.7, hold=3)
        b.step(st.show("title", title("Put a number on it")), t=0.8, hold=1)
        b.step(s.add(r"\text{her stake} = 0.01\% = 10^{-4}"), t=0.9, hold=3)
        b.step(s.add(r"\text{gain from her week} = 10{,}000{,}000"), t=0.9, hold=3)
        b.step(s.add(r"\text{her share} = 10^{-4}\times 10{,}000{,}000 = 1{,}000"),
               t=1.0, hold=3)
        b.step(s.add(r"\text{cost of the week} > 1{,}000 \;\Rightarrow\; "
                     r"\text{nobody monitors}", colour=BROKEN), t=1.0, hold=3)
        b.step(st.show("note", note("monitoring is a public good among shareholders")),
               t=0.7, hold=3)
        b.step(st.show("main", VGroup(crowd, arrow, ctl, mgr)), t=1.0, hold=3)
        b.step(st.show("note", note("dispersion “creates substantial managerial "
                                    "discretion, which can be abused”")), t=0.7, hold=4)
        b.step(st.show("note", note("insiders need not act in the best interests of the "
                                    "providers of the funds", colour=FOCUS)), t=0.7, hold=4)
        b.step(st.show("title", title("Governance, as Tirole uses it")), t=0.8, hold=1)
        b.step(st.show("main", defn), t=1.0, hold=4)
        b.step(st.show("note", note("Shleifer and Vishny's definition, adopted by Tirole")),
               t=0.6, hold=2)
        b.step([defn[2].animate.set_color(FOCUS)], t=0.7, hold=3)
        b.step(st.show("note", note("not how the firm maximises value; "
                                    "not how the board is organised")), t=0.7, hold=3)
        b.step(st.show("note", note("how those who handed over the money get some of it "
                                    "back")), t=0.7, hold=3)
        b.step(st.show("note", note("the narrow, orthodox view: governance is the "
                                    "outsiders' problem", colour=OUT)), t=0.7, hold=4)
        b.run()


class BeatFourGuises(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFourGuises")
        head, w = ["guise", "what it looks like", "example"], [3.3, 4.4, 4.5]
        g = [("insufficient effort", "effort spent in the wrong places",
              "cost cuts dodged, too many boards"),
             ("extravagant investment", "pet projects, empire building",
              "oil firms drilling, late 1970s"),
             ("entrenchment", "making oneself indispensable",
              "resisting takeovers"),
             ("self-dealing", "perks and, at the extreme, theft",
              "RJR Nabisco: 10 jets, 36 pilots")]

        def tab(n, ex, cc=None):
            rows = [(r[0], r[1], r[2] if i < ex else "") for i, r in enumerate(g[:n])]
            rows += [("", "", "")] * (4 - n)
            return table(head, rows, col_widths=w, font_size=20, cell_colours=cc)

        b.step(st.show("title", title("Moral hazard comes in many guises")), t=0.8, hold=2)
        b.step(st.show("note", note("Tirole, section 1.1.1: four of them")), t=0.6, hold=1)
        b.step(st.show("main", tab(0, 0)), t=0.9, hold=2)
        b.step(st.show("main", tab(1, 0)), t=0.9, hold=3)
        b.step(st.show("note", note("not hours at the office: where the effort goes")),
               t=0.6, hold=2)
        b.step(st.show("main", tab(1, 1)), t=0.9, hold=2)
        b.step(st.show("main", tab(2, 1)), t=0.9, hold=2)
        b.step(st.show("main", tab(2, 2)), t=0.9, hold=2)
        b.step(st.show("note", note("Jensen: buying oil on Wall Street was cheaper than "
                                    "drilling for it")), t=0.6, hold=3)
        b.step(st.show("main", tab(3, 2)), t=0.9, hold=2)
        b.step(st.show("note", note("too cautious when winning, gambling for resurrection "
                                    "when losing")), t=0.6, hold=2)
        b.step(st.show("main", tab(3, 3)), t=0.9, hold=2)
        b.step(st.show("note", note("Europe and Japan: cross-holdings, double voting "
                                    "rights")), t=0.6, hold=2)
        b.step(st.show("main", tab(4, 3)), t=0.9, hold=2)
        b.step(st.show("main", tab(4, 4)), t=0.9, hold=2)
        b.step(st.show("note", note("plain theft: Maxwell's pension fund; Tyco, 2002, over "
                                    "100 million dollars", colour=BROKEN)), t=0.6, hold=3)
        b.step(st.show("title", title("What the four rows share")), t=0.8, hold=2)
        b.step(st.show("main", tab(4, 4, {(i, 0): FOCUS for i in range(4)})), t=0.9, hold=2)
        b.step(st.show("note", note("an action that cannot be written into a contract",
                                    colour=FOCUS, size=30)), t=0.8, hold=5)
        b.run()


class BeatIceberg(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatIceberg")
        water = Line(LEFT * 2.8, RIGHT * 2.8, color=MUTED, stroke_width=3)
        tip = Polygon([-0.9, 0, 0], [-0.4, 1.0, 0], [0.1, 1.3, 0], [0.7, 0.5, 0],
                      [1.0, 0, 0], color=BROKEN, fill_opacity=0.3)
        tip_l = Text("what got through", font_size=20, color=BROKEN) \
            .next_to(tip, RIGHT, buff=0.15).shift(UP * 0.35)
        sub = Polygon([-1.0, -0.05, 0], [1.0, -0.05, 0], [2.0, -1.2, 0], [1.4, -2.8, 0],
                      [-0.6, -3.2, 0], [-2.1, -2.0, 0], [-1.8, -0.8, 0],
                      color=KEEP, fill_opacity=0.2)
        sub_l = Text("the averted ones", font_size=24, color=KEEP).move_to(sub).shift(UP * 0.2)
        berg = VGroup(water, tip, tip_l, sub, sub_l)
        Stage.fit(berg, "left")

        def fact(*lines, colour=WHITE):
            return VGroup(*[Text(l, font_size=24, color=colour) for l in lines]) \
                .arrange(DOWN, buff=0.25)

        averted = ["covenants", "the board", "the auditors", "the threat of a takeover",
                   "the lender who refused"]

        def kept(n):
            return bullets(averted[:n], size=24, colour=KEEP)

        b.step(st.show("title", title("Not a list of scandals: an iceberg")), t=0.8, hold=2)
        b.step(st.add_to("left", water), t=0.6, hold=1)
        b.step(st.add_to("left", tip), t=0.7, hold=1)
        b.step(st.add_to("left", tip_l), t=0.6, hold=1)
        b.step(st.show("right", fact("CEO pay, large US firms, real terms:",
                                     "×3 from 1980 to 1994", "×2 again by 2001")),
               t=0.8, hold=4)
        b.step(st.show("right", fact("CEO pay over the average wage:", "42× in 1982",
                                     "531× in 2000", colour=BROKEN)), t=0.8, hold=4)
        b.step(st.show("right", fact("pay for luck:", "as sensitive to a lucky dollar",
                                     "as to a general dollar")), t=0.8, hold=4)
        b.step(st.show("right", fact("a large shareholder on the board",
                                     "cuts pay for luck", "by 23 to 33 per cent",
                                     colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("right", fact("WorldCom: profits overstated",
                                     "by 7.1 billion dollars", colour=BROKEN)),
               t=0.8, hold=3)
        b.step(st.add_to("left", sub), t=0.9, hold=2)
        b.step(st.show("right", kept(1)), t=0.6, hold=1)
        b.step(st.show("right", kept(2)), t=0.6, hold=1)
        b.step(st.show("right", kept(3)), t=0.6, hold=1)
        b.step(st.show("right", kept(4)), t=0.6, hold=1)
        b.step(st.show("right", kept(5)), t=0.6, hold=1)
        b.step(st.add_to("left", sub_l), t=0.7, hold=3)
        b.step(st.show("note", note("few scandals: excellent governance, or nothing left "
                                    "to steal")), t=0.7, hold=4)
        b.step(st.show("note", note("the tip tells you little about the iceberg")),
               t=0.7, hold=3)
        b.step(st.show("note", note("her lenders' refusal is one of the averted ones: "
                                    "governance working, at a cost", colour=FOCUS)),
               t=0.7, hold=5)
        b.run()
