"""
Job scraper for my_career research using crawl4ai.
Use for: Bayt.com, Indeed UAE, GulfTalent, company career pages, direct job posting URLs.
NOT for: LinkedIn (requires authenticated session — use browser automation instead).

Usage:
    python scraper/job_scraper.py --urls urls.txt --out output.md
    python scraper/job_scraper.py --url "https://bayt.com/en/uae/jobs/..." --out result.md
"""

import asyncio
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

NAUKRIGULF_SCROLL_JS = "window.scrollTo(0, 2000); await new Promise(r => setTimeout(r, 3000));"
NAUKRIGULF_JOB_PATTERN = re.compile(
    r'\[([^\]]+)\]\((https://www\.naukrigulf\.com/[^)]+jid-[^)]+)\)\[([^\]]+)\]'
)


# --- Extraction schemas for known job boards ---

BAYT_SCHEMA = {
    "name": "Bayt Job Listings",
    "baseSelector": "li.has-pointer-d",
    "fields": [
        {"name": "title", "selector": "h2.jb-title", "type": "text"},
        {"name": "company", "selector": "b.jb-company", "type": "text"},
        {"name": "location", "selector": "span.jb-loc", "type": "text"},
        {"name": "salary", "selector": "span.jb-sal", "type": "text"},
        {"name": "posted", "selector": "span.jb-date", "type": "text"},
        {"name": "url", "selector": "a.jb-title-link", "type": "attribute", "attribute": "href"},
    ]
}

INDEED_SCHEMA = {
    "name": "Indeed UAE Job Listings",
    "baseSelector": "div.job_seen_beacon",
    "fields": [
        {"name": "title", "selector": "h2.jobTitle span", "type": "text"},
        {"name": "company", "selector": "span.companyName", "type": "text"},
        {"name": "location", "selector": "div.companyLocation", "type": "text"},
        {"name": "salary", "selector": "div.salary-snippet-container", "type": "text"},
        {"name": "url", "selector": "a.jcs-JobTitle", "type": "attribute", "attribute": "href"},
    ]
}


async def scrape_url(url: str, use_js: bool = True, extract_schema: dict = None, wait_for: str = None, js_code: str = None) -> dict:
    """Scrape a single URL and return clean content."""
    browser_config = BrowserConfig(
        headless=True,
        use_managed_browser=False,
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    )
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        word_count_threshold=10,
        remove_overlay_elements=False,
        wait_until="domcontentloaded",
        page_timeout=60000,
        delay_before_return_html=4.0,
        wait_for=wait_for,
        js_code=js_code,
        extraction_strategy=JsonCssExtractionStrategy(extract_schema) if extract_schema else None,
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=config)

    if not result.success:
        return {"url": url, "error": result.error_message, "content": None}

    output = {
        "url": url,
        "title": result.metadata.get("title", ""),
        "scraped_at": datetime.now().isoformat(),
    }

    if extract_schema and result.extracted_content:
        try:
            output["structured"] = json.loads(result.extracted_content)
        except Exception:
            output["structured"] = result.extracted_content

    md = result.markdown
    output["markdown"] = md.raw_markdown if hasattr(md, "raw_markdown") else str(md)
    return output


async def scrape_batch(urls: list[str], out_file: str, extract_schema: dict = None):
    """Scrape multiple URLs and save to markdown file."""
    results = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Scraping: {url}")
        try:
            data = await scrape_url(url, extract_schema=extract_schema)
            results.append(data)
            if data.get("error"):
                print(f"  ERROR: {data['error']}")
            else:
                content_len = len(data.get("markdown", "") or "")
                print(f"  OK — {content_len} chars")
        except Exception as e:
            results.append({"url": url, "error": str(e), "content": None})
            print(f"  EXCEPTION: {e}")

    # Write output
    out_path = Path(out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w") as f:
        f.write(f"# Crawl4AI Scrape Results\n\n")
        f.write(f"**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**URLs:** {len(urls)}\n\n---\n\n")

        for r in results:
            f.write(f"## {r.get('title', r['url'])}\n\n")
            f.write(f"**URL:** {r['url']}\n\n")
            if r.get("error"):
                f.write(f"**ERROR:** {r['error']}\n\n")
            elif r.get("structured"):
                f.write("### Structured Data\n\n```json\n")
                f.write(json.dumps(r["structured"], indent=2, ensure_ascii=False))
                f.write("\n```\n\n")
            else:
                content = (r.get("markdown") or "")[:3000]
                f.write(content)
                if len(r.get("markdown", "")) > 3000:
                    f.write("\n\n*[truncated — full content in raw output]*\n")
            f.write("\n\n---\n\n")

    print(f"\nSaved to: {out_path}")
    return results


async def scrape_naukrigulf(url: str, out_file: str, label: str = ""):
    """Scrape a Naukrigulf listing page with JS scroll trick, extract job URLs."""
    print(f"Scraping Naukrigulf: {url}")
    data = await scrape_url(url, js_code=NAUKRIGULF_SCROLL_JS)
    if data.get("error"):
        print(f"  ERROR: {data['error']}")
        return []

    md = data.get("markdown", "")
    jobs = NAUKRIGULF_JOB_PATTERN.findall(md)
    unique = {}
    for title, job_url, company in jobs:
        if job_url not in unique:
            unique[job_url] = {"title": title.strip(), "company": company.strip(), "url": job_url}

    out_path = Path(out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(f"# Naukrigulf Jobs — {label or url}\n\n")
        f.write(f"**Scraped:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n")
        f.write(f"**Jobs found:** {len(unique)}  \n**Source:** {url}\n\n---\n\n")
        for i, job in enumerate(unique.values(), 1):
            f.write(f"{i}. **{job['title']}** — {job['company']}  \n   {job['url']}\n\n")

    print(f"  {len(unique)} jobs extracted → {out_path}")
    return list(unique.values())


# --- Preset scrape targets ---

PRESETS = {
    "bayt_financial_analyst_uae": {
        "urls": [
            "https://www.bayt.com/en/uae/jobs/financial-analyst-jobs/",
            "https://www.bayt.com/en/uae/jobs/fp-a-analyst-jobs/",
            "https://www.bayt.com/en/uae/jobs/finance-analyst-jobs/",
        ],
        "schema": BAYT_SCHEMA,
        "out": "scraper/output/bayt_financial_analyst.md",
    },
    "indeed_fpa_dubai": {
        "urls": [
            "https://ae.indeed.com/jobs?q=FP%26A+analyst&l=Dubai&fromage=30",
            "https://ae.indeed.com/jobs?q=financial+analyst&l=Dubai&fromage=30&sc=0kf%3Aattr%28DSQF7%29%3B",
        ],
        "schema": INDEED_SCHEMA,
        "out": "scraper/output/indeed_fpa_dubai.md",
    },
    "gulfttalent_fa_uae": {
        "urls": [
            "https://www.gulfttalent.com/jobs/financial-analyst-jobs-in-uae.html",
        ],
        "schema": None,
        "out": "scraper/output/gulfttalent_fa.md",
    },
}

NAUKRIGULF_PRESETS = {
    "financial-analyst": "https://www.naukrigulf.com/financial-analyst-jobs-in-uae",
    "fpa-analyst": "https://www.naukrigulf.com/fp-a-analyst-jobs-in-uae",
    "planning-analyst": "https://www.naukrigulf.com/planning-analyst-jobs-in-uae",
    "commercial-analyst": "https://www.naukrigulf.com/commercial-analyst-jobs-in-uae",
    "management-reporting": "https://www.naukrigulf.com/management-reporting-analyst-jobs-in-uae",
    "finance-analyst": "https://www.naukrigulf.com/finance-analyst-jobs-in-uae",
    "budget-analyst": "https://www.naukrigulf.com/budget-analyst-jobs-in-uae",
    "corporate-finance": "https://www.naukrigulf.com/corporate-finance-analyst-jobs-in-uae",
}


def main():
    parser = argparse.ArgumentParser(description="Job scraper for my_career research")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="Single URL to scrape")
    group.add_argument("--urls", help="File with one URL per line")
    group.add_argument("--preset", choices=list(PRESETS.keys()), help="Use a preset configuration")
    group.add_argument("--naukrigulf", choices=list(NAUKRIGULF_PRESETS.keys()), help="Scrape a Naukrigulf preset (with JS scroll)")
    group.add_argument("--naukrigulf-all", action="store_true", help="Scrape all Naukrigulf presets")
    parser.add_argument("--out", default="scraper/output/results.md", help="Output file path")
    parser.add_argument("--schema", choices=["bayt", "indeed"], help="Apply CSS extraction schema")
    args = parser.parse_args()

    schema_map = {"bayt": BAYT_SCHEMA, "indeed": INDEED_SCHEMA}

    if getattr(args, 'naukrigulf_all', False):
        async def run_all():
            for key, url in NAUKRIGULF_PRESETS.items():
                out = f"scraper/output/naukrigulf_{key.replace('-', '_')}.md"
                await scrape_naukrigulf(url, out, label=key)
        asyncio.run(run_all())
    elif args.naukrigulf:
        key = args.naukrigulf
        url = NAUKRIGULF_PRESETS[key]
        out = args.out if args.out != "scraper/output/results.md" else f"scraper/output/naukrigulf_{key.replace('-', '_')}.md"
        asyncio.run(scrape_naukrigulf(url, out, label=key))
    elif args.preset:
        preset = PRESETS[args.preset]
        urls = preset["urls"]
        schema = preset["schema"]
        out = preset["out"]
        print(f"Scraping {len(urls)} URL(s)...")
        asyncio.run(scrape_batch(urls, out, schema))
    elif args.url:
        urls = [args.url]
        schema = schema_map.get(args.schema)
        out = args.out
        print(f"Scraping {len(urls)} URL(s)...")
        asyncio.run(scrape_batch(urls, out, schema))
    else:
        with open(args.urls) as f:
            urls = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        schema = schema_map.get(args.schema)
        out = args.out
        print(f"Scraping {len(urls)} URL(s)...")
        asyncio.run(scrape_batch(urls, out, schema))


if __name__ == "__main__":
    main()
