#!/usr/bin/env python3
"""Rank all jds/*.md by fit for Ashnad's profile.
Profile: EY accounting background + M.Sc Financial Economics + CMA(US) in progress,
ERP migration (Tally->Odoo), Python/automation, learning Power BI. Target: entry-mid
Financial Analyst / FP&A Analyst in Dubai, 5-day week, AED 5k+. Transitioning from
accounting ops into analytical finance.
Outputs JOB_RANKING.md (all ranked, tiered) + prints top tier."""
import os, re, glob, unicodedata as ud
JD="/Users/ashnad/my_career/jds"
OUT="/Users/ashnad/my_career/JOB_RANKING.md"

def read(f):
    t=open(f,encoding='utf-8',errors='ignore').read()
    def g(p,d=''):
        m=re.search(p,t,re.M|re.I); return m.group(1).strip() if m else d
    fit=g(r'^Fit:\s*(.+)')
    comp=g(r'\*\*Company:\*\*\s*(.+)')
    title=g(r'^#\s+(.+)')
    url=g(r'^URL:\s*(\S+)'); src=g(r'^Source:\s*(.+)'); loc=g(r'^Location:\s*(.+)')
    # description body
    dm=re.search(r'Full Job Description.*?\n(.*?)\n---\n\n## Portfolio', t, re.S)
    if not dm: dm=re.search(r'## (?:Full Job Description.*?|.*?)\n(.*)', t, re.S)
    desc=dm.group(1) if dm else t
    return dict(file=os.path.basename(f),fit=fit,comp=comp,title=title,url=url,src=src,loc=loc,desc=desc)

def norm(s): return re.sub(r'[^a-z0-9 ]','',ud.normalize('NFKD',(s or '').lower()))

def score(j):
    t=norm(j['title']); d=(j['desc'] or '').lower(); loc=(j['loc'] or '').lower()+' '+d[:300]
    s=0.0; why=[]
    # base fit
    fit=j['fit']
    if '✅' in fit or 'STRONG' in fit.upper(): s+=40
    elif '🟡' in fit or 'GOOD' in fit.upper(): s+=25
    else: s+=10
    # title relevance
    if re.search(r'\bfp ?& ?a analyst\b|financial planning (and )?analysis analyst|financial analyst\b|finance analyst\b|financial planning analyst', t): s+=32; why.append('core FA/FP&A title')
    elif re.search(r'budget analyst|commercial finance analyst|commercial analyst|planning analyst|reporting analyst|revenue analyst|business support analyst', t): s+=26; why.append('analyst title')
    elif re.search(r'corporate finance analyst|cost analyst|financial model|pricing analyst|business finance', t): s+=22; why.append('analyst-adjacent title')
    elif re.search(r'finance associate|financial reporting|decision support', t): s+=18; why.append('finance associate')
    elif re.search(r'cost accountant|management accountant', t): s+=12; why.append('cost/mgmt accountant')
    elif re.search(r'financial controller|finance manager', t): s-=6; why.append('senior/mgr title')
    elif re.search(r'\baccountant\b', t): s+=5; why.append('accountant (adjacent)')
    # seniority
    if 'senior' in t: s-=8
    if re.search(r'\bmanager\b', t): s-=8
    if re.search(r'head of|director|chief|vice president', t): s-=25
    if re.search(r'junior|associate|trainee|graduate|assistant', t): s+=8; why.append('entry-level')
    # experience
    exp=re.search(r'(\d+)\s*[-to]+\s*(\d+)\s*year', d)
    single=re.search(r'(?:minimum|min\.?|at least|over)?\s*(\d+)\+?\s*year', d)
    yrs=None
    if exp: yrs=int(exp.group(1))
    elif single: yrs=int(single.group(1))
    if yrs is not None:
        if yrs<=2: s+=15; why.append(f'{yrs}+ yrs exp')
        elif yrs<=3: s+=12
        elif yrs<=4: s+=6
        elif yrs<=5: s+=0
        else: s-=12; why.append('5+ yrs')
    # skill overlap (Ashnad's toolkit)
    skills={'budget':3,'forecast':3,'variance':3,'power bi':6,'financial model':4,'erp':4,
            'sap':2,'oracle':2,'tally':4,'odoo':5,'commercial':3,'profitab':3,'month-end':3,
            'management report':3,'dashboard':3,'automation':5,'python':5,'ifrs':2,'p&l':3,
            'scenario':2,'kpi':2}
    sk=0
    for k,v in skills.items():
        if k in d: sk+=v
    sk=min(sk,34); s+=sk
    if sk>=15: why.append('strong skill overlap')
    # brand/qual match
    if re.search(r'big 4|big four|\bey\b|ernst|professional services|audit firm', d): s+=4
    if re.search(r'cma|acca|cpa|cima|part.?qualified|pursuing', d): s+=3
    # location
    if 'dubai' in loc: s+=6
    elif 'abu dhabi' in loc: s+=3
    elif re.search(r'sharjah|ajman|fujairah|ras al', loc): s+=1
    if re.search(r'egypt|luxor|papua|new guinea|saudi|riyadh|jeddah|qatar|doha|oman|muscat', loc) and 'uae' not in loc[:80]: s-=15; why.append('non-UAE location')
    # 5-day week
    if re.search(r'5[ -]day|five[ -]day', d): s+=3; why.append('5-day week')
    if re.search(r'mon.?sat|6[ -]day|six[ -]day', d): s-=4
    # negatives
    if re.search(r'\btreasury\b', t): s-=10
    if re.search(r'internal audit|external audit|\baudit\b', t): s-=8
    if re.search(r'credit risk|market risk|brokerage|underwriting', t+' '+d[:200]): s-=8
    if re.search(r'philippines only|filipino|asian national|indian national|male only|female only|male candidate|female candidate|nationality\s*(india|philippines|nepal|asia)', d): s-=10; why.append('nationality-restricted')
    m=re.search(r'(\d[\d,]{2,})\s*(?:to|-)\s*(\d[\d,]{2,})\s*aed|aed\s*(\d[\d,]{2,})', d)
    if m:
        low=int(re.sub(r'[^0-9]','', m.group(1) or m.group(3) or '0'))
        if 0<low<5000: s-=8; why.append(f'salary<5k')
    return round(s,1), why

files=glob.glob(os.path.join(JD,'*.md'))
jobs=[read(f) for f in files]
# dedup by company+title (keep best-scoring)
seen={}
for j in jobs:
    j['score'],j['why']=score(j)
    key=(norm(j['comp'])[:20], norm(j['title'])[:25])
    if key not in seen or j['score']>seen[key]['score']:
        seen[key]=j
ranked=sorted(seen.values(), key=lambda x:-x['score'])

# tiers
def tier(s):
    if s>=75: return 'TIER 1 — Apply first (best fit)'
    if s>=60: return 'TIER 2 — Strong apply'
    if s>=45: return 'TIER 3 — Good apply'
    if s>=30: return 'TIER 4 — Stretch / volume'
    return 'TIER 5 — Low priority'

lines=['# Job Ranking — All roles scored for Ashnad\'s profile',
       f'\n**{len(ranked)} unique roles ranked** (deduped from {len(jobs)} JD files). Scored on title relevance, experience band, skill overlap (budgeting/forecasting/Power BI/ERP/automation/commercial), Dubai location, seniority, and negatives (senior/treasury/audit/nationality-gated/non-UAE/sub-5k).\n',
       '**Apply top-down.** Tier 1–2 = tailor a CV; Tier 3 = master CV; Tier 4 = Easy-Apply volume.\n']
cur=None
for i,j in enumerate(ranked,1):
    tg=tier(j['score'])
    if tg!=cur:
        cur=tg; lines.append(f'\n## {tg}\n'); lines.append('| # | Score | Fit | Company | Role | Src | Why | Apply |'); lines.append('|---|---|---|---|---|---|---|---|')
    url=j['url'] if j['url'].startswith('http') else ''
    ap=f'[link]({url})' if url else j['src']
    lines.append(f"| {i} | {j['score']:.0f} | {j['fit']} | {j['comp'][:26].replace('|','/')} | {j['title'][:40].replace('|','/')} | {j['src'][:9]} | {', '.join(j['why'][:3])} | {ap} |")
open(OUT,'w',encoding='utf-8').write('\n'.join(lines))

from collections import Counter
tc=Counter(tier(j['score']) for j in ranked)
print(f"Ranked {len(ranked)} unique roles (from {len(jobs)} files)")
for t in ['TIER 1 — Apply first (best fit)','TIER 2 — Strong apply','TIER 3 — Good apply','TIER 4 — Stretch / volume','TIER 5 — Low priority']:
    print(f"  {t}: {tc.get(t,0)}")
print("\n=== TOP 30 ===")
for i,j in enumerate(ranked[:30],1):
    print(f"{i:2}. [{j['score']:.0f}] {j['fit'][:2]} {j['comp'][:24]:24} | {j['title'][:38]:38} | {', '.join(j['why'][:2])}")
