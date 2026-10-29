# Plan — map the real lectures, one quiz each, one NotebookLM audio prompt each

Date: 2026-10-24. Inputs: `Aula/Topic1.pdf` (63 slides), `Aula/Topic2A.pdf` (105),
`Aula/Topic2B.pdf` (63), `Listas/PS1.pdf`, `Listas/PS2.pdf`, `syllabus(1).pdf` (Prof. Bernardo Ricca).

User choices: 10 questions per lecture, conceptual only (no math-intensive items), file-subject
mode, 1 Custom audio prompt (≤ 5,000 chars) per lecture.

## Steps
1. Text extracts (UTF-8) → `Aula/markitdown/*.txt`, `Listas/markitdown/*.txt`. Done.
2. `Map/lectures-index.md` (new): per lecture, slide blocks with slide ranges, worked examples,
   key results, PS questions that practise each block, book sections (pages from
   `Map/books-index.md`), rules file.
3. `Map/topics-index.md`, `Map/study-guide.md`: add the real lectures / PS / quizzes; flag that
   the real syllabus differs from the ementário-based plan. Do not rewrite the 16-class plan.
4. Quizzes in `Simulados/`: `quiz-topic1-…`, `quiz-topic2a-…`, `quiz-topic2b-…` (10 each).
   Gate: `.claude/quiz-validate.py` must print PASS.
5. NotebookLM: copy lectures/PS/syllabus to `NotebookLM/sources/` (done); write
   `NotebookLM/audio/topic1-audio.md`, `topic2a-audio.md`, `topic2b-audio.md`; update README.
   Gate: each ≤ 5,000 chars, no output-language line.
6. Report syllabus mismatch (CLAUDE.md scope guard, `rules/10_curso_programa.md`) and ask before
   changing them.
