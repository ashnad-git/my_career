# my_career — CHANGELOG

All notable changes to this repository are documented here. Timestamped entries track when work happened.

---

## [2026-08-25] — Session: LinkedIn Connections Batch — 19 Finance Directors / CFOs

### Added
- **2026-08-25** — `NETWORKING.md` — Entries #20–38: 19 Finance Directors, CFOs, Heads of FP&A identified via LinkedIn people search (pages 1–2, "FP&A Manager finance director" UAE). All 2nd-degree. All have invite notes drafted. Key targets: Niraj Madhogaria (FP&A Director Etihad), Veeshal T. (Finance Dir ex-Landmark/GMG), Mortada Hammoud (FD Americana Foods), CA Hariprasad Nair (Group CFO FMCG/Retail), Maaz Dastagir (Commercial FD Live Nation ME).

### Updated
- **2026-08-25** — `PENDING.md` — LinkedIn connections task marked complete.

---

## [2026-08-25] — Session: LinkedIn JD Extraction + STRETCH Audit

### Added
- **2026-08-25** — `jds/ENGIE_FinancialAnalyst_AMEA_2026-08-25.md` — STRETCH. Project finance/infrastructure role at ENGIE Middle East AIFA team. Banking/deal experience required.
- **2026-08-25** — `jds/Eaton_FPAAnalyst_Manufacturing_2026-08-25.md` — STRETCH. FP&A at Eaton Dubai manufacturing plant. SAP + 2yr manufacturing mandatory.
- **2026-08-25** — `jds/EmiratesFlightCatering_CostAnalyst_2026-08-25.md` — NOT SUITABLE. 5yr + production accounting + JDE ERP. Cost accounting track, not FP&A.
- **2026-08-25** — `jds/AlKhayyatInvestments_FinanceAnalystFPA_2026-08-25.md` — STRETCH (bonus find). AKI Central Finance FP&A; 4-6yr multinational + qualification required. Strong automation/BI focus aligns with profile.

### Updated
- **2026-08-25** — `PENDING.md` — LinkedIn JD extraction task marked complete. 12/14 jobs resolved; GymNation/Marsh McLennan/Sharaf DG confirmed expired/unavailable. New AKI STRETCH added to STRETCH list.

---

## [2026-08-25] — Session: Bulk Job Search — 82 New JDs Across 5 Platforms

### Added
- **2026-08-25** — `jds/` — 82 new JD files: Indeed (37 via JobSpy), Bayt (17 via crawl4ai), Naukrigulf (10 via browser + crawl4ai), GulfTalent (6), individual browser fetches (12). Total archive: 110 files.
- **2026-08-25** — `python-jobspy` established as primary Indeed scraper: 20 keyword queries, full JD text returned, no auth/API key needed. Documented in CLAUDE.md.
- **2026-08-25** — `JOB_PIPELINE.md` — Rows 19–63 added: 44 new STRONG/GOOD FIT roles. Includes ITP Media Group (STRONG), Greenbull Junior FA (STRONG), NEP Commercial Finance (STRONG), Associate Commercial Analyst x2 (STRONG), plus 20+ GOOD FIT analyst roles across all platforms.

### Fixed
- **2026-08-25** — `jds/` — 4 bad Indeed JD files that contained login page content instead of JD replaced with real content: Huda Beauty MEAI, Binance Business Analyst (NOT SUITABLE — Chinese/Mandarin required), Bahmani Group FP&R, AEJEA-POML MCV Finance Business Partner.
- **2026-08-25** — 9 duplicate JD files removed (same role saved twice from different crawl batches).

### Updated
- **2026-08-25** — `JOB_PIPELINE.md` — Last Updated updated to 2026-08-25. Old stale "APPLY TOMORROW 2026-08-21" content superseded by Session 2026-08-25 section.

---

## [2026-08-24] — Session 14: Modeling Best Practices + Textbook + CF Intro

### Added
- `learning/EXCEL_TEXTBOOK.md` — cumulative study textbook created. 7 chapters covering all Phase 2A learning to date: SUMIFS, VLOOKUP, INDEX-MATCH/IFERROR, Power Query, Pivot Tables, Charts, Modeling Best Practices. Every practice question with formula and answer.
- `learning/phase2a_excel/04_index_match_practice.xlsx` — INDEX-MATCH + IFERROR practice file. 30 employees, 11 exercises (right lookup, left lookup, IFERROR, MAX combo). Answer Key hidden.
- `learning/phase2a_excel/generate_index_match_practice.py` — generator script for above
- `learning/phase2a_excel/07_conditional_formatting_practice.xlsx` — CF practice file. P&L variance table with 4 tasks (Highlight Rules, Data Bars, Icon Sets, Custom Formula Rule).
- `learning/phase2a_excel/generate_cf_practice.py` — generator script for above
- `06_Model_Structure_practice.xlsx` — 3-tab linked model skeleton built this session (Assumptions → Calculations → Output, named ranges, color coding)

### Changed
- `CLAUDE.md` — two hard rules added: (1) Always generate Excel practice files, never ask Ashnad to type data manually. (2) Update EXCEL_TEXTBOOK.md after every teaching session.
- `learning/phase2a_excel/README.md` — file index corrected to match actual files created (not planned numbering)
- `DAILY_LOG.md` — retroactive entries written for Sessions 12 and 13 (Pivot Tables + Charts), scoreboard updated to 7.5 learning hours
- `PHASE2_MASTER_PLAN.md` — status dashboard and session log updated

### Learning (Day 8-9: Modeling Best Practices)
- 3-tab model structure: Assumptions (inputs only, blue) → Calculations (formulas only, black) → Output (links only, green)
- Named ranges: Name Box → type name → Enter. Formula reads `=Base_Revenue*(1+Growth_Rate)` not `=Assumptions!B2*(1+Assumptions!B3)`
- Color coding convention: blue = hardcoded, black = formula, green = cross-sheet link
- Practice build: 3-tab skeleton, Growth Rate changed 10%→20%, all tabs updated automatically ✅

### Learning (Day 10-11: Conditional Formatting — intro)
- 4 types explained: Highlight Cell Rules, Data Bars, Icon Sets, Custom Formula Rules
- Threshold concept: ±5% is noise, >5% is signal — only custom formula rules can enforce this
- $ anchor rule in custom formulas: `=$E5<-0.10` locks column, lets row move
- Task 1 (Highlight Rules) deferred to next session

---

## [2026-08-21] — Session 6: Block 2 Fresh Job Search + Search Terms Master List

### Added
- `SEARCH_TERMS.md` — Comprehensive 100-term search terms master list across 6 tiers: primary FP&A titles, role variants, sector-specific, company-targeted, creative/unconventional, and platform-specific URLs. Tracks terms used per session to avoid repetition. Created in response to user request for systematic search term rotation.
- `jds/MegaHealth_FinancialAnalyst_Dubai_2026-08-21.md` — 🟡 GOOD FIT. Financial Analyst, Mega Health Insurance Brokers, Dubai. No experience/certification blocker. Added to active pipeline.
- `jds/BukhatirBEAM_FPnA_Analyst_Sharjah_2026-08-21.md` — ❌ NOT SUITABLE. FP&A Analyst, Bukhatir BEAM, Sharjah. CFA Level 1 mandatory (hard blocker). Saved for skills frequency data.
- Cover letter PDF for TotalEnergies portal: `resumes/Muhammed_Ashnad_TotalEnergies_CoverLetter.pdf`
- `SESSION_PLAN_2026-08-21.md` — 38-task session checklist across 5 blocks

### Job Search Summary (2026-08-21 Block 2)
- **Platforms searched:** LinkedIn (8 search terms), Indeed UAE (5 search terms), Naukrigulf (Financial Analyst Dubai — 73 results)
- **LinkedIn IDs reviewed:** 42 new IDs across all searches — 41 NOT SUITABLE, 1 GOOD FIT (Mega Health)
- **Indeed UAE:** Mostly duplicates or senior roles; no new suitable roles beyond Mega Health
- **Naukrigulf:** 73 results; mostly senior/accountant roles; 1 pending (Confidential Junior FA, JD fetch failed)
- **Key insight:** Tier 1 LinkedIn terms exhausted for this week. Tier 2–4 terms queued in SEARCH_TERMS.md for next session.

### Updated
- `JOB_PIPELINE.md` — Added Mega Health (GOOD FIT, #16); Bukhatir BEAM archived (NOT SUITABLE); 21 reviewed IDs logged; 2 pending roles noted (Naukrigulf Confidential, Siemens Energy Project Controller); last search date updated to 2026-08-21
- `CLAUDE.md` — Hard rule added: JD content must be verbatim (no paraphrasing, no omissions); corrected this session for the third time — now permanent
- All 24 existing jds/ files — Rebuilt with full verbatim content (was: summaries; now: every bullet, every line)

### Pending from today (carry to next session)
- Fetch Naukrigulf Confidential Junior Financial Analyst JD (socket error today)
- Fetch Siemens Energy Project Controller JD from LinkedIn
- Block 1 applications (6 jobs with deadlines — postponed, apply today)
- Block 3: LinkedIn About section, connection requests, recruiter emails
- Block 4: Excel VLOOKUP lesson

---

## [2026-08-20] — Session 5: 4 More Applications + dubizzle Tailored Resume

### Applied
- **NAFFCO — FP&A Analyst** | NAFFCO TeamTailor portal | tailored PDF (audit-fixed, 58→65+/100)
- **Al Khayyat Investments (AKI) — Finance Analyst FP&A** | LinkedIn Easy Apply | master PDF | STRETCH
- **Eaton — FP&A Analyst (Manufacturing Finance)** | Eaton Eightfold portal | master PDF | STRETCH (SAP must-have gap; applied anyway)
- **dubizzle (Bayut) — Associate Commercial Analyst** | Workable portal | tailored PDF (72/100) | GOOD FIT

### Added
- `resumes/Muhammed_Ashnad_NAFFCO_FPnA_Analyst.md` — NAFFCO tailored resume (source)
- `resumes/Muhammed_Ashnad_NAFFCO_FPnA_Analyst.pdf` — NAFFCO tailored PDF (5 audit fixes)
- `resumes/Muhammed_Ashnad_Dubizzle_AssociateCommercialAnalyst.md` — dubizzle tailored resume
- `resumes/Muhammed_Ashnad_Dubizzle_AssociateCommercialAnalyst.pdf` — dubizzle tailored PDF
- `jds/Revolut_SeniorFixedIncomeResearchAnalyst_UAE_2026-08-20.md` — NOT SUITABLE (quant, STEM, 5yr req)
- `scripts/build_resume_pdf.py` — added `build_naffco()` and `build_dubizzle()` functions + dispatch keys

### Updated
- **Contact number** — +971 543255352 propagated across all files and all PDFs (master + Chalhoub + NAFFCO)
- **CLAUDE.md** — Added mandatory "Application Process — Mandatory Checklist" (12-step GOOD FIT / 5-step GOOD FIT Easy Apply / 4-step STRETCH process). Hard rules block added.
- **JOB_PIPELINE.md** — AKI, Eaton, dubizzle removed from active; all 6 total applications moved to APPLIED
- **PENDING.md** — 5 remaining STRETCH jobs documented with deadlines for tomorrow's session
- **Memory** — `feedback_tailored_resume_before_applying.md` updated with 10-step mandatory sequence

### Process fixes (3 failures caught and corrected this session)
1. NAFFCO form handed off without tailored resume → checklist added to CLAUDE.md
2. PDF sent to Ashnad without running hr-audit first → audit-before-send rule hardcoded
3. Audit findings not implemented before sending → must implement before SendUserFile

### Pending from today (carry to next session)
- LinkedIn headline still shows "Aspiring Financial Analyst" — update urgently (recruiters see this on every application)
- LinkedIn phone number not updated in LinkedIn profile settings
- DAILY_LOG Q&A entry for this session
- 5 remaining STRETCH applications (see PENDING.md "APPLY TOMORROW" section)

---

## [2026-08-20] — Session 3: First Application Submitted

### Applied
- **Chalhoub Group — FP&A Associate I (Zimmermann)** | LinkedIn Easy Apply | 2026-08-20
  - Tailored resume: `resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf`
  - hr-audit score: 74/100 (two rounds, up from 58/100)
  - Cover letter: human-voice rewrite after AI-sounding version flagged by Ashnad

### Added
- **2026-08-20** — `scripts/build_resume_pdf.py` — reportlab PDF builder for all resumes (master + tailored). Run: `python3 scripts/build_resume_pdf.py <key>`. Keys: master, chalhoub.
- **2026-08-20** — `resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.md` — Chalhoub tailored resume (source)
- **2026-08-20** — `resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf` — Chalhoub tailored resume (PDF)

### Updated
- **CLAUDE.md** — Added Resume PDF Generation section: command, style reference, how to add new resumes
- **PHASE2_MASTER_PLAN.md** — Applications Sent: 0 → 1. Status dashboard and session log updated.
- **JOB_PIPELINE.md** — Chalhoub moved to Applied. GBM flagged as next urgent (deadline Aug 21).
- **DAILY_LOG.md** — Session 3 entry added. Scoreboard: applications 0 → 1.

### Clarified
- ACCA references in research files are market data only — Ashnad pursues CMA (US), not ACCA.

---

## [2026-08-20] — Session 2: Resume Finalization

### Added
- **2026-08-20** — `Muhammed_Ashnad_Resume.pdf` — ATS-friendly 2-page PDF, single column, Helvetica, all text selectable
- **2026-08-20** — `.claude/commands/hr-audit.md` — slash command for HR-style critical resume audit vs any job description
- **2026-08-20** — `resumes/` directory — job-tailored resume versions go here, one per application
- **2026-08-20** — `promotech/` directory — Promotech Advertising source data: 2024 IFRS audit report (Kreston Menon) + 2025 Tally registers (Sales, Purchase, Payment, P&L)

### Updated (Resume — multiple iterations)
- **Positioning:** Headline changed from "Junior Accountant" to "Finance Professional | Financial Analysis & FP&A | M.Sc. Financial Economics | Ex-EY | Dubai"
- **Promotech bullets:** Reframed from "inherited chaos" to "designed and implemented from scratch" — avoids criticizing employer in writing. Removed confidential company financials (revenue, assets, payables). Kept process metrics: 30+ accounts, 1,000+ transactions, IFRS audit support.
- **EY Tax Analyst:** Restored to full 5 bullets — was incorrectly cut to 2. EY is the strongest credential and should never be trimmed.
- **Education:** Now a proper section — each degree on its own block with institution, location, year. Was previously crammed into one line.
- **Certifications:** Now a proper list — each certification on its own line. Was previously a footnote.
- **LinkedIn URL:** Confirmed as linkedin.com/in/muhammed-ashnad-k — embedded in PDF header.
- **Removed:** Employee count, company revenue figures, asset figures, Portfolio Projects section (not yet live), GitHub placeholder text.

### Key decisions logged
- Never put confidential employer financial data (revenue, profit, assets) on a public resume — private company, not authorized for disclosure
- Never list employee count next to employer name — unprofessional formatting
- Process metrics (transaction count, account count) are fine — they describe your work, not the company's financials
- Portfolio Projects section removed until at least 1 project is live on GitHub — unfinished work listed on a resume hurts more than it helps

## [2026-08-20] — continued

### Updated
- **2026-08-20 ~02:00** — Muhammed_Ashnad_Resume.md: Full FP&A-targeted reframe. Headline changed from "Junior Accountant | Accounting Operations" to "Finance Professional | Financial Analysis & FP&A | M.Sc. Financial Economics | Ex-EY | Dubai". Core Skills completely reorganized — FP&A competencies lead, accounting foundation moves to bottom. Promotech experience split into two subsections (Finance Systems Transformation + Financial Reporting & Analysis) to lead with analytical framing. EY bullets reframed from compliance documentation to financial analysis, discrepancy investigation, and stakeholder coordination. BB Advisory "Financial Analyst Intern" promoted with clearer framing around valuation models. Portfolio Projects section added. No fabricated experience — all changes reframe real work using FP&A vocabulary.

---

## [2026-08-20]

### Added
- **2026-08-20 00:15** — Initial repo structure with USER_PROFILE.md (comprehensive, evolving profile)
- **2026-08-20 00:20** — CHANGELOG.md + PENDING.md (version control discipline)
- **2026-08-20 00:20** — CLAUDE.md (session context + collaboration patterns)
- **2026-08-20 00:40** — Career Transition Brief integration (major strategy clarification)

### Updated
- **2026-08-20 00:30** — USER_PROFILE.md: Added detailed context on Promotech role transformation (chaos → order, filing systems, ERP migration)
- **2026-08-20 00:30** — Muhammed_Ashnad_Resume.md: Reframed to emphasize systems transformation, initiative-taking, technical migration (not just junior accountant tasks)
- **2026-08-20 00:30** — Professional summary updated to highlight process optimization and organizational transformation capabilities
- **2026-08-20 00:45** — CLAUDE.md: Major rewrite reflecting career transition strategy (accounting → FP&A), research methodology, work phases, critical research principles

### Context
Initial setup: Created `my_career` repo on GitHub (ashnad-git/my_career) with proper version control practices matching the Ultimate Trading Terminal project structure. Established detailed user profile documenting current role, expertise, values, and collaboration model with Claude.

**Resume reframing:** Current Promotech role repositioned as systems transformation work (inherited chaos, implemented filing frameworks, led ERP migration) rather than passive accounting tasks. Better aligns resume with demonstrated capability in systems thinking and technical problem-solving.

**MAJOR STRATEGY CLARIFICATION (2026-08-20 00:40):**
Read Career Transition Brief. Corrected fundamental misunderstanding: 
- User is NOT building trading platform as permanent career
- Trading platform = EVIDENCE of technical capability (automation, systems thinking, data handling)
- ACTUAL GOAL: Transition from accounting operations → Financial Analyst / FP&A / Finance Analytics
- Strategy: Research 100+ real UAE/Dubai job postings → identify requirements → build targeted portfolio projects → transition to analytical finance roles
- Narrative: Accounting foundation + EY experience + independent FP&A projects → Financial Analyst/FP&A role
- Next phase: Career transition research (job market analysis, skill gap analysis, portfolio roadmap)

---

## [2026-08-20 continued]

### Added
- **2026-08-20 02:00** — RESEARCH_Phase1_UAE_Job_Market_Report.md: Updated with confirmed Indeed salary data (64 reports, avg AED 8,686/month, range AED 4,422–17,061; Junior FA AED 6,906/month avg; Senior FA AED 13,505/month avg)
- **2026-08-20 02:00** — RESEARCH_Deliverable2_Skill_Gap_Analysis.md: Full gap analysis (technical, qualification, soft skills) with priority sprints to close gaps
- **2026-08-20 02:00** — RESEARCH_Deliverable3_Career_Target_Ranking.md: Role ranking by realistic fit, vacancy volume, salary, timeline — 4 tiers with detailed profiles
- **2026-08-20 02:00** — RESEARCH_Deliverable4_Portfolio_Roadmap.md: 7 projects designed from job market data — scenarios, tools, sequence, timeline
- **2026-08-20 02:00** — RESEARCH_Deliverable5_LinkedIn_Strategy.md: Headline options, about draft, keywords, content pillars, recruiter outreach strategy
- **2026-08-20 02:00** — RESEARCH_Deliverable6_Job_Application_Strategy.md: Phase-based application plan, cover letter formula, interview gap-handling, recruiter list

### Context
Phase 1 research deliverables completed (1 of 6 from prior session + 5 added here). All 6 deliverables address the career transition from accounting operations → FP&A / Financial Analyst in Dubai. Phase 1B planned: expand company universe beyond LinkedIn/Indeed — direct company career pages, freezone company lists, LinkedIn people search for target company identification.

---

## [2026-08-20 Phase 1B]

### Added
- **2026-08-20 04:00** — RESEARCH_Phase1B_Company_Universe.md: Expanded company universe to 57 identified UAE/Dubai employers (39 net new beyond Phase 1). Sources: LinkedIn job search (Financial Analyst + FP&A Analyst, 3 pages each), Bayt.com UAE (3 pages), Indeed UAE (2 pages).

### Key Findings from Phase 1B
- **Al-Futtaim Group** is the most active Dubai FP&A employer — multiple openings across retail, automotive, real estate, health divisions
- **NAFFCO FP&A Analyst salary confirmed: AED 8,000–12,000/month** (primary target benchmark)
- **Greenbull Dubai Junior FA: AED 15,000–18,000/month** (likely needs 2+ years despite "junior" title)
- **Fixed-term / temp contracts exist** (Huda Beauty, Ounass, Shiseido) — valid entry points
- **Retail/FMCG and Energy/Industrial** are most accessible sectors given accounting + ERP background
- **Tier 1 targets identified:** NAFFCO, Al-Futtaim, Huda Beauty, Fresha, Ounass, GBM, Eaton, TotalEnergies, ENGIE, Mohamed Hilal, NFPC
- **12 direct career pages** identified for companies that post outside job boards

---

## [2026-08-20 Phase 1B — Direct Career Pages]

### Added / Updated
- **2026-08-20 06:00** — RESEARCH_Phase1B_Company_Universe.md: Added direct career page research results for all 8 priority companies + 4 freezone directories

### Career Page Findings
- **TotalEnergies:** 2 UAE roles confirmed — "Financial Analyst" (Jan 2026) + "Financial Business and Reporting Analyst" (Jun 2026), both under TotalEnergies EP United Arab Emirates (Regular positions)
- **NAFFCO + Huda Beauty:** No career pages — LinkedIn/Indeed only. Already captured in job board scraping.
- **Al-Futtaim:** Workday ATS was down (global outage). Needs manual follow-up — most active Dubai FP&A employer.
- **Fresha:** Finance & Operations team has 2 roles (Financial Controller + Senior Accountant) — both Warsaw-based. No UAE finance openings.
- **Ounass:** No careers page (Al Tayer Group subsidiary). Posts exclusively on LinkedIn.
- **Checkout.com:** 8 Dubai roles found at checkout.com/jobs. Finance-relevant: Associate Financial Control, Senior Analyst Payments, Senior Associate Regional Treasury, Senior Manager Internal Audit. All fintech-specific.
- **ENGIE:** Needs manual UAE + Finance filter at jobs.engie.com — automation could not complete interactive dropdown filtering.

### Freezone Directory Findings
- **DIFC:** Public register accessible — company registrations only, not jobs. Mostly financial institutions.
- **DMCC:** Directory page loads but search form is JS-rendered; no accessible search via automation. 26,000+ companies, no sector filtering possible.
- **DAFZA + JAFZA:** Both 404 — no public company directories.
- **Verdict:** Freezone directories add no employer identification value beyond job board scraping.

---

## [2026-08-20 Phase 1C — LinkedIn Deep Research]

### Added
- **2026-08-20 07:00** — RESEARCH_Phase1C_LinkedIn_Deep_Research.md: Deep LinkedIn research across 4 simultaneous search streams

### Research Streams
- **LinkedIn Jobs (100+ results):** Broader query (financial analyst OR finance analyst OR FP&A analyst OR management reporting analyst OR commercial analyst), UAE, past month — 16+ jobs extracted across 3 pages. Key new finds: Al-Futtaim Senior Financial Analyst (active, 14 alumni), TotalEnergies Financial Analyst Abu Dhabi (3rd UAE role)
- **LinkedIn People:** 10 Dubai FP&A professionals profiled in depth — career paths, qualifications, tools, current employers. Key insight: CA/accounting → Financial Analyst is standard path. CMA appears in real profiles. "Rehab Ahmed" profile mirrors Ashnad's exact career transition.
- **LinkedIn Hiring Posts:** 4 active recruiter posts from past week — people posting jobs in feed (not company boards). 3 recruiter contacts captured with emails: maleek@talentsourceconsults.com, careers@fin-storm.com, nupur@futuretensehr.com
- **LinkedIn Project Posts:** FP&A project showcasers identified. Key insight: AI tools (ChatGPT, Claude, Gemini, Copilot) explicitly listed in Finance Analyst job requirements — Ashnad's automation background is a genuine differentiator.

### New Employers Found (from profiles + posts)
Swiss Arabian Perfumes Group, Sobha Realty, Star Metropolis Clinical Laboratories, Decision Sciences Company, 242 Diamond DMCC, EXL, PwC Middle East, AD Ports Group, Crossing Hurdles

---

## [2026-08-20 Phase 1C — Naukrigulf Scraper + crawl4ai]

### Added
- **2026-08-20 08:30** — scraper/job_scraper.py: crawl4ai-based job scraper wired up and tested. Works for Naukrigulf (133 vacancies in UAE). Documented limitations: Bayt.com (anti-bot blocked), Indeed UAE (anti-bot timeout), LinkedIn (needs auth — use browser automation).
- **2026-08-20 08:30** — scraper/output/naukrigulf_jobs.md: 21 unique jobs extracted from Naukrigulf page 1 — Financial Analyst in UAE query.
- **2026-08-20 08:30** — RESEARCH_Phase1C_LinkedIn_Deep_Research.md: Added Section 11 — Naukrigulf scrape results with full URLs for 8 finance-relevant roles.

### New Employers from Naukrigulf
- **CME Capital** — Lead Financial Analyst, Dubai, 3-6 yrs (capital markets firm, new to universe)
- **Al Kabeer Group** — Financial Planning Analyst (Sales Business Partnering), Dubai, 4-6 yrs (FMCG/food group — strong sector fit given ERP background)
- **YAS PARTNER L.L.C-FZ** — Financial Analyst, Dubai, 5-6 yrs

---

## [2026-08-20 Phase 1C — Continued Deep Research + JD Analysis]

### Added / Updated
- **2026-08-20 11:00** — RESEARCH_Phase1C_LinkedIn_Deep_Research.md: Sections 12-16 added
- **2026-08-20 11:00** — scraper/job_scraper.py: Added js_code parameter to scrape_url(), added scrape_naukrigulf() function with scroll trick, added NAUKRIGULF_PRESETS dict, updated CLI with --naukrigulf and --naukrigulf-all flags
- **2026-08-20 11:00** — 4 additional Naukrigulf keyword scrapes completed (FP&A analyst, planning analyst, commercial analyst, management reporting analyst)
- **2026-08-20 11:00** — Full JD extracted for Chalhoub Group FP&A Associate I (highest priority role)

### Key Research Findings (2026-08-20 11:00)

**New Employers Added to Universe:**
- Chalhoub Group — FP&A Associate I (luxury goods, 2-7 yrs, Zimmermann brand) ⭐ TOP TARGET
- Emirates Global Aluminium (EGA) — Multiple roles including Graduate Trainee (UAE National only)
- dubizzle — Associate Commercial Analyst (tech company, 2 weeks posted)
- LVMH — Senior Finance Controller (7-12 yrs, too senior)
- Aster DM Healthcare — Asst Manager Business Analysis (3-8 yrs)
- Abu Dhabi Ports — Senior Analyst Business Planning (4-6 yrs)
- Jumbo Electronics — Asst Manager General Ledger

**LinkedIn Jobs Additional Pages:**
- Ounass Financial Analyst (Temp), Dubai, Hybrid — accessible temporary role
- TotalEnergies FP&A and Economist, Dubai — second TotalEnergies Dubai role
- dubizzle Associate Commercial Analyst — confirmed active

**Chalhoub Group FP&A Associate I JD Analysis:**
- Zimmermann brand (luxury fashion) under Chalhoub distribution
- 2+ years minimum experience, SAP preferred, Advanced Excel core
- Responsibilities: P&L variance commentary, budgeting, balance sheet recon, board presentation support
- STRONG FIT for Ashnad: ERP migration ↔ SAP, 3+ yrs accounting ↔ 2yr min, portfolio project needed for P&L variance

**Hiring Posts (individual LinkedIn posts, not job boards):**
- Synthify HR Solutions: Financial Analyst at CFD/Forex brokerage — explicitly values trading/markets experience — email: talha.sajjad@synthify.ae
- Hensa Bhatia: Investment Analyst | DIFC | DCF/valuation — email: careers@fin-storm.com

---

## [2026-08-20 Phase 1C — LinkedIn People Research Deep Dive]

### Added
- **2026-08-20 12:00** — RESEARCH_Phase1C_LinkedIn_Deep_Research.md: Sections 17–19 added

### Section 17: LinkedIn People Pages 2–7 (~60 profiles mined)
- 60+ UAE Dubai FP&A professionals profiled from search result list view (Premium not needed for headline data)
- **New employers confirmed:** Dubai Aerospace Enterprise, dubizzle (Bayut), Landmark Group, LIFE Pharmacy, Majid Al Futtaim, Dubai Holding (2 people), Emaar, Commercial Bank of Dubai, Damac Digital, EY Dubai (FP&A Manager exists), Al-Futtaim Real Estate
- **CMA validation:** Muhammad Imaduddin (CMA USA) + Arun Kumar (US CMA in progress) confirm CMA is actively used and visible in UAE FP&A profiles — Ashnad's CMA pursuit is well-positioned
- **Closest mirror profile:** Arun Kumar — "FP&A Analyst · Financial Modeling & Power BI · US CMA (In Progress) · Targeting Finance roles in Dubai/UAE" — near-identical positioning to Ashnad's planned narrative
- **Mohammad Omar Mukhtar:** "Senior Accountant → Finance Analyst · 9+ yrs · ACCA Finalist · SAP" — most similar career path (accountant transitioning with ACCA, SAP = ERP background)

### Section 18: Cross-Profile Skills Frequency (60+ profiles)
- **Qualification frequency (from headlines):** ACCA ~20%, CA (Indian) ~17%, CMA (US) ~10%, CFA ~8%, MBA ~8%, FMVA ~7%
- **Tool frequency (explicit in headlines):** Power BI ~17%, SAP ~8%, Financial Modelling ~13%, Anaplan ~2%, Oracle FCCS ~2%, SQL ~3%, Python ~3%
- **Sector distribution:** Retail/FMCG (Landmark, MAF, Chalhoub), Real Estate (Emaar, Al-Futtaim RE), Conglomerates (Dubai Holding, DAE), Banking (CBD, FAB), Aviation, Industrial (EGA), Healthcare, Energy
- **Career path patterns:** (1) Big 4 audit → FA → FP&A (most common), (2) Accountant → FA → FP&A (Ashnad's path), (3) CA + FMVA cert → FP&A Analyst, (4) MBA Finance → FP&A

### Section 19: Showcaser Research — Final Finding
- **Conclusion: Zero genuine project showcasers in UAE FP&A community.** LinkedIn content search is globally noisy and cannot be geo-filtered.
- What Dubai FP&A people post: thought leadership, certification news, career updates — NOT dashboards, models, or project walkthroughs.
- **Strategic implication:** Anyone posting 2-3 well-documented FP&A portfolio projects on LinkedIn is among a tiny group in the UAE market. First-mover advantage is real.

---

## [2026-08-20 Phase 1C — LinkedIn People Database + Premium Profile Access]

### Added
- **2026-08-20 13:30** — RESEARCH_Phase1C_LinkedIn_People_Database.md: Comprehensive people database covering all 70 profiles from pages 1–7 of "FP&A analyst Dubai" search

### Key Database Contents
- **65+ LinkedIn URLs confirmed** via JavaScript extraction from each search result page
- **5 full Premium profiles extracted** (Parth Khona, Anjali C, Shobhit Gupta, Nijamudheen, Mohammad Omar Mukhtar)
- **Networking priority ranking:** Nandini Vijayan (21 mutual), Muhammad Danish Ali (14 mutual, 33K followers), Rehab Ahmed (14 mutual), Sabith Mohmed (13 mutual), Akhil Wadhwani (8 mutual at Swiss Arabian)
- **Key bridge contacts identified:** Jeff Landers ACA + Zaynah Aboobaker appear as mutual connections for the most profiles — connecting with them unlocks the widest network reach
- **22 confirmed employers with person-level evidence** (Majid Al Futtaim, Dubai Holding, Dubai Aerospace Enterprise, Dubai Airports, Landmark, Swiss Arabian, PwC, EY, etc.)
- **Existing connections reviewed:** current connections are non-FP&A; no insider network yet

### Premium Profile Insights
- **Shobhit Gupta (CA + FMVA):** Used 9-month intentional career break to earn FMVA + build projects → landed Dubai confidential FP&A role (Apr 2025). Direct proof: portfolio + certification → transition works
- **Parth Khona (MAF):** Manages AED 3Bn+ P&L across 10 malls; built Monte Carlo simulation models + Power BI dashboards adopted across the finance team
- **Anjali C (Olam):** EY audit India (2.75 yrs) → UAE accounting role with embedded FP&A; doing budgeting, forecasting, variance analysis inside "Finance Account Officer" title
- **Mohammad Omar Mukhtar (Savills):** 9+ yrs in accounting; SAP + TRAMPS; ACCA Finalist; STILL in accounting-titled role despite FP&A headline — transition NOT yet achieved after 9 years
- **Nijamudheen (Fat Hippo UK):** Real Financial Analyst role (2.3 yrs in UK hospitality); now in Dubai; CMA + CIMA Finalist; Power BI

### Global Showcaser Research — Flagged
- UAE community: zero project showcasers confirmed
- Recommendation added to database: research global finance creators (UK, India, US) to understand how to showcase FP&A projects on LinkedIn; first-mover advantage in UAE market is real

---

## [2026-08-20 Phase 1D — Global Showcaser Analysis]

### Added
- **2026-08-20 14:00** — RESEARCH_Phase1D_Global_Showcaser_Analysis.md: Full analysis of global finance project showcasers

### Key Research Findings

**8 real showcase posts analyzed** from LinkedIn content search (5 queries, past month). Best examples:

1. **Pankaj Kawade** — Driver-based 3-year forecast for Eternal/Zomato, Bear/Base/Bull scenarios, QA'd assumptions vs actual results, found model bugs. Gold standard for FP&A showcase format.
2. **Ben Capobianco** — Real restaurant internship: 95% data collection time reduction, 86% daily forecast accuracy, 24% revenue above historical average. Gold standard for quantified real-impact format.
3. **Kavish Kaul** — Series approach on SJS Enterprises (report → model → dashboard → pitch deck). Key insight: "The report is for the analyst. The dashboard is for the decision-maker."

**Post structure template documented:** Hook → Context → What built → Key findings → Lesson → CTA → Document carousel

**Content type ranking:** Real company + real impact (⭐⭐⭐⭐⭐) > Real listed company + public data (⭐⭐⭐⭐) > Series (⭐⭐⭐⭐) > Simulated case (⭐⭐⭐)

**Portfolio recommendations for Ashnad:**
- Project 1: Budget vs. Actual for a UAE-listed company (Emaar, Air Arabia, Aldar) — core FP&A deliverable
- Project 2: 3-statement model with driver-based 3-year forecast + Bear/Base/Bull (Pankaj Kawade format)
- Project 3: P&L variance analysis with management commentary (Chalhoub JD requirement)
- Project 4: Power BI CFO dashboard combining above

**UAE first-mover advantage confirmed:** Zero UAE FP&A showcasers found. 3–4 well-executed project posts = most visible finance portfolio in the UAE market.

---

## [2026-08-20 Phase 1D — Skills Matrix + Deliverable Updates — PHASE 1 CLOSED]

### Added
- **2026-08-20 15:00** — RESEARCH_Phase1D_Skills_Matrix.md: Complete UAE/Dubai FP&A skills frequency matrix. Synthesizes all 100+ job postings, 70 professional profiles, and full JD analysis into 8 sections: responsibilities, tools, qualifications, experience requirements, sector distribution, salary benchmarks, priority matrix, and key conclusions.

### Updated
- **2026-08-20 15:30** — RESEARCH_Deliverable2_Skill_Gap_Analysis.md: Added Phase 1C/1D Update section. Key updates: Power BI confirmed at 62% (higher than original estimate); CMA more relevant than originally stated (~10% of profiles vs. ~5% estimated); FMVA added as viable option (Shobhit Gupta precedent); Chalhoub JD confirms M.Sc. + portfolio = sufficient for FP&A Associate without ACCA; revised qualification table.
- **2026-08-20 15:30** — RESEARCH_Deliverable3_Career_Target_Ranking.md: Added Phase 1C/1D Update section. Key updates: Chalhoub Group FP&A Associate I confirmed STRONG FIT (full JD analyzed); 9 new confirmed employers from people research (Dubai Holding, DAE, Landmark Group, Swiss Arabian, Al Douri Group, etc.); sector concentration data updated (Retail/FMCG 26%); salary ranges updated with Naukrigulf + Indeed data.
- **2026-08-20 15:30** — RESEARCH_Deliverable4_Portfolio_Roadmap.md: Added Phase 1C/1D Update section. Key updates: global showcaser gold standards documented (Pankaj Kawade format, Ben Capobianco format); UAE-listed company data recommendation (Emaar, Air Arabia, Aldar); 3-post-per-project LinkedIn cadence (post → finding → lesson); post structure template added; unique automation framing angle documented.
- **2026-08-20 15:30** — PENDING.md: Phase 1 research decisions cleared as answered; Career Brand decisions updated.

### Phase 1 Closure Summary

**Phase 1 (Job Market Research) is complete as of 2026-08-20.**

Research scope achieved:
- 100+ real UAE/Dubai job postings analyzed (LinkedIn, Indeed, Naukrigulf, Bayt, direct JDs)
- 22 confirmed employers with person-level evidence
- 70 professional profiles reviewed (career paths, qualifications, tools)
- 6 research deliverables written and updated
- 1 Skills Matrix synthesizing all findings
- 1 People Database (networking intelligence, 70 profiles, mutual connections mapped)
- 1 Global Showcaser Analysis (gold-standard post formats documented)

All 6 Phase 1 research questions in CLAUDE.md have been answered with data-backed conclusions. Phase 2 (portfolio projects) begins next.

**Critical findings Phase 1 established:**
1. Excel → Power BI (62%) → cash flow is the correct skill build sequence
2. 50% of UAE FP&A market is accessible today with no portfolio
3. Chalhoub Group FP&A Associate I = confirmed STRONG FIT, apply first with Project 1
4. UAE LinkedIn FP&A community does zero project showcasing — first-mover advantage is real
5. M.Sc. Financial Economics + CMA (in progress) is sufficient qualification; no new certs needed before Oct 2026

---

## Format Notes

- **Timestamped entries:** `YYYY-MM-DD HH:MM` in +04 timezone
- **Categories:** Added, Updated, Fixed, Removed, Changed
- **Always commit + push:** No staging, continuous integration
- **State tracking:** Open items go to PENDING.md (timestamped, cleared when done)
