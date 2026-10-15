# Finanças II – Corporativas (MPE Insper)

Study project for *Finanças II – Corporativas*, Mestrado Profissional em Economia, Insper.
Main book: Tirole, *The Theory of Corporate Finance*. Syllabus: `Finanças II.pdf`.
Course program, topic x chapter table and bibliography: [rules/10_curso_programa.md](rules/10_curso_programa.md).
Book status (found / missing): [Livros/BOOKS.md](Livros/BOOKS.md).

## Structure

| Directory | Purpose |
|---|---|
| `Aula/` | Lecture slides and class scripts |
| `Listas/` | Problem sets; `lista-exam.tex` is the LaTeX template for lists and mock exams |
| `Monitoria/` | Tutorial / office-hour material |
| `Prova/` | Past exams and solutions |
| `Simulados/` | Quiz MD files for `quiz.html` |
| `Livros/` | Textbook PDFs, their MD conversions, and `BOOKS.md` |
| `rules/` | One file per topic (`01`–`09`), exam style (`00`), course program (`10`), plus Efficient Token packs |
| `Resolucao/` | Generated exercise solutions |
| `Map/` | Obsidian cross-reference maps (books ↔ lectures ↔ exercises) |
| `NotebookLM/` | Prompts (`slides/`, `audio/`, `video/`) and `sources/` for bulk upload |
| `Leituras/` | Chapter extracts and TTS narrations |
| `Notebooks/` | Jupyter projects, one per subdirectory (created by `/lab-init`) |
| `Videos/` | One subdirectory per `/explainer` video (created on first use) |
| `.agent/` | `plans/` before non-trivial changes, `notes/` for findings |
| `tools/` | Efficient Token sync and token-budget tooling |

## Commands

| Command | Example |
|---|---|
| `/convert` | `/convert Aula/` — PDFs/slides to Markdown |
| `/summarize` | `/summarize Aula/` |
| `/list-exercises` | `/list-exercises Listas/` |
| `/solution` | `/solution Listas/lista-1.md` |
| `/exam-gen` | `/exam-gen agency costs, liquidity` — list + key + rubric in LaTeX (style `macro-1`, rebound) |
| `/exam-grade` | `/exam-grade Listas/lista-1.tex my-answers.pdf` |
| `/exercise-plan` | `/exercise-plan asymmetric information` — points to Tirole exercises by number and page |
| `/quiz-gen` | `/quiz-gen Simulados/` |
| `/quiz-analyze` | `/quiz-analyze <paste results>` |
| `/study-map` | `/study-map .` |
| `/notebooklm` | `/notebooklm Aula/` — slides / audio / video prompts |
| `/speechify` | `/speechify rules/05_liquidez.md` (`--split`, `--short`) |
| `/intake` | `/intake Aula/aula-03.pdf` — front door for new material |
| `/lab` | `/lab credit rationing and net worth` |
| `/lab-init` | `/lab-init pledgeable-income` |
| `/lab-data` | `/lab-data selic` (`--offline` never touches the network) |
| `/explainer` | `/explainer Modigliani–Miller` — narrated 1080p video; needs `SPEECHIFY_API_KEY` in `.env` |
| `/manim-kit` | `/manim-kit .` — shared drawing layer from **Video explainer** |
| `/companion` | `/companion fixed-investment model` — interactive page, on request only |

## Quizzes

1. `cd` into this directory
2. `python -m http.server`
3. Open `http://localhost:8000/quiz.html`
4. Select a quiz MD file from `Simulados/`

## Obsidian

Open the project root as a vault; start from `Map/`.

## NotebookLM

1. Confirm Settings → Output language is English (it is an app setting, not a prompt line).
2. Upload everything in `NotebookLM/sources/`.
3. Run `/notebooklm Aula/` to generate prompts.
4. Open each prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM.
