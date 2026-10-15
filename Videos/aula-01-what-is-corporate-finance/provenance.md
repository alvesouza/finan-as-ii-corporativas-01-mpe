---
tags: [video, aula-01, explainer, provenance]
date: 2026-10-09
slug: aula-01-what-is-corporate-finance
---

# Provenance — Class 1: What Is Corporate Finance?

**Thesis.** Modigliani and Miller proved that how you carve the pie cannot change its size;
corporate finance exists because, once insiders' behaviour cannot be contracted on, the
carving changes the size — and a value-creating project can go unfunded.

## Sources (all pages printed; Tirole PDF = printed + 13)

Tirole, *The Theory of Corporate Finance*, Princeton UP (2005 printing of the 1st ed.):

| Used in | Content | Pages |
|---|---|---|
| BeatTwoSides, BeatPie | Introduction: Arrow–Debreu "said little…", MM, "the size of the pie is unaffected by the way it is carved", three asymmetries | 1–3 |
| BeatBerleMeans | Berle–Means 1932; governance definition (Shleifer–Vishny) | 15–16 |
| BeatFourGuises | §1.1.1 four guises; Jensen oil example; RJR Nabisco 10 aircraft / 36 pilots; Maxwell; Tyco > 100 million dollars | 16–17 |
| BeatIceberg | pay ×3 (1980–94), ×2 (1994–2001), 531× vs 42×; pay for luck, 23–33%; WorldCom 7.1 billion dollars; "the averted ones" | 17–20, 23 |
| BeatGrocer | instruments; Jensen–Murphy 0.25%, 3.25 per 1,000; grocer; Hall–Liebman 25 (5.30) | 20–25 |
| BeatOptions | share vs option payoff, max(0, P − P^S); under water; Ascend; > half out of the money in 2002 | 23–24 |
| BeatWatchers | turnover; Gilson 52% vs 19%; active vs speculative monitoring; non-audit fees, 28 of 30 Dow firms; competition quote | 25–29 |
| BeatTwoAgencyProblems | dispersed vs controlling shareholder; family firms (Sraer–Thesmar); Burkart et al.; investor protection and cross-listing | 15, 94, 118 |
| BeatValueAdditivity, BeatPayoutIrrelevance | §2.2 the two MM arguments | 77–78 |
| BeatPuzzle | "Whenever managerial decisions cannot be perfectly specified contractually…"; covenants, incentives, monitoring | 78–79 |
| BeatInternalFinance | Table 2.2, Mayer (1990) | 96 |
| BeatNetEquity | Rajan–Zingales 65% vs 68%; 14%; 1999 equity shares of GFCF | 96–97 |
| BeatLeverage | Table 2.4, White (1991); Bradley et al.; LBOs; Frank–Goyal 0.32 | 98–99 |
| BeatBanksVsMarkets | Table 2.5 (Thesmar, national accounts, 2002) | 99 |
| BeatAnnouncement | Table 2.6, Eckbo–Masulis (1995); bank-loan announcements (James 1987) | 101 |
| BeatTiming | business-cycle facts (i)–(vi); market timing | 101–102 |
| BeatFactsToClasses | §2.6 conclusion | 102 |
| Act IV | §3.2 fixed-investment model: (3.1)–(3.6), IC_b, IR_l, pledgeable income, Ā, agency rent, "one only lends to the rich", 1 + ι = 1/p_H, debt–equity equivalence (§3.2.3) | 115–119 |
| BeatClose | exercises 3.1–3.3 | 144 |

Every table value shown on screen was re-read from the PDF's own text layer on 2026-10-09
(not from the markdown conversion). Fig. 1.2 and Fig. 2.4 were **not** used: their bar values
cannot be assigned to countries in the text layer.

**Not from the course books** (institutional narrative, no numbers): Brazilian controlling-
shareholder structure and non-voting preferred shares; B3 Novo Mercado (one share, one vote,
created 2000); ADR cross-listing by large Brazilian firms; BNDES as a long-term lender; that
Modigliani (1985) and Miller (1990) both received the Nobel prize.

**The founder's calibration** is ours, not Tirole's: I = 100, A = 10, R = 160, p_H = 0.8,
p_L = 0.4, B = 20 (thousand reais). Every derived number is asserted in `check_numbers.py`.

## Assets

None borrowed. Every shape is drawn in Manim; no images, logos, or downloaded media.

## Build

| | |
|---|---|
| Manim Community | 0.21.0 |
| ffmpeg | 8.1.1 (gyan.dev full build) |
| Scene kit | `video_explainer` 0.2.0, pip -e from `D:/Documents/Git/Github/Video explainer` |
| Scenes | `scenes_common.py` + `scenes_g1`–`g5.py` → `scenes.py` (`build_scenes.py`); 28 beats, 487 steps |
| Gates | `beatcheck --rendered`: 28/28 ok, render − target within +0.00…+0.06 s; `layoutcheck`: 28/28 clean |
| Voice | **none** — Speechify returned HTTP 402 *Insufficient Credits* on 2026-10-09. Durations estimated at 195 wpm (george's measured rate over three Macro videos) + 2.5 s per `[pause]` |
| Draft | `aula-01-what-is-corporate-finance-480p.mp4`, 854×480, 15 fps, 3094.57 s (51 min 35 s), 24.16 MB, silent, drift 0.0 ms (no audio track); recompiled 2026-10-10 after fixing BeatThreshold and BeatBerleMeans |
| SHA-256 (draft) | `2FA8F3B8662F16C8B7378ED20E42C6B32A939EB9CDF3E05C3C9AF689382495DD` |
| Subtitles | `aula-01-what-is-corporate-finance-480p.srt`, 722 sentence cues, spans from rendered beat lengths (`build_beats.py --srt`) |

## Companion

`companion.html` — *The Rationing Threshold*, an interactive page on Tirole §3.2 (six sliders:
A, B, p_L, R, p_H, I; the step chart, the pledgeable-income bars, live figures, ∂Ā/∂·). Built
unrequested by a scene agent on 2026-10-09; kept at the user's request (2026-10-10) after
review: every expression matches (3.1)–(3.6), including ∂Ā/∂p_L = p_H B/Δp² and
∂Ā/∂p_H = −R − p_L B/Δp², which the video does not show; defaults are the video's
calibration. One fix: a footer reference to a non-existent notes file was removed. Loads
Google Fonts; otherwise self-contained. Note: its "B = 15" preset answers the viewer exercise
posed in BeatClose.

## Fixed after the first draft (2026-10-10)

- `BeatThreshold`: the "constraint fails" note now clears when the "can be negative" aside
  starts.
- `BeatBerleMeans`: the shareholder grid was shown via `show()`, which recentred it away from
  the arrow laid out against it; the early step now shows a copy.

## Known issues

- Kit issues found and fixed locally (worth fixing upstream in Video explainer): the Macro
  project's derivation `Stack` revealed every line at the first step; `speechify-tts --srt`
  ignores held-pause time and emits one cue per beat.

## Adding narration later

1. Top up Speechify; `speechify-tts --check`.
2. `speechify-tts --script beats.json` (synthesises 28 clips; the text is unchanged).
3. `python build_beats.py` — re-reads measured clip lengths, re-adds 2.5 s per pause.
4. Re-render (beat lengths change), `beatcheck . --rendered`, `explainer-compile .`,
   `python build_beats.py --srt media/videos/scenes/<quality>`.
