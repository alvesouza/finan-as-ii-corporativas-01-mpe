# Finanças II – Corporativas (MPE Insper)

Insper — Mestrado Profissional em Economia, curriculum 202431, 30 h. Professor: TBD.
Main book: Tirole, *The Theory of Corporate Finance* (`Livros/`). Program, topic x chapter
table, bibliography and rules index: [rules/10_curso_programa.md](rules/10_curso_programa.md).

## Scope guard
Only the nine syllabus topics (corporate governance, valuation, MM benchmark, agency costs,
liquidity, asymmetric information, activism, M&A, macro implications). Do NOT extrapolate
beyond them or beyond the course bibliography.

## Language and format
- Output in English; quotes, identifiers, file paths and book/section titles stay verbatim.
  Existing Portuguese files are not translated unless asked.
- Math in LaTeX (`$...$`, `$$...$$`); never a bare `$` for currency ("120 reais").
- pdflatex: `lmodern` + `cmap` after `fontenc`; check `pdffonts` (Type 1 only).
- NotebookLM output language is an app setting; never a prompt line. Confirm it before a batch.
- Code: Python (Jupyter via `/lab`). Grading style: `macro-1`, rebound in `rules/00_estilo_avaliacao.md`.

## Sibling projects
- Video explainer: `D:/Documents/Git/Github/Video explainer` (pip -e linked, never vendored)
- Efficient Token: `D:/Documents/Git/Github/Efficient Token`

<!-- GENERATED:tier0:start -->
### Non-negotiable

1. Escalate retrieval in this order and stop at the first rung that answers the
   question: **graph query → symbol lookup → structural search → ripgrep → file slice
   → whole file**.

2. Do not switch the main-loop model mid-session. Delegate to a subagent instead.

3. Write the plan to `.agent/plans/<slug>.md` before implementing any non-trivial
   change, then implement against it.

4. Report only outcomes observed in tool output. Failing tests are quoted, not
   summarized away. Skipped steps are stated.

5. Never read secrets into context: `.env`, key material, credential stores, tokens.
   Reference them by name.

6. Memory-safety, point-in-time, and idempotency gates do not relax under deadline.

### Prefer

7. Persist findings to `.agent/notes/<topic>.md` rather than re-deriving them.

8. Reuse before writing. If you write new code anyway, say what you found and why it
   did not fit.

9. Match the surrounding code. `.agent/conventions.md` outranks this repo's style
   preferences; correctness rules never yield.

10. Doc comments on public functions: purpose, parameter meaning, failures, calling
    context. Inline comments state constraints the code cannot express, never narration.

### Avoid

11. Making the diff larger than the change. Refactor inside the change's own context;
    outside it, ask (`codebase-work.md`).

12. Abstractions, defensive branches for impossible states, and speculative generality.

13. Claiming completion when part of the task is unfinished. Do the rest; if truly
    blocked, state plainly what is missing and why.

14. Re-deriving facts already established in the session.

Rationale and verification commands for each rule: `rules/core.md`
<!-- GENERATED:tier0:end -->
