# Job Harvest Pipeline

Automated scrape → fit-filter → dedup → save-JD pipeline for the UAE finance-analyst job hunt.

## What it does
- Scrapes Indeed + LinkedIn (via `python-jobspy`) across UAE locations and ~32 finance keywords.
- Fit-filters EACH job on find: rejects wrong-domain / UAE-National-only / 6+ years-senior; keeps STRONG/GOOD/STRETCH.
- Dedups against every JD already in `jds/` (URL + normalised company|title signature).
- Saves each keeper as `jds/Company_Role_DATE.md` (verbatim JD + Portfolio Relevance) and is resumable via `state.json`.

## Run
```bash
python3 scripts/job_harvest/run_full.py indeed 70     # full Indeed sweep
python3 scripts/job_harvest/run_full.py linkedin 40   # LinkedIn (rate-limited; small batches)
python3 scripts/job_harvest/dedup_today.py            # safe dedup of today's files vs archive
```

## Sources status (2026-08-28)
- Indeed: works. LinkedIn: works (rate-limits on large sweeps, run small).
- Bayt (403), Naukri API (recaptcha), Glassdoor (n/a UAE), Google (0) — blocked via jobspy.
- Naukrigulf / GulfTalent: use logged-in Chrome (browser automation) — slugs encode title/company/experience for cheap classify+dedup; fetch full JD with get_page_text.
