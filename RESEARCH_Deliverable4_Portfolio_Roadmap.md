# Deliverable 4 — Portfolio Roadmap

**Date:** 2026-08-20  
**Purpose:** 5–8 portfolio projects designed directly from job market research — covering real employer requirements with demonstrable, publishable work  
**Sequence:** Start with highest-frequency skills; each project should be completable in 1–4 weeks of evenings/weekends alongside your day job

---

## Overview

| # | Project | Sprint | Skills Covered | Time Estimate | Priority |
|---|---|---|---|---|---|
| 1 | FP&A Model — Retail Business | 1 | Excel, budgeting, forecasting, variance, scenarios | 3–4 weeks | ★★★★★ FIRST |
| 2 | CFO Dashboard — Power BI | 2 | Power BI, DAX, KPIs, data viz, management reporting | 2–3 weeks | ★★★★★ SECOND |
| 3 | 13-Week Cash Flow Forecast | 3 | Cash flow, liquidity analysis, stress scenarios | 1–2 weeks | ★★★★☆ THIRD |
| 4 | Financial Statement Analysis | 3 | FSA, ratios, comparative analysis, storytelling | 1–2 weeks | ★★★★☆ THIRD |
| 5 | Business Case Model (Investment) | 4 | NPV, IRR, sensitivity analysis, scenario modeling | 1–2 weeks | ★★★☆☆ FOURTH |
| 6 | SQL Finance Analytics | 4 | SQL, customer/margin/cohort analysis | 2 weeks | ★★★☆☆ OPTIONAL |
| 7 | Finance Automation Pipeline | 5 | Python, data pipeline, automation, reporting | 3 weeks | ★★☆☆☆ DIFFERENTIATOR |

---

## Project 1: FP&A Model — Retail Business (HIGHEST PRIORITY)

**Why this first:** Covers budgeting (~95%), forecasting (~95%), variance analysis (~90%), Excel (~100%), scenario analysis (~55%) — all at once.

**Scenario:**  
A mid-size UAE retail company (fashion, 3 outlets + e-commerce) needs a full annual budget with monthly forecasting and variance tracking.

**What to build:**
- Revenue budget (by outlet, by month, with seasonality — Ramadan uplift, summer dip)
- COGS model (markup %, product mix)
- OpEx model (rent by outlet, payroll, marketing spend)
- Complete P&L (budget vs. actual vs. prior year, 3-way variance)
- Rolling 3-month forecast (updates as actuals come in)
- Scenario analysis (base / upside / downside — what if e-commerce grows 30% YoY?)
- Dashboard tab (summary: key metrics, variances highlighted, traffic-light status)

**Tools:** Excel only (no Power BI yet — keep it pure Excel first)
- Power Query for data import/refresh
- Pivot Tables for variance summaries
- Dynamic named ranges
- Excel charts with conditional formatting

**Dataset:** Create a realistic fictional dataset (monthly sales by outlet, COGS, OpEx line items). Make numbers feel real — base on UAE retail sector context.

**Structure (tabs):**
1. Assumptions (inputs hub — all variables here)
2. Revenue Build
3. COGS Build
4. OpEx Detail
5. P&L Summary (actual vs. budget vs. prior)
6. Variance Analysis
7. Rolling Forecast
8. Scenario Analysis
9. Dashboard

**GitHub:** Upload Excel file + README explaining the business scenario, key modeling decisions, and insights from the model

**LinkedIn post angle:** "I built a complete FP&A model for a UAE retail business — here's what it revealed about seasonal planning"

---

## Project 2: CFO Dashboard — Power BI (SECOND PRIORITY)

**Why second:** Power BI appears in ~65% of postings. Building it after Project 1 means you already have the data/model to connect it to.

**Scenario:**  
The same retail company from Project 1 needs a live CFO dashboard so leadership can monitor performance without digging into Excel.

**What to build:**
- KPI cards: Revenue, Gross Margin %, OpEx Ratio, EBITDA, Cash Position
- Revenue trend chart (actual vs. budget, month by month)
- Variance waterfall chart (budget → actual)
- Outlet performance breakdown (which location is driving/dragging?)
- YoY comparison (this year vs. prior year by month)
- Drill-through: Click on a month → see underlying breakdown
- Filters/slicers: by outlet, by month, by scenario

**Tools:** Power BI Desktop (free) + data from Project 1 Excel model
- Learn DAX basics: CALCULATE, FILTER, SUMX, DIVIDE, date intelligence
- Import from Excel, build data model, create measures

**Dataset:** Export/connect from Project 1 Excel model (clean .csv or direct Excel connection)

**Structure:**
1. Executive Summary page (KPIs + trends)
2. P&L Deep Dive page
3. Outlet Performance page
4. Variance Analysis page

**GitHub:** .pbix file + screenshots + README explaining DAX measures used and design decisions

**LinkedIn post angle:** "I built a CFO dashboard in Power BI for the retail FP&A model — here's how I structured the data model"

---

## Project 3: 13-Week Cash Flow Forecast

**Why third:** Cash flow appears in ~55% of postings. Quick to build once you have Excel skills from Project 1.

**Scenario:**  
A UAE trading company needs a 13-week rolling cash flow forecast to manage liquidity ahead of a major procurement cycle.

**What to build:**
- Opening cash balance
- Collections model (AR aging: current / 30 days / 60 days / 90+ days overdue; collection rates)
- Payments model (supplier invoices, rent, payroll, VAT payments, loan installments)
- Net cash position per week
- Minimum cash threshold warning (highlight weeks below AED 50K floor)
- Stress scenarios: "What if 20% of AR is 90+ days overdue?" / "What if supplier demands early payment?"
- Action trigger: which weeks need cash injection / line of credit drawdown

**Tools:** Excel (Power Query + conditional formatting for warnings)

**Dataset:** Create realistic UAE trading company data (FMCG distribution, food trading — sectors you've seen at Promotech level)

**GitHub:** Excel file + README with business context and key findings

**LinkedIn post angle:** "Most SMEs in Dubai run cash flow on instinct. Here's a 13-week model that gives them a 3-month visibility window"

---

## Project 4: Financial Statement Analysis — Public Company

**Why fourth:** FSA appears in ~50% of postings. Teaches analytical writing + ratio interpretation. Uses a real public company (verifiable, credible).

**Scenario:**  
Write an analyst-style financial statement review of a publicly listed UAE or GCC company (e.g., Emaar Properties, Emirates NBD, DP World, Agthia Group, ADNOC Distribution).

**What to build:**
- Income statement analysis (revenue trends, margin evolution, YoY changes)
- Balance sheet analysis (asset mix, leverage, working capital)
- Cash flow analysis (operating vs. investing vs. financing cash flows)
- Key ratios (liquidity, profitability, efficiency, leverage)
- Peer comparison (vs. 1-2 comparable companies)
- 2–3 page narrative: what's driving performance, what risks exist, what to watch

**Format:** PDF report (well-formatted; looks like a real equity research note)

**Dataset:** Download from company investor relations page (annual report / financial statements)

**GitHub:** PDF report + Excel ratio workings

**LinkedIn post angle:** "I analyzed [Company]'s financials for 2024–2025. Three things surprised me about [metric/trend]"

---

## Project 5: Business Case Model (NPV/IRR/Sensitivity)

**Why fifth:** Investment analysis / business case mentioned in 25–30% of postings; great for roles that involve capital allocation decisions.

**Scenario:**  
A UAE logistics company is deciding whether to lease additional warehouse space in Dubai South vs. Jebel Ali for 5 years. Build the investment case.

**What to build:**
- Revenue uplift from expanded capacity (units × margin)
- Cost model (lease cost, fit-out capex, incremental headcount)
- Free cash flow projection (5 years)
- NPV analysis (at 8%, 10%, 12% discount rates)
- IRR calculation
- Payback period
- Sensitivity table (NPV vs. revenue growth assumption + vs. lease cost)
- Scenario comparison: Dubai South vs. Jebel Ali

**Tools:** Excel

**GitHub:** Excel file + 1-page executive summary slide (PowerPoint)

**LinkedIn post angle:** "How do you make a lease vs. buy decision in Dubai's logistics market? I built a business case to find out"

---

## Project 6: SQL Finance Analytics (Optional but Differentiating)

**Why:** SQL mentioned in ~30% of postings; you already have Python skills, so SQL is straightforward to add. Positions you as technically deeper than most FP&A candidates.

**Scenario:**  
Analyze a simulated e-commerce / retail transaction database to extract FP&A insights: customer profitability, product margin analysis, monthly revenue cohorts.

**What to build:**
- Database: SQLite or PostgreSQL with realistic transaction-level data (orders, products, customers, invoices)
- Queries:
  - Monthly revenue and MoM growth
  - Gross margin by product category
  - Customer lifetime value (basic: total revenue per customer)
  - AR aging: which invoices are overdue and by how long
  - Top 10 customers by revenue and margin
  - Cost trend analysis by category

**Tools:** SQL (SQLite/PostgreSQL) + Python (pandas for visualization layer) or export to Excel

**GitHub:** .sql file + README + screenshot of query results

**LinkedIn post angle:** "Finance isn't just Excel. Here's how SQL helps FP&A teams answer questions Excel can't"

---

## Project 7: Finance Reporting Automation (Differentiator — Low Priority)

**Why last:** Directly leverages your strongest skill (Python/automation) for a finance use case. Most FP&A candidates cannot do this — it differentiates significantly if framed correctly.

**Scenario:**  
Automate the monthly management reporting process: raw data → cleaned → aggregated → formatted report.

**What to build:**
- Input: Raw CSV export from an ERP (simulate Odoo/Tally export format)
- Step 1: Python script to clean data (handle duplicates, missing values, formatting)
- Step 2: Python to aggregate (monthly summary, variance calculation)
- Step 3: Auto-generate formatted Excel report (openpyxl) with charts
- Step 4 (optional): Schedule to run automatically each month

**Tools:** Python (pandas, openpyxl) — you already have these skills

**GitHub:** Python script + README explaining the use case + before/after examples

**LinkedIn post angle:** "Finance teams lose 2 days per month on manual reporting. Here's a Python script that does it in 2 minutes"

---

## Timeline Suggestion (Balanced with Job Applications)

| Week | Priority Task | Job Search |
|---|---|---|
| 1–2 | Begin Project 1 (FP&A model, revenue + COGS tabs) | Volume apply Tier 1 (FP&A Associate, junior FA) |
| 3–4 | Complete Project 1 (P&L, variance, scenarios, dashboard) | Continue Tier 1 applications; refine cover letter |
| 5–6 | Project 2: Power BI dashboard (connect to Project 1 data) | Begin Tier 2 applications (with Project 1 portfolio) |
| 7–8 | Complete Project 2; begin Project 3 (cash flow) | Active Tier 1 + Tier 2 volume |
| 9 | Project 3 complete; begin Project 4 (FSA) | Target NAFFCO-style roles with 2 projects complete |
| 10 | Project 4 complete | Continue all tiers; follow up on earlier applications |
| 11–12 | Project 5 (business case) or Project 6 (SQL) — based on what employers are asking in interviews | Adjust based on interview feedback |
| 13–16 | Refine portfolio based on interview feedback; continue applying | Intensify Tier 2 and Tier 3 applications |
| 17–20 | Final push — Oct 28 notice deadline approaches | Any role with AED 7,000+ and reasonable growth path |

---

## Project Quality Standards

Each project must have:
- [ ] **GitHub repo** (public, clean README, well-structured files)
- [ ] **Business scenario** clearly explained (what problem are you solving? for whom?)
- [ ] **Key insights** section (what does the analysis reveal? — this shows analytical thinking, not just technical execution)
- [ ] **LinkedIn post** written at project launch (1 post per project, professional framing)
- [ ] **Portfolio page or PDF summary** (1-2 slides per project; printable / shareable)

---

*Deliverable 4 of 6. Paired with Skill Gap Analysis and Job Application Strategy.*

---

## Phase 1C/1D Update — 2026-08-20

*Original deliverable based on 18 LinkedIn postings and generic best-practice advice. These additions reflect findings from global showcaser research (8 real showcase posts analyzed) and the Chalhoub JD, which provides the clearest single data point on what the first real application needs to demonstrate.*

### The Global Showcasing Benchmark (Why This Matters)

UAE FP&A community does zero portfolio showcasing. Zero. Out of 70 LinkedIn profiles and multiple content searches, no UAE FP&A professional posts project work. The global benchmark (primarily India, some UK/US) is active and growing. Posting 3-4 well-executed project posts makes Ashnad the most visible finance portfolio builder in the UAE market by default. The bar is genuinely zero.

### Gold Standard Formats (From Best Showcasers Globally)

**Format 1 — Pankaj Kawade (driver-based forecast):** Built a 3-year driver-based forecast for Eternal Ltd. (formerly Zomato). Used Bear/Base/Bull scenarios. Then QA'd every assumption against the company's actual FY26 results — found real model bugs (legacy "take rate" driver no longer applicable after Blinkit acquisition). Wrote about what the model got wrong, not just what it got right. This intellectual honesty is more credible than a perfect-looking model. His best line: *"Financial modelling is as much about knowing what you don't know as about the formulas."*

**Format 2 — Ben Capobianco (quantified real impact):** Built complete financial infrastructure for a real restaurant during an internship. Every result quantified: 95% data collection time reduction, 86% daily forecast accuracy, 24% revenue above 4-year historical average. No vague claims. Numbers tied to real business outcomes.

**Key insight:** Projects using real company data (listed company annual reports) outperform fictional scenarios in credibility. UAE-listed companies with usable public financial data: Emaar Properties, Air Arabia, Aldar Properties, Agthia Group, ADNOC Distribution, Emirates REIT.

### Updated Project 1 Guidance

The original Project 1 scenario (fictional UAE retail company) is still valid as a starting point. But based on showcaser research and the Chalhoub JD, two additions:

1. **Use a real UAE listed company for at least one project** — Agthia Group (FMCG, Abu Dhabi-listed) or Air Arabia (low-cost airline, Sharjah) are ideal: detailed annual reports, stable financials, not too complex. This gives "real data, real company" credibility that fictional scenarios can't match.

2. **Add written management commentary to every project** — Chalhoub JD specifically says: "prepare P&L variance commentary for presentation to senior management." A model without commentary is incomplete evidence. Each project needs a "What this tells leadership" section (1 paragraph minimum, executive-summary style).

### LinkedIn Post Cadence (Updated)

Original plan: 1 post per project. Updated based on Kavish Kaul's series approach:

**3 posts per project, same company/scenario:**
- **Post 1 (Week of project completion):** Share the project — what you built, hook + bullet list + carousel screenshots
- **Post 2 (1 week later):** Share one specific finding — the most interesting/counterintuitive thing the analysis revealed
- **Post 3 (2 weeks later):** Share one lesson — what building it taught you about the craft of FP&A

This gives 3 touchpoints per project, builds a series audience, and each post reinforces the previous one. For 4 projects = 12 LinkedIn posts over 3-4 months = sustained visibility.

### Post Structure Template (from global showcaser research)

```
[HOOK — one sentence that stops the scroll]
  Example: "I spent 4 days analyzing Air Arabia's financials. Here's what the budget vs. actual reveals about their post-COVID recovery."

[CONTEXT — 2-3 sentences: what problem, why this company]

[WHAT I BUILT — 4-6 bullets, specific and concrete]
  • Driver-based 3-year forecast with Bear/Base/Bull scenarios
  • Budget vs. Actual variance analysis (Revenue, Gross Margin, OpEx)
  • Monthly rolling forecast with automated recalculation

[KEY FINDING — 1-2 insights, honest about surprises or limitations]
  • The most interesting thing: Q3 margin compression is driven by fuel cost timing, not revenue softness

[LESSON — one genuine reflection on the craft]
  "Financial modelling is as much about knowing what you don't know as about the formulas."

[CTA]
  "Happy to share the methodology if useful — just comment below."

[ATTACHMENT — 4-8 screenshot carousel of actual work]
```

### Ashnad's Unique Framing Angle

Python/automation background is rare in UAE FP&A. The trading platform (data pipelines, API integration, automated reporting) maps directly to where FP&A is going. Frame it as:
> *"I automated the data pipeline so I could focus on the analysis, not the data wrangling."*

This positions ahead of where most FP&A analysts are today (still doing manual Excel refreshes) and where Mary Huseynova (Director FP&A, Dubai Holding) already operates (Power BI + PL SQL + VBA + automation). Project 7 (Finance Automation Pipeline) should be framed exactly this way.

### What Did Not Change

- Project sequence remains the same (FP&A Model → Power BI Dashboard → Cash Flow → FSA → Business Case → SQL → Automation)
- Timeline suggestion unchanged (20-week parallel with job applications)
- Project quality standards unchanged (GitHub + README + LinkedIn post + key insights)
