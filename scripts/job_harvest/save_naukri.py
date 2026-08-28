#!/usr/bin/env python3
"""Save one Naukrigulf JD. Usage:
  python3 save_naukri.py "<url>" "<company>" "<title>" "<fit>" "<loc>" < description_on_stdin
Writes jds/Company_Title_DATE.md with verbatim JD + Portfolio Relevance."""
import sys, os, re, datetime
ROOT="/Users/ashnad/my_career"; JD=os.path.join(ROOT,"jds"); TODAY=datetime.date.today().isoformat()
url,company,title,fit,loc = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],(sys.argv[5] if len(sys.argv)>5 else "")
desc=sys.stdin.read().strip()
def slug(s): return (re.sub(r'[^A-Za-z0-9]+','_',s).strip('_')[:40] or "X")
fname=f"{slug(company)}_{slug(title)}_{TODAY}.md"; path=os.path.join(JD,fname); n=1
while os.path.exists(path): path=os.path.join(JD,fname.replace('.md',f'_{n}.md')); n+=1
fitmap={"STRONG":"✅ STRONG FIT","GOOD":"🟡 GOOD FIT","STRETCH":"🟠 STRETCH"}
content=f"""---
Date Found: {TODAY}
Source: Naukrigulf
URL: {url}
Location: {loc}
Status: Found — not yet applied
Fit: {fitmap.get(fit,fit)}
Fit Reason: finance-analyst role (Naukrigulf harvest)
---

# {title}
**Company:** {company}
**Location:** {loc}
**Platform:** Naukrigulf
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
print("saved", os.path.basename(path), f"({len(desc)} chars)")
