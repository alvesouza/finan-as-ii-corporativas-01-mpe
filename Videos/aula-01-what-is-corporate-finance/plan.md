---
tags: [video, aula-01, explainer, plan]
date: 2026-10-09
slug: aula-01-what-is-corporate-finance
---

# Plan — Class 1: What Is Corporate Finance? Introduction and Stylized Facts

**Scoping answers (2026-10-09).** Purpose *first exposure*; length **~50 min**; math **textbook
derivation**, every line on screen; examples *a concrete firm story + Brazilian corporate
context + Tirole's stylized facts*. Narration **English** per the global rule.

Sources: Tirole (2005 printing of the 1st ed.), Introduction (pp. 1–10), Ch. 1 §1.1–1.2
(pp. 15–29), Ch. 2 §2.2 and §2.5–2.6 (pp. 77–80, 95–102), and the opening of §3.2 (pp. 115–118).
All pages are **printed** (PDF = printed + 13). Class plan: [[Map/study-guide|Class 1]].

---

## Thesis

> **Modigliani and Miller proved that how you carve the pie cannot change its size. Corporate
> finance exists because, once the people who run a firm are not the people who fund it, the
> carving *does* change the size — and a project that creates value can die for want of a
> few reais.**

Every beat serves one of three jobs: show the benchmark (MM), show the facts that contradict
it (Ch. 2), show the one assumption whose failure explains them (non-contractible behaviour,
§3.2).

## The cold open, with its clock (0:00–1:30)

One firm, three numbers, one refusal.

| | |
|---|---|
| Investment needed, $I$ | 100 thousand reais |
| The founder's own money, $A$ | 10 thousand reais |
| Expected value created, $p_H R - I$ | **+28 thousand reais** |

*"A founder in Campinas has a project that costs a hundred thousand reais and, run properly,
is expected to return a hundred and twenty-eight. She has ten of her own. Every investor she
meets agrees the project is good. Every one of them says no. By the end of this video you will
be able to compute exactly why — and you will find that she is short by two thousand reais of
something that is not money."*

No definition in the first ninety seconds. The hook is a refusal that a frictionless theory
says cannot happen, and resolving it is the whole of Act IV.

**The firm's numbers** (Tirole's fixed-investment model, §3.2, our calibration):
$I=100$, $A=10$, $R=160$, $p_H=0.8$, $p_L=0.4$, $B=20$ (thousand reais).
Checked: (3.1) $p_HR-I = 128-100 = 28 > 0$; (3.2) $p_LR-I+B = 64-100+20 = -16 < 0$;
$\Delta p=0.4$; $B/\Delta p = 50$; pledgeable income $p_H(R-B/\Delta p)=0.8\times110=88$;
needed $I-A=90$; agency rent $p_HB/\Delta p=40$; threshold $\bar A = 40-28 = 12$.
So $A=10<\bar A=12$: **rationed by 2**. (Verify again in `check_numbers.py` before narration.)

## Colour mapping — one meaning each, for the whole video

| Colour | Role |
|---|---|
| `BLUE` | insiders: the founder / manager, her stake $R_b$, her private benefit $B$ |
| `TEAL` | outsiders: investors, lenders, their claim $R_l$ |
| `YELLOW` | the live derivation line; the object of attention |
| `GREY` | muted: lines already past; background data |
| `RED` | what breaks: MM's prediction failing, the rationed project |
| `GREEN` | what survives: the funded project, the repaired result |

## Beat sheet — 28 beats

**Word budget.** `george` measured 192–197 wpm over three Macro videos; each `[pause]` is a
2.5 s held frame. Script: 9,192 words + 106 pauses ≈ **51.6 min** (`build_beats.py`). Seconds
below were the first-draft targets; `beats.json` is the contract, rebuilt from measured audio.

**Added after the first draft** (the 22-beat script came to 33 min; content from the assigned
chapters, not padding): `BeatOptions` (§1.2.2, shares vs options), `BeatWatchers` (§1.2.3–1.2.5),
`BeatBanksVsMarkets` (Table 2.5, p. 99), `BeatTiming` (p. 101), `BeatRicherFounder` (the
contract above $\bar A$, $1+\iota = 1/p_H$, p. 116), `BeatComparativeStatics` (derivatives of (3.3)).

### Act 0 — the refusal

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatOpen` | the three numbers, one at a time; investors' heads shaking | pose the refusal; promise to compute it | 90 | §3.2, p. 115 |

### Act I — what the field studies (Introduction; §1.1–1.2)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatTwoSides` | insiders (BLUE) and outsiders (TEAL) either side of a firm; arrows of money in, claims out | the field is a principal–agent relationship; the three asymmetries: adverse selection, hidden knowledge, moral hazard. Arrow–Debreu "said little about the firms' financial choices" | 130 | pp. 1–2 |
| `BeatBerleMeans` | dispersed shareholders → one manager; the governance definition written out | Berle–Means 1932; governance = how suppliers of finance "assure themselves of getting a return" | 120 | pp. 15–16 |
| `BeatFourGuises` | a real table, four rows: insufficient effort · extravagant investment · entrenchment · self-dealing | one example per row (Jensen's oil drilling; RJR Nabisco's ten aircraft) | 150 | §1.1.1, pp. 16–17 |
| `BeatIceberg` | an iceberg: tip = scandals, submerged = "the averted ones" | CEO pay ×3 (1980–94), ×2 again (1994–2001); 531× the average wage in 2000 vs 42× in 1982; WorldCom's 7.1 billion dollars. Observed misbehaviour is the tip | 130 | pp. 17–20 |
| `BeatGrocer` | **derivation-lite**: a 1,000-dollar rise in value → 3.25 dollars to the CEO; the grocer | Jensen–Murphy: median stake 0.25%; "start eating the apples". Instruments list: pay, implicit incentives, monitoring, competition | 150 | §1.2, pp. 20–25 |
| `BeatTwoAgencyProblems` | two org charts side by side: dispersed owners vs. a controlling shareholder | Anglo-Saxon vs. European (Tirole p. 15) — and Brazil sits with the second. Novo Mercado (one share, one vote) and ADR cross-listing as ways to import investor protection (p. 118) | 140 | pp. 15, 118 |

### Act II — the benchmark (§2.2)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatPie` | a pie, carved two ways, same size | MM 1958; "the size of the pie is unaffected by the way it is carved"; the four assumptions | 110 | pp. 1, 77 |
| `BeatValueAdditivity` | **derivation, ~7 lines**: equity payoff $\max(0,R-D)$, debt $\min(R,D)$, case split, sum $=R$, take expectations | value additivity: $V_E+V_D=E(R)$, independent of $D$ | 170 | p. 78 |
| `BeatPayoutIrrelevance` | **derivation, ~9 lines**: arbitrage price, the cash identity, substitute, iterate | dividend policy cannot change value: $V_t=E[\sum_{\tau\ge1}\beta^\tau(R_{t+\tau}-I_{t+\tau})]$ | 180 | p. 78 |
| `BeatPuzzle` | the opening firm put through MM: "NPV > 0 ⇒ funded" in RED, crossed out | **wrong first attempt**: MM says she gets funded. She does not. Tirole's sentence: when decisions cannot be specified contractually, "the split of the pie matters" | 130 | p. 79 |

### Act III — the facts MM has to face (§2.5)

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatInternalFinance` | Table 2.2 as a real table, five countries, four rows (retentions, loans, bonds, shares) | retained earnings dominate everywhere; banks next; new shares a small fraction | 150 | Table 2.2, p. 96 |
| `BeatNetEquity` | bars: equity share of fixed-capital formation in 1999 (US 12, UK 9, France 9, Japan 8, Germany 6) | in 1984–86 US firms bought back more shares than they issued; "basically all external financing was debt" | 130 | p. 97 |
| `BeatLeverage` | Table 2.4 subset: manufacturing, trade, services, banks | typical debt–equity ≈ 2; banks 11; who borrows: steady cash flow, redeployable collateral | 130 | pp. 98–100 |
| `BeatAnnouncement` | Table 2.6 subset: equity −3.1%, convertibles −2.0%, straight bonds −0.3% (n.s.) | the market reads a share issue as bad news; a bank loan as good news | 130 | p. 101 |
| `BeatFactsToClasses` | each fact on the left, the class that explains it on the right | information, incentives, capital, liquidity, collateral, monitoring (§2.6) — the map of the course | 90 | p. 102 |

### Act IV — the one assumption (§3.2) — the derivation

| Beat | On screen | Narration's job | s | Anchor |
|---|---|---|---|---|
| `BeatSetup` | the timeline (Fig. 3.1); the parameters table with our numbers | the founder can behave ($p_H$) or shirk ($p_L$, private benefit $B$); assumptions (3.1)–(3.2) checked numerically | 140 | pp. 115–116 |
| `BeatIncentive` | **derivation, ~6 lines**: IC → $R_b\ge B/\Delta p$ → max promise $R-B/\Delta p$ → pledgeable income $\mathcal P=p_H(R-B/\Delta p)$ | each line with its number: 50, 110, 88 | 170 | p. 116 |
| `BeatThreshold` | **derivation, ~6 lines**: $\mathcal P\ge I-A$ → $A\ge\bar A=p_HB/\Delta p-(p_HR-I)$ (3.3) | $40-28=12$; she has 10; rationed by 2. "One only lends to the rich" | 170 | p. 117 |
| `BeatStep` | $U_b(A)$: zero, then a jump to 28 at $\bar A$; our founder a RED dot at 10 | the jump (3.6); what moves $\bar A$: more net worth, smaller $B$, larger $\Delta p/p_H$; investor protection lowers $B$ | 130 | pp. 117–118 |
| `BeatMMRecovered` | set $B\to0$: $\bar A$ slides to $-28$, the dot turns GREEN | with contractible behaviour the model **is** MM — every positive-NPV project is funded. One assumption separates the two worlds | 110 | pp. 1, 79 |
| `BeatClose` | the closing image | the course as a list of relaxations of MM | 100 | — |

## The wrong first attempt

Act II ends by running the opening firm through MM: positive NPV, so it must be funded. It is
not. Act IV repairs it by dropping exactly one assumption (contractible behaviour) and shows
that putting it back (`BeatMMRecovered`) returns MM. The failure and the fix are the same
parameter, $B$.

## Scope line

- **Class 4–5 own** MM in full: MM2, home-made leverage, taxes, default costs, the trade-off.
  Here only Tirole's two p. 78 arguments.
- **Class 6 owns** the fixed-investment model in full: debt–equity equivalence (§3.2.3),
  overborrowing (§3.2.4), the equity multiplier. Here only IC → pledgeable income → $\bar A$.
- **Classes 11–12 own** why a share issue is bad news; it is shown as a fact only.
- Valuation (Classes 2–3) is not touched.
- **No exercise statement is animated.** Tirole Ch. 3 exercises 3.1–3.3 are cited by number
  and page (p. 144) as follow-up practice.
- Not used, because the conversion is unreadable: Fig. 1.2 (turnover by country) and Fig. 2.4
  (net sources). Brazil appears as institutional narrative only — no Brazilian numbers,
  because none are in the course books.

## Closing image

**The step.** $U_b(A)$ at zero, jumping to 28 at $\bar A=12$, with the founder as a red dot at
$A=10$, two units short. Above the step, the pie split: a BLUE slice the founder must keep
($R_b\ge 50$) and a TEAL slice that is all investors can be promised.

Why this frame: it holds the entire argument in one picture — MM is the world where the step
sits left of zero; corporate finance is the world where it does not.

## The novelty line

Textbooks state MM and list the facts that contradict it in separate chapters. This video
proves MM, lays the facts against it, and then shows — with one founder's numbers on screen —
the single assumption whose failure reconciles them, and that restoring it gives back MM
exactly.

## Build order

1. `check_numbers.py`: every number in the calibration and every table value re-read from the
   PDF (Tables 2.2, 2.4, 2.6; p. 18 pay; pp. 24–25 Jensen–Murphy; p. 97 equity shares).
2. `script.md` → `beats.json`.
3. **Narration is blocked**: the Speechify workspace returned HTTP 402 *Insufficient Credits*
   on 2026-10-09. Either top up, or build with `--no-voice` (silent, subtitled, durations
   estimated) and add narration later — the audio is a cached artefact, so the scenes do not
   change.
4. `scenes.py` with the kit (`Beat`, `Stage`, `table`, `eq`), the Macro project's fixed-grid
   derivation stack carried over; `layoutcheck` → `beatcheck` → render `-ql` → compile the
   480p draft → ask before 1080p.
