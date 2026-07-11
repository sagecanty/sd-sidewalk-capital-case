# Assumptions Log

Every model input lives here with its source and confidence rating.
**Ratings:** SOURCED (public record, cite attached) · DERIVED (calculated from
sourced figures, math shown) · ESTIMATE (assumption — must appear in
sensitivity analysis) · TO VERIFY / TO SOURCE (blocks the memo until resolved).

## 1. Liability (claim frequency & severity)

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| L1 | FY2018 sidewalk injury payouts, total | $2.94M across ~50 claims | SOURCED | NBC 7 San Diego (Jul 2019), public records request |
| L2 | Average payout per legal claim (2018) | $58,860 | SOURCED | NBC 7 San Diego (Jul 2019) |
| L3 | Severity tail: single 2017 bike settlement | $4.85M (of $5.3M 2017 total) | SOURCED | NBC 7 San Diego (Jul 2019) — model severity as a distribution, not a mean |
| L4 | Settlements exceeded sidewalk capital investment over same recent period | Directional (no $ pair published) | SOURCED | SD County Grand Jury 2023/24, "Maintaining San Diego's Sidewalks" |
| L5 | Post-2019 payout years (need ≥5-yr series) | — | TO SOURCE | City Attorney claim payout records / PRA request or IBA reports |

## 2. Backlog & repair cost

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| B1 | 2014–15 assessment: locations needing repair | 85,000+ locations, $57.2M est. | SOURCED | Voice of San Diego (2019), citing city assessment |
| B2 | City staff memo estimate (2019) | ~$100M, 80,000+ repairs | SOURCED | NBC 7 San Diego (2019), citing staff memo |
| B3 | Later city estimate (2024, secondary source) | $185M, ~37,000 sections | SOURCED-WEAK | Contractor blog citing city; corroborate against IBA/city doc before use |
| B4 | Implied per-repair unit cost | ~$673–$5,000 range across B1–B3 | DERIVED | Spread across estimates is itself a scenario axis — do not average it away |
| B5 | Cost-share program: avg resident spend | $4,500 (43 participants/yr) | SOURCED-AMBIG | VoSD — unclear if $4,500 is the 50% share or total job cost; resolve before using |
| B6 | Deferred-maintenance cost escalation rate | — | TO SOURCE | Do NOT assume the folk "1:4 rule" without a citable engineering source |
| B7 | D2/D7 open sidewalk backlog share | From own 311 analysis | SOURCED | Getitdone-teardown repo: 14,786 open citywide, 1,091-day median age, 82% >1yr |

## 3. Structural / legal

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| S1 | Repair responsibility: adjacent property owner (CA law), with SD Council Policy 200-12 exceptions | — | SOURCED | Grand Jury 2023/24; City Attorney 2013 Memorandum of Law |
| S2 | Tort liability for injuries: remains with City regardless of repair responsibility | — | SOURCED | City of San Diego staff report 15-13 (2015), Sidewalk Accident Decisions Doctrine discussion |
| S3 | Share of backlog that is city-responsibility vs owner-responsibility | Unknown — city says "some" | TO SOURCE | Critical model parameter; city spokesperson flagged the split exists but unquantified |

## 4. Finance parameters

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| F1 | Real discount rate | 3.0% placeholder | ESTIMATE / TO VERIFY | Pin to current OMB Circular A-94 rates or SD GO-bond real yield; sensitivity-test 2–7% |
| F2 | Analysis horizon | 10 yr placeholder | ESTIMATE | Justify against concrete sidewalk useful life; sensitivity-test 5/10/20 |
| F3 | Construction cost inflation (concrete/labor, San Diego) | — | TO SOURCE | ENR construction cost index or Caltrans; drives the "cost of waiting" |

## 5. Source links

- NBC 7 (2019): https://www.nbcsandiego.com/news/local/city-paid-over-29-million-last-year-on-sidewalk-injuries/78062/
- Grand Jury 2023/24: https://www.sandiegocounty.gov/content/dam/sdc/grandjury/reports/2023-2024/sidewalks/23-24%20Sidewalks%20Report.pdf
- Voice of San Diego (2019): https://voiceofsandiego.org/2019/06/17/sidewalk-repair-policy-still-confounds-residents-and-the-city-council/
- City staff report 15-13 (2015): https://www.sandiego.gov/sites/default/files/15_13_150415.pdf
- Own prior analysis: https://github.com/sezgiozrn/Getitdone-teardown
