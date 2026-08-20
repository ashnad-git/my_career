# Crawl4AI Scrape Results

**Scraped:** 2026-08-20 09:53
**URLs:** 1

---

## https://ae.indeed.com/jobs?q=FP%26A+analyst&l=Dubai&fromage=30

**URL:** https://ae.indeed.com/jobs?q=FP%26A+analyst&l=Dubai&fromage=30

**ERROR:** Unexpected error in _crawl_web at line 778 in _crawl_web (../../../opt/homebrew/lib/python3.13/site-packages/crawl4ai/async_crawler_strategy.py):
Error: Failed on navigating ACS-GOTO:
Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://ae.indeed.com/jobs?q=FP%26A+analyst&l=Dubai&fromage=30", waiting until "networkidle"


Code context:
 773                                   tag="GOTO",
 774                                   params={"url": url},
 775                               )
 776                               response = None
 777                           else:
 778 →                             raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
 779   
 780                       # ──────────────────────────────────────────────────────────────
 781                       # Walk the redirect chain.  Playwright returns only the last
 782                       # hop, so we trace the `request.redirected_from` links until the
 783                       # first response that differs from the final one and surface its



---

