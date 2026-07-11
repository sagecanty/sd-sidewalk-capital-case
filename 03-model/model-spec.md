# Model Spec — Sidewalk Capital Investment Case

Spec first, cells second. The workbook is not started until this spec and the
assumptions log are stable. One workbook, six tabs, every input cell colored
and traced to an assumptions-log ID.

## Tabs

1. **INPUTS** — every parameter, one place. Each row: value, unit,
   assumptions-log ID (L1, B4, F1...), rating. No hardcoded numbers anywhere
   else in the workbook. Scenario switch cell (Base / Upside / Downside) and
   funding-level toggle live here.
2. **CLAIMS** — expected annual liability = frequency × severity.
   Frequency scaled to open-hazard count (B7); severity as a sourced
   distribution (L2 mean, L3 tail), not a single average. Output: expected
   annual liability cost, with/without acceleration.
3. **REPAIRS** — repair program cost by funding level. Unit cost from the
   B1–B3 spread (three scenarios, not one average), escalation per F3.
   Output: annual capital outlay per scenario.
4. **NPV** — cash-flow table over horizon F2: capital outlay vs. avoided
   liability + avoided escalation. NPV, payback year, benefit-cost ratio,
   discounted at F1. City-responsibility share (S3) applied here.
5. **SENSITIVITY** — one-way tornado on: severity mean, claim frequency,
   unit cost, discount rate, S3 split, escalation rate. Two-way table on
   the two biggest drivers.
6. **OUTPUT** — the one-page view the memo screenshots: recommendation
   number, scenario range, tornado chart.

## Rules

- Every ESTIMATE-rated input MUST appear in the tornado. No exceptions.
- The memo may only cite figures that exist on the OUTPUT tab.
- If S3 (responsibility split) stays unsourced, the model runs it as a
  0–100% slider and the memo says so — do not silently assume 100%.
