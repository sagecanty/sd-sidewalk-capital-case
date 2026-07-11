# Generates the workbook SKELETON: tabs, inputs w/ log IDs, live formulas.
# Refinement (formatting, sensitivity tables, charts) happens by hand in Excel.
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")   # editable inputs: yellow
EST_FONT = Font(color="C00000", bold=True)            # ESTIMATE ratings: red

# (row label, value, unit, log ID, rating)
INPUTS = [
    ("Baseline annual claims cost (real $)", 2_500_000, "$/yr", "L1", "SOURCED"),
    ("Average payment per claim", 53_000, "$/claim", "L2", "SOURCED"),
    ("Annual CIP replacement need", 16_100_000, "$/yr", "V1", "SOURCED"),
    ("Actual avg CIP investment (FY18-24)", 1_570_000, "$/yr", "V2", "SOURCED"),
    ("City share of repair responsibility", 0.50, "share", "B3", "SOURCED (TD estimate)"),
    ("Hazard population (2014-15 assessment)", 85_000, "locations", "B1", "SOURCED"),
    ("City-responsibility replacement backlog", 8_500, "locations", "B2", "SOURCED (midpoint 8-9K)"),
    ("Ramping capacity unit cost (4 rampers FY24)", 900_000, "$", "B5", "SOURCED"),
    ("Mitigation effectiveness (claims avoided at full rollout)", 0.30, "share", "E1", "ESTIMATE - PLACEHOLDER"),
    ("Cost per location mitigated (ramp/slice)", 300, "$/location", "E1b", "ESTIMATE - PLACEHOLDER"),
    ("Option B target rollout (share of hazards mitigated)", 0.60, "share", "MB1", "ESTIMATE - policy lever"),
    ("Option C funding level (share of V1 need)", 1.00, "share", "MC1", "ESTIMATE - policy lever"),
    ("Replacement claims-reduction at full backlog clear", 0.50, "share", "MC2", "ESTIMATE - PLACEHOLDER"),
    ("Real discount rate", 0.03, "rate", "F1", "ESTIMATE - TO VERIFY"),
    ("Horizon", 10, "years", "F2", "ESTIMATE"),
]

wb = Workbook()

# ---- INPUTS ----
ws = wb.active
ws.title = "INPUTS"
ws.append(["Parameter", "Value", "Unit", "Log ID", "Rating"])
for r in INPUTS:
    ws.append(list(r))
for row in ws.iter_rows(min_row=2, max_row=len(INPUTS) + 1):
    row[1].fill = INPUT_FILL
    if "ESTIMATE" in str(row[4].value):
        row[4].font = EST_FONT
ws.column_dimensions["A"].width = 52
for c in "BCDE":
    ws.column_dimensions[c].width = 16
ws.column_dimensions["E"].width = 26
ws["G1"] = "Rule: no hardcoded numbers outside this tab."

# Named refs by row (INPUTS!B<row>): 2=claims, 4=need, 5=actual, 6=cityshare,
# 7=hazards, 8=backlog, 9=rampcost, 10=E1eff, 11=costloc, 12=rolloutB,
# 13=fundC, 14=effC, 15=disc, 16=horizon
I = lambda r: f"INPUTS!$B${r}"

# V3 total-need row (row 17)
ws.append(["Total sidewalk capital need (FY25-29 outlook)", 104_000_000, "$", "V3", "SOURCED"])
ws.cell(row=17, column=2).fill = INPUT_FILL

# ---- NPV (per-option cash flows; options A/B/C per spec) ----
npv = wb.create_sheet("NPV")
npv.append(["Year", "DiscFactor", "Claims_A", "Outlay_B", "Claims_B",
            "Net_B_vs_A", "PV_B", "Outlay_C", "CumClearShare_C", "Claims_C",
            "Net_C_vs_A", "PV_C"])
for t in range(1, 21):
    r = t + 1
    npv.append([
        t,
        f"=IF($A{r}<={I(16)},1/(1+{I(15)})^$A{r},0)",
        f"=IF($B{r}=0,0,{I(2)})",
        f"=IF(AND($B{r}>0,$A{r}<=3),{I(12)}*{I(7)}*{I(11)}/3,0)",
        f"=IF($B{r}=0,0,{I(2)}*(1-MIN($A{r}/3,1)*{I(12)}*{I(10)}))",
        f"=($C{r}-$E{r})-$D{r}",
        f"=$F{r}*$B{r}",
        f"=IF($B{r}=0,0,MAX(0,{I(13)}*{I(4)}-{I(5)}))",
        f"=MIN(1,SUM($H$2:$H{r})/{I(17)})",
        f"=IF($B{r}=0,0,{I(2)}*(1-$I{r}*{I(14)}))",
        f"=($C{r}-$J{r})-$H{r}",
        f"=$K{r}*$B{r}",
    ])
npv["N1"] = "NPV Option B vs A:"; npv["O1"] = "=SUM($G$2:$G$21)"
npv["N2"] = "NPV Option C vs A:"; npv["O2"] = "=SUM($L$2:$L$21)"
npv["N4"] = "Option B rollout spends over years 1-3; claims effect phases in with completion. Upkeep/re-mitigation not yet modeled - log it."

# ---- OUTPUT + stubs ----
out = wb.create_sheet("OUTPUT")
out.append(["Headline", "Value"])
out.append(["NPV, mitigation at scale (B) vs do nothing", "=NPV!$O$1"])
out.append(["NPV, replacement acceleration (C) vs do nothing", "=NPV!$O$2"])
out.append(["E1 effectiveness assumption driving B", f"={I(10)}"])
out.append(["Memo rule: cite ONLY cells on this tab.", ""])
out.column_dimensions["A"].width = 52

for name, note in [
    ("CLAIMS", "Hand-build per spec: 2015-21 series detail, severity distribution incl. L4 tail."),
    ("OPTIONS", "Hand-build per spec: per-option cost detail; NPV tab holds v0 math."),
    ("SENSITIVITY", "Hand-build: tornado on every ESTIMATE input (spec rule #1), two-way on top 2 drivers."),
]:
    s = wb.create_sheet(name)
    s["A1"] = note

wb.save(__file__.replace("build_model.py", "sidewalk_capital_model.xlsx"))
print("wrote sidewalk_capital_model.xlsx")
