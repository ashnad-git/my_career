# Daily Log — Career Transition Progress

**Owner:** Claude fills this in. Ashnad just answers questions.  
**When:** End of every session (Claude Q&As Ashnad) + catch-up at start of next session for any days in between.  
**Rule:** If it's not logged here, Claude treats it as not done.

---

## HOW IT WORKS

**End of every session — Claude asks:**
1. "Which jobs did you apply to today / since we last spoke?"
2. "Did you send any connection requests? Who?"
3. "Did you engage with any posts or share anything?"
4. "What learning did you do outside our sessions?"
5. "Any responses, calls, or messages from jobs or connections?"
6. "Anything blocking you or on your mind?"

Claude writes the answers into a log entry below. Ashnad never writes anything in this file.

**Start of every session — Claude reads the latest entries** and if days have passed since the last session, asks the catch-up questions first before anything else.

---

## PROGRESS SCOREBOARD
*(Claude updates this every session)*

| Metric | This Week | Total | Target/Week |
|---|---|---|---|
| Applications sent | 3 | 16 | 5–8 |
| Interviews booked | 0 | 0 | — |
| Connection requests sent | 0 (notes ready, Ashnad sends) | 7 | 10–14 |
| LinkedIn posts/comments | 3 | 3 | 5+ |
| Learning hours logged | 0 | 14 | 5–7 hrs |
| Days with full checklist | 0 | 0 | 7/7 |
| JDs saved in archive | — | 117 | — |

---

## LOG ENTRIES

*(Claude writes all entries. Most recent at top.)*

---

### 2026-08-25 | Session 19: Job Applications (3) + Script Refactor

**Session type:** Applications + infrastructure refactor
**Jobs applied:** 3
- ABDULLA ALARIF HOLDING — Strategy Analyst (Indeed Easy Apply, master PDF, STRETCH)
- ITP Media Group — Assistant Management Accountant (Indeed Easy Apply, tailored PDF, STRONG FIT)
- NEP Singapore — Commercial Finance Analyst (Indeed portal, tailored PDF, STRONG FIT)
- Greenbull — NOT applied. French fluency required, discovered on application page (not in JD preview)
**Connections sent:** Not done this session
**LinkedIn activity:** None
**Learning outside session:** Not asked
**Responses received:** None
**Session work:**
- Built NEP tailored resume from content prepared previous session; ran /hr-audit (66/100); applied 3 fixes (media sector framing, 475 accounts bullet, CEO presentation language); rebuilt PDF; applied
- Refactored build_resume_pdf.py: 1364 lines → 62-line dispatcher + scripts/resume_utils.py (157 lines) + 10 individual files in scripts/resumes/. All 10 builds verified. New resumes now cost ~100 lines per file; main dispatcher never grows
- JOB_PIPELINE.md updated: row 16 added (NEP)
**Blockers/notes:**
- 3 recruiter emails still unsent (Brian Casey / Cooper Fitch, Darius Dosieah / Robert Walters, Morgan Tull / Hays UAE) — now 4+ sessions overdue
- 19 LinkedIn connection notes ready to send (Ashnad sends)
- Remaining STRONG FIT queue: Bayt Associate Commercial Analyst x2 (Property Finder/BT-74868496/BT-74866070), zcreatix Junior Finance Analyst, Confidential Junior Process Performance Analyst (NG jid-130826000672)
- GOOD FIT batch not started (Black Pearl, Michael Page, Fresha, Rapyd, Taptap Send, Abbott, Al Tayer Retail Finance etc.)
- Phase 2B model paused for applications — resume next session (COGS tab)

---

### 2026-08-25 | Session 18: LinkedIn JD Extraction + Connections Batch

**Session type:** JD extraction (LinkedIn voyager API) + STRETCH job audit + connections batch
**Jobs applied:** 0 — Ashnad handles all submissions. ABDULLA ALARIF Indeed draft still saved (not submitted).
**Connections sent:** 0 this session — 19 Finance Director/CFO targets identified, notes written in NETWORKING.md (#20–38). Ashnad sends.
**LinkedIn activity:** None
**Learning outside session:** Not asked — applying-focused session
**Responses received:** None new logged
**Blockers/notes:**
- ABDULLA ALARIF: Indeed draft saved, user to submit when ready
- 3 recruiter emails (Brian Casey, Darius Dosieah, Morgan Tull): still NOT SENT — deferred two sessions running
- 44+ STRONG/GOOD FIT jobs in pipeline awaiting applications — NEXT SESSION priority
- No Phase 2B model work this session (job admin took full session)
**Claude notes:** 7 new JD files saved (Emarat STRETCH, Shiseido GOOD FIT, Fitch NOT SUITABLE, ENGIE STRETCH, Eaton STRETCH, EKFC NOT SUITABLE, AKI STRETCH bonus). GymNation/Sharaf DG/Marsh McLennan confirmed expired. 19 senior connections added to NETWORKING.md with invite notes — all 2nd-degree Finance Directors/CFOs/Heads of FP&A. Total JD archive: 117 files.

---

### 2026-08-25 | Session 17: Bulk Job Search — 82 New JDs

**Session type:** Bulk job search across 5 platforms (Indeed, Bayt, Naukrigulf, GulfTalent, browser viewjob fetches)
**Jobs applied:** None this session — pure research/collection
**Connections sent:** 0 — not started (carry to next session)
**LinkedIn activity:** None
**Learning outside session:** Not confirmed — carry to next session log
**Responses received:** Not confirmed — carry to next session log
**Blockers/notes:**
- ABDULLA ALARIF still not applied — now 3 sessions overdue. Apply FIRST next session.
- 14 LinkedIn JDs still pending extraction from browser
- 20 LinkedIn connections not started (CFOs/Finance Directors/FP&A Managers)
- 3 recruiter emails (Brian Casey/Cooper Fitch, Darius Dosieah/Robert Walters, Morgan Tull/Hays) not sent — drafted 2026-08-23
- 44 new STRONG/GOOD FIT jobs identified — none applied yet; ready to go next session
**Claude notes:** Established python-jobspy as permanent Indeed scraper (free, 20 keyword queries → 120+ jobs in 3 mins, full JD text). Total JD archive: 110 files (28 pre-existing + 82 new today). Top STRONG FIT from today: ITP Media Group (Asst Mgmt Accountant), Greenbull Junior FA (AED 15–18k), NEP Commercial Finance Analyst, Associate Commercial Analyst x2 (Bayt). JOB_PIPELINE.md updated rows 19–63.

---

### 2026-08-25 | Session 16: Networking Catch-up + Phase 2B Start

**Session type:** Networking backlog + Phase 2B kickoff
**Jobs applied:** None. ABDULLA ALARIF still outstanding — must apply next session.
**Connections sent:** None
**LinkedIn activity:** 3 replies sent —
- Shobhit Gupta: acknowledged CA credential gap, asked whether M.Sc. + CMA gets past FP&A screening in practice
- Theodore Bros: asked whether posting portfolio projects on LinkedIn gets traction with recruiters vs building network in person
- Nadiya Simran: closed the conversation politely (she's job-hunting herself, not an FP&A source)
**Recruiter activity:** Maleek (Talent Source Consults) replied with screening questions. Replied with: work environment (in-office/hybrid, structured FP&A team), deal-breakers (6-day week, below AED 5k), salary range (AED 5,000–7,000). Likely linked to Naukrigulf Confidential Junior FA role.
**Bounced emails:** morgan.tull@hays.com and brian.casey@cooperfitch.ae both returned address-not-found. Correct addresses still needed.
**Learning outside session:** None
**Responses received:** Shobhit Gupta, Theodore Bros, Nadiya Simran (all handled above). Maleek recruiter email received and replied.
**Blockers/notes:** ABDULLA ALARIF not applied. 5 LinkedIn comments still pending. Brian Casey + Morgan Tull correct email addresses still needed. Naukrigulf Confidential JD + Mark Williams JD + Alghanim JD still unfetched.
**Claude notes:** Networking backlog cleared at start of session. Phase 2B: 08_fpa_model.xlsx generated (9 tabs, Assumptions tab structured with all inputs). Revenue Build tab built from scratch — INDEX seasonality formula taught and applied, units × seasonality × ASP pattern built across 3 outlets × 4 categories × 12 months. Mixed-row summing error caught and fixed by Ashnad. Grand total AED 22.6M. CHECKPOINT 2B-1 called and passed. ~3 hrs learning. Committed and pushed.

---

### 2026-08-24 | Session 15: CF Complete + CHECKPOINT 2A-4 — Phase 2A Done

**Session type:** Learning — Conditional Formatting + Day 14 Sign-off Check
**Jobs applied:** None (catch-up Q&A deferred — second session in a row)
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** Not asked — Q&A deferred
**Responses received:** 2 LinkedIn responses still not reviewed — deferred again
**Blockers/notes:** 5 comments, ABDULLA ALARIF, 3 unsent recruiter emails, 2 LinkedIn responses all carried forward. Must address next session.
**Claude notes:** All 4 CF tasks done. $ anchor concept for custom formula rules understood — correctly identified the key question on named range auto-expand without prompting. Day 14 Sign-off passed — 6/6. CHECKPOINT 2A-4 called and passed. Phase 2A complete. ~1.5 hrs learning.

---

### 2026-08-24 | Session 14: Modeling Best Practices + Textbook + CF Intro

**Session type:** Learning — Modeling Structure + Conditional Formatting intro
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** 2 LinkedIn responses still not reviewed — deferred again to next session
**Blockers/notes:** 5 LinkedIn comments still pending. ABDULLA ALARIF still not applied. 2 LinkedIn responses not reviewed (Ashnad will paste in next session).
**Claude notes:** EXCEL_TEXTBOOK.md created (7 chapters). Hard rules added: always generate practice files, update textbook every session. 04_index_match_practice.xlsx generated retroactively. Day 8-9 Modeling complete — 3-tab skeleton built + tested. Day 10-11 CF intro done, Task 1 deferred. ~2 hrs learning.

---

### 2026-08-23 | Session 13: Charts Day 6 — CHECKPOINT 2A-3 Fully Passed

**Session type:** Learning — Excel Charts
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** 2 LinkedIn responses received during session — not yet reviewed (carry to next session)
**Blockers/notes:** 5 LinkedIn comments still pending. ABDULLA ALARIF still not applied.
**Claude notes:** Built Column chart (Budget vs Actual by outlet — 3 series, formatted: no gridlines, comma labels, grey Budget / dark blue Actual). Built Waterfall chart (Variance Bridge: Budget → Dubai Mall +70k → Marina Mall -40k → Online +30k → Actual — "Set as Total" concept taught). CHECKPOINT 2A-3 fully called and passed — all 5 criteria met (Pivot Tables, date grouping, calculated field, column chart, waterfall chart, all formatted). CLAUDE.md updated. 2 LinkedIn responses received but not reviewed — carry to next session. ~1.5 hrs learning.

---

### 2026-08-23 | Session 12: Pivot Tables Day 5 — CHECKPOINT 2A-3 Partially Passed

**Session type:** Learning — Pivot Tables
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None
**Blockers/notes:** Charts still pending to complete CHECKPOINT 2A-3.
**Claude notes:** Built Pivot Table (Revenue by Outlet) from scratch without guidance. Slicers: inserted Category slicer, filtered to 2 outlets, read correct total (301,110). Date grouping: manually grouped by Quarter + Month via right-click → Group. Calculated field: Gross Margin % = (Revenue - COGS) / Revenue — built without guidance, formatted as %. Final build: full PT (Quarters/Months rows, Outlet columns, Revenue + GM%, Category slicer) rebuilt from scratch — all correct. CHECKPOINT 2A-3 partially called — Pivot Tables complete, charts still pending. ~1.5 hrs learning.

---

### 2026-08-23 | Session 10: Power Query Day 3

**Session type:** Learning — Power Query
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None
**Blockers/notes:** Clean session. 4 recruiter emails + 5 LinkedIn comments + ABDULLA ALARIF still pending — carry to next session.
**Claude notes:** CHECKPOINT 2A-2 passed. Power Query full workflow completed from scratch: connect CSV → promote headers → filter junk rows → remove columns → rename → unpivot → load. Key lesson: never open source CSVs in Excel. Next: Pivot Tables Day 5.

---

### 2026-08-23 | Session 9: Applications + LinkedIn Skills + Networking

**Session type:** Applications + LinkedIn skills update + networking
**Jobs applied:** Khazna Data Centers #11 (LinkedIn Easy Apply, STRETCH, master PDF), AD Ports Group #12 (Oracle HCM portal, STRETCH, master PDF — Ashnad completed form), Al Tayer Group #13 (Oracle HCM portal, GOOD FIT, tailored PDF + cover letter built and sent). Total: 13 applied.
**Connections sent:** 7 — Théodore Bros (TotalEnergies), Nadiya Simran (LIVBNB), Devika Menon (Dubai Aerospace), Shraddha Chichani (Ex-Landmark), Anil Kumar CFA, CA Hardik Patel (Diamond DMCC), CA Adrian Machado (Sobha / Ex-KPMG). All with personalised notes.
**LinkedIn activity:** Skills updated — ADDED: FP&A, SQL, Power BI, Budgeting, Forecasting, Variance Analysis. REMOVED: Equity Trading, Private Equity. Python + Financial Modeling already on profile.
**Learning outside session:** None
**Responses received:** None from any of the 13 jobs applied.
**Blockers/notes:** 5 LinkedIn comments still pending. 4 recruiter emails not yet sent. ABDULLA ALARIF HOLDING (STRETCH) not yet applied. Power Query Day 3 not done.
**Claude notes:** Chrome browser issue resolved (Mac local browser selected). Al Tayer cover letter template added to build script (altayer_cl key). NETWORKING.md created — tracks all 7 connections with profile links, invite notes, and conversation strategy. Next session: check for connection responses, send 4 recruiter emails, 5 comments, ABDULLA ALARIF, then Power Query Day 3.

---

### 2026-08-23 | Session 8: Applications + LinkedIn Profile Overhaul

**Session type:** Applications + LinkedIn profile update
**Jobs applied:** TotalEnergies (portal, STRETCH), Huda Beauty (Easy Apply, STRETCH), Mohamed Hilal Group (Easy Apply, STRETCH). Sundus: CLOSED.
**Connections sent:** None
**LinkedIn activity:** Full profile overhaul completed — About section, all 4 work experience descriptions, skills per experience, all 4 project descriptions reframed (done manually by Ashnad).
**Learning outside session:** None
**Responses received:** None from any of the 9 jobs applied so far.
**Blockers/notes:** LinkedIn skills section not yet updated — must do first next session (ADD: FP&A, Python, SQL, Power BI, Financial Modeling, Budgeting, Forecasting, Variance Analysis | REMOVE: Equity Trading, Private Equity). 5 applications still pending — Khazna + AD Ports have Aug 28 deadline.
**Claude notes:** Browser automation for LinkedIn was unreliable this session — project edits done manually by Ashnad. Next session: review project descriptions first, then skills update, then applications, then Power Query Day 3.

---

### 2026-08-21 to 2026-08-23 | Catch-up (2-day gap)

**Jobs applied independently:** None
**Connections sent:** None
**LinkedIn activity:** None (LinkedIn profile overhaul done in today's session)
**Learning outside session:** None
**Responses received:** None
**Blockers/notes:** Clean gap — no slippage to note.

---

### 2026-08-21 | Day 1 — Session 7: Excel Day 2 (End of Session)

**Session type:** Excel learning
**Jobs applied:** None — 9 applications postponed to next session (Excel done, ran out of time for applications today)
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None from any of the 6 jobs applied 2026-08-20
**Blockers/notes:** 9 applications still pending — TotalEnergies + Huda Beauty have Aug 25 deadline (4 days). Must do first next session.
**Claude notes:** SUMIFS review 6/6 correct. VLOOKUP all 5 exercises correct (FALSE habit confirmed). INDEX-MATCH taught, written correctly, left-lookup demonstrated. IFERROR wrapped correctly. Checkpoint 2A-1 called and passed — all 4 formula criteria met. Next: Power Query (Day 3).

---

### 2026-08-21 | Day 1 — Session Start: Catch-up Q&A

**Session type:** Catch-up (overnight since last session)
**Jobs applied independently:** None
**Connections sent:** None
**LinkedIn activity:** None (planned for today's session)
**Learning outside session:** None
**Responses received:** Generic auto-acknowledgement emails from applied companies (no interview requests)
**Blockers/notes:** LinkedIn "About" section still not updated — to complete today. All 5 queued applications (TotalEnergies, Huda Beauty, Sundus, Mohamed Hilal, Khazna) still pending — proceeding now in deadline order.
**Claude notes:** Clean overnight. No slippage. Proceeding to full session plan.

---

### 2026-08-20 | Day 0 — Session 4: JD Archive + Pipeline Applications

**Session type:** Catch-up + JD archiving + pipeline applications
**Catch-up period:** Since Session 3 (same day)
**Jobs applied independently:** None
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None
**Blockers/notes:** 8 pipeline JDs not yet saved to jds/. NAFFCO deadline Aug 22. LinkedIn headline still shows "Aspiring Financial Analyst" — needs updating.
**Claude notes:** Session opened with accountability correction — multiple protocol items missed in Session 3 (end-of-session Q&A not done, DAILY_LOG missing GBM application, SESSION LOG and APPLICATION LOG not updated in PHASE2_MASTER_PLAN). All gaps fixed. Catch-up Q&A completed. Now proceeding to fetch all 8 pipeline JDs and apply to NAFFCO (Aug 22 deadline).

---

### 2026-08-20 | Day 0 — Session 5: Applications (x4 more = 6 total today)

**Session type:** Applications + resume tailoring
**Jobs applied:**
3. NAFFCO — FP&A Analyst | TeamTailor portal | tailored PDF (58→65+ after 5 audit fixes)
4. Al Khayyat Investments (AKI) — Finance Analyst FP&A | LinkedIn Easy Apply | master PDF | STRETCH
5. Eaton — FP&A Analyst (Manufacturing Finance) | Eightfold portal | master PDF | STRETCH (SAP must-have gap; applied anyway per Ashnad's call)
6. dubizzle (Bayut) — Associate Commercial Analyst | Workable portal | tailored PDF 72/100 | GOOD FIT
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None
**Learning this session:** SUMIFS formula — 4 practice questions (all correct including written from memory: =SUMIFS(C2:C10,B2:B10,"Sales",A2:A10,"Feb")). ~30 min. Checkpoint 2A-1 criteria: SUMIFS ✅. Next: VLOOKUP.
**Blockers/notes:**
- LinkedIn "About" section still not updated (headline ✅ done)
- 5 remaining STRETCH applications due tomorrow (TotalEnergies Aug 25, Huda Beauty Aug 25, Sundus Aug 26, Mohamed Hilal Aug 26, Khazna Aug 28)
**Claude notes:** 3 process failures caught and corrected: (1) NAFFCO form handed off without tailored resume, (2) PDF sent without hr-audit, (3) audit findings not implemented before SendUserFile. Mandatory checklist added to CLAUDE.md. Contact number updated to 543255352 across all files. NAFFCO: 5 audit fixes (summary reframe, AP/AR → data consolidation, cash flow reframe, EY filing bullet removed, projects reframed). dubizzle: commercial analytics angle, Python/SQL/Power BI leading, deep-dive analysis + dashboard JD language embedded.

---

### 2026-08-20 | Day 0 — Session 3: First Applications (x2)

**Session type:** Application + resume tailoring
**Jobs applied:**
1. Chalhoub Group — FP&A Associate I (Zimmermann) via LinkedIn Easy Apply (tailored resume 74/100, cover letter)
2. GBM — Financial Analyst via LinkedIn Easy Apply (STRETCH — applied standard CV after JD confirmed 5yr requirement + 200+ applicants)
**Connections sent:** None
**LinkedIn activity:** None
**Learning outside session:** None
**Responses received:** None
**Blockers/notes:** LinkedIn profile still not updated — headline says "Aspiring Financial Analyst". NAFFCO deadline Aug 22 = next urgent application.
**Claude notes:** Tailored resume built for Chalhoub (74/100 on hr-audit, up from 58). Two audit rounds. Cover letter rewritten from AI-sounding to natural human voice after Ashnad flagged it. PDF built via reportlab (matching master resume style). Process documented in CLAUDE.md + scripts/build_resume_pdf.py. JD archive process established — both JDs saved to jds/. ACCA clarified — only appears in files as market research data, not as Ashnad's qualification. CMA is the only qualification being pursued.

---

### 2026-08-20 | Day 0 — Session 2: Resume Build

**Session type:** Resume + setup  
**Jobs applied:** None  
**Connections sent:** None  
**LinkedIn activity:** None  
**Learning outside session:** None  
**Responses received:** None  
**Blockers/notes:** Full session spent building master resume. No applications or networking done yet. Chalhoub application is the most urgent task — it was posted 2 days ago.  
**Claude notes:** Master resume completed (PDF + MD). Key decisions made: (1) LinkedIn URL confirmed as linkedin.com/in/muhammed-ashnad-k. (2) No company financials on resume — they are private/confidential. (3) Promotech bullets reframed to lead with what was BUILT, not what was broken — avoids criticizing employer in writing. (4) EY experience restored to full 5 bullets. (5) Education and Certifications given proper section formatting. (6) /hr-audit skill created. (7) resumes/ directory created for tailored versions. Resume concerns were raised by Ashnad but session ended before all were resolved — must address at start of next session.

---

### 2026-08-20 | Day 0 — Infrastructure Setup

**Session type:** Setup  
**Jobs applied:** None — pipeline built today for the first time  
**New jobs found:** 10 roles added to JOB_PIPELINE.md (Batch 1). Top priority: Chalhoub Group FP&A Associate I (Zimmermann), posted 1 day ago — Ashnad to apply tonight.  
**Networking:** None — daily system just created today  
**Learning:** None — Phase 2A starts next session  
**Responses received:** None  
**Blockers:** None  
**Claude notes:** Full Phase 2 infrastructure built today. PHASE2_MASTER_PLAN.md, JOB_PIPELINE.md, DAILY_CHECKLIST.md, DAILY_LOG.md, checkpoint system, session prompts all in place. Audit identified 7 gaps — resume and LinkedIn profile are the most urgent (blocking current applications). Resume reframe and LinkedIn profile update to be done before or alongside Week 1 Excel learning.

---

### 2026-08-23 | Session 13 — Charts Day 6 + CHECKPOINT 2A-3 Complete

**Session type:** Learning (Charts)
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None — 5 comments still pending
**Learning outside session:** None
**Responses received:** 2 LinkedIn messages received — not yet reviewed, carry to next session
**Blockers/notes:** 5 LinkedIn comments still pending. ABDULLA ALARIF still not applied. 2 LinkedIn responses to review.
**Claude notes:** Column chart (Budget vs Actual, 3 outlets) built and formatted. Waterfall chart (Variance Bridge: Budget → Actual through outlet variances) built and formatted. Key concept taught: "Set as Total" for anchor bars vs chain bars. CHECKPOINT 2A-3 fully passed — all 5 criteria met. CLAUDE.md Files table updated. Process discipline saved as hard rule. Next: Day 8-9 Modeling Best Practices.

---

### 2026-08-23 | Session 12 — Pivot Tables Day 5 + Networking Updates

**Session type:** Learning (Pivot Tables) + Networking
**Jobs applied:** None
**Connections sent:** None
**LinkedIn activity:** None — 5 comments still pending
**Learning outside session:** None
**Responses received:** Théodore Bros (second reply — key intel on Dubai networking strategy), Nadiya Simran (second reply — wants to go back to financial services, not FP&A source), Shobhit Gupta (first reply — asked about current role), CA Tony Thomas (accepted connection)
**Blockers/notes:** 5 LinkedIn comments still pending. ABDULLA ALARIF still not applied. No job responses yet.
**Claude notes:** Pivot Tables Day 5 complete. Skills covered: basic PT, date grouping (month/quarter), slicers, calculated field (Gross Margin %). CHECKPOINT 2A-3 partially passed — charts (bar + waterfall) still pending for Day 6-7. Networking: Théodore gave major strategy intel (connect up to CFOs not analysts, LinkedIn toward controlling, attend events). Shobhit is highest-value connection — honest reply sent about accounting ops reality. Nadiya is peer in opposite direction, not FP&A source. Tony Thomas first message sent.

---

### 2026-08-23 | Session 11 — Recruiter Outreach + LinkedIn Networking

**Session type:** Recruiter cold emails + LinkedIn connection batch + first messages
**Jobs applied:** None
**Connections sent:** 12 (batch 2 FP&A professionals via LinkedIn invite — Nandini Vijayan, Muhammad Danish Ali, Sabith Mohmed, Mudasir Aslam, Haider Javed, Subodh Lamichhane, Shobhit Gupta, Anjali C, Ayush Sitani, CA Tony Thomas)
**LinkedIn activity:**
- 7 recruiter cold emails revised to humanized style and sent (Talha Khandelwal, Hensa Bhatia, Nupur Sinha, Maleek Fajoyomi — sent; Brian Casey/Cooper Fitch, Darius Dosieah/Robert Walters, Morgan Tull/Hays — new contacts added and emailed)
- First messages sent to Jeff Landers and Zaynah Aboobaker (existing connections, bridge outreach)
- Théodore Bros (TotalEnergies FA) accepted connection → first message sent
- Nadiya Simran (LIVBNB FA) replied to invite note → response drafted and sent
- Anil Kumar (FP&A Dubai) accepted connection → first message sent (no invite note had been sent with the request)
**Learning outside session:** None
**Responses received:** Théodore Bros (accepted, no reply to note), Nadiya Simran (replied — pricing/commercial decisions point + Dubai move context), Anil Kumar (accepted)
**Blockers/notes:**
- Emails 1-4 (Talha, Hensa, Nupur, Maleek) were scheduled for Monday AM — user needs to update those drafts in email client to the revised humanized versions before they send
- Nadiya conversation ongoing — next move is to wait for her reply
- Nadiya conversation ongoing — next move is to wait for her reply to the response sent today
**Claude notes:** All 7 recruiter emails rewritten to human voice after Ashnad flagged AI patterns (em dashes, credential-first openers, structured headers). Humanized writing hard rule saved to memory and feedback file. NETWORKING.md batch-2 status update (Python script fix) applied — all 10 entries now 🟡 PENDING with date 2026-08-23. Portfolio domain plan (ashnad.finance or similar) added to PENDING.md — implement after Phase 2B/2C projects ready.

---

*(New entries go above this line)*

## 2026-08-28 (Fri)
**Mega-harvest session.** Claude built an automated job-harvest pipeline and ran a full multi-source sweep.
- Jobs found today (apply-ready, after rejections): **315** (target was 200). Archive now 432 JDs.
- LinkedIn connection targets built: **201** (senior finance + HR/TA), with draft notes → NETWORKING.md.
- Cold-email contacts harvested: **100** real recruiter/HR emails → COLD_EMAILS.md.
- Next action for Ashnad: start sending connection invites (~20/day) and cold emails in batches; apply to STRONG/GOOD roles.
