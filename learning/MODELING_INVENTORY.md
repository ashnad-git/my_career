# Financial Modeling Practice — Case Inventory

Source: https://financial-modeling.carrd.co (hosted on Quantus — quantus.finance)  
**Documented:** 2026-08-29 | **Full decision log:** PHASE2_MASTER_PLAN.md → "QUANTUS MODELING CASES" section

**19 cases selected. 7 skipped (M&A + LBO — not relevant for UAE FP&A roles).**

Each case replicated as a standalone Excel file in `learning/phase2c_modeling/` and solved in order. Completed Hard cases posted on LinkedIn.

---

## UAE Data Replacement Rule — HARD CASES ONLY (Decided 2026-08-29)

The 5 Hard/real-company cases swap US company data for UAE listed company data. The model structure and mechanics stay identical — only the source data changes.

| Case | Original Company | Replace With | Reason |
|---|---|---|---|
| Case 3 — P&L Hard | Apple (US GAAP) | **Air Arabia PJSC** (IFRS, ADX) | UAE company, IFRS, recruiter-relevant |
| Case 6 — CFS Hard | Apple (US GAAP) | **Air Arabia PJSC** (same) | Same source as Case 3 — consistent company |
| Case 9 — BS Hard | Apple (US GAAP) | **Air Arabia PJSC** (same) | Same source — builds toward 3SM |
| Case 12 — 3SM Hard ★ | Amazon (US GAAP) | **Air Arabia PJSC** (IFRS, ADX) | MAIN PORTFOLIO PIECE — UAE 3-statement model |
| Case 16 — DCF Hard | Oracle (US GAAP) | **Air Arabia or Emaar** (IFRS) | UAE valuation is more credible for regional roles |

**Backup companies if Air Arabia data is insufficient:** Emaar Properties, Aldar Properties, Agthia Group — all ADX/DFM listed, IFRS, annual reports publicly available.

**Easy and Medium cases:** Keep original fictional or US data — these are mechanics practice, not showcase pieces. The company name doesn't matter when you're learning how to wire formulas.

**Advanced schedules (Cases 17–19):** Keep Microsoft and Delta data — schedule mechanics are universal, company name irrelevant.

---

---

## Completion Tracker

| # | Case | Difficulty | Company | Excel File | Status | LinkedIn |
|---|---|---|---|---|---|---|
| 1 | Simple P&L Forecast | Easy | Fictional | `01_pnl_simple.xlsx` | Not started | - |
| 2 | P&L Forecast with Historical Growth Rates | Medium | Fictional | `02_pnl_growth_rates.xlsx` | Not started | - |
| 3 | P&L Forecast — Apple | Hard | Apple | `03_pnl_apple.xlsx` | Not started | - |
| 4 | Simple Cash Flow Forecast | Easy | Fictional | `04_cfs_simple.xlsx` | Not started | - |
| 5 | Cash Flow Forecast Advanced | Medium | Fictional | `05_cfs_advanced.xlsx` | Not started | - |
| 6 | Cash Flow Forecast — Apple | Hard | Apple | `06_cfs_apple.xlsx` | Not started | - |
| 7 | Simple Balance Sheet Forecast | Easy | Fictional | `07_bs_simple.xlsx` | Not started | - |
| 8 | Balance Sheet Forecast with Growth Rates | Medium | Fictional | `08_bs_growth_rates.xlsx` | Not started | - |
| 9 | Balance Sheet Forecast — Apple | Hard | Apple | `09_bs_apple.xlsx` | Not started | - |
| 10 | Simple 3-Statement Model | Easy | Fictional | `10_3sm_simple.xlsx` | Not started | - |
| 11 | 3-Statement Model Advanced | Medium | Fictional | `11_3sm_advanced.xlsx` | Not started | - |
| 12 | 3-Statement Model — Amazon ★ | Hard | Amazon | `12_3sm_amazon.xlsx` | Not started | - |
| 13 | Simple DCF Model | Easy | Fictional | `13_dcf_simple.xlsx` | Not started | - |
| 14 | DCF — WebMD | Medium | WebMD | `14_dcf_webmd.xlsx` | Not started | - |
| 15 | DCF — Activision Blizzard | Medium | Activision | `15_dcf_atvi.xlsx` | Not started | - |
| 16 | DCF — Oracle | Hard | Oracle | `16_dcf_oracle.xlsx` | Not started | - |
| 17 | PP&E & D&A Schedule — Microsoft | Hard | Microsoft | `17_ppe_microsoft.xlsx` | Not started | - |
| 18 | Revolver Schedule — Delta Air Lines | Hard | Delta | `18_revolver_delta.xlsx` | Not started | - |
| 19 | Equity Schedule — Microsoft | Hard | Microsoft | `19_equity_microsoft.xlsx` | Not started | - |

---

## Case Details — Full Specifications

---

### 1. Simple P&L Forecast (Easy)
**URL:** https://quantus.finance/learn/modeling/pnl-forecast-practice  
**Company:** Fictional | **$ in thousands** | **Success rate: 87%**

**Data:**
- Historical: 2014, 2015, 2016
- Forecast: 2017, 2018, 2019, 2020, 2021

**Tasks:**
1. Forecast Revenue, COGS, Operating Expenses, and Taxes for 2017–2021 using the given growth rate assumptions
2. Calculate Gross Profit, EBITDA, EBIT, EBT, and Net Income for 2017–2021

**Key concepts:** Growth rate-based forecasting, P&L structure, margin calculations

---

### 2. P&L Forecast with Historical Growth Rates (Medium)
**URL:** https://quantus.finance/learn/modeling/pnl-forecast-advanced-practice  
**Company:** Fictional | **$ in thousands** | **Success rate: 82%**

**Historical data (visible):**
- Revenue: 54,553 / 58,088 / 62,368 (2020 / 2021 / 2022)
- COGS: 25,541 / 25,297 / 26,558
- Gross Profit: 29,012 / 32,791 / 35,810
- D&A: 1,983 / 1,878 / 1,948
- G&A: 3,942 / 4,302 / 4,131
- Marketing (fixed): 15,750 / 17,801 / 20,656
- LT Debt interest: 6.20% (given for all years)

**Forecast:** 2023, 2024, 2025

**Tasks:**
1. Identify historical drivers from 2020–2022 (Sales YoY Growth, Gross Margin, D&A %, G&A %, Marketing fixed cost, Other OpEx %, LT Debt interest %, Tax Rate %, Dividend Payout %)
2. Calculate historical averages for each driver
3. Use historical averages to forecast P&L for 2023–2025

**Key concepts:** Driver-based forecasting, Assumptions & Drivers section, calculating averages

---

### 3. P&L Forecast — Apple (Hard)
**URL:** https://quantus.finance/learn/modeling/pnl-forecast-apple-practice  
**Company:** Apple Inc. | **$ in millions** | **Sep fiscal year-end** | **Success rate: 82%**

**Historical data:**
- Revenue: 215,639 / 229,234 / 265,595 (FY2016 / FY2017 / FY2018)
- Cost of revenue: (131,376) / (141,048) / (163,756)
- Gross Profit: 84,263 / 88,186 / 101,839
- R&D: (10,045) / (11,581) / (14,236)
- SG&A: (14,194) / (15,261) / (16,705)
- EBIT: 60,024 / 61,344 / 70,898
- Interest income: 3,999 / 5,201 / 5,686
- Interest expense: (1,456) / (2,323) / (3,240)
- Other expense net: (1,195) / (133) / (441)
- EBT: 61,372 / 64,089 / 72,903
- Taxes: (15,685) / (15,738) / (13,372)
- Net Income: 45,687 / 48,351 / 59,531
- D&A: 10,505 / 10,157 / 10,903
- EBITDA: 70,529 / 71,501 / 81,801
- SBC: 4,210 / 4,840 / 5,340

**Forecast:** FY2019, FY2020, FY2021 (Sep year-end)

**Tasks:**
1. Forecast Revenue, Gross Profit, R&D, SG&A, Taxes, Cost of Revenue using growth rates and margin assumptions
2. Debt & Interest Schedule: Calculate interest income and expense, link to IS
3. PP&E Schedule: Complete and link D&A back to IS
4. Calculate EBITDA, EBIT, EBT, Net Income

**Key concepts:** Real-company data, supporting schedules, linking IS to schedules, Sep FY

---

### 4. Simple Cash Flow Statement Forecast (Easy)
**URL:** https://quantus.finance/learn/modeling/cash-flow-practice  
**Company:** Fictional | **$ in thousands** | **Success rate: 92%**

**Data provided (given on right side of sheet):**

Income Statement (FY2022 actual / FY2023 forecast):
- Revenue: 13,760 / 16,582
- COGS: (7,502) / (8,334)
- Gross Profit: 6,258 / 8,248
- SG&A: (2,711) / (2,989)
- EBITDA: 3,547 / 5,259
- D&A: (234) / (328)
- EBIT: 3,313 / 4,931
- Interest: (10) / (15)
- EBT: 3,303 / 4,916
- Taxes: (496) / (737)
- Net Income: 2,807 / 4,179

Balance Sheet (FY2022 / FY2023):
- Cash: 3,418 / 6,727
- Inventory: 35 / 70
- Accounts receivable: 777 / 936
- Other assets: 420 / 882
- PP&E: 1,454 / 1,955
- Total Assets: 6,104 / 10,570

CFS to build — FY2022 (actual given) / FY2023 (forecast to fill):
- EBITDA → Interest → Taxes → WC changes (Inventory, AR, Other assets, AP, Other liabilities) → CFO
- CAPEX (474) → CFI
- Borrowings / Equity changes → CFF
- Ending cash balance

**Tasks:**
1. Calculate CFO, CFI, CFF by linking IS and BS figures
2. Calculate ending cash balance for 2023

**Key concepts:** Indirect method cash flow, working capital changes, linking statements

---

### 5. Cash Flow Statement Forecast Advanced (Medium)
**URL:** https://quantus.finance/learn/modeling/cash-flow-advanced-practice  
**Company:** Fictional | **$ in millions** | **Dec year-end** | **Success rate: 94%**

**Balance Sheet provided (12/31/2020 / 12/31/2021):**
- Cash: 8,790 / [to calculate]
- Accounts Receivable: 2,750 / 4,460
- Inventory: 7,370 / 6,850
- Other Current Assets: 1,650 / 1,500
- Total Current Assets: 20,560 / 12,810
- Gross PP&E: 12,760 / 13,170
- Accumulated Depreciation: 4,800 / 5,160
- Net PP&E: 7,960 / 8,010
- Other LT Investments: 1 / 16
- Other Assets: 2,330 / 2,910
- Total Non-current Assets: 10,291 / 10,936
- Total Assets: 30,851 / 23,746
- Short-term debt: 693 / 469
- Current LTD: 3 / [data continues]
- Accounts Payable: 3,050 / [continued]

**CFS structure:**
- CFO: Net Income, D&A, WC changes (AR, Inventory, Other CA, Deferred Revenue, AP, Tax Payable, Other CL)
- CFI: Purchase of PP&E, LT Investments, Other Assets
- CFF: LT Debt increase, Other liabilities, Share issuance, Dividends paid (1,638)

**Tasks:**
1. Calculate all CFS figures by linking to BS
2. Calculate ending cash balance 12/31/2021 and link back to BS

**Key concepts:** More detailed WC items, deferred revenue, debt/equity in CFF, BS linkage

---

### 6. Cash Flow Statement Forecast — Apple (Hard)
**URL:** https://quantus.finance/learn/modeling/cash-flow-apple-practice  
**Company:** Apple Inc. | **$ in millions** | **Sep fiscal year-end** | **Success rate: 91%**

**Historical data:**
- FY2017 (30-Sep-17), FY2018 (29-Sep-18) — actuals given
- Forecast: FY2019 (30-Sep-19), FY2020, FY2021

**CFS structure:**
- CFO: Net Income, D&A, SBC, WC changes (AR, Inventory, Other CA, AP, Other CL, Deferred Revenue), Change in Other NCA/NCL
- CFI: Capital expenditures
- CFF: LT Debt, Revolver, Share repurchases (73,056 given for FY2018 → (73,056) for FY2019–2021), Common dividends (given)

**Supporting schedules needed first:**
- PP&E Schedule (to get D&A and CapEx figures)
- Other Non-Current Assets Schedule

**Tasks:**
1. Complete PP&E Schedule
2. Complete Other Non-Current Assets Schedule
3. Build CFO / CFI / CFF
4. Calculate ending cash → link to Balance Sheet for 2019–2021

---

### 7. Simple Balance Sheet Forecast (Easy)
**URL:** https://quantus.finance/learn/modeling/balance-sheet-practice  
**Company:** Fictional | **$ in millions** | **Dec year-end** | **Success rate: 85%**

**Historical BS (31-Dec-14 / 31-Dec-15 / 31-Dec-16):**
- Accounts Receivable: 143.90 / 154.80 / 169.30
- Inventory: 85.00 / 92.00 / 110.00
- Other Assets: 45.90 / 46.90 / 68.00
- Total Assets: 274.80 / 293.70 / 347.30
- Accounts Payable: 68.00 / 68.90 / 68.90
- Other Liabilities: 48.30 / 43.30 / 38.90
- Total Liabilities: 116.30 / 112.20 / 107.80
- Days in Period: 360 (all years)

**IS given for 2014–2016 (actual) and 2017–2021 (forecast already given):**
- Revenue: 2,922.00 / 2,984.00 / 3,040.00 → 3,131.20 / 3,225.14 / 3,321.89 / 3,421.55 / 3,524.19
- COGS: 1,401.00 / 1,383.00 / 1,367.00 → 1,409.04 / 1,451.31 / 1,494.85 / 1,539.70 / 1,585.89

**Tasks:**
1. Calculate DSO, DPO, DIO, Other Assets % of Revenue, Other Liabilities % of Revenue for 2014–2016
2. Calculate historical averages of each ratio
3. Use averages to forecast BS line items for 2017–2021 (linking to IS revenue/COGS)

**Key concepts:** DSO/DPO/DIO calculations, ratio-based BS forecasting

---

### 8. Balance Sheet Forecast with Historical Growth Rates (Medium)
**URL:** https://quantus.finance/learn/modeling/balance-sheet-advanced-practice  
**Company:** Fictional (same as P&L Medium) | **$ in thousands** | **Success rate: 88%**

**Historical BS:** 2020, 2021, 2022 | **Forecast:** 2023, 2024, 2025

**Tasks:**
1. Identify key historical drivers from 2020–2022 for each BS account
2. Calculate the average rate of change for each driver
3. Apply averages to forecast all BS accounts for 2023–2025

**Key concepts:** Rate-of-change method, BS driver identification

---

### 9. Balance Sheet Forecast — Apple (Hard)
**URL:** https://quantus.finance/learn/modeling/balance-sheet-apple-practice  
**Company:** Apple Inc. | **$ in millions** | **Sep fiscal year-end** | **Success rate: 73%**

**Historical BS (30-Sep-17 / 29-Sep-18):**
- Cash & equivalents: 268,895 / 237,100
- Accounts receivable: 17,874 / 23,186
- Inventories: 4,855 / 3,956
- Other current assets: 31,735 / 37,896
- PP&E: 33,783 / 41,304
- Other non-current assets: 18,177 / 22,283
- Total Assets: 375,319 / 365,725
- Accounts payable: 44,242 / 55,888
- Other current liabilities: 30,551 / 32,687
- Deferred revenue: 10,384 / 10,340
- Commercial paper / revolver: 11,977 / 11,964
- LT Debt: 103,703 / 102,519 → given for forecast: 102,519 (constant)
- Other non-current liabilities: 40,415 / 45,180
- Total Liabilities: 241,272 / 258,578
- Common stock: 35,867 / 40,201
- Retained earnings: 98,330 / 70,400
- Other comprehensive income: (150) / (3,454) → forecast given: (3,454) constant
- Total Equity: 134,047 / 107,147

**Forecast:** FY2019, FY2020, FY2021

**Supporting schedules:**
- PP&E Schedule (roll-forward)
- Retained Earnings Schedule (Net Income - Dividends)
- Revolver Schedule (draws and repayments)

**Tasks:**
1. Complete PP&E Schedule
2. Complete Retained Earnings Schedule
3. Complete Revolver Schedule
4. Forecast all BS items 2019–2021

**Key concepts:** Three supporting schedules, Apple real filing data, balance check (Assets = Liabilities + Equity)

---

### 10. Simple 3-Statement Model (Easy)
**URL:** https://quantus.finance/learn/modeling/financial-statement-practice  
**Company:** Fictional (same as P&L Medium) | **$ in thousands** | **Success rate: 63%**

**Historical:** 2020, 2021, 2022 | **Forecast:** 2023, 2024, 2025

**Assumptions & Drivers section has two parts:**

IS Drivers: Sales YoY Growth, Gross Margin, D&A % Revenue, G&A % Revenue, Marketing (Fixed Cost), Other OpEx % Revenue, LT Debt interest % Avg Debt, Tax Rate, Dividend Payout %

BS Drivers: Days in Period (365 all years), PPE Turnover Ratio, AR Days, Inventory Days, AP Days, Other CL % Revenue, LT Debt (given: 13,400 → 20,000 / 25,000 / 28,000 for forecast), Common Share Capital (5,110 constant)

**Tasks:**
1. Calculate all historical IS and BS drivers
2. Forecast IS for 2023–2025
3. Forecast BS for 2023–2025
4. Derive CFS from projected IS and BS
5. Link cash balances (CFS ending cash = BS cash)

**Key concepts:** Full integrated model, both IS and BS drivers, cash reconciliation between statements

---

### 11. 3-Statement Model Advanced (Medium)
**URL:** https://quantus.finance/learn/modeling/financial-statement-advanced-practice  
**Company:** Fictional (different dataset) | **Success rate: 52%**

**Historical:** 2016, 2017, 2018 | **Forecast:** 2019, 2020, 2021, 2022, 2023

**Drivers:**
- IS: Gross Margin → use average rate of change (not average level)
- BS: Same approach — average rate of change
- CFS: Same approach

**Tasks:**
1. IS Drivers: Calculate avg rate of change over 2016–2018 → use as forecast assumption
2. BS Drivers: Same
3. CFS Drivers: Same
4. Project IS, BS, and CFS for 2019–2023
5. Link cash balances

**Key concepts:** Rate-of-change assumptions vs level assumptions, 5-year forecast, longer horizon

---

### 12. 3-Statement Model — Amazon ★ PORTFOLIO CENTREPIECE (Hard)
**URL:** https://quantus.finance/learn/modeling/financial-statement-amazon-practice  
**Company:** Amazon.com, Inc. (AMZN) | **$ in millions** | **Dec year-end** | **Success rate: 36%**  
*Tagged: Real-World Modeling*

**Historical data:**
- FY2021A, FY2022A, FY2023A | Projection date: 2023-12-31
- Revenue: 469,822 / 513,983 / 574,785
- Cost of sales: (272,344) / (288,831) / (304,739)
- Gross Profit: 197,478 / 225,152 / 270,046
- R&D: (56,052) / (73,213) / (85,622)
- SG&A: (116,547) / (138,591) / (147,572)
- EBIT: 24,879 / 13,348 / 36,852
- Interest income: 448 / 989 / 2,949
- Interest expense: (1,809) / (2,367) / (3,182)
- Other expense, net: 14,637 / (17,909) / 926

**Forecast:** 2024E, 2025E, 2026E, 2027E

**Supporting schedules required:**
- Interest Income & Expense Schedule
- D&A Schedule
- PP&E Schedule
- Working Capital Schedule
- Debt Schedule
- Equity Schedule

**Tasks:**
1. Forecast IS using provided assumptions + complete Interest & D&A schedules → link back
2. Forecast BS using all supporting schedules (PP&E, WC, Debt, Equity) → link to IS
3. Build CFS from projected IS and BS
4. Reconcile: CFS ending cash = BS Cash & Equivalents

**Key concepts:** Most complex case — fully integrated model with 6 supporting schedules. Real Amazon data.

---

### 13. Simple DCF Model (Easy)
**URL:** https://quantus.finance/learn/modeling/dcf-practice  
**Company:** Fictional | **Success rate: 75%**

**Assumptions:**
- Growth Rate: 1.7%, EV/EBITDA Multiple: 7.0x
- Cost of Debt: 5%, Tax Rate: 25%, 10Y Treasury: 1.5%
- Beta: 1.3, Market Return: 10%
- Equity Value: 17,500, Debt Value: 15,000

**FCF inputs (Year 1–5):**
- EBIT: 5,000 / 5,200 / [mid] / 5,400 / 5,500
- D&A: 325 / 330 / 330 / 330 / 320 / 320
- CapEx: (1,550) / (1,550) / ... / (1,500) / (1,500)
- WC increase: (180) / (170) / ... / (160) / (150) / (145)

**Sections:**
- Free Cash Flow (FCF)
- WACC (Cost of Equity via CAPM, Debt/Equity weights)
- Discounting (PV of each year's FCF)
- Terminal Value (Perpetuity Growth + Exit Multiple — both)
- Equity Value & Share Price

**Tasks:**
1. Forecast FCF for Years 1–5
2. Compute WACC
3. Discount each year's FCF to PV
4. Terminal Value (both methods)
5. Equity Value and share price

---

### 14. DCF — WebMD (Medium)
**URL:** https://quantus.finance/learn/modeling/dcf-webmd-practice  
**Company:** WebMD Health Corp. | **Success rate: 72%**  
**Tabs:** DCF + Financials

**Tasks:**
1. Build 3-statement model for WebMD (Financials tab — IS, BS, CFS)
2. Calculate FCF for 2014–2018 (5 years)
3. Compute WACC using provided assumptions
4. Discount FCFs to PV
5. Terminal Value — Perpetuity Growth Method only
6. Enterprise Value → Equity Value → Share Price

**Key concepts:** First case combining 3SM + DCF together, perpetuity only

---

### 15. DCF — Activision Blizzard (Medium)
**URL:** https://quantus.finance/learn/modeling/dcf-atvi-practice  
**Company:** Activision Blizzard (ATVI) | **Success rate: 60%**  
**Tabs:** DCF + 3SM

**Tasks:**
1. Full 3-statement model in 3SM tab
2. Complete Debt Schedule (principal repayments)
3. Compute WACC
4. Forecast Unlevered FCF for 2022–2026
5. Discount FCFs
6. Terminal Value (Perpetuity Growth)
7. Enterprise Value → Equity Value → Fair Share Price
8. Trading Comps: LTM EBITDA multiples vs gaming industry peers

**Key concepts:** Debt amortization schedule, unlevered FCF, trading comps (first appearance)

---

### 16. DCF — Oracle (Hard)
**URL:** https://quantus.finance/learn/modeling/dcf-oracle-practice  
**Company:** Oracle Corporation (ORCL) | **May fiscal year-end** | **Success rate: 33%**  
**Tabs:** DCF + Shares  
*Tagged: Real-World Modeling*

**Assumptions sourced from:**
- Beta: Bloomberg (2-year weekly adjusted)
- Market Risk Premium: Kroll U.S. ERP Study
- Cost of Debt: Bloomberg YTM of specific Oracle bond
- Risk-Free Rate: WSJ 10Y Treasury

**Tasks:**
1. Diluted shares outstanding from Shares tab
2. IS projections + FCF for FY2025–FY2029 (May year-end)
3. WACC → discount CFs → EV (both Perpetuity Growth + Exit Multiple)
4. Equity Value + Fair Price under both methods

**Key concepts:** Professional-grade assumptions (Bloomberg/Kroll), diluted shares calc, dual terminal value methods

---

### 17. PP&E & D&A Schedule — Microsoft (Hard)
**URL:** https://quantus.finance/learn/modeling/ppe-schedule-advanced-microsoft  
**Company:** Microsoft Corp. | **$ in millions** | **Jun fiscal year-end** | **Success rate: 65%**  
*Tagged: Real-World Modeling*

**Historical data (2020–2023):**
- Revenue: 143,015 / 168,088 / 198,270 / 211,915
- Gross PP&E by category:
  - Land: 3,660 / 4,333 / 4,734 / 5,640
  - Buildings: 31,655 / 46,766 / 55,014 / 68,156
  - Leasehold Improvements: 6,111 / 6,801 / 7,365 / 8,554
  - Computers & Equipment: 37,002 / 47,033 / 60,416 / 75,524
  - Furniture & Fixtures: 4,920 / 6,133 / 6,529 / 6,018
  - Total: 87,348 / 111,066 / 134,058 / 163,892
- CapEx % Revenue: 14.11% / 11.60% / 14.08% / 13.26%
- Forecast growth: 12% revenue growth for 2024–2027

**Sections:**
- Gross PP&E / Projected CapEx by asset category
- CapEx % Revenue by segment
- Useful Lives (for depreciation calculation)
- Depreciation Waterfall (cohort-based)
- Ending Net PP&E (roll-forward)
- Intangible Assets Amortization
- Total D&A

**Tasks:**
1. Forecast Total Gross PP&E Additions by category for 2024–2027
2. Complete Depreciation Waterfall for 2024–2027
3. Calculate Ending Net PP&E using roll-forward
4. Complete Intangibles Amortization + Total D&A

**Key concepts:** Asset-category-level CapEx forecast, depreciation waterfall (most technical schedule)

---

### 18. Revolver Schedule — Delta Air Lines (Hard)
**URL:** https://quantus.finance/learn/modeling/revolver-schedule-delta-airlines  
**Company:** Delta Air Lines (DAL) | **Success rate: 73%**  
*Tagged: Real-World Modeling*

**Tasks:**
1. Forecast debt balances for 2025–2027
2. Liquidity Analysis: determine cash shortfalls and required revolver funding
3. Revolver Schedule: revolver draws, repayments, ending balance for 2025–2027
4. Total Interest Expense: debt interest + revolver borrowing interest for 2025–2027

**Key concepts:** Revolver as liquidity backstop, draws/repayments logic, total interest calc

---

### 19. Shareholders' Equity Schedule — Microsoft (Hard)
**URL:** https://quantus.finance/learn/modeling/shareholders-equity-schedule  
**Company:** Microsoft Corp. | **Success rate: 100%**  
*Tagged: Real-World Modeling*

**Forecast:** FY2023E – FY2027E

**Tasks:**
1. Complete AOCI Schedule (Accumulated Other Comprehensive Income) for FY2023E–FY2027E
2. Build Shareholders' Equity Roll-Forward:
   - Beginning equity + Net Income + OCI + SBC + Share repurchases + Dividends = Ending equity

**Key concepts:** Equity statement roll-forward, AOCI components, SBC treatment

---

## Learning Order & Rationale

```
Phase A — Foundation (Cases 1-9): Build IS, CFS, BS skills separately
  Week 1: Cases 1, 2 (P&L Easy + Medium)
  Week 2: Case 3 (P&L Apple Hard)
  Week 3: Cases 4, 5 (CFS Easy + Medium)
  Week 4: Case 6 (CFS Apple Hard)
  Week 5: Cases 7, 8 (BS Easy + Medium)
  Week 6: Case 9 (BS Apple Hard)

Phase B — Integration (Cases 10-12): Put all 3 statements together
  Week 7: Case 10 (3SM Easy)
  Week 8: Case 11 (3SM Advanced Medium)
  Week 9-10: Case 12 (3SM Amazon Hard) ← MAIN PORTFOLIO PIECE

Phase C — Valuation (Cases 13-16): Add DCF on top
  Week 11: Case 13 (DCF Simple)
  Week 12: Case 14 (DCF WebMD — 3SM + DCF combined)
  Week 13: Case 15 (DCF Activision — with Trading Comps)
  Week 14: Case 16 (DCF Oracle Hard)

Phase D — Advanced Schedules (Cases 17-19): Professional-grade components
  Week 15: Case 17 (PP&E Microsoft)
  Week 16: Case 18 (Revolver Delta)
  Week 17: Case 19 (Equity Microsoft)
```

---

## How Each Session Works

1. Claude opens the Quantus case in browser, reads instructions + data
2. Claude generates a pre-populated Excel practice file with:
   - Historical data filled in
   - Yellow-highlighted blank cells for you to complete
   - Assumptions section pre-built
3. You open the file and solve it
4. Claude checks your answers and explains any errors
5. Claude updates EXCEL_TEXTBOOK.md with the concepts
6. Completed + polished model → LinkedIn post

---

## LinkedIn Post Structure (for each completed case)

```
What I just built: [Case name]
Company: [Real company or scenario]
Tools: Excel, [specific functions used]

Key steps:
- [3-4 bullet points on what was done]

What I learned:
- [1-2 insights]

[Screenshot of the completed model]

#FinancialModeling #FPnA #Excel #Finance
```
