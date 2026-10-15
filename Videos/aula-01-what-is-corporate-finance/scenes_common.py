"""Shared header for aula-01-what-is-corporate-finance scenes.

Scenes are written in groups (scenes_g1..g4.py, one per act) that import this file, and
concatenated into scenes.py by build_scenes.py for the single-module render the compiler needs.
Beat lengths come from beats.json (narration + 2.5 s per [pause]; see build_beats.py).

Colour roles, fixed for the whole video and declared in plan.md:
    INS    BLUE    insiders: founder/manager, R_b, B      FOCUS  YELLOW  live line / attention
    OUT    TEAL    outsiders: investors, lenders, R_l     MUTED  GREY    lines already past
    BROKEN RED     what breaks                            KEEP   GREEN   what survives
"""
from manim import *
from video_explainer import (SLOTS, Beat, Stage, axes_panel, bullets, cell, eq, note,
                             side_by_side, table, title)

INS, OUT, FOCUS, MUTED, BROKEN, KEEP = BLUE, TEAL, YELLOW, GREY, RED, GREEN


def beat(scene, bid):
    """A Beat whose length is beats.json's `seconds` (narration plus held pauses)."""
    return Beat(scene, bid)


class Stack:
    """A column of equation lines on a FIXED grid: live line FOCUS, lines above MUTED.

    Carried from the Macro project (aula-02): positions are computed once from the slot's
    geometry, so a line is never re-fitted after it is placed and lines cannot collide.
    `rows` must be at least the number of lines the scene writes.
    """

    def __init__(self, stage, size=36, rows=6, slot="main"):
        self.st, self.size, self.rows, self.slot = stage, size, rows, slot
        self.group = VGroup()
        box = SLOTS[slot]
        self.pitch = box["height"] / rows
        self.top = box["center"][1] + box["height"] / 2
        self.x = box["center"][0]

    def _place(self, line, row):
        box = SLOTS[self.slot]
        if line.width > box["width"]:
            line.scale_to_fit_width(box["width"])
        if line.height > self.pitch * 0.86:
            line.scale_to_fit_height(self.pitch * 0.86)
        return line.move_to([self.x, self.top - self.pitch * (row + 0.5), 0])

    def add(self, tex, colour=FOCUS, size=None):
        """Animations that mute the current live line and write `tex` on the next row.

        Each line enters the slot on its own (show, then add_to). Showing `self.group`
        instead faded in EVERY line at the first step: steps play in Beat.run(), after
        construct() has already appended all later lines to that group. Muting uses
        ApplyMethod, built at play time; `.animate` snapshots at construct time and would
        undo a transform() applied in between. (Found by the g3 render, 2026-10-09.)
        """
        line = eq(tex, size=size or self.size, colour=colour)
        row = len(self.group)
        self._place(line, row)
        if row == 0:
            anims = self.st.show(self.slot, line, fit=False)
            self._place(line, 0)      # show() recentres the slot's occupant; undo that
        else:
            anims = [ApplyMethod(self.group[-1].set_color, MUTED)] + \
                self.st.add_to(self.slot, line)
        self.group.add(line)
        return anims

    def transform(self, tex, colour=FOCUS, size=None):
        """Rewrite the live line in place (a rearrangement, not a new statement).

        Transform reshapes the held mobject, so collapse() still fades it out;
        ReplacementTransform left the new line outside the slot, stranded on screen.
        """
        new = eq(tex, size=size or self.size, colour=colour)
        self._place(new, len(self.group) - 1)
        return [Transform(self.group[-1], new)]

    def collapse(self, tex, size=46):
        """Clear the column and re-show the result alone -- never carry muted lines on."""
        return self.st.show(self.slot, eq(tex, size=size, colour=KEEP))
