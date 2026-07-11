# San Diego Sidewalk Repair — Capital Investment Case

**Status: WIP — model in progress. Nothing below the assumptions log is final.**

A finance-BA engagement on a question the [Get It Done teardown](https://github.com/sezgiozrn/Getitdone-teardown)
left open: its decision memo recommended a capital-assessment track for
sidewalk repair and flagged, as the first thing to validate, whether the
backlog is a capital-funding constraint. This project prices that constraint.

**The question:** The 2023/24 Grand Jury recommended proactive sidewalk
remediation but explicitly declined to size it — no crew count, no budget, no
scope. This model sizes it: which intervention mix (cheap mitigation vs.
replacement acceleration, at what funding level, targeted by backlog age vs.
claims density) minimizes the city's total cost of sidewalks — claims plus
repairs — in NPV terms?

**Deliverables (planned):**
[Assumptions log](02-assumptions-log.md) ·
[Model spec](03-model/model-spec.md) ·
Excel model (`03-model/`) ·
[Business case memo](04-business-case-memo.md)

**Stack:** Excel (model) · Python (data prep only) · Claude + Copilot (AI-assisted)

## Why this exists

The 2023/24 San Diego County Grand Jury found the City has paid more in
trip-and-fall settlements in recent years than it invested in sidewalk capital
repair over the same period. That is a qualitative finding; this repo builds
the quantitative version — an NPV model with scenario toggles and sensitivity
analysis on every soft assumption — and wraps it in a business case addressed
to the city budget office.

## A note on how this will be built

**Self-directed analysis on public data and public records.** Not commissioned
by the City of San Diego or any employer. The addressee of the business case
is illustrative. Every model input is sourced or explicitly flagged as an
estimate in the [assumptions log](02-assumptions-log.md) — the log is the
audit trail, and no figure appears in the memo that is not in the log.
