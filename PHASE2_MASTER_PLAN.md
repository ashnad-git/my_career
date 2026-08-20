# Phase 2 Master Plan — Portfolio Build + Job Applications

**Tutor/Mentor Protocol:** Claude reads this file at the START of every Phase 2 session.  
**Last Updated:** 2026-08-20 16:00  
**Phase 2 Start Date:** TBD (next session)  
**Notice Deadline:** 2026-10-28 (Oct 28, 2026)  
**Contract End:** 2027-01-28

---

## STATUS DASHBOARD
*(Update at the end of every session — this is the memory)*

| Field | Value |
|---|---|
| **Current Week** | Not started |
| **Current Phase** | Phase 2A — Excel Foundations (not yet begun) |
| **Current Task** | — |
| **Last Session Date** | 2026-08-20 (Phase 1 closure) |
| **Last Session Summary** | Phase 1 complete. Skills Matrix built. All 6 deliverables updated. Tutor plan created. |
| **Next Session: Start With** | Week 1, Day 1 — Excel foundations. Begin with CFI Excel Crash Course, Topic 1. |
| **Blockers** | None |
| **Applications Sent** | 0 |
| **Interviews Booked** | 0 |
| **Project 1 Progress** | 0% — Not started |
| **Project 2 Progress** | 0% — Not started |
| **Project 3 Progress** | 0% — Not started |

---

## KEY FILES (Read These Every Session)

| File | Purpose |
|---|---|
| **PHASE2_MASTER_PLAN.md** | This file — overall plan + status + session log |
| **JOB_PIPELINE.md** | All live jobs found, applied, responses — update every session |
| **DAILY_CHECKLIST.md** | Ashnad's daily 45-min routine — verify completion at session start |

---

## TUTOR PROTOCOL (How Every Session Works)

### At Start of Session
1. Read STATUS DASHBOARD — know exactly where we are
2. Read JOB_PIPELINE.md — check what was applied since last session, any responses received
3. Run fresh job search (LinkedIn + Indeed UAE) — find new openings, add to pipeline with fit ratings
4. Read LAST SESSION SUMMARY — know what learning topic we left off on
5. State today's plan: "Today we're doing X for Y minutes, then Z."

### During Session
- Teach concept → demonstrate → Ashnad practices → review → correct → move on
- Never move to next topic until current one is understood (ask "can you do this without help now?")
- If something isn't working after 2 attempts, try a different explanation — not the same one louder
- Every build task gets broken into steps no bigger than "do this one thing, tell me what you see"

### At End of Session
1. Update STATUS DASHBOARD (Current Week, Current Task, Next Session: Start With)
2. Write SESSION LOG entry (date + what was covered + what was understood + what was skipped + what's next)
3. Update PROJECT PROGRESS % if anything was built
4. Update JOB_PIPELINE.md — move applied jobs, add new ones found
5. Commit + push to GitHub (all files: master plan + pipeline + checklist)

### Red Lines
- Never end a session without updating the status dashboard
- Never skip the session log
- If Ashnad says "I'm lost" or "I don't understand" — stop, back up, find where understanding broke
- If an application deadline appears in job search — interrupt the build plan and apply first

---

## FULL TIMELINE

| Week | Dates (approx) | Phase | Focus |
|---|---|---|---|
| 1 | Aug 21–27 | 2A Excel | Excel foundations: formulas, lookups, Power Query basics |
| 2 | Aug 28–Sep 3 | 2A Excel | Excel modeling: Pivots, named ranges, dynamic charts |
| 3 | Sep 4–10 | 2B Project 1 | FP&A model: Assumptions + Revenue tab |
| 4 | Sep 11–17 | 2B Project 1 | FP&A model: COGS + OpEx + P&L Summary |
| 5 | Sep 18–24 | 2B Project 1 | FP&A model: Variance Analysis + management commentary |
| 6 | Sep 25–Oct 1 | 2B Project 1 | FP&A model: Scenarios + Dashboard tab + LinkedIn post |
| 7 | Oct 2–8 | 2C Project 2 | Power BI: data model + 3 core pages |
| 8 | Oct 9–15 | 2C Project 2 | Power BI: DAX measures + drill-through + publish |
| 9 | Oct 16–22 | 2D Project 3 | Cash flow forecast (simpler — 1.5 weeks) |
| 10 | Oct 23–28 | 2D + Applications | Project 3 complete + notice deadline = review + apply hard |
| 11–14 | Oct 29–Nov 25 | 2E Project 4 | Financial Statement Analysis (public UAE company) |
| 15–16 | Nov 26–Dec 9 | 2F Project 5 | Business case model (NPV/IRR) |
| 17–20 | Dec 10–Jan 10 | 2G Project 6/7 | SQL analytics + automation pipeline (if needed) |

**Applications run every week in parallel — do not wait for projects.**

---

## PHASE 2A — EXCEL FOUNDATIONS
**Duration:** 2 weeks  
**Goal:** Go from accounting-level Excel to financial modeling Excel  
**Success criteria:** Can build a multi-tab linked model without needing to look up basic formulas

### Week 1 — Core Formulas + Data Tools

**Day 1-2: Formula Foundations**
- [ ] VLOOKUP (understand the syntax, practice 3 examples)
- [ ] INDEX-MATCH (why it's better than VLOOKUP, practice)
- [ ] XLOOKUP (simpler modern version — learn this if on Excel 365)
- [ ] IF / IFS / IFERROR (error handling in models)
- [ ] SUMIFS / COUNTIFS / AVERAGEIFS (multi-condition aggregation)

*Resource:* CFI Excel Crash Course (free) — or ExcelJet.net for quick formula reference

*Practice file:* Claude will provide a practice dataset — Ashnad applies each formula to real data

**Day 3-4: Power Query**
- [ ] What Power Query is and why finance uses it (import raw data, clean it, refresh with one click)
- [ ] Connect to a CSV file
- [ ] Remove columns, rename headers, change data types
- [ ] Unpivot columns (turning monthly columns into rows — critical for FP&A data)
- [ ] Load query to a table in the sheet

*Practice:* Import a sample revenue CSV, clean it, load to Excel table

**Day 5-7: Pivot Tables**
- [ ] Build a basic Pivot Table from a table
- [ ] Add row fields, column fields, values
- [ ] Use slicers to filter
- [ ] Group dates (by month, by quarter)
- [ ] Calculated field (custom metric inside a Pivot)

*Note: Ashnad used Pivots at EY — this will come back fast. Focus on grouping and calculated fields (likely new).*

### Week 2 — Modeling Structure + Charts

**Day 8-9: Modeling Best Practices**
- [ ] What "structured modeling" means (inputs → calculations → outputs, never hardcode in formula)
- [ ] Named ranges (naming a cell/range so formulas read like English)
- [ ] Structured Table references (`Table1[Revenue]` instead of `A2:A100`)
- [ ] Color coding convention (blue = hardcoded input, black = formula, green = linked from other sheet)
- [ ] Simple model structure: one Assumptions tab, separate calculation tabs, one Output/Summary tab

*Practice:* Build a 3-tab skeleton (Assumptions → Calculations → Output) with linked cells

**Day 10-11: Conditional Formatting**
- [ ] Highlight cells based on value (variances: red if negative, green if positive)
- [ ] Data bars
- [ ] Icon sets (traffic light status)
- [ ] Custom formula-based rules

**Day 12-13: Charts for Finance**
- [ ] Column/bar chart (budget vs. actual)
- [ ] Line chart (trend over time)
- [ ] Waterfall chart (variance bridge: budget → actual)
- [ ] Combo chart (bar + line on same axis)
- [ ] Format charts: remove gridlines, clean labels, match color scheme

**Day 14: Sign-off Check**
- [ ] Can you build a 3-tab linked model from a blank sheet?
- [ ] Can you write SUMIFS without looking it up?
- [ ] Can you import a CSV via Power Query and refresh it?
- [ ] Can you build a variance analysis with color-coded formatting?

If all yes → move to Phase 2B (Project 1 build).

---

## PHASE 2B — PROJECT 1: FP&A MODEL
**Duration:** 4 weeks (Weeks 3–6)  
**Deliverable:** Complete Excel FP&A model for a UAE retail company  
**Tools:** Excel only (no Power BI yet)  
**LinkedIn post:** Yes — written and posted when model is complete

### Business Scenario
*Mid-size UAE fashion retail company, 3 outlets (Dubai Mall, Marina Mall, Online). FY2025 annual budget with monthly tracking, variance analysis vs. actuals, rolling forecast, and scenario analysis. Company name: "Zara & Co." (fictional UAE fashion retailer).*

### Model Architecture (9 tabs)

| Tab | Name | What It Contains | Week |
|---|---|---|---|
| 1 | **Assumptions** | All inputs: growth rates, margins, costs — the only place to hardcode numbers | 3 |
| 2 | **Revenue Build** | Units × price × outlet × month — pulls from Assumptions | 3 |
| 3 | **COGS Build** | Cost of goods = revenue × COGS% by category | 4 |
| 4 | **OpEx Detail** | Rent, payroll, marketing, other — monthly, by outlet | 4 |
| 5 | **P&L Summary** | Revenue → Gross Profit → EBITDA — actual vs. budget vs. prior year | 4 |
| 6 | **Variance Analysis** | $ variance and % variance with traffic light formatting | 5 |
| 7 | **Rolling Forecast** | 3-month forward view, updates as actuals are entered | 5 |
| 8 | **Scenario Analysis** | Base / Bear / Bull — dropdown switches entire model | 6 |
| 9 | **Dashboard** | 1-page summary: KPI cards, 3 charts, commentary box | 6 |

### Week 3 — Assumptions + Revenue Tab
- [ ] Set up workbook structure (name tabs, color-code tabs)
- [ ] Build Assumptions tab: revenue drivers (monthly units per outlet, avg selling price by category), seasonality multipliers (Ramadan +20%, summer -15%)
- [ ] Build Revenue tab: link from Assumptions, calculate monthly revenue by outlet × category
- [ ] Add annual total column and row totals
- [ ] Validate: does the annual total make sense for a 3-outlet fashion retailer? (~AED 15–25M range)

### Week 4 — COGS + OpEx + P&L
- [ ] Build COGS tab: COGS% per category from Assumptions, link to Revenue
- [ ] Build OpEx tab: monthly rent per outlet (fixed), payroll (fixed + variable), marketing (% of revenue)
- [ ] Build P&L Summary: link from all tabs — Revenue → Gross Profit → EBITDA
- [ ] Add Actual columns (hardcode a few months of "actuals" to demonstrate model works both ways)
- [ ] Add Prior Year column (hardcode FY2024 for comparison)

### Week 5 — Variance Analysis + Commentary
- [ ] Build Variance tab: $ variance (actual - budget) for each P&L line, each month
- [ ] Add % variance column
- [ ] Apply conditional formatting: negative variance = red, positive = green (>5% threshold)
- [ ] Write management commentary: 2 paragraph "what the variance means" template
- [ ] Build Rolling Forecast: current month actuals locked in, remaining months = updated assumptions

### Week 6 — Scenarios + Dashboard + LinkedIn Post
- [ ] Build scenario toggle: Data Validation dropdown on Assumptions tab (Base / Bear / Bull)
- [ ] Wire revenue assumptions to change based on scenario selection
- [ ] Build Dashboard tab: KPI cards (Revenue, Gross Margin%, EBITDA), bar chart (actual vs budget), waterfall (variance bridge), commentary box
- [ ] Format entire workbook for professional presentation (clean, consistent, printable)
- [ ] Write GitHub README explaining the business scenario, key decisions, key findings
- [ ] Draft and post LinkedIn post (see post template in Deliverable 4 Phase 1D update)
- [ ] **Project 1 complete**

---

## PHASE 2C — PROJECT 2: POWER BI DASHBOARD
**Duration:** 2 weeks (Weeks 7–8)  
**Deliverable:** 3-page Power BI dashboard connected to Project 1 data  
**Tools:** Power BI Desktop (free download)

### Week 7 — Power BI Foundations + Data Model
*Starting from zero Power BI. This is genuinely easier than it looks.*

**Day 1-2: Setup + Orientation**
- [ ] Download Power BI Desktop (free)
- [ ] Connect to Project 1 Excel file
- [ ] Understand the 3 views: Report / Data / Model
- [ ] Create first table visual and card visual (just to get oriented)

*Resource:* Guy in a Cube — YouTube channel. Watch: "Power BI for Beginners" playlist (first 3 videos only — ~45 minutes total)

**Day 3-4: Data Model**
- [ ] Understand what a data model is (tables connected by relationships)
- [ ] Set up relationships between tables from your Excel model
- [ ] Create a Date table (critical for time intelligence)

**Day 5-7: Core DAX Measures**
- [ ] SUM and SUMX (adding up values)
- [ ] CALCULATE (filter context — the most important DAX concept)
- [ ] DIVIDE (safe division that handles divide-by-zero)
- [ ] SAMEPERIODLASTYEAR (year-over-year comparison)
- [ ] Write 5 measures: Total Revenue, Budget Revenue, Variance $, Variance %, YoY %

*Resource:* Microsoft Learn — "DAX fundamentals" module (free, ~2 hours)

### Week 8 — Build the Dashboard
- [ ] **Page 1 — Executive Summary:** 4 KPI cards (Revenue, Gross Margin, EBITDA, Variance), revenue trend line chart, gauge chart for margin %
- [ ] **Page 2 — P&L Deep Dive:** Matrix visual (months as columns, P&L lines as rows), actual vs. budget bar chart, slicers for month range and outlet
- [ ] **Page 3 — Variance Analysis:** Waterfall chart (budget → actual bridge), outlet performance table with conditional formatting, drill-through to month detail
- [ ] Add slicers (month, outlet, scenario) to all pages
- [ ] Format: consistent color scheme, no chart junk, mobile-friendly layout
- [ ] Export screenshots for LinkedIn post
- [ ] Draft LinkedIn post: "I built a CFO dashboard in Power BI..."
- [ ] **Project 2 complete**

---

## PHASE 2D — PROJECT 3: CASH FLOW FORECAST
**Duration:** 1.5 weeks (Week 9 + half of Week 10)  
**Deliverable:** 13-week rolling cash flow forecast, UAE trading company scenario  
**Tools:** Excel

### What to Build
- Opening cash balance
- Collections model (AR aging buckets: current / 30 / 60 / 90+ days, collection rates)
- Payments model (supplier invoices, rent, payroll, VAT, loan installments)
- Net cash per week
- Minimum cash threshold warning (highlight weeks below AED 50K)
- 2 stress scenarios

*This is simpler than Project 1 — one scenario of scope, one tab for collections, one for payments, one summary. Should complete in 1.5 weeks if Project 1 skills are solid.*

---

## PHASE 2E — PROJECT 4: FINANCIAL STATEMENT ANALYSIS
**Duration:** 2 weeks (Weeks 11–12)  
**Deliverable:** Analyst-style financial review of a real UAE listed company  
**Company options:** Agthia Group (FMCG), Air Arabia (aviation), Aldar Properties (real estate)  
**Format:** PDF report + Excel ratio workings

### What to Build
- Income statement analysis (revenue trends, margin evolution, YoY)
- Balance sheet analysis (asset mix, leverage, working capital)
- Cash flow analysis (operating/investing/financing)
- Key ratios (liquidity, profitability, efficiency, leverage)
- Peer comparison (1 comparable company)
- 2-3 page narrative: what's driving performance, what risks exist

*Uses real public company data from investor relations page — annual report download.*

---

## PHASE 2F — PROJECT 5: BUSINESS CASE MODEL
**Duration:** 2 weeks (Weeks 15–16)  
**Deliverable:** NPV / IRR / sensitivity analysis for a UAE logistics decision  
**Tools:** Excel

*Details in Deliverable 4 Portfolio Roadmap. Defer planning until Project 4 complete.*

---

## PHASE 2G — PROJECTS 6 & 7 (OPTIONAL)
**Weeks 17–20:** SQL Finance Analytics + Python Finance Automation  
*Build only if: (a) no job offer yet and (b) these skills are being asked for in interviews*

---

## PARALLEL — JOB APPLICATIONS

### Application Rules
- Apply every week regardless of project progress
- Start with Tier 1 (FP&A Associate, junior FA) — EY + M.Sc. alone gets interviews
- Tier 2 (FP&A Analyst 2-4yr) — apply once Project 1 is complete
- Never apply without a tailored cover letter paragraph (2-3 sentences, not a generic template)
- Log every application in APPLICATION LOG below

### Weekly Application Target
- Weeks 1-6: 5–8 applications/week (Tier 1 focus)
- Weeks 7-10: 8–12 applications/week (Tier 1 + Tier 2)
- Weeks 11-20: 10–15 applications/week (all tiers, follow up on earlier apps)

### Priority Applications (from Phase 1 research)
- [ ] **Chalhoub Group FP&A Associate I** — check if still live, apply immediately
- [ ] **TotalEnergies Financial Analyst (Abu Dhabi)** — check if still live
- [ ] **NAFFCO FP&A Analyst** — apply with Project 1 complete
- [ ] Any new Landmark Group / Dubai Holding / Swiss Arabian openings
- [ ] Temp/contract roles: TASC Outsourcing, Hays UAE, Robert Half

### Application Log
*(Add one row per application)*

| Date | Company | Role | Status | Notes |
|---|---|---|---|---|
| — | — | — | — | — |

---

## SESSION LOG
*(Add one entry per session — never delete old entries)*

### 2026-08-20 — Phase 1 Closure + Phase 2 Full Setup
**Covered:**
- Built Skills Matrix (RESEARCH_Phase1D_Skills_Matrix.md)
- Added Phase 1C/1D updates to Deliverables 2, 3, 4
- Created PHASE2_MASTER_PLAN.md (tutor plan, 20-week timeline, project specs)
- Created JOB_PIPELINE.md — 10 live jobs found and assessed (Batch 1)
- Created DAILY_CHECKLIST.md — daily 45-min routine: apply + network + learn + log
- Live job search run: LinkedIn (FP&A analyst, financial analyst, FP&A associate, management reporting — Dubai) + Indeed UAE

**Skill levels confirmed:** Excel = accounting-level (Pivots at EY, years ago, nothing remembered). Power BI = zero.

**URGENT ACTION FOR ASHNAD TONIGHT:**
Apply to Chalhoub Group FP&A Associate I (Zimmermann) — posted 1 day ago, STRONG FIT, apply before it closes.
URL: https://www.linkedin.com/jobs/view/4452830346
Cover letter in JOB_PIPELINE.md BATCH 1 section — copy and personalise.

**Next session:** Week 1, Day 1 — Excel foundations. Start with VLOOKUP. Check JOB_PIPELINE for applications sent. Run new job search.
**Committed:** Yes — all files pushed.

---

## RESOURCES REFERENCE

| Topic | Resource | Format | Free? |
|---|---|---|---|
| Excel formulas | ExcelJet.net | Reference site | Yes |
| Excel for finance | CFI Excel Crash Course | Video course | Yes |
| Power Query | Excel Campus — Power Query for Beginners | YouTube series | Yes |
| Financial modeling structure | Breaking Into Wall Street | Paid (consider if needed) | No |
| Power BI basics | Guy in a Cube — Power BI Beginners playlist | YouTube | Yes |
| DAX fundamentals | Microsoft Learn — DAX in Power BI | Interactive course | Yes |
| Financial statement analysis | Investopedia + company annual reports | Reference | Yes |
| FP&A modeling concepts | CFI — FP&A course | Some free content | Partial |

---

## PROJECT QUALITY CHECKLIST
*(Apply to every project before publishing)*

- [ ] GitHub repo with clean README (business scenario, what was built, key findings)
- [ ] Management commentary included (not just a model — explain what it means)
- [ ] LinkedIn post drafted and published
- [ ] Screenshot carousel prepared (4-8 images of the actual work)
- [ ] GitHub link added to LinkedIn featured section

---

**This file is the single source of truth for Phase 2.  
Read it first. Update it last. Never skip the session log.**
