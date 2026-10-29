"""Check that every exercise copied into Listas/lista-r*.md really appears in its source book.

Usage: python -I tools/check_lists.py [Listas/lista-r*.md ...]   (default: all lista-r*.md)

Each exercise block starts with a line `**Source:** <book>, ... (PDF <n>) ...` followed by the
verbatim statement. The check takes the first 60 letters of the statement (math, digits and
whitespace dropped, so LaTeX re-typesetting does not matter) and looks for them in the book's
MD within PDF pages n-1..n+2. Prints one FAIL line per miss and exits 1 if any.
"""
import glob
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = {  # keyword in the Source line -> MD file prefix in Livros/
    "Tirole": "Jean Tirole",
    "Amaro de Matos": "de Matos",
    "Higgins": "Jennifer L. Koski",
    "Ross": "ROSS, WESTERFIELD",
    "Berk": "Fundamentals of Corporate Finance",
    "Grinblatt": "Financial Markets And Corporate Strategy",
}


def letters(s, latex=True):
    """Lower-case ASCII letters only; drops accents, hyphenation and spacing.

    latex=True (list side): drop escaped currency, inline math and LaTeX commands.
    latex=False (book side): the MDs use `$` as currency, so only the sign itself goes.
    """
    if latex:
        s = s.replace("\\$", " ")  # escaped currency sign, not a math delimiter
        s = re.sub(r"\$[^$]*\$|\\[a-zA-Z]+", "", s)
    s = unicodedata.normalize("NFKD", s.replace("-\n", ""))
    return re.sub(r"[^a-z]", "", s.lower())


def pages(md_path):
    text = md_path.read_text(encoding="utf-8")
    parts = re.split(r"<!-- page (\d+) -->", text)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


def main(files):
    cache, fails, n = {}, 0, 0
    for f in files:
        blocks = re.split(r"\n(?=\*\*Source:\*\*)", Path(f).read_text(encoding="utf-8"))
        for b in blocks[1:]:
            head, _, body = b.partition("\n")
            body = re.split(r"\n(?:#{2,3} |---)", body)[0]
            key = next((k for k in BOOKS if k in head), None)
            pdf = re.search(r"PDF (\d+)", head)
            if not key or not pdf:
                print(f"FAIL {f}: unparsable source line: {head[:90]}")
                fails += 1
                continue
            if key not in cache:
                md = next((ROOT / "Livros").glob(BOOKS[key] + "*.md"))
                cache[key] = pages(md)
            p = int(pdf.group(1))
            hay = letters("".join(cache[key].get(q, "") for q in range(p - 1, p + 3)), latex=False)
            probe = letters(body)[:60]
            n += 1
            if len(probe) < 30 or probe not in hay:
                print(f"FAIL {f}: not found near PDF {p}: {head[:90]}")
                fails += 1
    print(f"{n} exercises checked, {fails} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:] or sorted(glob.glob(str(ROOT / "Listas/lista-r*.md")))))
