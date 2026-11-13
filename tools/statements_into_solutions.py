"""Put each exercise's full text (source line, statement, context) right before its worked solution.

Usage: python -I tools/statements_into_solutions.py Listas/<list>-solutions.tex [...]

The list is the solutions file's name without `-solutions` (`Listas/<list>.md`). Block `### n.` of the
list goes right after exercise heading n of the solutions file: `\\exsec{n. ...}`, or the n-th
`\\section{...}` in files that number exercises by section order. Each block is converted with pandoc
and wrapped in `%% BEGIN-STATEMENT n` / `%% END-STATEMENT`; re-running replaces those blocks, so run
it again after editing a list. A preamble block (`%% STATEMENT-PREAMBLE`) defines what pandoc's
LaTeX needs and maps the Unicode characters the lists use. Fails (exit 1) when headings and blocks
do not pair up, or when a block holds a character with no mapping (add it to UNI).
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from list_pdf import prepare  # wiki links -> labels, superscript digits -> ^n^

UNI = {  # characters outside what utf8 inputenc + T1 handle; ■ drawn, so no font without ToUnicode
    "→": r"\ensuremath{\rightarrow}", "−": r"\ensuremath{-}", "•": r"\textbullet{}",
    "≈": r"\ensuremath{\approx}", "′": r"\ensuremath{^{\prime}}", "₁": r"\ensuremath{_{1}}",
    "θ": r"\ensuremath{\theta}", "λ": r"\ensuremath{\lambda}", "ψ": r"\ensuremath{\psi}",
    "α": r"\ensuremath{\alpha}", "■": r"\rule{0.7em}{0.7em}",
}
NATIVE = set("…–—“”‘’")
PREAMBLE = [
    "%% STATEMENT-PREAMBLE BEGIN (tools/statements_into_solutions.py)",
    r"\usepackage{longtable,array,calc}",
    r"\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}",
    r"\providecommand{\href}[2]{#2}",
    r"\providecommand{\real}[1]{#1}",
    r"\makeatletter\@ifundefined{c@none}{\newcounter{none}}{}\makeatother  % pandoc's \LTcaptype{none}",
    r"\newcommand{\stmtbegin}{\par\medskip\noindent\textbf{Statement.}\par\nopagebreak\begingroup\small\setlength{\tabcolsep}{3pt}\sloppy}",
    r"\newcommand{\stmtend}{\par\endgroup\nopagebreak\noindent\rule{\linewidth}{0.4pt}\par\medskip}",
    *[rf"\DeclareUnicodeCharacter{{{ord(c):04X}}}{{{v}}}" for c, v in UNI.items()],
    "%% STATEMENT-PREAMBLE END",
]
HEAD_EXSEC = re.compile(r"^\s*\\exsec\{(\d+)\.")
HEAD_SECTION = re.compile(r"^\s*\\section\{")


def blocks(md):
    """{n: markdown body of block `### n.`} — Source/Origin line through the end of its context."""
    out = {}
    parts = re.split(r"^### (\d+)\.[^\n]*\n", md, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^## |^---\s*$", parts[i + 1], flags=re.M)[0]
        out[int(parts[i])] = body.strip()
    return out


def to_latex(body):
    body = prepare(body)
    bad = sorted({c for c in body if ord(c) > 0xFF and c not in UNI and c not in NATIVE})
    if bad:
        raise SystemExit(f"unmapped characters {bad}: add them to UNI")
    r = subprocess.run(["pandoc", "-f", "markdown-auto_identifiers-yaml_metadata_block", "-t", "latex",
                        "--columns=100"], input=body, capture_output=True, text=True,
                       encoding="utf-8", check=True)
    return r.stdout.rstrip()


def run(sol):
    lst = sol.with_name(sol.name.replace("-solutions.tex", ".md"))
    blk = blocks(lst.read_text(encoding="utf-8"))
    lines = sol.read_text(encoding="utf-8").splitlines()
    # drop old statement and preamble blocks
    keep, skip = [], False
    for l in lines:
        s = l.strip()
        if s.startswith("%% BEGIN-STATEMENT") or s.startswith("%% STATEMENT-PREAMBLE BEGIN"):
            skip = True
        if not skip:
            keep.append(l)
        if s == "%% END-STATEMENT" or s.startswith("%% STATEMENT-PREAMBLE END"):
            skip = False
    use_exsec = any(HEAD_EXSEC.match(l) for l in keep)
    out, k, done = [], 0, set()
    for l in keep:
        if l.strip() == r"\begin{document}":
            out += PREAMBLE
        out.append(l)
        m = HEAD_EXSEC.match(l) if use_exsec else HEAD_SECTION.match(l)
        if m:
            k = int(m.group(1)) if use_exsec else k + 1
            if k not in blk:
                raise SystemExit(f"{sol.name}: heading {k} has no block in {lst.name}")
            out += [f"%% BEGIN-STATEMENT {k}", r"\stmtbegin", to_latex(blk[k]), r"\stmtend", "%% END-STATEMENT"]
            done.add(k)
    missing = sorted(set(blk) - done)
    if missing:
        raise SystemExit(f"{sol.name}: list blocks {missing} have no heading")
    sol.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{sol.name}: {len(done)} statements")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:]:
        run(Path(a))
