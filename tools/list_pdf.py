"""Build the PDF of an exercise list MD with pandoc + LuaLaTeX (vector OpenType fonts, Unicode text,
so the PDF is copyable without lmodern/cmap).

Usage: python -I tools/list_pdf.py Listas/<list>.md [...]   -> Listas/<list>.pdf

Obsidian wiki links `[[target|label]]` become `label`; Unicode superscript footnote digits (⁷⁹)
become pandoc superscripts. Fails with pandoc's own message if the conversion breaks.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def prepare(md):
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)  # Obsidian front matter (tags, date)
    md = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", md)
    md = re.sub(r"\[\[([^\]]+)\]\]", r"\1", md)
    return re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: "^" + m.group(0).translate(SUP) + "^", md)


def build(src):
    with tempfile.TemporaryDirectory() as tmp:
        mid = Path(tmp) / src.name
        mid.write_text(prepare(src.read_text(encoding="utf-8")), encoding="utf-8")
        subprocess.run(["pandoc", str(mid), "-f", "markdown-yaml_metadata_block", "-o", str(src.with_suffix(".pdf")),
                        "--pdf-engine=lualatex", "--columns=200",
                        "-V", "geometry:margin=2cm", "-V", "fontsize=10pt",
                        "-V", "mainfont=Latin Modern Roman", "-V", "colorlinks=true",
                        # Greek, primes, ≈, subscript digits typed as text in verbatim statements
                        "-V", "mainfontfallback=Latin Modern Math:mode=node;",
                        "-V", "mainfontfallback=Cambria Math:mode=node;"], check=True)
    print("built", src.with_suffix(".pdf"))


if __name__ == "__main__":
    for a in sys.argv[1:]:
        build(Path(a))
