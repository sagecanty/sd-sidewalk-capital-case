# Business Case Memo — Sidewalk Capital Investment

**To:** Office of the Independent Budget Analyst / Active Transportation &
Infrastructure Committee staff
**From:** Sezgi Ozturan, Business Analyst
**Date:** 2026-07-22
**Re:** Sizing the sidewalk mitigation program the 2023/24 Grand Jury
recommended but declined to size — and what the arithmetic actually supports

*Portfolio artifact — self-directed analysis on public data; the addressee is
illustrative, not a real engagement. Every model figure below is cited from
the workbook's OUTPUT tab; every input traces to an ID in
`02-assumptions-log.md` (L1, B5, E1...).*

---

## Recommendation

1. **Do not fund sidewalk repair on the "repairs pay for themselves through
   avoided lawsuits" argument.** It does not survive arithmetic (below), and a
   program sold on it will be judged a failure by its own stated metric —
   exactly what happened in Los Angeles.
2. **If the City proceeds — and there are legitimate reasons to — fund the
   Grand Jury's mitigation-at-scale option (B), not replacement acceleration
   (C),** shaped by the two levers the model says actually matter: unit cost
   per location mitigated, and claims-density targeting.
3. **Make the honest case, and quantify the bar for it:** Option B becomes
   NPV-positive if benefits beyond avoided claims — ADA compliance, asset
   preservation, societal injury costs — are worth at least **$1.29M/yr**
   (OUTPUT tab). That is the number the real business case must clear, and it
   is small relative to the City's own $16.1M/yr stated replacement need (V1).

## Situation

The 2023/24 County Grand Jury found 85,000+ damaged sidewalk locations (B1),
a city-responsibility replacement backlog of 8,000–9,000 locations moving at
~400/yr — a 20+ year backlog (B2, B4) — and ~$2.5M/yr in trip-and-fall claim
payouts with the City liable regardless of who owns the repair (L1, L6). The
Grand Jury recommended assessment plus ramping/slicing mitigation at scale but
explicitly declined to size the program. This model sizes it.

## Options and results (10-yr horizon, 3% real discount — F1/F2)

| Option | Description | NPV vs. do-nothing (OUTPUT tab) |
|---|---|---|
| A | Do nothing (baseline: ~$2.5M/yr claims continue) | — |
| B | Assessment + ramping/slicing at scale (GJ proposal, sized: 60% of hazard population over 3 yrs) | **–$11.0M** |
| C | Replacement acceleration via CIP (fund the full $16.1M/yr need) | **–$116.8M** |

**Neither option pays for itself on avoided liability alone.** The intuition
fails on scale: total claims exposure is ~$2.5M/yr (L1), so even eliminating
every claim caps the benefit at roughly that annuity — while Option B's
rollout costs multiples of it, and Option C spends ~$14.5M/yr above current
funding (V1–V2) against the same small claims pool.

## Sensitivity: what actually moves the answer

The tornado (SENSITIVITY tab) contradicted this model's own spec, which
predicted mitigation effectiveness (E1) would dominate:

1. **Cost per location mitigated — $21.6M swing.** The biggest lever by 4x.
   At the estimate range ($150–600/location, E1b) Option B is negative
   everywhere; the derived breakeven is **~$71/location** (OUTPUT tab).
   Implication: procurement and delivery-model design matter more than
   program design. A slicing contract at true marginal cost is a different
   business case than crew-based mitigation.
2. **E1 effectiveness — $5.7M swing, floored at 0.0 deliberately.** The floor
   is Los Angeles' revealed experience: ~$226M of repair spend since 2016
   without claims-density targeting, while injury settlements *rose* (E1
   evidence base, assumptions log §4). Untargeted spend earns the zero bar.
   San Diego's own claims concentrate — five ZIP codes account for 45% of
   claim count (L5) — so targeting is designable, but it is a requirement,
   not a preference.
3. **No single variable at its favorable extreme turns Option B positive**
   (SENSITIVITY tab, all high-NPV cells negative). The liability-only case
   is not rescued by optimism about any one input. The case must add benefit
   lines or reduce unit cost below breakeven — there is no third path.

## What the model deliberately excludes (and why the recommendation survives it)

Benefits omitted, making the NPVs above conservative *against* investment:
ADA/legal compliance exposure beyond trip-and-fall claims; asset preservation
against a 50–75-yr useful life (B9); societal injury costs beyond paid claims
(paid claims undercount injuries, F5) — valued properly via DOT's MAIS
injury-severity fractions of VSL, not full VSL per claim, which would
overstate benefits by an order of magnitude (F3, F4); and construction-cost
escalation on deferred work (E3, methodology sourced, rate not yet computed).
The recommendation does not need these to be zero — it needs them to be
honestly quantified, because **$1.29M/yr of them is the entire gap.**

## Risks and limits

- E1 and cost/location are ESTIMATE-rated; both sit in the tornado per the
  log's rule. The breakeven figure inherits their uncertainty.
- Option C's backlog-clearing benefit is modeled as linear in cumulative
  spend against the $104M five-year need (V3) — crude, and flagged as such.
- Upkeep/re-mitigation cycles are not yet modeled (NPV tab note); adding
  them worsens B, strengthening conclusion #1.
- The discount-rate regime is genuinely unsettled (F1: OMB reinstated the
  7% base while Appendix C publishes ~2%); the tornado shows the answer is
  insensitive to it ($0.5M swing) — the conclusion survives the regime flux.

## Next step

(1) Price a slicing/ramping contract to test the $71/location breakeven
against a real quote — the single highest-value piece of missing information.
(2) Quantify the excluded benefit lines against the $1.29M/yr bar, starting
with ADA exposure. (3) Compute the E3 escalation rate from the CCCI table so
deferral cost enters the comparison. (4) Design the claims-density targeting
rule from L5 before any funding decision, per the LA evidence.
