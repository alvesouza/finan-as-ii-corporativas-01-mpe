# Rule index

Grep this file to find the right pack. **Do not read packs to find a rule** — that is
the expensive path this index exists to avoid.

Packs are self-contained: every rule states its own mechanism and carries no citation,
so nothing here depends on an external library. Optional provenance for a curious
reader lives in `docs/09-bibliography.md` and is never required to apply a rule.

## Contract

| Pack | Covers | Skill |
|---|---|---|
| `core.md` | Tier 0: context budget, plan/verify, gates, scope | — |

## Engineering

| Pack | Covers | Skill |
|---|---|---|
| `context.md` | Retrieval ladder, graph/symbol tooling, cache hygiene | `/ctx` |
| `model-routing.md` | Model + effort selection, delegation over switching | `/route` |
| `codebase-work.md` | Reuse, refactor scope, minimal diff, doc comments, conventions | `/codebase` |

## Languages

| Pack | Covers | Skill |
|---|---|---|
| `lang-python.md` | Python | `/langpack` |

## Domain

| Pack | Covers | Skill |
|---|---|---|
| `microeconomics.md` | Choice, duality, GE, uncertainty, mechanism design | `/econ` |
| `game-theory.md` | Equilibria, repeated games, auctions, matching | `/econ` |

## Rule citation

Rules are cited `<pack-id>#<number>` — e.g. `outbox-cdc#1`, `quant-ml#3`. Use the
citation in review comments, commit messages, and code comments where a non-obvious
constraint needs a reference.

## Editing

Use `/rulesmith`. One pack per change. `python tools/sync_rules.py` after every edit.
Never edit `CLAUDE.md`, `AGENTS.md`, or `.github/**` by hand — they are generated.
