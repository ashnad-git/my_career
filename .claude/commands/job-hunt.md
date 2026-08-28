---
description: Run the full UAE finance job-hunt pipeline — scrape+filter+dedup+save apply-ready JDs (Indeed/LinkedIn/Naukrigulf/GulfTalent), harvest LinkedIn connection targets with humanized notes, harvest cold-email contacts with drafts, and rank every job by fit. Args: jobs | people | emails | rank | all (default: all).
allowed-tools: Bash, Read, Write, Edit, WebFetch, WebSearch, AskUserQuestion, TaskCreate, TaskUpdate, TaskList
---

You are running Ashnad's **job-hunt pipeline**. Reusable engine lives in `scripts/job_harvest/`. This is his real career transition from accounting operations into FP&A / Financial Analyst roles in Dubai — apply the profile filters seriously and never save rejects or duplicates.

**Argument (`$ARGUMENTS`)** selects the phase. Empty = run all in order.
- `jobs` — scrape + filter + dedup + save apply-ready JDs
- `people` — harvest LinkedIn connection targets + notes
- `emails` — harvest cold-email contacts + drafts
- `rank` — score & tier all saved JDs
- `all` (default) — jobs → people → emails → rank

Create a task list (TaskCreate) for the phases you're about to run, mark in_progress/completed as you go.

## Profile filters (apply everywhere)
- **Target:** entry-mid Financial Analyst / FP&A / Finance Analyst / budget / commercial / cost / planning / reporting analyst. Adjacent (user-approved): accountant / senior accountant / management accountant / finance officer / cost accountant. Finance/Assistant Manager = STRETCH.
- **Reject (never save):** UAE-National / Emirati-only (also `(UAEN)`, "Emarati talent"), 6+ years minimum, Director/Head/Chief/VP, wrong domain (sales/IT/QA/data-eng/credit-risk/marketing/HR/procurement), clerical/junior (Junior/Assistant Accountant, cashier, admin-cum, data-entry, PA-cum-accountant, receptionist), non-UAE location (Egypt/KSA/PNG/etc), sub-5k AED salary bands.
- **No duplicates:** dedup every new JD against everything already in `jds/` (URL + normalised company|title). Run the dedup scripts after each batch.

---

## PHASE: jobs

Automated sources first (fast), then browser sources (logged-in, on Ashnad's **Mac** only).

### 1. jobspy — Indeed + LinkedIn
```bash
python3 scripts/job_harvest/run_full.py indeed 70      # full Indeed sweep (~32 keywords x 4 UAE locations)
python3 scripts/job_harvest/run_full.py linkedin 40    # LinkedIn (rate-limits on big sweeps; keep small)
python3 scripts/job_harvest/dedup_today.py             # safe dedup of today's files vs archive
python3 scripts/job_harvest/trim_junk.py               # remove clerical/junior/gender-gated junk
```
- These append to `jds/` and are resumable via `scratchpad/jobpipe/state.json`. Rebuild state after manual JD edits by deleting `state.json` and running `load_state`/`save_state` once.
- Bayt (403), Naukri API (recaptcha), Glassdoor (n/a UAE), Google (0) are **blocked** via jobspy — use the browser sources for those.
- After trimming, audit today's titles for anything that slipped: `for f in jds/*$(date +%F)*.md; do grep -m1 '^# ' "$f"; done | sort | uniq -c`.

### 2. Browser sources — Naukrigulf + GulfTalent (needs Ashnad's Mac Chrome, logged in)
Load browser tools with ToolSearch (one call): `select:mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__select_browser,mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__javascript_tool`.

**ALWAYS** call `list_connected_browsers` and confirm with the user via AskUserQuestion, then `select_browser` the **macOS / isLocal:true** device — never the Windows work laptop.

**Naukrigulf** (`https://www.naukrigulf.com/<title>-jobs-in-uae`, paginate with `-2`, `-3`, ...): job URL slugs encode title, company, and experience, so classify + dedup from the slug (cheap), then fetch full JDs only for net-new keepers via `get_page_text`. Save with `scripts/job_harvest/save_naukri.py "<url>" "<company>" "<title>" "<fit>" "<loc>" <<<DESC`.

**GulfTalent** (`https://www.gulftalent.com/uae/jobs/title/<title>`): the full JD is server-rendered in `.job-description`, so batch-fetch in-browser with same-origin `fetch()`. Loop ~22 URLs per `javascript_tool` call (CDP times out ~45s), store keepers to `localStorage`. To get JDs to disk, inject them into an `<article id="__dump">` and read via `get_page_text` (which **persists >~110KB outputs to a file** you can parse). Then `scripts/job_harvest/save_gulftalent.py <batch.json>` (dedups by GulfTalent id + company|title, skips national/clerical). Regenerate `scratchpad/jobpipe/archive_keys.json` first for in-browser dedup if needed.

**Gotchas:** `javascript_tool` return is capped ~1KB (pull data in small chunks or via the persist-file trick); `get_page_text` returns much more. Chrome blocks repeated auto-`download()` after the first — prefer chunked pulls or the persist-file trick; if you must download, ask the user (per the download rule) and expect only the first to land.

### 3. Save every JD you can see (hard rule)
Any job title + URL seen anywhere → save to `jds/CompanyName_Role_YYYY-MM-DD.md` (verbatim responsibilities + requirements + a Portfolio Relevance section) if opened, or to `JOB_PIPELINE.md` if only seen in a sidebar. No exceptions.

### 4. Report + pipeline + commit
- Report today's net-new count and STRONG/GOOD/STRETCH split.
- Append a dated batch summary to `JOB_PIPELINE.md` (priority analyst/FP&A roles as a table; note adjacent-accountant volume).
- Commit + push (main branch, per repo convention). Commit message ends with the repo's Co-Authored-By + Claude-Session trailers.

---

## PHASE: people (200 LinkedIn connection targets)

Needs Ashnad's Mac Chrome, logged into LinkedIn. Connect-UP strategy (see `NETWORKING.md`): CFOs, Finance Directors, VP Finance, FP&A/Finance Managers, Heads of FP&A, and HR/Talent-Acquisition gatekeepers — Dubai/Abu Dhabi/Sharjah + UAE-wide.

1. For each search, navigate to `https://www.linkedin.com/search/results/people/?keywords=<query>&origin=SWITCH_SEARCH_VERTICAL` (rotate queries: "Finance Director Dubai", "CFO UAE", "Head of FP&A UAE", "FP&A Manager Dubai/Abu Dhabi", "Finance Manager <city>", "Financial Controller <city>", "Talent Acquisition Finance Dubai", "Finance Recruiter Dubai", "Finance Business Partner UAE", etc.). Diversify cities/titles once returns start overlapping.
2. Extract cards with the JS parser (LinkedIn classes are obfuscated — find each card as the tightest ancestor containing a Connect/Message action; parse name / headline / location / mutuals from its innerText). Accumulate into `localStorage['__people']` (dedup by profile URL). ~10 real cards/page.
3. Get the data to disk: `download()` a `linkedin_targets.json` (ask permission first per the download rule; the first download usually lands). Copy into `scratchpad/jobpipe/` and run `python3 scripts/job_harvest/build_networking.py` → appends a tiered section to `NETWORKING.md` with a **humanized ≤200-char connection note** per person (follow the repo humanized-writing rules: no em dashes, no AI openers, specific to their company).
4. **Sending is Ashnad's action** — never auto-send invites (LinkedIn flags automation; ~20/day cap). Commit + push.

---

## PHASE: emails (100 cold-email contacts)

`python3 scripts/job_harvest/build_emails.py` → merges the jobspy `emails` field (`scratchpad/jobpipe/harvested_emails.csv`) + emails found inside `jds/` into `COLD_EMAILS.md`, deduped and junk-filtered, with two humanized cold-email drafts (generic inbox vs named person). Optionally add company contact/careers-page emails found while browsing. **Sending is Ashnad's action** (attach `resumes/Muhammed_Ashnad_Resume.pdf`). Commit + push.

---

## PHASE: rank

`python3 scripts/job_harvest/rank_jobs.py` → scores every `jds/*.md` for Ashnad's profile (title relevance, experience band, skill overlap [budgeting/forecasting/Power BI/ERP/automation/commercial], Dubai location, seniority, negatives) and writes `JOB_RANKING.md` (Tier 1 apply-first → Tier 5 low). Print the tier counts and the top ~25. Commit + push.

---

## After running
Briefly report what changed (net-new JDs, connection targets, emails, ranking tiers) and what's ready for Ashnad to act on (apply to Tier 1, send invites, send cold emails). Keep `DAILY_LOG.md` and `CHANGELOG.md` updated per repo convention.
