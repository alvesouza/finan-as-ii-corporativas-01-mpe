"""Scenes group 4 (Act III: the stylized facts) for aula-01-what-is-corporate-finance."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scenes_common import *
# ---- scenes ----


def _g4_fill(rows, k):
    """The first k rows, the rest blank, so a table keeps its size while it fills."""
    return list(rows[:k]) + [("",) * len(rows[0])] * (len(rows) - k)


def _g4_paint(cells, colour):
    """{(row, col): colour} for every (row, col) in `cells`."""
    return {rc: colour for rc in cells}


def _g4_bars(items, maxv, k=None, height=3.6, bar_w=1.2, gap=0.8, size=26, diff=None):
    """Bar chart from plain rectangles: items = [(label, value, colour)], first k drawn.

    An invisible frame fixes the bounding box, so re-showing with more bars never moves the
    baseline. diff=(i, lo): paint bar i from lo up to its value in BROKEN, labelled.
    """
    n = len(items)
    base_w = n * bar_w + (n - 1) * gap + 0.6
    g = VGroup(Rectangle(width=base_w, height=height + 1.4, stroke_opacity=0, fill_opacity=0)
               .move_to([0, (height + 0.6) / 2 - 0.4, 0]),
               Line(LEFT * base_w / 2, RIGHT * base_w / 2, color=MUTED))
    for i, (lab, val, col) in enumerate(items):
        x = -base_w / 2 + 0.3 + bar_w / 2 + i * (bar_w + gap)
        g.add(Text(lab, font_size=size, color=MUTED).move_to([x, -0.35, 0]))
        if k is not None and i >= k:
            continue
        h = val / maxv * height
        bar = Rectangle(width=bar_w, height=h, fill_color=col, fill_opacity=0.85,
                        stroke_width=0).move_to([x, h / 2, 0])
        g.add(bar, Text(str(val), font_size=size, color=col).next_to(bar, UP, buff=0.12))
        if diff and diff[0] == i:
            lo = diff[1] / maxv * height
            seg = Rectangle(width=bar_w, height=h - lo, fill_color=BROKEN, fill_opacity=0.95,
                            stroke_width=0).move_to([x, (h + lo) / 2, 0])
            g.add(seg, Text(f"net −{val - diff[1]}", font_size=size, color=BROKEN)
                  .next_to(seg, RIGHT, buff=0.25))
    return g


def _g4_chain(labels, colours):
    """Boxes joined by arrows, left to right."""
    boxes = VGroup(*[VGroup(RoundedRectangle(width=3.3, height=1.5, corner_radius=0.15,
                                             color=c),
                            Text(l, font_size=26, color=c, line_spacing=0.8))
                     for l, c in zip(labels, colours)]).arrange(RIGHT, buff=0.9)
    arrows = [Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.08, color=MUTED)
              for i in range(len(boxes) - 1)]
    return VGroup(boxes, *arrows)


class BeatInternalFinance(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatInternalFinance")
        head = ["", "U.S.", "U.K.", "Germany", "France", "Japan"]
        w = [2.6, 1.75, 1.75, 1.75, 1.75, 1.75]
        rows = [("retentions", "66.9", "72.0", "55.2", "44.1", "33.7"),
                ("loans", "23.1", "21.4", "21.1", "41.5", "40.7"),
                ("bonds", "9.7", "0.8", "0.7", "2.3", "3.1"),
                ("shares", "0.8", "4.9", "2.1", "10.6", "3.5")]
        row = lambda r, c=FOCUS: _g4_paint([(r, j) for j in range(6)], c)

        def tab(k, colours=None):
            return table(head, _g4_fill(rows, k), col_widths=w, row_height=0.8,
                         font_size=26, cell_colours=colours)

        b.step(st.show("title", title("Act III: how firms actually finance themselves")),
               t=0.8, hold=3)
        b.step(st.show("title", title("Tirole, Table 2.2 — Mayer (1990): % of total "
                                      "financing, 1970–85", size=26))
               + st.show("main", tab(0)), t=1.0, hold=3)
        b.step(st.show("main", tab(1)), t=1.0, hold=4)
        b.step(st.show("main", tab(2)), t=1.0, hold=4)
        b.step(st.show("main", tab(3)), t=1.0, hold=3)
        b.step(st.show("main", tab(4)), t=1.0, hold=4)
        b.step(st.show("main", tab(4, row(0, KEEP)))
               + st.show("note", note("1. internal financing (retained earnings) dominates "
                                      "in every country")), t=1.0, hold=3)
        b.step(st.show("main", tab(4, {**row(1), **row(3, MUTED)}))
               + st.show("note", note("2. bank loans: the bulk of external financing; "
                                      "new equity a small fraction")), t=1.0, hold=3)
        b.step(st.show("main", tab(4, {**row(2, MUTED), (2, 1): FOCUS}))
               + st.show("note", note("3. bond markets play a minor role, "
                                      "except in North America")), t=1.0, hold=3)
        b.step(st.show("main", tab(4, _g4_paint([(1, 4), (1, 5)], FOCUS)))
               + st.show("note", note("loans: about 41% in France and Japan, "
                                      "about 22% in the U.K. and U.S.")), t=1.0, hold=3)
        b.step(st.show("main", tab(4, {**row(0, KEEP), **row(3, MUTED)}))
               + st.show("note", note("in every column the top row beats the bottom row, "
                                      "by a wide margin")), t=1.0, hold=3)
        b.step(st.show("title", title("The order of distance"))
               + st.show("main", _g4_chain(["money the firm\nalready has", "a bank that\n"
                                            "watches closely", "strangers on a\n"
                                            "stock exchange"], [INS, OUT, OUT]))
               + st.show("note", note("first, then, and rarely")), t=1.2, hold=4)
        b.step(st.show("note", note("increasing distance between the insiders and "
                                    "the people supplying the money")), t=0.8, hold=4)
        b.step(st.show("note", note("a theory where financing does not matter "
                                    "cannot explain this order", colour=BROKEN)),
               t=0.8, hold=4)
        b.run()


class BeatNetEquity(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatNetEquity")
        flows = [("issued", 65, OUT), ("retired", 68, OUT)]
        ctry = [("U.S.", 12, OUT), ("U.K.", 9, OUT), ("France", 9, OUT), ("Japan", 8, OUT),
                ("Germany", 6, OUT)]
        b.step(st.show("title", title("The share row is even smaller than it looks")),
               t=0.8, hold=3)
        b.step(st.show("title", title("Rajan & Zingales: U.S. firms 1984–86, "
                                      "% of external financing", size=26))
               + st.show("main", _g4_bars(flows, 70, k=1)), t=1.0, hold=4)
        b.step(st.show("main", _g4_bars(flows, 70)), t=1.0, hold=4)
        b.step(st.show("main", _g4_bars(flows, 70, diff=(1, 65)))
               + st.show("note", note("65 in, 68 out: net equity issuance was negative",
                                      colour=BROKEN)), t=1.0, hold=3)
        b.step(st.show("note", note("“basically all external financing was debt” "
                                    "— Tirole")), t=0.8, hold=3)
        b.step(st.show("note", note("net external financing: 14% of operating cash flow "
                                    "plus net external financing")), t=0.8, hold=4)
        b.step(st.show("note", note("most investment was paid for with the firm's own cash",
                                    colour=INS)), t=0.8, hold=3)
        b.step(st.show("title", title("New equity, % of gross fixed-capital formation, 1999 "
                                      "(Tirole, p. 97)", size=26))
               + st.show("main", _g4_bars(ctry, 14, k=1))
               + st.show("note", note("first-time and later issues together")),
               t=1.0, hold=3)
        b.step(st.show("main", _g4_bars(ctry, 14, k=2)), t=0.8, hold=1)
        b.step(st.show("main", _g4_bars(ctry, 14, k=3)), t=0.8, hold=1)
        b.step(st.show("main", _g4_bars(ctry, 14, k=4)), t=0.8, hold=1)
        b.step(st.show("main", _g4_bars(ctry, 14, k=5)), t=0.8, hold=3)
        b.step(st.show("note", note("retained earnings and new shares: "
                                    "either way, it is shareholders' money")), t=0.8, hold=4)
        b.step(st.show("note", note("why is leaving profits in easier than buying "
                                    "new shares?", colour=FOCUS)), t=0.8, hold=4)
        b.step(st.show("note", note("Classes 11–12. For now: a fact a theory has to match")),
               t=0.8, hold=3)
        b.run()


class BeatLeverage(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatLeverage")
        head = ["U.S., 1985", "equity / (debt + equity)", "debt / equity"]
        w = [4.6, 4.2, 2.8]
        rows = [("All industries", "0.32", "2.11"),
                ("Manufacturing", "0.45", "1.20"),
                ("Wholesale and retail trade", "0.29", "2.49"),
                ("Services", "0.31", "2.25"),
                ("Commercial banks", "0.08", "11.00")]
        banks = _g4_paint([(4, 0), (4, 1), (4, 2)], FOCUS)

        def tab(k, colours=None):
            return table(head, _g4_fill(rows, k), col_widths=w, row_height=0.75,
                         font_size=26, cell_colours=colours)

        dh = ["high debt", "low debt"]
        dr = [("safe, steady cash flows", "risky firms"),
              ("resaleable assets:", "little cash flow"),
              ("buildings, aircraft, inventory", "intangible value:"),
              ("", "research, brands, growth options")]

        def det(k_low, colours=None):
            r = [(a, bb if k_low else "") for a, bb in dr]
            return table(dh, r, col_widths=[5.8, 5.8], row_height=0.75, font_size=24,
                         cell_colours=colours)

        b.step(st.show("title", title("Tirole, Table 2.4 — White (1991): "
                                      "how much U.S. firms borrow", size=26))
               + st.show("main", tab(0)), t=1.0, hold=3)
        b.step(st.show("main", tab(1, {(0, 2): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("a typical debt–equity ratio: around 2")), t=0.8, hold=3)
        b.step(st.show("main", tab(2)), t=1.0, hold=3)
        b.step(st.show("main", tab(4)), t=1.0, hold=3)
        b.step(st.show("main", tab(5, banks))
               + st.show("note", note("commercial banks: equity 8% of the total, "
                                      "debt 11 times equity")), t=1.0, hold=4)
        b.step(st.show("note", note("utilities: long-term debt over half (51.5% telecom, "
                                    "53% gas and electric) vs 29.1% average")),
               t=0.8, hold=4)
        b.step(st.show("note", note("leveraged buyouts: debt at 10 or 20 times equity")),
               t=0.8, hold=3)
        b.step(st.show("note", note("aggregate U.S. ratio: about 0.32, "
                                    "stable for half a century")), t=0.8, hold=4)
        b.step(st.show("title", title("Who borrows a lot, and who does not?"))
               + st.show("main", det(False)) + st.clear("note"), t=1.0, hold=4)
        b.step(st.show("main", det(True)), t=1.0, hold=4)
        b.step(st.show("main", det(True, _g4_paint([(i, 0) for i in range(3)], OUT)))
               + st.show("note", note("easy to borrow against: what an outsider can count on "
                                      "without trusting the insider", colour=OUT)),
               t=1.0, hold=4)
        b.step(st.show("main", det(True, {**_g4_paint([(i, 0) for i in range(3)], OUT),
                                          **_g4_paint([(i, 1) for i in range(4)], INS)}))
               + st.show("note", note("hard to borrow against: value that depends on "
                                      "what the insider does next", colour=INS)),
               t=1.0, hold=4)
        b.step(st.show("note", note("the shape of the answer we are about to derive",
                                    colour=FOCUS)), t=0.8, hold=3)
        b.run()


class BeatBanksVsMarkets(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatBanksVsMarkets")
        head = ["% of liabilities", "France", "Germany", "U.K.", "Italy", "U.S.", "Japan"]
        w = [3.8, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
        rows = [("securities other than stocks", "7.3", "2.3", "10.6", "2.3", "15.6", "8.0"),
                ("credit (loans)", "24.3", "43.2", "30.7", "32.1", "10.0", "39.5"),
                ("stocks (market value)", "52.9", "40.7", "53.0", "49.4", "45.6", "28.0"),
                ("system", "", "bank", "", "", "market", "bank")]
        hi = _g4_paint([(0, 5), (1, 2), (1, 6), (3, 2), (3, 5), (3, 6)], FOCUS)

        def tab(k, colours=None):
            return table(head, _g4_fill(rows, k), col_widths=w, row_height=0.8,
                         font_size=24, cell_colours=colours)

        b.step(st.show("title", title("Countries differ in who supplies the debt")),
               t=0.8, hold=2)
        b.step(st.show("title", title("Tirole, Table 2.5 — non-financial firms, 2002 "
                                      "(national accounts)", size=26))
               + st.show("main", tab(0)), t=1.0, hold=3)
        b.step(st.show("main", tab(1)), t=1.0, hold=3)
        b.step(st.show("note", note("essentially bonds")), t=0.7, hold=2)
        b.step(st.show("main", tab(2)) + st.show("note", note("credit: loans, mostly from "
                                                              "banks")), t=1.0, hold=4)
        b.step(st.show("main", tab(3)) + st.show("note", note("stocks: from 28% in Japan to "
                                                              "53% in Britain and France")),
               t=1.0, hold=3)
        b.step(st.show("main", tab(3, hi))
               + st.show("note", note("U.S. firms borrow from markets; "
                                      "German and Japanese firms from banks")),
               t=1.0, hold=3)
        b.step(st.show("main", tab(4, hi))
               + st.show("note", note("market-based vs bank-based financial systems")),
               t=1.0, hold=3)
        b.step(st.show("note", note("Brazil: public and private banks, BNDES long-term credit "
                                    "— closer to bank-based")), t=0.8, hold=4)
        b.step(st.show("title", title("Why would it matter, if debt is debt?"))
               + st.show("main", table(["a bank", "a dispersed bondholder"],
                                       [("monitors actively", "reads the price"),
                                        ("renegotiates", "and leaves"),
                                        ("learns about the borrower", "")],
                                       col_widths=[5.4, 5.4], row_height=0.8, font_size=26,
                                       cell_colours=_g4_paint([(0, 0), (1, 0), (2, 0)], OUT)))
               + st.clear("note"), t=1.0, hold=4)
        b.step(st.show("note", note("which one a firm faces changes what insiders "
                                    "can get away with")), t=0.8, hold=3)
        b.step(st.show("note", note("active vs speculative monitoring: Class 13",
                                    colour=FOCUS)), t=0.8, hold=3)
        b.run()


class BeatAnnouncement(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatAnnouncement")
        head = ["industrial firms announce", "2-day abnormal return (%)"]
        w = [5.8, 5.4]
        rows = [("common stock", "−3.1"), ("convertible bonds", "−2.0"),
                ("straight bonds", "−0.3*"), ("a bank loan agreement", "price rises")]
        neg = {(0, 1): BROKEN, (1, 1): BROKEN, (2, 0): MUTED, (2, 1): MUTED}

        def tab(k, colours=None):
            return table(head, _g4_fill(rows, k), col_widths=w, row_height=0.85,
                         font_size=28, cell_colours={**neg, **(colours or {})})

        b.step(st.show("title", title("Announce how you will raise money. "
                                      "What does the price do?")), t=0.8, hold=3)
        b.step(st.show("title", title("Tirole, Table 2.6 — Eckbo & Masulis (1995), "
                                      "U.S. firms", size=26))
               + st.show("main", tab(0)), t=1.0, hold=2)
        b.step(st.show("note", note("abnormal return: the price move beyond what "
                                    "the market as a whole did")), t=0.8, hold=3)
        b.step(st.show("main", tab(1)), t=1.0, hold=3)
        b.step(st.show("main", tab(2)), t=1.0, hold=2)
        b.step(st.show("main", tab(3))
               + st.show("note", note("* not statistically different from zero")),
               t=1.0, hold=3)
        b.step(st.show("note", note("a share issue is bad news; a bond issue, "
                                    "roughly no news")), t=0.8, hold=3)
        b.step(st.show("main", tab(4, {(3, 0): KEEP, (3, 1): KEEP})), t=1.0, hold=3)
        b.step(st.show("title", title("Under Modigliani–Miller, every entry should be zero"))
               + st.show("note", note("if the split does not change the pie, announcing it "
                                      "cannot move the pie")), t=0.8, hold=4)
        b.step(st.show("main", tab(4, {(0, 0): FOCUS, (0, 1): BROKEN}))
               + st.show("note", note("the average firm loses 3% of its value "
                                      "on an irrelevant announcement", colour=BROKEN)),
               t=1.0, hold=4)
        b.step(st.show("note", note("asymmetric information: issuing says insiders think "
                                    "the shares are overpriced")), t=0.8, hold=4)
        b.step(st.show("note", note("Classes 11–12. Today: a fact the benchmark "
                                    "cannot explain", colour=FOCUS)), t=0.8, hold=3)
        b.run()


class BeatTiming(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTiming")
        head = ["financing moves with the business cycle"]
        items = [("1. bank finance is countercyclical: bonds in booms, banks in recessions",),
                 ("2. strong firms extend trade credit, issue commercial paper in recessions",),
                 ("3. small and medium firms, bank-dependent, are hit harder in downturns",),
                 ("4. equity issues more frequent in upswings, absolutely and vs debt",),
                 ("5. the price drop on a share issue is smaller in expansions",),
                 ("6. firms issue after their share price rises, buy back after it falls",)]

        def tab(k, colours=None):
            return table(head, _g4_fill(items, k), col_widths=[12.0], row_height=0.68,
                         font_size=24, cell_colours=colours)

        b.step(st.show("title", title("One of the best-documented facts (Tirole §2.5)")),
               t=0.8, hold=2)
        b.step(st.show("main", tab(0)), t=1.0, hold=2)
        b.step(st.show("main", tab(1, {(0, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(2, {(1, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(3, {(2, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(4, {(3, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(5, {(4, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(6, {(5, 0): FOCUS})), t=1.0, hold=4)
        b.step(st.show("main", tab(6, {(5, 0): FOCUS}))
               + st.show("note", note("equity market timing: issue when shares are dear, "
                                      "buy back when cheap")), t=0.8, hold=3)
        b.step(st.show("title", title("Candidate explanations — Tirole does not choose"))
               + st.show("main", bullets(["investment really is more productive in booms",
                                          "adverse selection is milder in good times",
                                          "bubbles",
                                          "irrational markets"], size=30, buff=0.4)),
               t=1.0, hold=4)
        b.step(st.show("note", note("if financing were irrelevant, firms would have "
                                    "no reason to time it")), t=0.8, hold=3)
        b.step(st.show("title", title("They time it constantly"))
               + st.show("main", tab(6, _g4_paint([(1, 0), (2, 0)], FOCUS)))
               + st.show("note", note("items 2–3 → the macroeconomics of Classes 15–16",
                                      colour=FOCUS)), t=1.0, hold=4)
        b.run()


class BeatFactsToClasses(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFactsToClasses")
        head = ["fact", "explained in"]
        rows = [("retained earnings and bank loans, few share issues", "Classes 6–8"),
                ("leverage tracks safe cash flow and resaleable assets", "Class 7"),
                ("share issues lower the price, bank loans raise it", "Classes 11–12, 13"),
                ("some countries borrow from banks, others from markets", "Class 13"),
                ("financing follows the cycle; the small hit hardest", "Classes 9–10, 15–16")]
        why = ["agency costs and borrowing capacity",
               "collateral and pledgeable income",
               "asymmetric information; monitoring by banks and large investors",
               "active versus speculative monitoring",
               "liquidity; then the macroeconomic implications"]

        def tab(k):
            return table(head, _g4_fill(rows, k), col_widths=[7.6, 4.2], row_height=0.75,
                         font_size=23, cell_colours={(k - 1, 1): FOCUS} if k else None)

        close = [("information", "capital"), ("incentives", "liquidity"),
                 ("", "value of collateral"), ("", "external monitoring")]

        b.step(st.show("title", title("Each fact, and the part of the course that explains it")),
               t=0.8, hold=1)
        b.step(st.show("main", tab(0)), t=1.0, hold=1)
        b.step(st.show("main", tab(1)) + st.show("note", note(why[0])), t=1.0, hold=4)
        b.step(st.show("main", tab(2)) + st.show("note", note(why[1])), t=1.0, hold=4)
        b.step(st.show("main", tab(3)) + st.show("note", note(why[2])), t=1.0, hold=4)
        b.step(st.show("main", tab(4)) + st.show("note", note(why[3])), t=1.0, hold=4)
        b.step(st.show("main", tab(5)) + st.show("note", note(why[4])), t=1.0, hold=4)
        b.step(st.show("title", title("Tirole's closing list (§2.6)"))
               + st.show("main", table(["in general", "more specifically"],
                                       [(a, "") for a, _ in close], col_widths=[5.4, 5.4],
                                       row_height=0.8, font_size=28,
                                       cell_colours=_g4_paint([(0, 0), (1, 0)], FOCUS)))
               + st.clear("note"), t=1.0, hold=3)
        b.step(st.show("main", table(["in general", "more specifically"], close,
                                     col_widths=[5.4, 5.4], row_height=0.8, font_size=28,
                                     cell_colours=_g4_paint([(i, 1) for i in range(4)],
                                                            FOCUS))), t=1.0, hold=3)
        b.step(st.show("note", note("every one of those words is a lecture in this course")),
               t=0.8, hold=3)
        b.step(st.show("note", note("and all of them start from the same place")),
               t=0.8, hold=2)
        b.step(st.show("note", note("back to the founder, and compute", colour=FOCUS)),
               t=0.8, hold=2)
        b.run()
