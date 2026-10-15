"""Scenes group 2 (Act I, second half) for aula-01-what-is-corporate-finance."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scenes_common import *
# ---- scenes ----
from video_explainer import label_near  # not re-exported by scenes_common


def _g2_staged(group, first=1):
    """Hide every element of `group` after the first `first`, so the whole layout can be
    shown once (positions fixed) and its parts revealed one per step with _g2_on."""
    for m in group[first:]:
        m.set_opacity(0)
    return group


def _g2_on(mob):
    """Reveal one element hidden by _g2_staged."""
    return [mob.animate.set_opacity(1)]


def _g2_bar(pct, colour, caption, scale=0.065):
    """One bar of a two-bar comparison: rectangle, value above, caption below."""
    bar = Rectangle(width=1.6, height=pct * scale, color=colour, fill_color=colour,
                    fill_opacity=1, stroke_width=0)
    val = Text(f"{pct}%", font_size=30, color=colour).next_to(bar, UP, buff=0.18)
    cap = Text(caption, font_size=20, color=WHITE, line_spacing=0.8) \
        .next_to(bar, DOWN, buff=0.25)
    return VGroup(bar, val, cap)


def _g2_box(text, colour, width=2.2, height=0.75, size=22):
    """A filled box with a label inside -- one node of an org chart."""
    box = RoundedRectangle(width=width, height=height, corner_radius=0.1, color=colour,
                           fill_color=colour, fill_opacity=1, stroke_width=0)
    lab = Text(text, font_size=size, color=WHITE, line_spacing=0.8).move_to(box)
    return VGroup(box, lab)


def _g2_dots(rows, cols, colour=OUT, buff=0.32, radius=0.09):
    """A grid of small shareholders."""
    return VGroup(*[Dot(radius=radius, color=colour) for _ in range(rows * cols)]) \
        .arrange_in_grid(rows, cols, buff=buff)


class BeatGrocer(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGrocer")
        tools = _g2_staged(bullets([
            "1.  Monetary compensation: salary, bonus, shares, stock options",
            "2.  Implicit incentives: the threat of firing, takeover, bankruptcy",
            "3.  Monitoring: by the board and by large investors",
            "4.  Competition in the product market"], size=26, buff=0.45))
        s = Stack(st, size=38, rows=4)
        b.step(st.show("title", title("Tirole, section 1.2: four instruments")), t=0.8, hold=1)
        b.step(st.show("main", tools), t=1.0, hold=2)
        b.step(_g2_on(tools[1]), t=0.6, hold=2)
        b.step(_g2_on(tools[2]), t=0.6, hold=1.5)
        b.step(_g2_on(tools[3]), t=0.6, hold=1.5)
        b.step(st.show("note", note("how strong are they in practice? Let us write it out")),
               t=0.7, hold=3)
        b.step(st.show("title", title("Jensen and Murphy: the 250 largest US public firms")),
               t=0.8, hold=2)
        b.step(s.add(r"\text{median CEO stake} = 0.25\%"), t=1.0, hold=3)
        b.step(s.add(r"\Delta W = 1000 \text{ dollars of shareholder wealth}"), t=1.0, hold=2)
        b.step(s.add(r"\Delta(\text{CEO's pocket}) = 3.25 \text{ dollars}"), t=1.0, hold=2)
        b.step(st.show("note", note("shares, options, this year's and next year's salary, "
                                    "the chance of dismissal")), t=0.7, hold=3)
        b.step(s.add(r"\frac{3.25 \text{ dollars}}{1000 \text{ dollars}} \approx 0.3\%"),
               t=1.0, hold=4)
        b.step(st.show("note", note("a grocer who keeps 0.3 cents of each extra dollar "
                                    "and gives 99.7 cents away")), t=0.7, hold=4)
        b.step(st.show("note", note("... would start eating the apples on the fruit stand",
                                    colour=FOCUS)), t=0.7, hold=4)
        b.step(st.show("title", title("Two caveats from the book")), t=0.8, hold=1)
        b.step(st.show("main", table(
            ["study", "CEO's gain per 1,000 dollars"],
            [("Jensen and Murphy", "3.25 dollars"),
             ("Hall and Liebman, mean", "25 dollars"),
             ("Hall and Liebman, median", "5.30 dollars")],
            col_widths=[4.6, 4.6], cell_colours={(1, 1): KEEP, (2, 1): KEEP})),
            t=1.0, hold=4)
        b.step(st.show("note", note("and a stake can be too large: a risk-averse manager "
                                    "refuses risky but valuable projects", colour=BROKEN)),
               t=0.7, hold=4)
        b.step(st.show("title", title("Not incentives or no incentives, but how much")),
               t=0.8, hold=2)
        b.step(st.show("main", Text("How much of the pie must the insider keep?",
                                    font_size=40, color=FOCUS)), t=1.0, hold=5)
        b.run()


class BeatOptions(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatOptions")
        ax, panel = axes_panel([0, 10, 1], [0, 10, 1], x_label="share price P at payout",
                               y_label="manager's payoff", width=6.4, height=4.2)
        show_panel = st.show("main", panel)
        panel.shift(LEFT * 2.2)            # leave room on the right for the line labels
        share = ax.plot(lambda x: x, x_range=[0, 10], color=INS, stroke_width=5)
        option = VGroup(Line(ax.c2p(0, 0), ax.c2p(5, 0), color=FOCUS, stroke_width=7),
                        Line(ax.c2p(5, 0), ax.c2p(10, 5), color=FOCUS, stroke_width=5))
        many = DashedLine(ax.c2p(5, 0), ax.c2p(10, 8), color=FOCUS, stroke_width=4)
        kink = Dot(ax.c2p(5, 0), color=FOCUS, radius=0.07)
        water = Rectangle(width=ax.c2p(5, 0)[0] - ax.c2p(0, 0)[0],
                          height=ax.c2p(0, 10)[1] - ax.c2p(0, 0)[1],
                          stroke_width=0, fill_color=BROKEN, fill_opacity=0.18) \
            .move_to(ax.c2p(2.5, 5)).set_z_index(-1)
        share_lab = label_near(share.get_end(), Text("straight share: pays P", font_size=22,
                                                     color=INS))
        opt_lab = label_near(option[1].get_end(), MathTex(r"\max(0,\, P - P^S)",
                                                          font_size=34, color=FOCUS))
        many_lab = label_near(many.get_end(), Text("same budget, more options",
                                                   font_size=22, color=FOCUS))
        strike_lab = label_near(kink, MathTex("P^S", font_size=34, color=FOCUS), UP, buff=0.2)
        water_lab = Text("under water", font_size=24, color=BROKEN) \
            .move_to(ax.c2p(2.5, 8.8))

        b.step(st.show("title", title("Which kind of stake? Shares versus options")),
               t=0.8, hold=2)
        b.step(show_panel, t=1.0, hold=4)
        b.step([Create(share)], t=1.2, hold=2)
        b.step(st.add_to("main", share_lab), t=0.6, hold=1)
        b.step(st.show("note", note("every real of extra value moves her pocket "
                                    "by the same amount")), t=0.7, hold=2)
        b.step([Create(option)], t=1.2, hold=3)
        b.step(st.add_to("main", VGroup(kink, strike_lab)), t=0.6, hold=2)
        b.step(st.add_to("main", opt_lab), t=0.6, hold=4)
        b.step(st.show("note", note("an option is cheaper than a share, so the same budget "
                                    "buys many more of them")), t=0.7, hold=2)
        b.step([Create(many)], t=1.0, hold=1)
        b.step(st.add_to("main", many_lab), t=0.6, hold=1)
        b.step(st.show("note", note("per real spent, options give stronger incentives "
                                    "near the top", colour=KEEP)), t=0.7, hold=4)
        b.step(st.add_to("main", water), t=0.8, hold=1)
        b.step(st.add_to("main", water_lab), t=0.6, hold=2)
        b.step(st.show("note", note("nothing to lose from a wild gamble: "
                                    "the gamble for resurrection", colour=BROKEN)),
               t=0.7, hold=3)
        b.step(st.show("note", note("repricing: Ascend Communications fell from 80 to 23 "
                                    "dollars, and the strikes were cut")), t=0.7, hold=4)
        b.step(st.show("note", note("in 2002, over half of all stock options "
                                    "were under water")), t=0.7, hold=4)
        b.step(st.show("title", title("In bad states, the slice points the other way")),
               t=0.8, hold=2)
        b.step(st.show("note", note("the design of the insider's slice is itself "
                                    "part of the problem", colour=FOCUS)), t=0.7, hold=3)
        b.run()


class BeatWatchers(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatWatchers")
        bars = VGroup(_g2_bar(52, BROKEN, "financially\ndistressed"),
                      _g2_bar(19, MUTED, "equally poor returns,\nno distress")) \
            .arrange(RIGHT, buff=2.4, aligned_edge=DOWN)
        base = Line(bars.get_corner(DL) + LEFT * 0.6, bars.get_corner(DR) + RIGHT * 0.6,
                    color=GREY).align_to(bars[0][0], DOWN)
        chart = _g2_staged(VGroup(VGroup(base, bars[0]), bars[1]))
        head = ["active monitoring", "speculative monitoring"]
        act = [("forward-looking", ""), ("control rights: intervenes", ""),
               ("board member, bank, creditor", "")]
        both = [("forward-looking", "backward-looking"),
                ("control rights: intervenes", "no control: prices and exit"),
                ("board member, bank, creditor", "analyst, rating agency, lender")]
        w = [5.4, 5.4]
        comp = _g2_staged(bullets(["a rival's performance is a yardstick",
                                   "a weak firm risks bankruptcy"], size=28, buff=0.5))
        b.step(st.show("title", title("Pay is one instrument; three work through watchers")),
               t=0.8, hold=2)
        b.step(st.show("title", title("Implicit incentives: the threat of replacement")),
               t=0.8, hold=1)
        b.step(st.show("note", note("turnover rises after poor performance: "
                                    "US, Germany and Japan alike")), t=0.7, hold=3)
        b.step(st.show("main", chart), t=1.0, hold=2)
        b.step(_g2_on(chart[1]), t=0.8, hold=2)
        b.step(st.show("note", note("Gilson: firms replacing senior management. "
                                    "Debt itself disciplines")), t=0.7, hold=3)
        b.step(st.show("title", title("Monitoring, split in two")), t=0.8, hold=1)
        b.step(st.show("main", table(head, act, col_widths=w, font_size=20)), t=1.0, hold=4)
        b.step(st.show("main", table(head, both, col_widths=w, font_size=20)), t=1.0, hold=5)
        b.step(st.show("title", title("The watchers have their own incentives")),
               t=0.8, hold=1)
        b.step(st.show("note", note("analysts may push the shares of firms "
                                    "their bank wants as clients")), t=0.7, hold=2)
        b.step(st.show("main", VGroup(
            Text("28 of 30", font_size=80, color=BROKEN),
            Text("Dow Jones firms, 2001: non-audit fees were more than\n"
                 "half of what they paid their accounting firms", font_size=26,
                 line_spacing=0.85)).arrange(DOWN, buff=0.4)), t=1.0, hold=4)
        b.step(st.show("title", title("Competition in the product market")), t=0.8, hold=1)
        b.step(st.show("main", comp), t=1.0, hold=1)
        b.step(_g2_on(comp[1]), t=0.6, hold=1)
        b.step(st.show("note", note("Tirole: it \"will never substitute for a proper "
                                    "governance structure\"", colour=FOCUS)), t=0.7, hold=3)
        b.run()


class BeatTwoAgencyProblems(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTwoAgencyProblems")
        # left: dispersed owners, one manager
        mgr_l = _g2_box("manager", INS)
        dots_l = _g2_dots(3, 7).next_to(mgr_l, DOWN, buff=1.3)
        cap_l = Text("many small shareholders", font_size=20, color=OUT) \
            .next_to(dots_l, DOWN, buff=0.25)
        arr_l = DoubleArrow(mgr_l.get_bottom(), dots_l.get_top(), buff=0.12, color=BROKEN)
        reg_l = Text("Anglo-Saxon", font_size=26).next_to(cap_l, DOWN, buff=0.35)
        left = VGroup(VGroup(mgr_l, dots_l, cap_l), reg_l, arr_l)
        # right: a controlling block, minority dots, the manager it watches
        mgr_r = _g2_box("manager", INS)
        ctrl = _g2_box("controlling\nshareholder", OUT, width=2.4, height=1.0, size=20)
        dots_r = _g2_dots(2, 3)
        VGroup(ctrl, dots_r).arrange(RIGHT, buff=1.4).next_to(mgr_r, DOWN, buff=1.3)
        ctrl.shift(LEFT * 0.4)
        watch = Arrow(ctrl.get_top(), mgr_r.get_bottom(), buff=0.1, color=OUT)
        cap_r = Text("minority", font_size=20, color=OUT).next_to(dots_r, DOWN, buff=0.25)
        arr_r = DoubleArrow(ctrl.get_right(), dots_r.get_left(), buff=0.12, color=BROKEN)
        reg_r = Text("continental Europe", font_size=26) \
            .next_to(VGroup(ctrl, cap_r), DOWN, buff=0.35)
        brazil = Text("... and Brazil", font_size=28, color=FOCUS) \
            .next_to(reg_r, DOWN, buff=0.3)
        right = VGroup(VGroup(mgr_r, ctrl, dots_r, watch, cap_r), reg_r, arr_r, brazil)
        pair = side_by_side(left, right, ratio=0.5)
        left.align_to(right, UP)
        _g2_staged(left)
        for m in right:
            m.set_opacity(0)
        why = _g2_staged(bullets([
            "750 French listed firms: two-thirds with significant family ownership",
            "and family ownership went with better performance",
            "Burkart et al.: with lower investor protection,\n"
            "ownership concentration is called for"], size=26, buff=0.45))
        fix = _g2_staged(bullets(["Novo Mercado: one share, one vote",
                                  "ADR cross-listing in New York: imports investor protection"],
                                 size=28, buff=0.5))
        why[2].set_color(FOCUS)
        for m in fix:
            m.set_color(KEEP)

        b.step(st.show("title", title("Two shapes of the agency problem")), t=0.8, hold=2)
        b.step(st.show("main", pair), t=1.0, hold=2)
        b.step(_g2_on(reg_l), t=0.6, hold=1)
        b.step(_g2_on(arr_l), t=0.8, hold=1)
        b.step(st.show("note", note("the conflict: manager against the shareholders "
                                    "as a group")), t=0.7, hold=2)
        b.step(_g2_on(right[0]), t=1.0, hold=2)
        b.step(_g2_on(reg_r), t=0.6, hold=1)
        b.step(_g2_on(arr_r), t=0.8, hold=1)
        b.step(st.show("note", note("controller against minority. "
                                    "Who monitors the controller?", colour=BROKEN)),
               t=0.7, hold=3)
        b.step(_g2_on(brazil), t=0.7, hold=2)
        b.step(st.show("note", note("control through voting shares; the public holds "
                                    "non-voting preferred shares")), t=0.7, hold=3)
        b.step(st.show("note", note("protection of minority shareholders: "
                                    "the Brazilian version of the problem")), t=0.7, hold=3)
        b.step(st.show("title", title("Concentration is not simply a defect")),
               t=0.8, hold=1)
        b.step(st.show("main", why), t=1.0, hold=3)
        b.step(_g2_on(why[1]), t=0.6, hold=2)
        b.step(_g2_on(why[2]), t=0.6, hold=4)
        b.step(st.show("title", title("Brazil's institutional answers")), t=0.8, hold=1)
        b.step(st.show("main", fix), t=1.0, hold=4)
        b.step(_g2_on(fix[1]), t=0.6, hold=3)
        b.step(st.show("note", note("strong protection limits squandering: lower agency "
                                    "costs, easier financing")), t=0.7, hold=4)
        b.step(st.show("main", Text("agency cost", font_size=64, color=FOCUS)),
               t=1.0, hold=3)
        b.step(st.show("note", note("in Act Four it gets a symbol")), t=0.7, hold=3)
        b.run()
