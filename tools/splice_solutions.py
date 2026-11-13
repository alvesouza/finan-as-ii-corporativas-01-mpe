"""Copy exercise sections from one solutions .tex into another, so a list that shares exercises
with a topic list carries the same worked solution.

Usage: python -I tools/splice_solutions.py Listas/<target>-solutions.tex [...]

In the target, a line
    %% INSERT-FROM <source>.tex EX <m> AS <n>
(source path relative to the target's folder) is replaced by the source's section `\\exsec{<m>. ...}`
renumbered to <n>, wrapped in `%% BEGIN-FROM ... AS <n>` / `%% END-FROM`. Running again refreshes
every BEGIN/END block from the current source, so re-run after editing a topic solutions file.
Fails (exit 1) if a source section is missing. Labels are copied unchanged: each source file keeps
its own prefix (t3e, t4e, t5e), so sections from different sources do not collide.
"""
import re
import sys
from pathlib import Path

MARK = re.compile(r"^%% (?:INSERT|BEGIN)-FROM (\S+) EX (\d+) AS (\d+)$")


def section(src_text, ex):
    """Body of `\\exsec{<ex>. ...}` up to the next \\exsec or \\end{document}; trailing blank and
    comment lines dropped (they head the *next* section in the source)."""
    lines = src_text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith(f"\\exsec{{{ex}.")), None)
    if start is None:
        return None
    end = next((j for j in range(start + 1, len(lines))
                if lines[j].startswith("\\exsec{") or lines[j].startswith("\\end{document}")), len(lines))
    body = lines[start:end]
    while body and (not body[-1].strip() or body[-1].lstrip().startswith("%")):
        body.pop()
    return body


def splice(target):
    out, fails, n = [], 0, 0
    lines = target.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = MARK.match(lines[i].strip())
        if not m:
            out.append(lines[i]); i += 1; continue
        if lines[i].startswith("%% BEGIN-FROM"):  # skip the stale copy
            while i < len(lines) and lines[i].strip() != "%% END-FROM":
                i += 1
        i += 1
        src, ex, as_ = m.groups()
        body = section((target.parent / src).read_text(encoding="utf-8"), ex)
        if body is None:
            print(f"FAIL {target.name}: no \\exsec{{{ex}.}} in {src}")
            fails += 1
            out.append(f"%% INSERT-FROM {src} EX {ex} AS {as_}")
            continue
        body[0] = body[0].replace(f"\\exsec{{{ex}.", f"\\exsec{{{as_}.", 1)
        out += [f"%% BEGIN-FROM {src} EX {ex} AS {as_}", *body, "%% END-FROM"]
        n += 1
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{target.name}: {n} sections spliced, {fails} failures")
    return fails


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(1 if sum(splice(Path(a)) for a in sys.argv[1:]) else 0)
