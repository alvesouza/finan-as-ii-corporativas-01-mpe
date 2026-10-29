# Spec — roadmaps/study packs (R1–R6) and solution PDFs (R1–R3)

User choices (2026-10-24): roadmap PDF for all 7 lists; worked solutions for R1–R3 first.
Lists: `Listas/lista-r*.md` (format: `.agent/notes/exercise-list-spec.md`). Style rule:
`rules/00_estilo_avaliacao.md` §4 (solution format) and §9.

## A. Roadmap + study pack (per list)
File `Listas/roteiro-<list slug without "lista-">.md`, e.g. `Listas/roteiro-r2-valuation.md`.
Three tables, exactly these headings (parsed by `~/.claude/commands/templates/study_pack.py`):

```
## Leituras Consolidadas por Livro
### Berk
| Tópico | Capítulo / Seção | Páginas | Prioridade |
|---|---|---|---|
| NPV and stand-alone projects | Ch. 8, §8.1–8.2 | p. 242–249 | Fundamentos |
### Tirole
...
## Exercícios Consolidados
| # | Exercício | Livro | Página | Tópico | Nível |
|---|---|---|---|---|---|
| 1 | 8.2 | Berk | p. 272 | NPV | Fundamentos |
## Roteiro de Estudo
| Prioridade | Tópico | Leitura | Exercícios | Tempo sugerido |
```
Parser constraints (rows are silently dropped otherwise):
- `###` book headings must be exactly a registry key: `Tirole`, `Amaro`, `Higgins`, `Ross`,
  `Berk`, `Grinblatt` (see `Livros/book-registry.json`).
- In the exercise table the `Livro` cell must contain that same key; `Página` = **printed**
  page(s) (`p. 494–495` for a statement over two pages).
- Data rows must NOT contain the words `Topic`, `Tópico`, `Exercise`, `Exercício`, nor a `#` in
  the first cell (those mark header rows). Priority: Fundamentos / Prova / Avançado (= list tiers).
- Pages are printed pages; ranges `p. a–b`, sorted by page within each book, overlaps merged.
Reading rows = the section(s) each exercise practises, taken from `Map/books-index.md` (sections
with printed pages; Grinblatt & Titman is chapter-level there — use the Context lines in the list
or the chapter's relevant pages). Keep it tight: the sections needed, not whole chapters.
Build: `python -I ~/.claude/commands/templates/study_pack.py "Listas/roteiro-<slug>.md" "Livros" "Listas/study-pack-<slug>.pdf" --registry="Livros/book-registry.json"`.
Verify: every book prints "using registry", page count reasonable, open 2–3 pages and confirm
an exercise page shows the expected problem number.

## B. Solutions PDF (R1–R3)
Files: `Listas/<list slug>-solutions.tex` → `.pdf`, plus `Listas/<list slug>-solutions_check.py`.
- Preamble from `Listas/lista-exam.tex` style: `\usepackage[T1]{fontenc}` then `lmodern`, `cmap`
  (mandatory), `babel` english (add brazil for Ross Portuguese quotes), amsmath, geometry,
  booktabs. pdflatex twice; `pdffonts` must show only Type 1 with `uni` = yes.
- One section per exercise in list order: heading `<n>. <title> — <Book> <exercise>, p. <printed>`.
  **Do not restate the statement** (it is in the list); cite it by number and page.
- §4 format for each: **Notation** list (every symbol, meaning, range) → numbered steps
  "Step k — title." → numbered display equations (`\label`/`\eqref`), one operation per line,
  every substitution shown with the substituted expression in parentheses, then the result →
  **Intuition** (short paragraph) → **Ref:** book section and printed pages. No rubric.
- Book answers exist for Tirole (Part VII), Higgins odd problems, Amaro de Matos (App. C): solve
  first, then compare and state "Matches the book's answer (p. X)" or explain the difference.
- Every computed number appears as an `assert` in the check script (`python -I`, plain asserts,
  tolerance stated, prints `PASS <n> checks`). Displayed arithmetic must reproduce the printed
  result (carry enough decimals).
- Currency: `\$` in LaTeX. English throughout.
