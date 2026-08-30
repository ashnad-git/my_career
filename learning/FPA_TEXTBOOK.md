# FP&A Model Textbook — Zara & Co. FY2025

**Purpose:** Reference guide for rebuilding or explaining the 9-tab FP&A model. Every concept taught, every formula pattern, every decision. Read this before Phase 2C or any interview.

---

## CHAPTER 1 — What Is an FP&A Model and Why Does It Exist

An FP&A model is a structured Excel workbook that translates business assumptions into a P&L forecast. It answers three questions leadership always asks:

1. **Are we on track?** (Variance Analysis — Actual vs Budget)
2. **Where do we end up?** (Rolling Forecast — full-year view)
3. **What if things go wrong (or right)?** (Scenario Analysis — Bull/Bear/Base)

The model is not a reporting tool — it is a decision-making tool. Its value is that changing one assumption (e.g., COGS%) automatically cascades through Revenue → Gross Profit → EBITDA across all 12 months and all three scenarios.

### The 9-Tab Architecture

| Tab | Type | Purpose |
|---|---|---|
| Assumptions | Input | All hardcoded values live here. Nothing is hardcoded elsewhere. |
| Revenue Build | Calculation | Units × Price × Seasonality = monthly revenue by outlet/category |
| COGS Build | Calculation | Revenue × COGS% per category |
| OpEx Detail | Calculation | Fixed costs + variable marketing % per outlet |
| P&L Summary | Output | Budget P&L: Revenue → GP → EBITDA, monthly + annual |
| Variance Analysis | Output | Actual vs Budget, $ and % variance, Fav/Unfav |
| Rolling Forecast | Output | Actuals locked for past months, budget for future |
| Scenario Analysis | Output | Base/Bull/Bear — one assumption change moves the entire P&L |
| Dashboard | Output | Executive summary — KPIs, Q1 scorecard, FY outlook |

**One-way data flow rule:** Data flows from left to right — Assumptions → Build tabs → P&L Summary → Variance/Forecast/Dashboard. Never link backwards.

---

## CHAPTER 2 — Assumptions Tab

### Why a Dedicated Assumptions Tab

Every number that can change belongs in Assumptions. This means:
- Price points, growth rates, COGS%, rent, payroll — all live here
- Build tabs never contain a hardcoded number — they always reference Assumptions
- When management says "what if rent goes up 10%?" — you change one cell, the entire model updates

### Structure — Zara & Co.

| Section | Rows | Content |
|---|---|---|
| A — Products | 2–10 | Category names, price by outlet |
| B — Revenue Drivers | 12–22 | Monthly units budget by outlet/category |
| C — Seasonality | 24–34 | Monthly multipliers (Ramadan = 1.4×, summer = 0.85×) |
| D — Price Escalation | 36–40 | Annual price growth % |
| E — Discount | 42–44 | Markdown % per outlet |
| F — COGS% | 47–50 | COGS as % of revenue per category |
| G — OpEx Inputs | 54–56 | Rent AED/month, Payroll AED/month, Marketing % of revenue |

### COGS% Values (Section F)

| Row | Category | COGS% |
|---|---|---|
| B47 | Women's Wear | 45% |
| B48 | Men's Wear | 48% |
| B49 | Kids' Wear | 50% |
| B50 | Accessories | 35% |

### OpEx Inputs (Section G)

| Row | Item | Dubai Mall | Marina Mall | Online |
|---|---|---|---|---|
| B/C/D54 | Rent (AED/month) | 180,000 | 120,000 | 15,000 |
| B/C/D55 | Payroll (AED/month) | 150,000 | 100,000 | 45,000 |
| B/C/D56 | Marketing % of Revenue | 3% | 3% | 2% |

---

## CHAPTER 3 — Revenue Build

### Formula Pattern: Units × Price × Seasonality

```
Revenue = Units × Price × Seasonality multiplier
```

Column layout: A = Category, B = Metric (Units/Revenue), C–N = Jan–Dec, O = Annual Total.

Monthly revenue for each category:
```excel
= Units_row × Price_from_Assumptions × Seasonality_from_Assumptions
```

**Mixed reference pattern ($B6):**
- `$B` — lock the column (always pull from column B = Price)
- `6` — float the row (shifts down when copied across categories)

Use this when one column of inputs applies to multiple rows of output.

### Outlet Row Structure

| Outlet | Revenue rows |
|---|---|
| Dubai Mall | 8, 10, 12, 14 (with unit rows 7, 9, 11, 13 above each) |
| Marina Mall | 18, 20, 22, 24 |
| Online | 29, 31, 33, 35 |
| Grand Total Revenue | Row 39 |

### Annual Total Formula
```excel
=SUM(C8:N8)
```
Applied in col O for every revenue and units row.

---

## CHAPTER 4 — COGS Build

### Core Concept

COGS (Cost of Goods Sold) = what it costs to buy/make the goods you sold. For retail, this is the purchase cost of inventory. Expressed as a % of revenue because it scales with sales volume.

```excel
COGS = Revenue × COGS%
```

### Formula Pattern

In COGS Build, for each category row:

```excel
= 'Revenue Build'!C8 × Assumptions!$B$47
```

- `'Revenue Build'!C8` — the revenue for that category/month (float both — shifts across months and down categories)
- `Assumptions!$B$47` — COGS% for Women's Wear (fully locked — always points to same assumption cell)

### Why Fully Absolute for COGS% ($B$47)

COGS% doesn't change by month or by outlet. It's a category-level assumption. Lock both row and column.

Contrast with price (mixed $B6) — price doesn't change by month but does change by category, so you float the row.

### Tab Structure

| Row group | Content |
|---|---|
| 5 | Dubai Mall header |
| 6–9 | Women's/Men's/Kids'/Accessories COGS rows (DM) |
| 10 | Dubai Mall Total COGS |
| 12–17 | Marina Mall rows + total |
| 19–24 | Online rows + total |
| 26 | Grand Total COGS — All Outlets |

Annual total in col O = SUM(C:N) for each row.

---

## CHAPTER 5 — OpEx Detail

### Three Types of Operating Expense

| Type | Example | Formula logic |
|---|---|---|
| Fixed — no volume link | Rent | Always = the assumption. Use fully absolute ref. |
| Fixed — no volume link | Payroll | Always = the assumption. Fully absolute. |
| Variable — % of revenue | Marketing | = Revenue × Marketing%. Mixed ref — float month column. |

### Fixed Cost Formula (Rent/Payroll)
```excel
= Assumptions!$B$54
```
Fully absolute. Rent is AED 180,000 every month regardless of sales. The same number appears in all 12 monthly columns — don't link it to the revenue column.

### Variable Cost Formula (Marketing)
```excel
= 'Revenue Build'!C15 × Assumptions!$B$56
```
- `'Revenue Build'!C15` — Dubai Mall total revenue for that month (float column C → shifts Jan to Dec)
- `Assumptions!$B$56` — Marketing % for Dubai Mall (locked — always same cell)

### Why Online Has "Rent"

Online is a warehouse-and-fulfilment operation. "Rent" = warehouse rent. It's still a fixed cost even though there's no retail storefront. The label is accurate — the concept is the same.

### Tab Structure

Column layout: A = Item, B = narrow spacer, C–N = Jan–Dec, O = Total.

| Rows | Content |
|---|---|
| 5 | Dubai Mall header |
| 6–8 | Rent / Payroll / Marketing (DM) |
| 9 | Dubai Mall Total OpEx |
| 11–15 | Marina Mall |
| 17–21 | Online |
| 23 | Grand Total OpEx — All Outlets |

---

## CHAPTER 6 — P&L Summary

### Structure

The P&L Summary is the first "output" tab — it consolidates all build tabs into one view.

| Column | Content |
|---|---|
| B | FY2024 Prior Year (hardcoded — for context) |
| C–N | Jan–Dec Budget (formula — links from build tabs) |
| O | FY2025 Annual Budget (SUM of C–N) |
| P–R | Jan/Feb/Mar Actuals (hardcoded — data given) |

### P&L Row Map

| Row | Line Item |
|---|---|
| 6 | Revenue |
| 7 | Less: COGS |
| 8 | Gross Profit |
| 9 | Gross Margin % |
| 10 | spacer |
| 11 | Less: OpEx |
| 12 | EBITDA |
| 13 | EBITDA Margin % |

### Key Formulas

| Cell | Formula | Explanation |
|---|---|---|
| C6 | `='Revenue Build'!C39` | Jan budget revenue from grand total row |
| C7 | `='COGS Build'!C26` | Jan budget COGS from grand total row |
| C11 | `='OpEx Detail'!C23` | Jan budget OpEx from grand total row |
| C8 | `=C6-C7` | Gross Profit = Revenue − COGS |
| C9 | `=C8/C6` | Gross Margin % = GP / Revenue |
| C12 | `=C8-C11` | EBITDA = GP − OpEx |
| C13 | `=C12/C6` | EBITDA% = EBITDA / Revenue |
| O6 | `=SUM(C6:N6)` | Annual budget revenue |

### Hardcoded Actuals (Jan/Feb/Mar)

| | Jan (P) | Feb (Q) | Mar (R) |
|---|---|---|---|
| Revenue | 1,900,000 | 1,860,000 | 2,280,000 |
| COGS | 858,000 | 840,000 | 1,040,000 |
| OpEx | 685,000 | 658,000 | 710,000 |

Derived actuals (GP, GM%, EBITDA, EBITDA%) are formula cells — same formulas as the budget columns, just referencing the actuals.

---

## CHAPTER 7 — Variance Analysis

### What Is Variance Analysis

Variance = the gap between what you planned (Budget) and what actually happened (Actual). It tells you where to look, not what to do.

```
$ Variance = Actual − Budget
% Variance = $ Variance ÷ Budget
```

### Fav / Unfav Convention

A variance is only meaningful if you know whether it's good or bad. The label depends on the type of line:

| Line type | Positive $Var (Actual > Budget) | Negative $Var (Actual < Budget) |
|---|---|---|
| Revenue, GP, EBITDA, margins | **Fav** — you made more than planned | **Unfav** — you made less |
| COGS, OpEx | **Unfav** — you spent more than planned | **Fav** — you spent less |

### IF Formula for Fav/Unfav

Revenue line (profit type):
```excel
=IF(D7<0,"Unfav","Fav")
```

Cost line (COGS, OpEx):
```excel
=IF(D8>0,"Unfav","Fav")
```

The sign flips because for costs, overspending (positive $Var = Actual > Budget) is bad.

### Column Layout

5-column block per month:

| Col offset | Content | Example (Jan) |
|---|---|---|
| +0 | Budget | B |
| +1 | Actual | C |
| +2 | $ Variance | D |
| +3 | Fav/Unfav | E |
| +4 | % Variance | F |

Jan = B–F, Feb = H–L, Mar = N–R, Q1 = T–X. Spacers at G, M, S (width 2).

### Q1 Aggregation — Common Mistake

For AED rows (Revenue, COGS, GP, OpEx, EBITDA):
```excel
Q1 Budget (T7) = B7 + H7 + N7   ← SUM Jan + Feb + Mar
```

For margin % rows (GM%, EBITDA%):
```excel
Q1 Budget GM% (T10) = T9 / T7   ← Q1 GP ÷ Q1 Revenue
```

**Never** sum monthly percentages. `=B10+H10+N10` sums three monthly GM%s into ~165% — meaningless. The Q1 margin must be recalculated from the Q1 AED totals.

### % Variance for Margin % Rows

The $Var for a margin row = Actual% − Budget% (in percentage points):
```excel
V10 = U10 - T10    ← NOT V9/V7
```

Then % variance = $Var ÷ Budget% — technically valid but rarely used in practice. Most analysts just show basis point change (the $Var column) for margin rows.

### Conditional Formatting — Formula-Based Rules

Do not use "Text Contains" — it matches substrings. "Fav" inside "Unfav" gets caught.

Use formula-based exact match:
- Rule 1: `=$E7="Fav"` → Fill #C6EFCE, Font #006100
- Rule 2: `=$E7="Unfav"` → Fill #FFC7CE, Font #9C0006

Apply both rules to all Fav/Unfav columns at once as one range:
`E7:E10,E12:E14,K7:K10,K12:K14,Q7:Q10,Q12:Q14,W7:W10,W12:W14`

**Why no `$` on the column in the formula:** Since you're selecting only the Fav/Unfav columns (E, K, Q, W), the formula reference shifts correctly to match each column. Locking `$E` would make K and Q check column E — wrong.

---

## CHAPTER 8 — Rolling Forecast

### What Is a Rolling Forecast

A rolling forecast replaces the budget as actual results arrive. It always shows a full 12-month view:

- Past months: **locked actuals** (what happened — don't touch)
- Future months: **updated forecast** (re-run from build tabs or revised assumptions)

The result is always a realistic full-year number. A static budget becomes stale after January — a rolling forecast stays current.

### Column Layout

| Cols | Content |
|---|---|
| B–D | Jan/Feb/Mar — hardcoded actuals (yellow) |
| E–M | Apr–Dec — formula cells linking from build tabs (green) |
| N | FY2025 Total — SUM of all 12 months |

### Key Formula Patterns

Derived rows (GP, EBITDA) — use cells within the same tab, consistent across all 12 months:
```excel
B9 = B7 - B8    (Jan GP = Jan Revenue - Jan COGS)
E9 = E7 - E8    (Apr GP = Apr Revenue - Apr COGS)
```

Same formula, same tab — whether it's an actual or a forecast month.

Forecast revenue links from Revenue Build:
```excel
E7 = 'Revenue Build'!F39    (Apr revenue grand total)
```

FY Total:
```excel
N7 = SUM(B7:M7)
```

FY margin %:
```excel
N10 = N9 / N7    ← GP / Revenue, NOT SUM of monthly %s
```

### Actuals Used (Jan/Feb/Mar)

| | Jan | Feb | Mar |
|---|---|---|---|
| Revenue | 1,900,000 | 1,860,000 | 2,280,000 |
| COGS | 858,000 | 840,000 | 1,040,000 |
| OpEx | 685,000 | 658,000 | 710,000 |

---

## CHAPTER 9 — Scenario Analysis

### What It Is and Why It Matters

A scenario analysis shows the P&L under different futures simultaneously. Management can see:
- How much EBITDA upside in a good year (Bull)
- How much downside in a bad year (Bear)
- Whether the risk/reward is symmetric or skewed

### Two-Section Structure

**Section 1 — Assumptions (inputs):** The levers you change. Contains both typed inputs and derived values.

**Section 2 — P&L Output (formulas):** Recalculates automatically when Section 1 changes.

### Assumption Rows — Zara & Co.

| Row | Assumption | Base | Bull | Bear |
|---|---|---|---|---|
| 6 | Full-Year Revenue (AED) | Link from P&L Summary O6 | =B6×(1+C7) | =B6×(1+D7) |
| 7 | Revenue Growth % vs Budget | 0% (type) | 5% (type) | -5% (type) |
| 8 | Blended COGS % of Revenue | ='P&L Summary'!O7/'P&L Summary'!O6 | 42% (type) | 47% (type) |
| 9 | Full-Year OpEx (AED) | Link from P&L Summary O11 | =B9×(1+C10) | =B9×(1+D10) |
| 10 | OpEx Growth % vs Budget | 0% (type) | -2% (type) | 5% (type) |

**Rule:** Growth % rows (7, 10) are typed inputs for Bull/Bear, 0% for Base. AED rows (6, 9) are derived for Bull/Bear, linked for Base.

### P&L Output Formulas (Section 2)

| Line | Formula (Base column B) |
|---|---|
| Revenue (B14) | `=B6` — pull from assumption row |
| COGS (B15) | `=B14*B8` — Revenue × COGS% |
| GP (B16) | `=B14-B15` |
| GM% (B17) | `=B16/B14` |
| OpEx (B19) | `=B9` — pull from assumption row |
| EBITDA (B20) | `=B16-B19` |
| EBITDA% (B21) | `=B20/B14` |

Same pattern for C (Bull) and D (Bear) — just reference those columns.

Impact columns (Bull vs Base, Bear vs Base):
```excel
F14 = C14 - B14    (Bull Revenue - Base Revenue)
```
Skip margin % rows in impact columns — % difference of a % is not useful for management.

### The Key Insight: Volume vs Rate

In a Bear case, revenue falls (volume) and COGS% rises (rate). If the volume drop is large enough, absolute COGS in AED can actually be lower than Base even with a higher COGS%:

```
Base COGS:  22,602,000 × 44.86% = 10,138,140
Bear COGS:  21,471,900 × 47.00% = 10,091,793  ← lower in AED
```

This doesn't mean the Bear case is okay — GP still falls because revenue fell more. Always look at GP and EBITDA as the bottom line, not COGS in isolation.

---

## CHAPTER 10 — Dashboard

### Purpose

The dashboard is a one-page executive view. It answers three questions in 30 seconds:
1. How did we do in Q1? (Scorecard)
2. Where do we end up for the year? (FY Outlook)
3. What are the headline KPIs? (KPI tiles)

### Three Sections

**Section 1 — KPI Tiles:** Four headline metrics from Variance Analysis Q1 block.

| Metric | Source |
|---|---|
| Q1 Revenue Actual | ='Variance Analysis'!U7 |
| Q1 EBITDA Actual | ='Variance Analysis'!U13 |
| Q1 Gross Margin % | ='Variance Analysis'!U9/'Variance Analysis'!U7 |
| Q1 EBITDA Margin % | ='Variance Analysis'!U13/'Variance Analysis'!U7 |

**Section 2 — Q1 Scorecard:** Full P&L comparison, Budget vs Actual. Links from Variance Analysis Q1 block (T=Budget, U=Actual, V=$Var, W=Fav/Unfav, X=%Var).

**Section 3 — FY Outlook:** Budget vs Rolling Forecast.
- Budget column: link from P&L Summary col O (annual budget)
- Forecast column: link from Rolling Forecast col N (FY Total)
- $Var, Fav/Unfav, %Var: same formulas as Variance Analysis

### Dashboard Formula Pattern

All dashboard cells are links — no data is generated here. The dashboard consumes from other tabs.

```excel
Q1 Revenue Budget (B11) = 'Variance Analysis'!T7
Q1 Revenue Actual (C11) = 'Variance Analysis'!U7
Q1 $ Variance (D11)     = 'Variance Analysis'!V7
FY Budget Revenue (B22) = 'P&L Summary'!O6
FY Forecast Revenue (C22) = 'Rolling Forecast'!N7
FY $Var (D22)           = C22 - B22
FY Fav/Unfav (E22)      = IF(D22<0,"Unfav","Fav")
FY %Var (F22)           = D22/B22
```

---

## CHAPTER 11 — Reference Formulas Quick Sheet

### Cross-Sheet Reference
```excel
='Sheet Name'!CellRef
='Revenue Build'!C39
```

### SUM Across Months
```excel
=SUM(C7:N7)    ← Jan to Dec
```

### Gross Profit
```excel
=Revenue - COGS
```

### Margin %
```excel
=GP / Revenue
=EBITDA / Revenue
```

### $ Variance
```excel
=Actual - Budget
```

### % Variance
```excel
=$ Variance / Budget
```

### Fav/Unfav — Revenue/Profit lines
```excel
=IF(D7<0,"Unfav","Fav")
```

### Fav/Unfav — Cost lines (COGS, OpEx)
```excel
=IF(D8>0,"Unfav","Fav")
```

### Q1 Budget (AED rows)
```excel
=Jan_Budget + Feb_Budget + Mar_Budget
```

### Q1 Margin % (NOT a sum)
```excel
=Q1_GP / Q1_Revenue
```

### Scenario Revenue (Bull/Bear)
```excel
=Base_Revenue × (1 + Growth_%)
```

### Scenario COGS
```excel
=Scenario_Revenue × Scenario_COGS%
```

---

## CHAPTER 12 — The P&L Story: Zara & Co. Q1 FY2025

*Know this by heart — it is the management commentary you would write.*

**Revenue:** Q1 came in at AED 6.04M against a budget of 6.12M, a miss of AED 81k (-1.3%). January and February underperformed budget. March recovered — Ramadan drove a beat of AED 20k (+0.9%) — but was insufficient to offset the Q1 shortfall.

**Gross Profit:** Despite COGS tracking slightly below budget in absolute terms (-AED 8k, Fav), the revenue miss compressed GP to AED 3.30M vs 3.38M budgeted. Gross Margin was 54.7% vs 55.1% budgeted (-0.48pp) — COGS% was largely controlled but the volume shortfall meant less contribution per revenue lost.

**OpEx:** Overspent by AED 67k (+3.4%) vs budget. Marketing spend in Q1 ran above plan, likely to drive Ramadan traffic.

**EBITDA:** Squeezed from both directions — revenue miss and OpEx overrun — landing at AED 1.25M vs 1.39M budgeted, a shortfall of AED 141k (-10.1%). EBITDA margin 20.7% vs 22.7% budgeted (-2.0pp).

**FY Outlook:** If Apr–Dec performs exactly to budget, full-year EBITDA will be AED 4.43M vs 4.57M budgeted (the Q1 miss flows through). A recovery in H2 revenue or tighter OpEx control is needed to close the gap.

---

*Next: Chapter 13 — Power BI connection to this model (Phase 2C)*
