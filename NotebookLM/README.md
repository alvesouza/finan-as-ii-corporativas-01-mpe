# NotebookLM prompts — Finanças II – Corporativas

**Open any prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM (slides → slide creation field; audio → Audio Overview Customize field or as Source)**

| File | Type | Lecture/Book | Words | Chars | Paste into |
|---|---|---|---|---|---|
| `audio/topic1-audio-part1.md` | Audio (Custom, hard) 1/3 concepts | Topic 1 — two promises and the balance sheet, debt vs. equity instruments, book vs. market (SVB, Starbucks), accrual income statement, operating leverage, NWC and liquidity, ratios as a map (Berk Ch. 2, Higgins Ch. 1–2, Grinblatt–Titman Ch. 1–3) | 577 | 3,783 | Audio Overview → Customize |
| `audio/topic1-audio-part2.md` | Audio (Custom, hard) 2/3 derivations | Topic 1 — value additivity and its limit, DuPont vs. MM II, ROIC, P/E drivers, cash-flow statement signs, unlevered FCF (capex, ΔNWC, depreciation tax shield), NI→FCF bridge, FCFE, deferred taxes (PS1 Ex. 1b), uses of FCF and corporate cash | 636 | 3,943 | Audio Overview → Customize |
| `audio/topic1-audio-part3.md` | Audio (Custom, hard) 3/3 exercises | Topic 1 — PS1 Ex. 1(a)–(b); Lista R1 ex. 1, 3, 4, 6, 7, 8, 10, 11, 12, 13, 15; four misconceptions; objects carried into 2A | 540 | 3,510 | Audio Overview → Customize |
| `audio/topic2a-audio-part1.md` | Audio (Custom, hard) 1/3 concepts | Topic 2A — discount rates and systematic risk, incremental cash flows, matching flows and rates, when NPV ≠ shareholder gain, debt vs. equity contracts and equity as a call, complete markets and state prices (Berk Ch. 8–9, 12–13, Grinblatt–Titman Ch. 7, 11, Tirole) | 600 | 3,740 | Audio Overview → Customize |
| `audio/topic2a-audio-part2.md` | Audio (Custom, hard) 2/3 derivations | Topic 2A — unlevering by linearity of covariance, no arbitrage ⇔ positive state prices, Fisher separation, penniless entrepreneur, MM I (homemade leverage, put–call parity, Tirole's identity), MM II and the cost of risky debt (Amaro de Matos Ch. 1–2, Berk §21.5–21.6, Tirole §2.2) | 601 | 3,846 | Audio Overview → Customize |
| `audio/topic2a-audio-part3.md` | Audio (Custom, hard) 3/3 exercises | Topic 2A — PS1 Ex. 2–3; PS2 Ex. 1(a)–(e), 4; Lista R2 ex. 6–11, 14–15; Lista R3 ex. 5, 11, 15; the "borrow more" fallacy; four misconceptions | 572 | 3,691 | Audio Overview → Customize |
| `audio/topic2b-audio-part1.md` | Audio (Custom, hard) 1/3 concepts | Topic 2B — the tax friction, risk of the shield, Miller (1977) and DeAngelo–Masulis, distress costs and evidence, agency costs of debt, bank capital, payout policy (Berk Ch. 16–17, Grinblatt–Titman Ch. 13–16, Amaro de Matos Ch. 2) | 584 | 3,777 | Audio Overview → Customize |
| `audio/topic2b-audio-part2.md` | Audio (Custom, hard) 2/3 derivations | Topic 2B — PV of the shield, three closed forms with growth, WACC vs. APV recursion, MM adjusted cost of capital, Miller's equilibrium, risk-shifting and debt overhang, trade-off FOC, dividend irrelevance | 661 | 4,138 | Audio Overview → Customize |
| `audio/topic2b-audio-part3.md` | Audio (Custom, hard) 3/3 exercises | Topic 2B — Lista R3 ex. 2–4, 6, 8–10, 12–14; PS2 Ex. 1(f), 2, 3; three misconceptions; bridge to Tirole Ch. 3 | 561 | 3,569 | Audio Overview → Customize |

Each topic is a three-episode series: (1) concepts, (2) derivations, (3) exercises and
misconceptions. Generate them in order; each part tells the hosts what the listener already heard.

The prompts follow the real lectures (Prof. Bernardo Ricca, `Map/lectures-index.md`) and the
Ricca remap (books R1–R3, `Listas/lista-r1…r3`). The Tirole-based `aula-01-audio-part1/2` prompts
were retired on 2026-10-24, and the single-file `topic1/2a/2b-audio.md` prompts on 2026-10-31,
when each topic was split into three parts (all recoverable from git history).

> ⚠️ Slide and Audio Customize fields truncate silently at ~6,000 chars. All prompts are kept under 5,000 chars for safety.

> Output language is set once in NotebookLM's **Settings → Output language** (English). The prompts never contain a language line; confirm the setting before generating.

All course materials should be uploaded as separate sources in the same NotebookLM notebook; the
files in `sources/` are the current set, named exactly as the prompts cite them: lecture slides
(`Aula_Topic*.pdf`), problem sets (`Lista_PS*.pdf`), exercise lists (`Lista_R1…R3 *.md`), books
(`Livro_*.pdf`, including Berk–DeMarzo–Harford and Grinblatt–Titman) and syllabi (`Programa_*.pdf`).
These prompts guide how NotebookLM processes those sources.
