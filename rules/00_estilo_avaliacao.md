# Estilo de Avaliação (MPE) — regras de listas, simulados e correção

> **Style `macro-1`, rebound to Finanças II – Corporativas (MPE Insper).** Grading rules
> (anatomy, scoring, distractors, solution/rubric format, graduate mode) are kept from the
> Macro I original; course bindings (§1 blocks, §2 distractors, §3 context, §5 bibliography,
> §7 exclusions, §8 scope) are rewritten for corporate finance.

Especificação do estilo das avaliações de **Finanças II – Corporativas (MPE Insper)**. É a fonte única
de verdade para os comandos `/exam-gen` (gerar lista + gabarito) e `/exam-grade` (corrigir a
resolução do aluno). Casada com o template `Listas/lista-exam.tex`.

## 1. Estrutura do documento

- Organização em **blocos temáticos** (1 a 4). Cada bloco mapeia a um conjunto de aulas e
  vale um total de pontos (no simulado completo: 4 blocos × 25 = 100 pts; numa lista
  temática, use 1–2 blocos).
- Cada bloco tem, tipicamente, **duas questões**:
  - **Questão objetiva** (10 pts): itens **a) e b)** de múltipla escolha (3 pts cada, 4–5
    alternativas, sem penalização por erro) + itens **c) e d)** de **Verdadeiro/Falso**
    (2 pts cada).
  - **Questão discursiva** (15 pts): um enunciado-mãe contextualizado + sub-itens **a), b),
    c)** (5 pts cada), com espaço "Resolução:".
- Numa **lista de exercícios** o tamanho é flexível (o aluno escolhe o escopo); mantenha a
  mesma anatomia de questões.

### Regra de V/F (sempre na capa/instruções)
Nota dos itens V/F $=\max\{0,\ \text{acertos}-\text{erros}/2\}\times$ valor do item. Itens
em branco não contam como erro.

### Natural blocks in Finanças II

Classes follow the proposed 16-class plan in `Map/study-guide.md` until the real calendar arrives.

| Block | Topics | Classes | Theme |
|---|---|---|---|
| I | 1-3 | 1-5 | Stylized facts, valuation, frictionless (MM) benchmark |
| II | 4-5 | 6-10 | Agency costs, borrowing capacity, governance, liquidity management |
| III | 6-7 | 11-13 | Asymmetric information and capital structure; activism and monitoring |
| IV | 8-9 | 14-16 | Mergers and acquisitions; macroeconomic implications |

## 2. Taxonomia das questões

- **Múltipla escolha (a, b):** aplicação direta de fórmula ou identificação de conceito.
  4–5 alternativas. Distratores plausíveis e do **mesmo comprimento** da correta
  (anti-chute), reflecting common corporate-finance mistakes:
  - confusing **pledgeable income × total NPV**, **book × market leverage**, **cash flow × earnings**;
  - discounting **equity** cash flows at the **WACC** (or FCFF at the cost of equity);
  - applying MM irrelevance where taxes, default costs or agency frictions are in the model;
  - getting the sign of the **incentive (IC) constraint** wrong, or dropping limited liability;
  - reading a **pooling** equilibrium as separating (or the reverse) under asymmetric information;
  - treating the target's free-rider problem in takeovers as if bidders captured the full gain.
- **True/False (c, d):** test **false converses** and conceptual traps (e.g. "higher
  pledgeable income raises borrowing capacity" is T; "a positive-NPV project is always
  financed" is F under moral hazard; "debt is irrelevant to firm value" needs the MM
  assumptions). One claim per item, no ambiguity.
- **Discursive (a, b, c):** increasing progression — set up the problem (agents, contracts,
  IR/IC constraints, timing) → solve/derive (optimal contract, financing capacity,
  equilibrium) → interpret (comparative statics, welfare, governance or policy). Each
  sub-item tests a distinct aspect of the same scenario.

## 3. Contextualização (marca do estilo)

- **Every** question is anchored in a **plausible, current Brazilian corporate scenario**:
  a real institution, instrument or episode — B3 listing segments (Novo Mercado), CVM rules,
  debêntures and CRI/CRA, BNDES credit, Selic and CDI as benchmark rates, JCP (juros sobre
  capital próprio) tax treatment, judicial recovery (recuperação judicial), takeovers and
  tender offers (OPA), activist funds, controlling-shareholder structures. The context is a
  shell; the core is the course model.
- Numerical parameters **chosen for clean closed-form answers** (binary outcomes, success
  probabilities $p_H, p_L$, private benefit $B$, investment $I$, net worth $A$, risk-neutral
  investors with zero rate). Say "illustrative values" when appropriate.
- Não confundir realismo institucional com extrapolação teórica: **só modelos do curso**
  (ver `CLAUDE.md`, seção "NÃO extrapolar").

## 4. Formato da solução (gabarito)

- **Objetivas:** `Gabarito: X` + 1–3 linhas justificando (conta ou conceito).
- **Discursivas:** sequência numerada **"Passo — título. texto."** (montagem → derivação →
  resultado → verificação). Inclua:
  - **Intuição econômica.** parágrafo curto com o "porquê".
  - **Ref:** âncora bibliográfica (capítulo + seção, e página quando o `Map/` tiver).
  - **Rubrica de correção.** distribuição de pontos por passo, com:
    - **Tetos por erro conceitual** (ex.: "confundir taxa de poupança da Regra de Ouro com
      a que maximiza $k^*$ → máx. 2 pts no sub-item"; "usar $\Delta k = sf(k)$ sem
      depreciação → máx. 1 pt").
    - **Penalidades leves** por erro aritmético com método correto ($-1$ pt).
    - **Não-cumulatividade:** tetos conceituais prevalecem sobre penalidades leves (não se
      somam).
  - **Risco residual** (opcional): pegadinha comum / ambiguidade do enunciado a evitar.
- **Graphs.** Several Tirole results read off a diagram (financing region in $(A, I)$ space,
  pledgeable income vs. investment, credit rationing). The rubric scores **labelled axes,
  named curves/regions and the direction of shifts** separately from the verbal conclusion.

## 5. Uso da bibliografia (obrigatório)

Ancore conteúdo e referências nos livros do curso, via `Map/` e `rules/` quando existirem:

- **Tirole (2006)** — **floor** (chapter/section in every question); its exercises and
  Review Problems (Part VII) are the main source of ideas.
- **Amaro de Matos (2001)** — formal MM, asymmetric-information and security-design results.
- **Ross et al.** — valuation and cost of capital. Local copy: *Fundamentos de Administração
  Financeira* (9th ed., 2013), not the syllabus's *Administração Financeira* (10th ed., 2015).
- **Higgins** — practitioner valuation and financial analysis. Local copy: 13th ed. (2023),
  not the syllabus's 2011 edition.

⚠️ Cite the **local** edition and say which (see `Livros/BOOKS.md`); never cite pages of a
book that is not in `Livros/`.

Formule questões **originais** a partir do entendimento dos conceitos; nunca copie ou
parafraseie exercícios do livro. Use o `Map/` para pesos por tópico e para páginas nas
linhas `Ref:`.

## 6. Convenções LaTeX

- Template: `Listas/lista-exam.tex`. Um único `.tex` com `\ifsolucoes`:
  - `\solucoesfalse` → **lista em branco** (espaço para resolver).
  - `\solucoestrue` → **gabarito + rubrica** (mesmo arquivo).
- Macros: `\bloco`, `\questao`, `\alternativas`, `\gabarito`, `\resolespaco`, `\passo`,
  `\intuicao`, `\refbib`, `\rubrica`; blocos de solução dentro do ambiente `sol` (excluído
  na lista em branco via pacote `comment`).
- **Regra global de PDF copiável:** preâmbulo já traz `\usepackage{lmodern}` e
  `\usepackage{cmap}` após `fontenc`. Compilar com `pdflatex` (2×) e verificar `pdffonts`
  (tudo **Type 1**, nunca Type 3).
- Matemática em `$...$`/`$$...$$`. Nunca usar `$` solto para moeda (escreva "120 reais").
- Graphs in **TikZ/pgfplots** (financing regions, pledgeable income) — never a raster image.

## 7. Anti-padrões

- Do not extrapolate beyond the course (check `CLAUDE.md`). In particular: no continuous-time
  asset pricing, no option-pricing derivations beyond what the syllabus topics need, no
  material outside the nine syllabus topics.
- **Anti-chute de formatação:** a correta não pode ser sistematicamente a mais longa, nem a
  única com parênteses/fórmula/exemplo. Escreva os distratores no mesmo nível de detalhe e
  no mesmo estilo da correta (parênteses, hedges, símbolos, unidades) — às vezes mais
  longos, às vezes mais curtos. A única coisa que distingue a correta é ser verdadeira,
  nunca o formato. Distribua a posição da correta (não fixar A).
- **Majority-vote guessing.** If every distractor changes exactly one feature of the key, the
  key is the feature-by-feature majority of the options and can be found without the
  content: at least one distractor per item combines two named mistakes. Check the correct
  letters across the whole list too (every letter used, no repeating pattern), above all
  when different blocks were written separately.
- V/F sem pegadinha = questão fraca; prefira recíprocas e hipóteses que "quebram".
- Solução sem rubrica e sem intuição = incompleta.
- A moral-hazard question that does not state **who is risk-neutral, whether limited
  liability holds, and the investors' required return** is ambiguous. Always declare.

## 8. Graduate level (opt-in for lists and mock exams)

Chosen in `/exam-gen` Step 3 (*Graduate level* depth, *Graduate* math complexity). The
anatomy of §1–§4 stays (blocks, objective + discursive, rubric, intuition, `Ref:`); the bar
moves.

**Scope.** The syllabus does not grow: the exclusions of §7 and `CLAUDE.md` hold. What
rises is the mathematics applied to the course's own models. In this mode Tirole's
continuous-investment, variable-investment and multi-period variants, his Review Problems,
and Amaro de Matos's formal treatment are the main source of ideas. *Why:* a harder list that changes the
topics trains for an exam the student will not sit.

**Symbolic by default.** Graduate lists and mock exams are posed and solved in parameters
($\alpha,\beta,\sigma,\dots$ with their admissible ranges), without calibrated numbers:
answers are closed forms, conditions, signs, orderings and limits; multiple-choice options
are expressions or conditions; a result with no closed form is characterized (existence,
uniqueness, monotonicity, bounds) and proved. The Brazilian context stays as narrative.
`/exam-gen` asks whether to include numbers; only on an explicit yes do items add calibrated
values, numeric sensitivity tables and numbered axes. *Why:* at this level the skill tested
is deriving and signing results; calibrated numbers move the effort to arithmetic and let a
student who cannot read the model score by computing.

**Questions.**
- Every discursive question starts from **primitives** (agents, technology, information,
  contracting constraints, timing). The student derives what an intermediate list would hand
  over (IC and IR constraints, pledgeable income, financing threshold $\bar A$, separating
  condition) and then uses it.
- General forms come before special cases: continuous before binary effort, variable before
  fixed investment, general return distribution before two-point. Distractors and traps come
  from applying the special case where it fails.
- Each block contains at least one item of each kind: a **proof** ("show that", existence,
  uniqueness, sign of a derivative by implicit differentiation); an **equilibrium
  characterization** (pooling vs. separating, existence of a financing equilibrium, optimal
  liquidity buffer, takeover-bid equilibrium); a **limit or knife-edge case** ($B\to0$,
  $\Delta p\to0$, $A\to\bar A$, full vs. no pledgeability); a **quantification** in closed
  form (agency cost, deadweight loss of rationing, value of a credit line; calibrated
  numbers only when opted in).
- Objective items need three or more derivation steps or a trap only the general case
  reveals; none is answerable by plugging into a memorized formula.
- **Cross-topic questions.** Every discursive question chains at least two course topics
  that interact inside one model: the result of one is an input of the other (agency ×
  liquidity, asymmetric information × capital structure, control rights × activism,
  takeovers × governance, credit rationing × macro activity). Name the topics in the question's heading. At least two objective items per block
  also cross topics. *Why:* at this level the exam tests whether a result can be carried from
  one model into another, not whether one model can be reproduced.
- **Integrative questions.** Each graduate list has an integrative block, and each block of a
  graduate mock exam has at least one integrative question: one model in which three or more
  topics from at least two different lectures cross (e.g. moral hazard × liquidity shocks ×
  credit lines; adverse selection × debt vs. equity × signaling; activism × control rights ×
  takeover premium; borrowing capacity × asset prices × aggregate credit rationing). Name the topics in the heading. *Why:* the final exam rewards
  carrying a result through several models; questions that stay inside one topic do not train it.
- **No answer in the statement.** Ask to find, characterize or determine; do not print the
  formula to be proven, except when the result has a name the student should recognize.
- **Parameter analysis in every discursive question**, as the course's lists do ("what
  happens to … if … rises", "for which values of $B$ …", "as $A \to \bar A$"): (i) the sign of each
  comparative static, proved by implicit differentiation or a closed form; (ii) a table of
  those signs (results × parameters; $+$, $-$, $0$, or the condition that decides the sign),
  plus a numeric sensitivity table computed by the check script when numbers are opted in;
  (iii) limiting and knife-edge values; (iv) the economic reading of each change.
- **Graphs where the model is read graphically, not in every question.** Each block has at
  least one sub-item that asks the student to draw (financing region in $(A, I)$ space;
  pledgeable income vs. NPV; payoff of debt vs. equity claims; liquidity-shock cutoff;
  aggregate credit supply and demand), and at most half of the sub-items do. The answer key
  draws it in TikZ/pgfplots from the model's own equations, never a freehand sketch; in
  symbolic mode any admissible parameter values shape the curves, numeric ticks are
  suppressed, and axes, curves and points carry symbolic labels ($\bar A$, $I^*$, $\rho^*$).
- Discursive questions have four or five sub-items **a)–e)** (e.g. 3×5 = 15 pts): set up →
  derive → characterize (proof, dynamics, limits) → quantify → parameter analysis.

**Solutions.**
- Rebuild each model from its primitives every time: state the problem, the Lagrangian or
  the substitution used, every FOC (with what the multiplier means), the market-clearing or
  equilibrium condition, then solve. No step is "it can be shown"; second-order or
  sufficiency conditions are noted where they decide the answer.
- Each step says what it uses ("from the household FOC (2) and goods clearing (4)").
- An independent script (`Listas/<list>-check.py`) verifies every result and aborts on a
  mismatch: each closed form with sympy; each claimed sign, limit and ordering (symbolically,
  or at many random admissible parameter draws); each existence claim by root-finding at
  random draws; that every multiple-choice distractor differs from the key; and, with numbers
  opted in, every number, table entry and plotted coordinate. *Why:* long derivations hide
  sign and exponent slips that a reader cannot catch at a glance.
- **Length: 10 to 15 pages of answer key per list**, in the same format (numbered steps,
  intuition, `Ref:`, rubric). If the key has fewer than 10 pages, add questions (integrative
  ones first) until it reaches 10, never pad the prose; above 15, cut questions, never
  steps. A graduate mock exam's key has at least 10 pages. Spend the space on derivations,
  proofs, sign tables and figures. *Why:* a cross-topic question with a parameter analysis
  cannot be solved step by step in one page, and the student studies from the key.

**Rubric.** Score the setup and each derivation step separately. Caps: a special-case
result used in the general case (max. half the item); a result the item asks to derive that
is quoted instead (max. a third); a stability, sign or limit claim without proof (0 for that
line); a parameter analysis that lists signs without proving them or without reading them
economically (max. half the item); a cross-topic question answered inside one model only,
ignoring the link (max. half the item). A requested graph is scored on its own lines: axes
and labels, each locus with its slope, the shift or dynamics (arrows, saddle path, jump), and
the point read off it; a graph contradicting the student's algebra loses the graph points.
