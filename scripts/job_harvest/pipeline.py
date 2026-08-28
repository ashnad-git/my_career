#!/usr/bin/env python3
"""Job scraping + fit-filter + dedup + JD-save pipeline for my_career.
Resumable: tracks saved signatures in state.json so repeated runs accumulate toward 200.
Each keeper saved to jds/ as a verbatim JD file. Rejects discarded on the spot.
"""
import os, re, json, sys, datetime, hashlib
import pandas as pd
from jobspy import scrape_jobs

ROOT = "/Users/ashnad/my_career"
JD_DIR = os.path.join(ROOT, "jds")
STATE = os.path.join(ROOT, "scratchpad/jobpipe/state.json")
EMAILS_CSV = os.path.join(ROOT, "scratchpad/jobpipe/harvested_emails.csv")
TODAY = datetime.date.today().isoformat()

# ---------- load state ----------
def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    # seed from existing jds
    urls=set(); sigs=set()
    for f in os.listdir(JD_DIR):
        if not f.endswith(".md"): continue
        txt=open(os.path.join(JD_DIR,f),encoding="utf-8",errors="ignore").read()
        m=re.search(r'URL:\s*(\S+)', txt)
        if m and m.group(1).strip().lower().startswith("http"):
            urls.add(m.group(1).strip().lower())
        c=re.search(r'\*\*Company:\*\*\s*(.+)', txt)
        t=re.search(r'^#\s+(.+)', txt, re.M)
        if c and t:
            sigs.add(sig(c.group(1), t.group(1)))
    return {"urls":list(urls),"sigs":list(sigs),"saved":0,"kept_titles":[]}

import unicodedata as _ud
def _norm(s):
    s=_ud.normalize("NFKD", s or "")
    return re.sub(r'[^a-z0-9]','', s.lower())
def sig(company, title):
    cn=re.sub(r'(llc|fzco|fze|pjsc|llp|ltd|limited|group|international)$','',_norm(company))
    tn=_norm(title)
    tn=re.sub(r'^jd','',tn)                 # strip 'JD:' prefix used in curated files
    # drop trailing location tokens commonly appended
    for loc in ["dubai","abudhabi","sharjah","uae","unitedarabemirates"]:
        tn=tn.replace(loc,"")
    return cn+"|"+tn[:22]

def save_state(st):
    json.dump(st, open(STATE,"w"), indent=1)

# ---------- fit filter ----------
# TITLE must contain one of these strong finance-analyst tokens to qualify.
STRONG_TITLE = [
    "financial analyst","finance analyst","fp&a","fp & a","fpa analyst",
    "financial planning","budget analyst","budgeting","commercial finance","commercial analyst",
    "cost analyst","cost controller","cost accountant","revenue analyst","management report",
    "management reporting","planning analyst","finance business partner","business finance partner",
    "financial reporting","finance associate","financial modeller","financial modeler",
    "pricing analyst","treasury analyst","business support analyst","fp&a manager",
    "finance manager","decision support analyst","financial controller","forecasting analyst",
    "financial planning & analysis","financial planning and analysis","business support - finance",
    # adjacent titles (user-approved 2026-08-28): accountant family + finance officer + BA-finance
    "accountant","senior accountant","management accountant","general accountant",
    "financial accountant","chief accountant","accounts manager","finance officer",
    "accounts executive","gl accountant","staff accountant","finance controller",
    "business analyst",
]
# hard reject if any of these appear in TITLE (wrong domain / too senior / reserved)
TITLE_EXCLUDE = [
    "qa","test","software","developer","data engineer","devops","fraud","credit","risk",
    "sales","business development","marketing","procurement","supply chain",
    "hr ","human resource","recruit","nurse","driver","warehouse","seo","penetration",
    "cyber","network engineer","full stack","frontend","backend","ui/ux","designer",
    "product manager","product management","product analyst","mechanical","civil engineer","electrical",
    "teacher","receptionist","admin assistant","customer service","call center","insurance analyst",
    "director","head of","chief","vp ","vice president","cfo","data analyst","it business",
    "esg","sustainability","audit senior","internal audit","tax manager","valuation",
    "investment analyst","portfolio manager","actuar","payroll","accounts payable","accounts receivable",
]
# desc / title-level hard rejects
NATIONAL_RE = re.compile(r'uae national|emirati|emiratis?\b|emiratisation|emiratization', re.I)
SENIOR_YEARS = re.compile(r'(minimum|min\.?|at least|over|require[sd]?)?\s*(6|7|8|9|10|11|12|15)\s*\+?\s*years', re.I)

def classify(title, desc):
    t=(title or "").lower()
    d=(desc or "").lower()
    # title exclude
    for x in TITLE_EXCLUDE:
        if x in t:
            return None, "title-exclude:"+x
    # STRONG title match required
    matched=[k for k in STRONG_TITLE if k in t]
    if not matched:
        return None, "no-strong-finance-title"
    # business-analyst needs finance context in description (avoid IT/product BAs)
    if matched==["business analyst"]:
        if not re.search(r'financ|fp&a|budget|forecast|p&l|variance|accounting|revenue|cost', d):
            return None, "business-analyst-non-finance"
    # national only (title or explicit desc reservation)
    if NATIONAL_RE.search(t):
        return None, "national-only-title"
    if re.search(r'(uae national|emirati)s?\s*(only|candidate|preferred|role|applicants)', d):
        return None, "national-only-desc"
    # too-senior years requirement
    if SENIOR_YEARS.search(d):
        return None, "senior-6plus-years"
    # fit rating
    fit="🟡 GOOD FIT"; reason=f"core finance title: {matched[0]}"
    if any(k in t for k in ["manager","controller","business partner"]):
        fit="🟠 STRETCH"; reason=f"finance title (seniority stretch): {matched[0]}"
    if any(k in t for k in ["financial analyst","finance analyst","fp&a analyst","budget analyst","commercial analyst","financial planning analyst"]) and not any(k in t for k in ["manager","senior","controller","lead"]):
        fit="✅ STRONG FIT"; reason=f"direct analyst-title match: {matched[0]}"
    if "junior" in t or "associate" in t or "graduate" in t or "entry" in d[:400]:
        fit="✅ STRONG FIT"; reason="entry/junior finance analyst"
    return (fit, reason)

def slug(s):
    s=re.sub(r'[^A-Za-z0-9]+','_', (s or 'X')).strip('_')
    return s[:40] or "X"

def save_jd(row, fit, reason, st):
    company=str(row.get("company") or "Unknown").strip()
    title=str(row.get("title") or "Role").strip()
    url=str(row.get("job_url") or "").strip()
    site=str(row.get("site") or "").strip()
    loc=str(row.get("location") or "").strip()
    desc=str(row.get("description") or "").strip()
    fname=f"{slug(company)}_{slug(title)}_{TODAY}.md"
    path=os.path.join(JD_DIR, fname)
    n=1
    while os.path.exists(path):
        path=os.path.join(JD_DIR, fname.replace(".md", f"_{n}.md")); n+=1
    salary=""
    if pd.notna(row.get("min_amount")) and row.get("min_amount"):
        salary=f"{row.get('currency','')} {row.get('min_amount')}–{row.get('max_amount')} ({row.get('interval','')})"
    content=f"""---
Date Found: {TODAY}
Source: {site}
Job ID: {row.get('id','')}
URL: {url}
Location: {loc}
Salary: {salary or 'Not specified'}
Status: Found — not yet applied
Fit: {fit}
Fit Reason: {reason}
---

# {title}
**Company:** {company}
**Location:** {loc}
**Platform:** {site}
**URL:** {url}

---

## Full Job Description (verbatim)

{desc}

---

## Portfolio Relevance

- **Phase 2B FP&A Model** — demonstrates budgeting, forecasting, variance analysis
- **EY background** — professional services finance experience; Big 4 brand
- **M.Sc. Financial Economics** — validates analytical and quantitative foundation
- **Odoo ERP migration (Promotech)** — ERP/systems finance experience
- **Python/automation skills** — differentiates for data/analytics hybrid roles
"""
    open(path,"w",encoding="utf-8").write(content)
    st["urls"].append(url.lower())
    st["sigs"].append(sig(company,title))
    st["saved"]+=1
    st["kept_titles"].append(f"{fit} | {company} | {title} | {url}")
    return fname

# ---------- search config ----------
SEARCH_TERMS = [
    "financial analyst","FP&A analyst","finance analyst","financial planning analyst",
    "budget analyst","commercial analyst","management reporting analyst","cost analyst",
    "revenue analyst","finance business partner","business support analyst finance",
    "financial reporting analyst","pricing analyst","finance associate","financial modeller",
    # expanded keyword coverage
    "FP&A","financial planning and analysis","corporate finance analyst","commercial finance analyst",
    "management accountant","cost accountant","junior financial analyst","graduate finance",
    "finance graduate","financial controller","group reporting analyst","consolidation analyst",
    "profitability analyst","margin analyst","business performance analyst","financial performance analyst",
    "decision support analyst","forecasting analyst","planning and reporting analyst","finance executive",
    "financial data analyst","reporting accountant","senior financial analyst","treasury analyst",
    "budgeting analyst","financial planning specialist","business finance analyst","cost controller",
    # adjacent-title search queries (user-approved 2026-08-28)
    "accountant","senior accountant","management accountant","general accountant",
    "financial accountant","chief accountant","finance officer","accounts executive",
    "business analyst finance","staff accountant","accounts manager",
]
LOCATIONS = ["Dubai","Abu Dhabi","Sharjah","United Arab Emirates"]

def run_batch(terms, sites, locations, results=40, hours=1000):
    st=load_state()
    existing_urls=set(st["urls"]); existing_sigs=set(st["sigs"])
    seen_this_run=set()
    kept=0; rejected=0; dup=0
    email_rows=[]
    for term in terms:
        for loc in locations:
            try:
                jobs=scrape_jobs(site_name=sites, search_term=term, location=loc,
                                 results_wanted=results, hours_old=hours,
                                 country_indeed="United Arab Emirates",
                                 linkedin_fetch_description=("linkedin" in sites))
            except Exception as e:
                print(f"  [scrape-fail] {term}@{loc}: {e}")
                continue
            if jobs is None or len(jobs)==0:
                print(f"  [empty] {term}@{loc}")
                continue
            for _,row in jobs.iterrows():
                url=str(row.get("job_url") or "").strip().lower()
                company=str(row.get("company") or "").strip()
                title=str(row.get("title") or "").strip()
                s=sig(company,title)
                # harvest emails regardless
                em=row.get("emails")
                if em and str(em)!="nan":
                    email_rows.append({"email":em,"company":company,"title":title,"url":url})
                if not url or url in existing_urls or url in seen_this_run or s in existing_sigs:
                    dup+=1; continue
                seen_this_run.add(url)
                res=classify(title, str(row.get("description") or ""))
                if res[0] is None:
                    rejected+=1; continue
                fit,reason=res
                fname=save_jd(row, fit, reason, st)
                existing_urls.add(url); existing_sigs.add(s)
                kept+=1
                print(f"  [SAVE {st['saved']:>3}] {fit} {company} — {title[:50]}")
            save_state(st)
            print(f"[batch] {term}@{loc}: kept={kept} rej={rejected} dup={dup} | total saved={st['saved']}")
    # write emails
    if email_rows:
        df=pd.DataFrame(email_rows)
        if os.path.exists(EMAILS_CSV):
            old=pd.read_csv(EMAILS_CSV); df=pd.concat([old,df]).drop_duplicates("email")
        df.to_csv(EMAILS_CSV,index=False)
    print(f"\n=== RUN DONE: kept={kept} rejected={rejected} dup={dup} | TOTAL SAVED={st['saved']} ===")
    return st

if __name__=="__main__":
    sites=sys.argv[1].split(",") if len(sys.argv)>1 else ["indeed"]
    nterms=int(sys.argv[2]) if len(sys.argv)>2 else 5
    nloc=int(sys.argv[3]) if len(sys.argv)>3 else 1
    run_batch(SEARCH_TERMS[:nterms], sites, LOCATIONS[:nloc])
