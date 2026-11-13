# Hard conceptual quizzes, 10 questions per topic

Date: 2026-11-13. User request: "conceptual quizzes (hard) of 10 questions for each topic"; then push.
Parameters fixed by the user (so quiz-gen's Step 0 confirmation is skipped): hard, conceptual,
10 questions. Format and anti-cheat rules: `~/.claude/commands/quiz-gen.md`; gate
`python -I .claude/quiz-validate.py <quiz.md>` → PASS.

| Agent | Quizzes (`Simulados/quiz-<slug>-hard-2026-11-13.md`) |
|---|---|
| A | `topic1-accounting` (R1), `topic2a-valuation-npv` (R2), `bonds` (R2b) |
| B | `financial-planning` (R2c), `topic2b-taxes-distress-payout` (R3), `trade-credit-working-capital` (R5b) |
| C | `topic3-asymmetric-information` (Topic 3, R5), `topic4a-moral-hazard` (R4), `topic4b-overhang-renegotiation` (Topic 4) |
| D | `topic5-nonverifiable-income-sovereign` (Topic 5), `liquidity-risk-management` (R6), `macro-implications` (R10) |
| E | `governance-activism` (R8), `executive-compensation` (R8b), `mergers-acquisitions` (R9) |

Questions are original (no copied book text); `> Similar:` lines point at list exercises.
After: validator PASS on all 15; commit; push to origin (requested).
