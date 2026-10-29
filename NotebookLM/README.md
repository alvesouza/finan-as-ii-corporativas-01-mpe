# NotebookLM prompts — Finanças II – Corporativas

**Open any prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM (slides → slide creation field; audio → Audio Overview Customize field or as Source)**

| File | Type | Lecture/Book | Words | Chars | Paste into |
|---|---|---|---|---|---|
| `audio/topic1-audio.md` | Audio (Custom, hard, cross-topic) | Topic 1 — accounting review: market-value identity and its MM/agency limits, book vs. market, DuPont vs. MM II, ROIC, accrual vs. cash, FCF/FCFE, uses of FCF; PS1 Ex. 1; Lista R1 ex. 4, 8, 11–13 (Berk Ch. 2, Higgins Ch. 1–2, Grinblatt–Titman Ch. 1–3) | 751 | 4,850 | Audio Overview → Customize |
| `audio/topic2a-audio.md` | Audio (Custom, hard, cross-topic) | Topic 2A — unlevering, incremental FCF, when NPV ≠ shareholder gain, complete markets and Fisher separation, entrepreneur example, MM I (homemade leverage, put–call parity, Tirole's identity), MM II; PS1 Ex. 2–3, PS2 Ex. 1, 4; Lista R2 ex. 6–11, 14–15; Lista R3 ex. 5, 11, 15 (Berk, Grinblatt–Titman Ch. 7, 11, 14, Amaro de Matos Ch. 1–2, Tirole §2.2) | 720 | 4,682 | Audio Overview → Customize |
| `audio/topic2b-audio.md` | Audio (Custom, hard, cross-topic) | Topic 2B — tax shield and its risk, WACC vs. APV, Miller (1977) and DeAngelo–Masulis, distress costs and evidence, risk-shifting/debt overhang, trade-off FOC, bank capital, payout irrelevance and its breakdowns; PS2 Ex. 1(f), 2, 3(c); Lista R3 ex. 3–4, 6, 8–10, 12–14 (Berk Ch. 16–17, Grinblatt–Titman Ch. 13–16, Amaro de Matos Ch. 2) | 724 | 4,613 | Audio Overview → Customize |

The prompts follow the real lectures (Prof. Bernardo Ricca, `Map/lectures-index.md`) and the
Ricca remap (books R1–R3, `Listas/lista-r1…r3`). The Tirole-based `aula-01-audio-part1/2` prompts
were retired on 2026-10-24 (recoverable from git history).

> ⚠️ Slide and Audio Customize fields truncate silently at ~6,000 chars. All prompts are kept under 5,000 chars for safety.

> Output language is set once in NotebookLM's **Settings → Output language** (English). The prompts never contain a language line; confirm the setting before generating.

All course materials should be uploaded as separate sources in the same NotebookLM notebook; the
files in `sources/` are the current set, named exactly as the prompts cite them: lecture slides
(`Aula_Topic*.pdf`), problem sets (`Lista_PS*.pdf`), exercise lists (`Lista_R1…R3 *.md`), books
(`Livro_*.pdf`, including Berk–DeMarzo–Harford and Grinblatt–Titman) and syllabi (`Programa_*.pdf`).
These prompts guide how NotebookLM processes those sources.
