# Lists rewritten under exercise-lists rule + NotebookLM audio split

Date: 2026-10-31. Rule: `rules/exercise-lists.md` (source first; full, self-contained statement).
Spec updated: `.agent/notes/exercise-list-spec.md` ("Self-contained" bullet replaces the
one-line `*Context:*` pointer).

## Part A — lists (4 background agents, one file group each)
- A1: lista-r1, r2, r3 · A2: lista-r4 · A3: lista-r5, r5b · A4: lista-r6.
- Per block: keep exercise choice, order, numbering, titles and the verbatim statement; check the
  Source line (printed p., PDF p., answer in book); replace every `*Context:*` pointer and every
  outside dependency (chapter model, table, figure, earlier problem) with a
  `#### Context needed to solve it` sub-block copied verbatim from the book.
- Gate: `python -I tools/check_lists.py <file>` -> 0 failures.
- After agents: copy R1–R3 to `NotebookLM/sources/Lista_R*.md` (they are identical copies today).

## Part B — audio prompts (main loop)
- Split each of `NotebookLM/audio/topic1|topic2a|topic2b-audio.md` into 3 parts
  (`topicX-audio-part1..3.md`): concepts, derivations, exercises and pitfalls.
- Each part < 5,000 chars, no output-language line, cites sources by their `sources/` names.
- Delete the single-file prompts; update `NotebookLM/README.md` table (words, chars).

## Verify
- check_lists gate per file; `wc -m` per prompt; grep prompts for "language".
