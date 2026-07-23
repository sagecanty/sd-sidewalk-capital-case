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
]:
    s = wb.create_sheet(name)
    s["A1"] = note

# ============================================================
# SENSITIVITY  (live tornado + static two-way)
# ============================================================
# Base values pulled from INPUTS by log ID so this stays in sync w/ workbook.
# npvB() mirrors the NPV-tab Option-B (mitigation) formula exactly.
base = {logid: val for (_l, val, _u, logid, _r) in INPUTS}

def npvB(claims=base["L1"], e1=base["E1"], rollout=base["MB1"],
         costloc=base["E1b"], hazards=base["B1"], disc=base["F1"],
         horizon=base["F2"]):
    total = 0.0
    for t in range(1, int(horizon) + 1):
        d = 1 / (1 + disc) ** t
        outlay = rollout * hazards * costloc / 3 if t <= 3 else 0.0
        claims_b = claims * (1 - min(t / 3, 1) * rollout * e1)
        total += ((claims - claims_b) - outlay) * d
    return total

BASE_NPVB = npvB()

# ---- one-way tornado (static values; ranges trace to assumptions log) ----
tornado_vars = [
    ("E1 mitigation effectiveness", "e1", 0.0, 0.50, "floor 0.0 = LA untargeted downside (E1 evidence base); 0.50 targeted upper remains a guess"),
    ("Cost per location mitigated", "costloc", 150, 600, "E1b ESTIMATE anchored to B5 ramping-crew cost; log rule: every ESTIMATE stays in the tornado"),
    ("Option B rollout share", "rollout", 0.30, 0.90, "policy lever, not uncertainty - shown for completeness; scenario axis in the memo"),
    ("Baseline annual claims", "claims", 2.0e6, 2.9e6, "L1 2015-21 avg to L3 FY23 high"),
    ("Discount rate", "disc", 0.02, 0.07, "F1 regime flux: A-94 Appendix C ~2% to reinstated 7% base"),
    ("Horizon (years)", "horizon", 5, 20, "F2; vs B9 50-75yr useful life"),
]
sens = wb.create_sheet("SENSITIVITY")
sens["A1"] = "TORNADO (Python-computed; ranges trace to assumptions-log IDs; E1 floored at 0.0 per LA natural experiment)"
sens.append([])
sens.append(["Input", "Low NPV_B", "High NPV_B", "Swing", "Base NPV_B", "Range rationale"])
trows = []
for label, kw, lo, hi, why in tornado_vars:
    nlo, nhi = npvB(**{kw: lo}), npvB(**{kw: hi})
    trows.append((label, nlo, nhi, abs(nhi - nlo), BASE_NPVB, why))
trows.sort(key=lambda r: r[3], reverse=True)
for r in trows:
    sens.append([r[0], round(r[1]), round(r[2]), round(r[3]), round(r[4]), r[5]])
sens.column_dimensions["A"].width = 30
sens.column_dimensions["F"].width = 50

# ---- static two-way: E1 x cost-per-location (E1=0.0 row = LA untargeted downside) ----
e1_axis = [0.0, 0.10, 0.20, 0.30, 0.40, 0.50]
cost_axis = [150, 250, 350, 450, 600]
st = len(trows) + 6
sens.cell(row=st, column=1, value="TWO-WAY: NPV_B by E1 (rows) x $/location (cols). Rebuild as a live Excel Data Table in the hand-finished workbook (What-If Analysis; corner ='NPV'!O1, row input INPUTS!B11, col input INPUTS!B10).")
sens.cell(row=st + 1, column=1, value="E1 \\ $loc")
for j, c in enumerate(cost_axis):
    sens.cell(row=st + 1, column=2 + j, value=c)
for i, e in enumerate(e1_axis):
    sens.cell(row=st + 2 + i, column=1, value=e)
    for j, c in enumerate(cost_axis):
        sens.cell(row=st + 2 + i, column=2 + j, value=round(npvB(e1=e, costloc=c)))

out["B2"] = round(BASE_NPVB)
out.cell(row=2, column=1, value="NPV Option B vs do-nothing (Python base = NPV tab)")

# Writes model_skeleton.xlsx — the reproducible scaffold. The hand-finished
# canonical workbook is sidewalk_capital_model.xlsx: copy the skeleton over it
# ONLY when regenerating from scratch is intended; the script never touches
# the canonical file, so hand refinements (Data Table, formatting) are safe.
wb.save(__file__.replace("build_model.py", "model_skeleton.xlsx"))
print(f"wrote model_skeleton.xlsx | base NPV_B = {BASE_NPVB/1e6:.1f}M")
for r in trows:
    print(f"  {r[0]:<32} swing {r[3]/1e6:5.1f}M")
