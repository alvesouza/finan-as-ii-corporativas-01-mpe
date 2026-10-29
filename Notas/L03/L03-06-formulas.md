---
tags: [notes, lecture-03, formulas, reference]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 2–51, 54–63; block map Map/lectures-index.md (Topic 2B, 2B.1–2B.10)"
---

# L03 · Formulas — every definition, result and number

> Prev: [[L03-05-bank-capital-dividend-irrelevance]] · Next: [[L03-07-pitfalls]] · Map: [[L03-00-map]]

---

## 0 · The exam specification, mapped

The slides carry no learning-goal list; the specification is the lecture's block map
([[../../Map/lectures-index|lectures-index]], Topic 2B), item by item.

| Block | What you must be able to do | Note |
|---|---|---|
| 2B.1 | compute the ITS from two income statements; say why unlevered FCF ignores it; name the friction (differential treatment) | [[L03-01-tax-shield-mm-taxes]] §1–§3 |
| 2B.2 | derive $V_L=V_U+\tau D$ for perpetual safe debt; write the market-value balance sheet and both $r_E$ formulas; derive the three $V_{ITS}$ closed forms; price a debt-financed repurchase | [[L03-01-tax-shield-mm-taxes]] §4, §7–§9 |
| 2B.3 | write the after-tax WACC; derive the three WACC formulas | [[L03-02-after-tax-wacc-apv]] §1–§2 |
| 2B.4 | run APV and WACC; prove their equivalence under constant $D/E$; value a fixed loan by APV | [[L03-02-after-tax-wacc-apv]] §3–§6 |
| 2B.5 | state the 100%-debt puzzle and the evidence against it | [[L03-03-debt-puzzle-bankruptcy-costs]] §1–§2 |
| 2B.6 | explain why default is not an MM violation; classify direct vs. indirect costs; name the three equity–debt conflicts | [[L03-03-debt-puzzle-bankruptcy-costs]] §3–§5 |
| 2B.7 | derive $E(K)$, $D(K)$, $V(K)$; the FOC; sign $dK^*/d\tau$, $dK^*/dC$; solve the uniform case | [[L03-04-static-trade-off]] |
| 2B.8 | judge the three bank-capital statements | [[L03-05-bank-capital-dividend-irrelevance]] §1 |
| 2B.9 | derive $V_t=E\sum\delta^i(X_{t+i}-I_{t+i})$ from sources = uses | [[L03-05-bank-capital-dividend-irrelevance]] §2–§3 |
| 2B.10 | derive the WACC from $V_{L,t}=(FCF_{t+1}+\tau r_DD_t+V_{L,t+1})/(1+r_L)$; use $\bar r_D$, not $r_D$, for a risky bond's shield | [[L03-02-after-tax-wacc-apv]] §7–§8 |

## 1 · Definitions and results

| # | Statement | Assumption that drives it | Derived in |
|---|---|---|---|
| ITS | $ITS=\tau r_DD$ (Berk 16.4) | interest deductible | 01 (1) |
| Perpetual safe debt | per-period payout $(1-\tau)X+\tau r_fD$; $V_{ITS}=\tau D$ | constant, safe, permanent $D$ | 01 (2)–(5) |
| **MM I with taxes** | $V_L=V_U+V_{ITS}$ (Ross 16.3; Berk 16.5; Amaro Prop. 2.1.3, $V^\tau_l=V^\tau_u+\tau B$) | no other friction | 01 (8) |
| Balance-sheet identity | $\frac{D}{V}r_D+\frac{E}{V}r_E=\frac{V_U}{V_L}r_U+\frac{V_{ITS}}{V_L}r_{ITS}$; same for betas | $V_L=D+E=V_U+V_{ITS}$ | 01 (9)–(10) |
| MM II, constant debt | $r_E=r_U+\frac{D}{E}(1-\tau)(r_U-r_D)$ (Ross 16.4); Hamada $\beta_E=\beta_U[1+(1-\tau)D/E]$ | $r_{ITS}=r_D$ | 01 (11) |
| MM II, target $D/E$ | $r_E=r_U+\frac{D}{E}(r_U-r_D)$; $\beta_U=\frac{E}{V}\beta_E+\frac{D}{V}\beta_D$ | $r_{ITS}=r_U$ ("usual assumption") | 01 (12)–(13) |
| $V_{ITS}$, constant debt | $\tau D$ | $r_{ITS}=r_D$ | 01 (14) |
| $V_{ITS}$, continuous target | $\frac{\tau r_DD}{r_U-g}$ | $r_{ITS}=r_U$ | 01 (15) |
| $V_{ITS}$, annual target | $\frac{\tau r_DD}{r_U-g}\cdot\frac{1+r_U}{1+r_D}$ (slide prints $1+r_g$) | shield known one period ahead | 01 (16) |
| After-tax WACC | $r_{WACC}=\frac{E}{V}r_E+\frac{D}{V}r_D(1-\tau)$ (Berk 16.8) | continuous target $D/E$ | 02 (1), (5) |
| General WACC | $r_{WACC}-g=(r_U-g)(1-V_{ITS}/V_L)$ | growing perpetuity | 02 (3) |
| WACC, continuous / annual | $r_U-\tau r_D\frac{D}{V}$; $r_U-\tau r_D\frac{D}{V}\frac{1+r_U}{1+r_D}$ | | 02 (4), (6) |
| WACC, constant debt | $(1-\tau\frac{D}{V})r_U$ | **$g=0$ only** | 02 (7)–(8) |
| APV = WACC | $\frac{FCF_1}{r_{WACC}-g}=\frac{FCF_1}{r_U-g}+\frac{Dr_D\tau}{r_U-g}$ | constant $D/E$ | 02 (9)–(13) |
| APV (Higgins p. 322) | $NPV_{\text{all-equity}}+PV_{ITS}+PV_{\text{side effects}}$ | — | 02 §3 |
| Appendix | $V_{L,t}=\frac{FCF_{t+1}+r_DD_t\tau+V_{L,t+1}}{1+r_L}\Rightarrow V_{L,t}=\sum_i\frac{FCF_{t+i}}{(1+r_{WACC})^i}$ | constant ratio, constant $r_U$ | 02 (14)–(20) |
| Shield of risky debt | $\bar r_D=E[C_{t+1}]/D_t$; after-tax cost $r_D-\tau\bar r_D$ | deduction = coupon paid | 02 (21)–(22) |
| Puzzle | $V_L/V_U=1+\tau D/V_U$ | MM + taxes only | 03 (2) |
| Trade-off: $V_U$ | $\frac{(1-\tau)E[X]}{1+r_f}$ | risk neutrality | 04 (2) |
| Safe debt | $V_L(K)=V_U+\frac{\tau K}{1+r_f}$, $K<\underline X$ | | 04 (3) |
| Equity, debt | $E(K)=\frac{1}{1+r_f}\int_K^{\bar X}(1-\tau)(X-K)h$; $D(K)=\frac{1}{1+r_f}\big[\int_{\underline X}^K(X-C)h+K(1-H(K))\big]$ | tax only if solvent; $C<\underline X$ | 04 (4)–(5) |
| **Firm value** | $V(K)=V_U+\frac{1}{1+r_f}\big[\tau\big(\int_{\underline X}^Kxh+K(1-H)\big)-CH(K)\big]$ | | 04 (6) |
| APV with distress | $V_L=V_U+V_{ITS}-PV(\text{bankruptcy costs})$ (Berk 16.10) | | 04 (7) |
| Second reading | $V=V_U+\tau D(K)-\frac{(1-\tau)CH(K)}{1+r_f}$; $C=0\Rightarrow V_U+\tau D(K)$ | | 04 (8)–(9) |
| Marginal value | $(1+r_f)V'(K)=\tau[1-H(K)]-Ch(K)$ | Leibniz | 04 (10) |
| **FOC** | $\tau[1-H(K^*)]=Ch(K^*)$ | | 04 (11) |
| SOC; statics | $-\tau h-Ch'<0$; $dK^*/d\tau>0$, $dK^*/dC<0$ | SOC | 04 (12)–(14) |
| Uniform $h$ | $K^*=\bar X-C/\tau$ if $C<\tau(\bar X-\underline X)$, else $\underline X$ | | 04 (16) |
| MM3 | $V_t=E\big[\sum_{i\ge1}\delta^i(X_{t+i}-I_{t+i})\big]$ (Amaro Prop. 4.1.1, (4.5)) | investment plan fixed | 05 (1)–(6) |

## 2 · Every number in the lecture

| Case | Data | Result | Note |
|---|---|---|---|
| Two firms (slide 2, Berk Table 16.2) | EBIT 1850, interest 350, τ 35% | taxes 525 vs 647.5; NI 975 vs 1202.5; **ITS 122.5**; FCF 1502.5 both | 01 §1–§2 |
| Ross firms U, L (pp. 551–553) | EBIT 1000, D 1000 at 8%, τ 30%, $R_U$ 10% | ITS 24; $V_{ITS}$ 300; $V_U$ 7,000; $V_L$ 7,300; $R_E$ 10.22%; WACC 9.59% | 01 §5 |
| Higgins Timid/Bold (p. 225) | EBIT 400, 800 debt at 10%, τ 40% | 80% vs 96% for 200 of equity; gap 32 = 0.4 × 80 | 01 §6 |
| Repurchase (slides 14–15) | $V_U$ 600, 1000 shares, D 500, τ 40% | $V_L$ 800, E 300, **P = 0.8**, N = 625, gain 200 | 01 §9 |
| Slide-13 forms at slide-28 data | D 25,000, $r_D$ 5%, τ 40%, $r_U$ 12%, g 4% | 6,250 (continuous); 6,666.67 (annual); 10,000 (fixed) | 01 §8 |
| Project (slides 28–31) | 60,000; FCF 7,500, g 4%; τ 40%; D/V 25%; $r_E$ 14.33%; $r_D$ 5% | **WACC 11.5%**, $V_L$ 100,000, NPV 40,000; $r_U$ 12%, $V_U$ 93,750, $V_{ITS}$ 6,250 | 02 §5 |
| Fixed loan (slide 32) | 60,000 at 5%, repaid year 5 | ITS 1,200 × 5; $V_{ITS}$ 5,195; **$V_L$ 98,945** | 02 §6 |
| Berk Example 16.4 (p. 476) | 2 bn, 6%, 10 years, τ 35% | 42 m/yr; PV 309 m | 02 §6 |
| Risky bond (slides 62–63) | face 1,000, coupon 5%; $E[\cdot]$ 700, D 525 | $r_D$ 33.33%; with coupon 50: $\bar r_D$ 9.52% | 02 §8 |
| Puzzle (slide 33) | τ 35% | +7% at D = 20% $V_U$; +17.5% at 50% | 03 §1 |
| Jagannathan et al. (slide 34) | 10 industries, 2016 | $D/(D+S)$ 0.12 (high-tech) – 0.44 (durable) | 03 §2 |
| Trade-off, uniform (own calibration) | $U[50,150]$, τ 35%, C 20, $r_f$ 5% | $V_U$ 61.90; **$K^*$ 92.86**; $H$ 0.429; $V_{ITS}$ 27.89; PV(bc) 8.16; **$V^*$ 81.63**; D 71.53; E 10.11 | 04 §5 |
| Wharton (Ross p. 588) | 10,000 × 2 years, 100 shares, 10% | 173.55 under 100/100 and 110/89 | 05 §3 |
| Genron (Berk pp. 503–507) | FCF 48 m, 12%, cash 20 m, 10 m shares | 42 under all three policies | 05 §3 |
