# Plan — Class 1 notes + interactive companion

Date: 2026-10-09. Scoping answered via AskUserQuestion (one round).

## Deliverables
1. `Aula/aula-01-notes.md` — class notes, Markdown, English. Sections: what corporate finance
   studies (Intro pp. 1–2), governance (Ch. 1 §1.1–1.2), MM benchmark (§2.2 pp. 77–79, two
   derivations), stylized facts (§2.5 Tables 2.2, 2.4, 2.5, 2.6, p. 97, p. 101), the
   resolution (§3.2 pp. 115–118), scope line, readings, self-check questions.
2. Fill placeholders in `rules/01_introducao_fatos.md` with formulas and signed comparative
   statics (they are the authority the companion's read-outs must agree with).
3. `Videos/aula-01-what-is-corporate-finance/companion.html` — published as a private Artifact.

## Companion contract
Model: Tirole §3.2.1–3.2.2, eqs. (3.1)–(3.6), pp. 115–118. Units: thousand reais.

| Control | Range | Step | Default | Group |
|---|---|---|---|---|
| A net worth | 0–60 | 1 | 10 | founder |
| B private benefit | 0–60 | 1 | 20 | agency |
| p_L success prob. if shirking | 0–(p_H) | .01 | .40 | agency |
| R income if success | 100–250 | 1 | 160 | technology |
| p_H success prob. if behaving | .50–1.00 | .01 | .80 | technology |
| I investment | 70–200 | 1 | 100 | technology |

Panels: (1) U_b(A) step over A ∈ [0, 60], Ā marked, founder dot; (2) bars: P vs I − A;
split of R into max promise R − B/Δp (teal) and min stake B/Δp (blue), needed R_l tick.
Headline: FUNDED / RATIONED + gap A − Ā (= P − (I − A)).
Degenerate: Δp = 0 with B > 0 (no IC possible), Ā < 0, Ā > A-axis, (3.1)/(3.2) violated,
p_L > p_H clamped by the control itself.
Verification: Python at three vectors (low ends, default, high ends).
