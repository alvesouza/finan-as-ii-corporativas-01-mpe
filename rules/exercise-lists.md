---
id: exercise-lists
title: Exercise lists built from real exercises
tier: 2
applyTo: "Listas/**, Simulados/**"
skills: [list-exercises, exercise-plan, exam-gen]
owner: repo-owner
---

A list built from real exercises (course books, problem sets, past exams) is studied away from
the books. Each block must say where the exercise comes from and must be solvable on its own.
This overrides the references-only format of `/exercise-plan` whenever real exercises are listed.

## Non-negotiable

1. Open every exercise block with its source: book or document, chapter, exercise number,
   printed page with the PDF page in brackets, and whether the source gives the answer.
   *Why:* the reader can find and verify the original, and a wrong page or number shows up
   immediately instead of after a study session built on the wrong problem.
   *Check:* each block starts with a `**Source:**` line (format below); `python -I tools/check_lists.py`
   finds the statement in the book at that page.

2. Reproduce the statement completely, with everything needed to solve it: every part
   (a), (b)…, every number, every data table, the content of any figure the question reads from,
   and any earlier problem, example or table the exercise refers to ("Repeat Problem 6 with…",
   "using the data in Table 9.2"), copied into the same block.
   *Why:* a list that sends the reader back to the book for a missing table or a referenced
   problem cannot be solved where it is read, which defeats its purpose.
   *Check:* reading only the block, every input the solution uses appears in it.

## Avoid

3. Paraphrasing, summarizing or trimming a statement. Keep the source's words, order and
   language.
   *Why:* a paraphrase silently drops conditions (timing, tax treatment, "in thousands") that
   change the answer, and the result no longer matches the book's answer key.

## Quick reference

- Source line: `**Source:** <Book short name>, Ch. <c>, Exercise <id>, p. <printed> (PDF <pdf>) · Answer in book: <yes, p. X | no>`,
  then a blank line, then the statement.
- Allowed edits only: re-typeset math in LaTeX; rebuild tables as Markdown tables; undo
  hyphenation and line breaks; drop margin sidebars, glossary boxes and online-platform notes
  that are not part of the problem; write currency as `\$`, never a bare `$`.
- A figure that cannot be reproduced is described with all its values (axes, points, labels).
- A dependency on an earlier problem is copied as part 0 of the same block, with its own source.
