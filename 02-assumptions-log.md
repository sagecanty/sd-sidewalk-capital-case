# Assumptions Log

Every model input lives here with its source and confidence rating.
**Ratings:** SOURCED (public record, cite attached) · DERIVED (calculated from
sourced figures, math shown) · ESTIMATE (assumption — must appear in
sensitivity analysis) · TO VERIFY / TO SOURCE (blocks the memo until resolved).

"GJ24" = SD County Grand Jury 2023/24, *Maintaining San Diego's Sidewalks*.

## 1. Liability (claim frequency & severity)

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| L1 | Avg annual sidewalk injury claim payouts, 2015–2021 | ~$2.5M/yr | SOURCED | GJ24, citing City Risk Management data |
| L2 | Average payment per claim, 2015–2021 | ~$53,000 | SOURCED | GJ24, citing City Risk Management data |
| L3 | FY2023 trip-and-fall payouts | $2.9M | SOURCED | GJ24, citing Annual Transportation Dept Update (2024) |
| L4 | Severity tail: single 2017 bike settlement | $4.85M | SOURCED | NBC 7 San Diego (2019) — severity is a distribution with a fat tail, not a mean |
| L5 | Claims geography: 5 ZIPs = 45% of claim count | Downtown, Pacific Beach, Hillcrest, La Jolla, North Park | SOURCED | GJ24 — claims density ≠ backlog-age density (D2/D7); targeting is a scenario axis |
| L6 | City liable regardless of repair responsibility; constructive notice suffices (Gov Code §835) | — | SOURCED | GJ24, citing City Attorney 2013 Memorandum of Law ML-2013-16 |

## 2. Backlog, capacity & repair cost

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| B1 | 2014–15 citywide assessment | 85,000+ damaged locations | SOURCED | GJ24 |
| B2 | City-responsibility replacement backlog | 8,000–9,000 locations | SOURCED | GJ24 |
| B3 | Responsibility split of damaged locations | ~50/50 City vs. owner (TD estimate) | SOURCED | GJ24 — applies to REPAIR cost only; liability (L6) applies to 100% |
| B4 | Replacement capacity | 2 crews × ~200 locations/yr; intake 20–50/day; 20+ yr backlog at current funding; Chollas yard space caps added crews | SOURCED | GJ24 — replacement scales via CIP contractors, not city crews |
| B5 | Ramping capacity unit cost | 4 rampers + equipment = $900K (FY24) | SOURCED | GJ24 — the cheap-mitigation option's price tag |
| B6 | Sidewalk KPI: repaired sq ft | Goal 820K sq ft/yr; actual avg <89K (~11%) | SOURCED | GJ24, citing FY24 Adopted Budget KPIs |
| B7 | Earlier backlog cost estimates | $57.2M (2019, VoSD) / ~$100M (2019, staff memo) / $185M (2024, weak secondary) | SOURCED / SOURCED-WEAK | Use as unit-cost scenario spread, not an average |
| B8 | D2/D7 open sidewalk backlog (own analysis) | 14,786 open citywide, 1,091-day median age, 82% >1yr | SOURCED | Getitdone-teardown repo |
| B9 | Concrete sidewalk useful life | 50–75 years | SOURCED | GJ24 |

## 3. Funding need vs. actual (variance series)

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| V1 | Annual CIP need for sidewalk replacement (TD asset-mgmt estimate) | $16.1M/yr | SOURCED | GJ24 |
| V2 | Actual avg CIP investment, last 7 yrs (FY18–FY24) | $1.57M/yr (<10% of need) | SOURCED | GJ24, Figure 1 — digitize yearly values from chart or pull underlying ATI committee docs |
| V3 | 5-Yr Capital Outlook: sidewalk need / funding gap | $104M / $88.1M | SOURCED | GJ24, citing FY25–29 Five-Year Capital Infrastructure Planning Outlook |
| V4 | Deficit rolls forward (accumulates, not resets) | — | SOURCED | GJ24, explicit statement |

## 4. Intervention effectiveness (the remaining soft spot)

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| E1 | Ramping/slicing reduces trip-and-fall likelihood | Directional (GJ24 Finding F4) | SOURCED-DIRECTIONAL | GJ24 — but NO effectiveness %. The claims-avoided-per-mitigated-location rate is the model's single most important ESTIMATE; must dominate the tornado |
| E2 | Ramping turnaround target after FY24 crew adds | 1 day report-to-ramp | SOURCED | GJ24, citing budget KPI target |
| E3 | Construction cost inflation (concrete/labor, SD) | — | TO SOURCE | ENR CCI or Caltrans index; drives cost-of-waiting |

## 5. Finance parameters

| # | Input | Value | Rating | Source |
|---|---|---|---|---|
| F1 | Real discount rate | 3.0% placeholder | ESTIMATE / TO VERIFY | Pin to OMB Circular A-94 or SD GO-bond real yield; sensitivity 2–7% |
| F2 | Analysis horizon | 10 yr placeholder | ESTIMATE | Test 5/10/20; justify vs. B9 useful life |

## 6. Model-shaping facts

- Three options, not one: (a) do nothing, (b) assessment + ramping/slicing at
  scale (GJ24's own proposal, deliberately unsized by them), (c) replacement
  acceleration via CIP. The Grand Jury explicitly declined to size option (b) —
  "does not make any specific recommendation on the scope or frequency… nor the
  number of new ramping crews or slicing budget." **This model's job is to size it.**
- Liability applies to the full hazard population (L6); city repair cost applies
  to ~50% of it (B3). Model these as separate populations.
- Targeting axis: backlog-age (D2/D7, B8) vs. claims-density (L5). The city's
  own CIP prioritization already weights claims/lawsuit density — model both.

## 7. Source links

- GJ24: https://www.sandiegocounty.gov/content/dam/sdc/grandjury/reports/2023-2024/sidewalks/23-24%20Sidewalks%20Report.pdf
- NBC 7 (2019): https://www.nbcsandiego.com/news/local/city-paid-over-29-million-last-year-on-sidewalk-injuries/78062/
- Voice of San Diego (2019): https://voiceofsandiego.org/2019/06/17/sidewalk-repair-policy-still-confounds-residents-and-the-city-council/
- IBA Report 15-13 (2015): https://www.sandiego.gov/sites/default/files/15_13_150415.pdf
- FY25–29 Capital Outlook: https://www.sandiego.gov/sites/default/files/2024-01/fy-25-29-five-year-capital-infrastructure-planning-outlook.pdf
- City Attorney ML-2013-16: https://docs.sandiego.gov/memooflaw/ML-2013-16.pdf
- Own prior analysis: https://github.com/sezgiozrn/Getitdone-teardown
