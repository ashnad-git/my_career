# my_career — Claude Session Context

This file documents the collaboration model, conventions, and context for working on the my_career project.

---

## Project Purpose

`my_career` is a personal career repository that tracks a **strategic transition from accounting operations into Financial Analyst / FP&A / Finance Analytics roles.**

**Core Strategy:**
1. **Research actual job market** — analyze 100+ real UAE/Dubai job postings to identify what employers actually want
2. **Build targeted portfolio projects** — create 5–8 excellent projects demonstrating those specific capabilities
3. **Leverage existing strengths** — use accounting foundation + technical/automation skills + independent projects to differentiate candidacy
4. **Transition to analytical finance** — move from accounting-operations title into higher-value analytical/systems finance roles

**Key Distinction:** 
- Ultimate Trading Terminal project is **evidence of technical capability** (automation, systems thinking, data pipelines), not the career end goal
- Goal is to use that capability to strengthen candidacy for Finance/FP&A roles

**Distinct from:** Ultimate Trading Terminal (product/research repo). This is the **career transition and job market strategy** repo.

---

## Conventions (Matching Ultimate Trading Terminal)

1. **Commit + push at every clean milestone** — no staging, continuous integration
2. **Timestamped entries** — `YYYY-MM-DD HH:MM` in +04 timezone
3. **State tracking** — CHANGELOG.md (what's done) + PENDING.md (what's open, prioritized)
4. **Clear specs** — research methodology explicit, success criteria defined
5. **Main branch only** — immediate push, no feature branches
6. **Documentation-first** — big-picture strategy documented before implementation

---

## Job Description Archive

**Every JD must be saved immediately after fetching it — no exceptions.**

### Location
`jds/` directory — one file per job, named `CompanyName_RoleTitle_YYYY-MM-DD.md`

### File contents (required fields)
- Date found, LinkedIn job ID, URL, status, fit rating
- **Full responsibilities — copy verbatim, every bullet, every line. No paraphrasing. No omissions.**
- **Full requirements — copy verbatim: experience, education, certifications, technical skills, every line.**
- **Portfolio Relevance section** — map each JD requirement to the relevant portfolio project (only section Claude writes, not copies)

### HARD RULE: JD content must be verbatim
The responsibilities and requirements sections must be copied exactly as written in the job posting — not summarised, not paraphrased, not selectively pulled. The exact language is what matters for keyword matching in resume tailoring, hr-audit, and skills frequency analysis. A summarised JD corrupts all downstream work. This has been corrected multiple times — it will not happen again.

### When to save
- Immediately after fetching a JD — same session, before moving on
- Every job seen in sidebars, search results, or recommended jobs — if a URL is visible, save it
- Every job that appears in any browser page during a session — even if not applying, even if too senior
- Even for STRETCH / NOT SUITABLE / rejected roles — skill frequency and employer data is still valuable
- Jobs seen but not yet opened: save the URL + title + company at minimum in JOB_PIPELINE.md

### Hard rule: If you can see a URL, save the job
Any job title + URL that appears anywhere during browsing goes into jds/ (if opened) or JOB_PIPELINE.md (if only seen in sidebar/results). No exceptions. A job seen and not saved is lost intelligence.

### Why
JDs are the primary input for portfolio project design and skills matrix validation. Every job seen — regardless of fit — adds data. If a skill appears repeatedly across 30+ JDs, it validates what to build next. The portfolio roadmap is only as good as the JD data behind it.

---

## Application Process — Mandatory Checklist

**Every application follows this exact sequence. No steps may be skipped or reordered.**

### For GOOD FIT roles (non-Easy Apply portal: TeamTailor, company career site, etc.)

```
Step 1  Save JD to jds/CompanyName_Role_Date.md immediately on finding it
Step 2  Rate fit (STRONG / GOOD / STRETCH / NOT SUITABLE)
Step 3  Run /hr-audit: master resume vs JD → identify tailoring gaps
Step 4  Write tailored content in resumes/<Company>_<Role>.md
Step 5  Add build_<key>() function to scripts/build_resume_pdf.py
Step 6  Build PDF: python3 scripts/build_resume_pdf.py <key>
Step 7  Run /hr-audit: tailored resume vs JD → verify fixes addressed gaps
Step 8  Implement audit fixes → rebuild PDF
Step 9  SendUserFile → PDF to Ashnad for review
Step 10 Provide handoff: what to fill, what to answer, which file to upload
Step 11 After Ashnad confirms submission → update JOB_PIPELINE.md to Applied
Step 12 Commit + push
```

### For GOOD FIT roles (Easy Apply)

```
Step 1  Save JD to jds/ immediately
Step 2  Run /hr-audit quick check on master resume
Step 3  If master is adequate → Easy Apply using master PDF
        If significant gaps → build tailored version (Steps 4–9 above), then Easy Apply
Step 4  Update JOB_PIPELINE.md to Applied
Step 5  Commit + push
```

### For STRETCH roles (Easy Apply only — no tailored resume)

```
Step 1  Save JD to jds/ immediately
Step 2  Easy Apply using master resume PDF
Step 3  Update JOB_PIPELINE.md to Applied
Step 4  Commit + push
```

**Hard rules:**
- NEVER hand off an application form without having sent the tailored PDF first
- NEVER send a PDF without having run /hr-audit on it first
- NEVER submit Easy Apply without master PDF confirmed in repo
- If a step is skipped, stop and go back — never proceed forward

---

## Resume PDF Generation

**ALWAYS use reportlab. Never use Chrome headless, pandoc, or HTML conversion.**

### Command
```bash
python3 scripts/build_resume_pdf.py <key>
```

| Key | Output file | Purpose |
|---|---|---|
| `master` | `Muhammed_Ashnad_Resume.pdf` | Master resume — broad FP&A/Finance positioning |
| `chalhoub` | `resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf` | Tailored for Chalhoub FP&A Associate I |

### To add a new tailored resume
1. Build content in `resumes/<Company>_<Role>.md`
2. Add a `build_<key>()` function in `scripts/build_resume_pdf.py`
3. Add the key to the `RESUMES` dict at the bottom of the script
4. Run `python3 scripts/build_resume_pdf.py <key>`
5. Send the PDF to Ashnad for review before submitting

### Style reference (do not deviate)
- Font: Helvetica throughout
- Name: bold 20pt, colour `#1e3a5f` (dark blue)
- Section headers: bold 8.5pt, colour `#1e3a5f`, underlined with 0.4pt rule
- Bullets: 8.5pt, 10pt left indent, hanging indent
- Margins: left/right 17mm, top/bottom 14mm
- Page size: A4, single column, all text selectable (ATS-safe)

---

## Files & Their Purpose

| File | Purpose |
|---|---|
| **USER_PROFILE.md** | Comprehensive, evolving profile: role, competencies, work patterns, values, collaboration model. Updated as you provide new context. |
| **Muhammed_Ashnad_Resume.md** | Current resume (accounting operations focus). Needs reframing to align with actual capabilities. |
| **Ashnad_Career_Transition_Brief_for_Claude_Cowork.md** | Career transition context document (existing). To be integrated/updated. |
| **CHANGELOG.md** | Timestamped log of all changes (what was done, when). Never delete entries. |
| **PENDING.md** | Open items, decisions pending, backlog. Clear as items complete. |
| **CLAUDE.md** | This file — session context, conventions, collaboration patterns. |

---

## Collaboration Model

### Phase 1: Job Market Research (Current Phase)

**Your Role:**
- Review research findings and validate against your understanding
- Provide feedback on priorities, target roles, skill relevance
- Access accounts if needed (LinkedIn, Indeed) for research verification
- Make decisions: which research findings shift strategy

**Claude's Role:**
- Execute systematic job posting analysis (100+ postings)
- Build skills-frequency matrix and pattern identification
- Produce research reports and actionable recommendations
- Be skeptical (don't flatter; identify realistic entry points only)
- Maintain source documentation (URLs, posting dates, company names)
- Commit findings + push progress continuously

### General Collaboration Pattern

1. **You define** — research questions, career goals, success criteria
2. **Claude researches** — job postings, market data, skill frequency analysis
3. **Claude produces** — research reports, recommendations, roadmaps
4. **You validate** — review findings, challenge assumptions, make decisions
5. **Iterate** — refine based on feedback, commit progress

### Key Values for This Repo
- **Realism over flattery** — identify what's actually feasible, not what's encouraging
- **Data-driven** — decisions based on 100+ real job postings, not generic advice
- **Honesty about gaps** — where you lack experience vs. demonstrable via projects
- **No fake claims** — projects are independent portfolio work, not professional experience

---

## Research Parameters (Confirmed 2026-08-20)

| Parameter | Decision |
|---|---|
| **Primary target roles** | Financial Analyst, FP&A Analyst, Finance Planning Analyst, Management Reporting Analyst |
| **Timeline** | Contract ends Jan 28 2027 · Notice deadline ~Oct 28 2026 · **5 months total** · Apply + build portfolio simultaneously |
| **Company preference** | Reputable and stable · 5-day work week (non-negotiable) · No industry restriction |
| **Salary** | Current: 4,000 AED · Target: 5,000 AED minimum · Below 5k only if strong growth trajectory |
| **Qualification** | CMA (US) early stages — not a near-term credential, "pursuing" line only |
| **Geography** | Dubai primary · UAE secondary · GCC as comparison only |

---

## Critical Research Questions (To Answer via Job Market Analysis)

These questions should be answered through analysis of 100+ real UAE/Dubai job postings:

**Career Targeting:**
1. Which roles are most realistic with current background? (Financial Analyst vs FP&A vs Finance Analyst vs Finance BI vs Finance Systems)
2. How much professional FP&A experience do employers actually require? (entry-level feasible or 2–3 years necessary?)
3. Which roles have the most vacancies in Dubai?
4. Which roles offer best salary potential?

**Skill Prioritization:**
5. What skills appear in 70%+ of postings? (high-ROI core skills)
6. What skills appear in 30–50%? (secondary skills, can specialize)
7. What skills appear in <20%? (niche, deprioritize)
8. Which skills can be demonstrated through portfolio projects? Which require employment experience?

**Technical Skills:**
9. How critical is Power BI vs SQL vs Python for target roles?
10. What's the expected proficiency level for each tool?
11. Is advanced Excel still foundational or being replaced by BI tools?

**Qualification Strategy:**
12. Do employers require CFA/CMA/ACCA for Financial Analyst / FP&A roles in UAE?
13. Which qualification (if any) has best ROI for your profile?
14. Does having CMA (in progress) help or hurt candidacy?

**Portfolio Strategy:**
15. What specific project types demonstrate job-posting requirements best?
16. Should projects be fictional scenarios or based on real company data?
17. How should technical/automation skills (Python, APIs, data pipelines) be positioned?

**Career Narrative:**
18. Should crypto trading system be included on professional profile?
19. How to frame technical projects without claiming to be a software engineer?
20. Best positioning: "Finance professional transitioning to analytical finance" or something else?

---

## Work Phases (from PENDING.md, prioritized)

### Phase 1: Job Market Research (PRIMARY)
**Objective:** Understand what UAE/Dubai employers actually want

- [ ] **Research 100+ real vacancies** — LinkedIn, Indeed UAE, GulfTalent, Bayt, company career pages
- [ ] **Build skills-frequency matrix** — which skills in which % of postings, importance ranking
- [ ] **Produce 6 research deliverables:**
  1. UAE Finance Job Market Report (role analysis, salary, vacancies, trends)
  2. Skill Gap Analysis (what employers want vs. what you have vs. demonstrable projects)
  3. Career Target Ranking (which roles realistic, entry barriers, salary potential)
  4. Portfolio Roadmap (5–8 projects, business scenarios, skills, timeline)
  5. LinkedIn Strategy (headline, keywords, featured projects, content pillars)
  6. Job Application Strategy (which jobs to target, experience mismatch rules, CV tailoring)

### Phase 2: Portfolio Projects (SECONDARY)
**Objective:** Build evidence of FP&A/analytics capabilities

- [ ] **5–8 excellent projects** based on Phase 1 research findings
- [ ] Projects should directly address job posting requirements
- [ ] Each project publishable on LinkedIn with business-problem focus

### Phase 3: LinkedIn & Branding (PARALLEL)
**Objective:** Position for recruiter discovery

- [ ] Update headline based on research
- [ ] Refine "About" section
- [ ] Add portfolio projects to featured section
- [ ] Publish project write-ups on LinkedIn

### Phase 4: Job Applications (FOLLOW-UP)
**Objective:** Target roles systematically based on Phase 1 findings

- [ ] Apply to roles matching research findings
- [ ] Use portfolio projects as evidence when experience gaps exist
- [ ] Prepare for interviews: "Why no formal FP&A experience?"

---

## Useful Patterns (from Ultimate Trading Terminal)

### Commit Message Format
```
Brief one-line summary of what changed

More context if needed (why, what impact, any notes).

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Example
```
Resume: reframe Promotech role to emphasize systems & automation work

Highlighted ERP migration project, data validation, workflow optimization 
to better reflect capability in technical problem-solving and product thinking.
Aligns resume with actual expertise in platform building.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

---

## Critical Research Principles (From Career Transition Brief)

**What NOT to do:**
- ❌ Don't rely on generic career advice ("Financial Analysts should learn Excel")
- ❌ Don't assume a skill is important without validating in real job postings
- ❌ Don't use American job market data when UAE/Dubai data is available
- ❌ Don't position portfolio projects as fake professional experience
- ❌ Don't promise that projects guarantee job offers (they're evidence, not guarantees)
- ❌ Don't recommend qualifications without ROI analysis against actual postings

**What to do:**
- ✅ Reverse-engineer requirements from 100+ real job postings
- ✅ Separate high-frequency requirements (70%+ of postings) from niche requirements
- ✅ Identify which skills employers request vs. which are teachable via projects
- ✅ Preserve source URLs for every important finding
- ✅ Focus on Dubai/UAE; use GCC comparisons only as secondary validation
- ✅ Be brutally realistic: which roles are entry-level feasible vs. 2–3 years required
- ✅ Challenge the hypothesis: does portfolio building actually help FP&A transition?

**Research Methodology:**
Sources in priority order:
1. LinkedIn job postings (current + recently closed with visible description)
2. LinkedIn recruiter/hiring-manager posts about open roles
3. Indeed UAE (FP&A, Financial Analyst, Finance Analyst, related)
4. GulfTalent, Bayt, Naukrigulf
5. Direct company career pages (for validation)

Capture for each role:
- Company, job title, location, date posted
- Experience required, education required
- Technical skills, tools, ERP/BI requirements
- Responsibilities (budgeting, forecasting, reporting, modelling, business partnering)
- Salary if available
- URL + source date
- Whether role appears realistic for your profile

---

**Last Updated:** 2026-08-20 00:45  
**Current Phase:** Job Market Research (Phase 1)  
**Next Review:** After first batch of research findings
