#!/usr/bin/env python3
"""Save GulfTalent JDs from a parsed batch json (list of {url,title,comp,fit,desc}).
Cleans company (text after 'by'), dedups vs archive (gulftalent id + company|title sig),
skips UAE-National / clerical, writes verbatim JD files. Usage: save_gulftalent.py <batch.json>"""
import json,re,os,sys,glob,datetime
sys.path.insert(0,os.path.dirname(__file__))
from pipeline import sig
ROOT="/Users/ashnad/my_career"; JD=os.path.join(ROOT,"jds"); TODAY=datetime.date.today().isoformat()
fitmap={"STRONG":"✅ STRONG FIT","GOOD":"🟡 GOOD FIT","STRETCH":"🟠 STRETCH"}

# archive keys
arch_ids=set(); arch_sigs=set()
for f in glob.glob(os.path.join(JD,'*.md')):
    t=open(f,encoding='utf-8',errors='ignore').read()
    for m in re.findall(r'gulftalent\.com/uae/jobs/[a-z0-9-]+-(\d+)', t): arch_ids.add(m)
    c=re.search(r'\*\*Company:\*\*\s*(.+)',t);comp=c.group(1).strip() if c else ""
    ti=re.search(r'^#\s+(.+)',t,re.M);title=ti.group(1).strip() if ti else ""
    arch_sigs.add(sig(comp,title))
# also today's already-saved gulftalent ids (avoid intra-run dup)
def slug(s): return (re.sub(r'[^A-Za-z0-9]+','_',s).strip('_')[:40] or "X")

def clean_comp(c):
    m=re.search(r'\bby\s+(.+)$', c)
    c=m.group(1).strip() if m else re.sub(r'^.*?,\s*UAE\s*','',c).strip()
    return c or "GulfTalent (see JD)"

batch=json.load(open(sys.argv[1]))
saved=0; skip_dup=0; skip_exc=0
for o in batch:
    title=o['title'].strip(); comp=clean_comp(o['comp']); desc=o['desc'].strip()
    jid=re.search(r'-(\d+)$', o['url']); jid=jid.group(1) if jid else ''
    tl=title.lower()
    if 'uae national' in tl or 'personal assistant' in tl or 'cum accountant' in tl:
        skip_exc+=1; continue
    if len(desc)<120:
        skip_exc+=1; continue
    if jid in arch_ids or sig(comp,title) in arch_sigs:
        skip_dup+=1; continue
    arch_ids.add(jid); arch_sigs.add(sig(comp,title))
    fname=f"{slug(comp)}_{slug(title)}_{TODAY}.md"; path=os.path.join(JD,fname); n=1
    while os.path.exists(path): path=os.path.join(JD,fname.replace('.md',f'_{n}.md')); n+=1
    content=f"""---
Date Found: {TODAY}
Source: GulfTalent
URL: {o['url']}
Status: Found — not yet applied
Fit: {fitmap.get(o['fit'],o['fit'])}
Fit Reason: finance-analyst/accounting role (GulfTalent harvest)
---

# {title.title()}
**Company:** {comp}
**Location:** UAE
**Platform:** GulfTalent
**URL:** {o['url']}

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
    open(path,"w",encoding="utf-8").write(content); saved+=1
print(f"saved={saved} skip_dup={skip_dup} skip_excluded={skip_exc}")
PY_END = None
