#!/usr/bin/env python3
"""Process LinkedIn target list -> cleaned records + humanized connection notes,
then append a structured section to NETWORKING.md. Notes follow the repo's
humanized rules (no em dashes, no AI openers, short, specific to their company)."""
import json, re, os

SRC="/Users/ashnad/my_career/scratchpad/jobpipe/linkedin_targets.json"
NET="/Users/ashnad/my_career/NETWORKING.md"

# Load already-saved profile URLs from NETWORKING.md so we never duplicate
_known_urls: set = set()
if os.path.exists(NET):
    _net_text = open(NET, encoding="utf-8", errors="ignore").read()
    _known_urls = set(re.findall(r'https://www\.linkedin\.com/in/[a-zA-Z0-9\-_%]+', _net_text))
    print(f"Loaded {len(_known_urls)} existing profile URLs from NETWORKING.md")

data=json.load(open(SRC))

def clean_name(n):
    n=re.sub(r'•.*','',n)
    n=re.split(r',', n)[0]                 # drop ", CFA" etc
    n=re.sub(r'\s*[-–]\s*(MBA|CFA|CMA|ACCA|CPA|CA|FMVA|PhD|MSc|FCCA|ACA)\b.*','',n,flags=re.I)
    return n.strip()

HONOR=re.compile(r'^(dr|mr|ms|mrs|eng|ca|cpa|cfa|cma|acca|aca|fcca|mba|the)\.?$', re.I)
def first_name(n):
    n=clean_name(n)
    parts=[p for p in n.split() if p and not HONOR.match(p)]
    return parts[0] if parts else (n.split()[0] if n.split() else n)

def company(headline):
    h=headline
    if ' at ' in h:
        c=h.split(' at ')[-1]
    else:
        return ''
    # cut at pipe/bullet
    c=re.split(r'[|•]', c)[0]
    # strip trailing ", <location>" only
    c=re.sub(r',\s*(Dubai|Abu Dhabi|Sharjah|UAE|United Arab Emirates|Dubaï|Middle East|MENA|GCC)\s*$','',c,flags=re.I).strip()
    c=re.sub(r',.*$','',c)          # drop anything after a comma (usually location/qualifier)
    c=re.sub(r'\s+',' ',c).strip(' -.')
    return c if len(c)>1 else ''

def tier(headline):
    h=headline.lower()
    if re.search(r'talent|recruit|acquisition|hr |human resource|hiring', h): return "Gatekeeper (HR/TA)"
    if re.search(r'cfo|chief financial|vp finance|vice president|group cfo', h): return "Decision-maker (CFO/VP)"
    if re.search(r'director|head of', h): return "Decision-maker (Director/Head)"
    if re.search(r'manager|controller|business partner|lead', h): return "Hiring manager"
    return "Senior finance"

def note(fn, comp, t, headline):
    hl=headline.lower()
    c = comp if comp and len(comp)>1 else ""
    if "Gatekeeper" in t:
        if c:
            n=f"Hi {fn}, I'm a finance analyst moving into FP&A in Dubai. Saw you look after talent at {c}, wanted to connect in case anything relevant comes up."
        else:
            n=f"Hi {fn}, I'm a finance analyst targeting FP&A roles in Dubai. Saw you work in finance recruitment here and wanted to connect."
    else:
        if c:
            n=f"Hi {fn}, came across your profile while looking at finance folks in Dubai. I'm moving into FP&A from an accounting background and following what {c} does. Would be good to connect."
        else:
            n=f"Hi {fn}, came across your profile while looking at finance leaders in Dubai. I'm an analyst moving into FP&A and keen to connect with people doing it well."
    # LinkedIn free connection note cap ~200 chars: trim if needed
    if len(n)>200:
        if c:
            n=f"Hi {fn}, came across your profile looking at finance folks in Dubai. I'm moving into FP&A and following {c}. Would be good to connect."
        else:
            n=f"Hi {fn}, came across your profile looking at finance leaders in Dubai. I'm an analyst moving into FP&A. Would be good to connect."
    if len(n)>200:
        n=n[:196].rsplit(' ',1)[0]+'...'
    return n

rows=[]; seen=set(); skipped_dups=0
NONFIN=re.compile(r'financ|account|fp&a|fpa\b|cfo|controller|treasury|audit|budget|fp and a|commercial finance|revenue', re.I)
for d in data:
    name=clean_name(d.get('name',''))
    if not name or name.lower() in seen: continue
    hl=d.get('headline','')
    t=tier(hl)
    if len(hl.strip())<3:
        continue
    # dedup against already-saved profiles
    profile_url = d.get('url', '')
    norm_url = profile_url.split('?')[0].rstrip('/').lower()
    if norm_url and any(norm_url in k.lower() or k.lower() in norm_url for k in _known_urls):
        skipped_dups += 1
        continue
    seen.add(name.lower())
    comp=company(hl)
    fn=first_name(name)
    rows.append({"name":name,"first":fn,"headline":hl.strip(),"company":comp,"loc":d.get('loc',''),"tier":t,"url":profile_url,"note":note(fn,comp,t,hl)})

if skipped_dups:
    print(f"Skipped {skipped_dups} already-saved profiles (dedup)")

# order by tier priority
prio={"Decision-maker (CFO/VP)":0,"Decision-maker (Director/Head)":1,"Hiring manager":2,"Gatekeeper (HR/TA)":3,"Senior finance":4}
rows.sort(key=lambda r:prio.get(r['tier'],5))

json.dump(rows, open("/Users/ashnad/my_career/scratchpad/jobpipe/networking_rows.json","w"), indent=1)

# build markdown section
out=[]
out.append(f"\n\n---\n\n## 201 CONNECTION TARGETS — 2026-08-28 (LinkedIn people search, logged-in)\n")
out.append(f"**{len(rows)} senior UAE finance decision-makers + hiring managers + HR/TA gatekeepers, harvested per the Connect-UP strategy.**")
out.append("Draft notes below follow the humanized rules and fit LinkedIn's ~200-char connection-note limit. **Sending is Ashnad's action** (LinkedIn flags automation and limits invites to ~20/day; send in small daily batches).\n")
from collections import Counter
cc=Counter(r['tier'] for r in rows)
out.append("**Tier breakdown:** " + " · ".join(f"{k}: {v}" for k,v in cc.items()) + "\n")
out.append("| # | Name | Title / Company | Tier | Profile | Draft connection note |")
out.append("|---|---|---|---|---|---|")
for i,r in enumerate(rows,1):
    tc=(r['headline'][:60]).replace("|","/")
    out.append(f"| {i} | {r['name']} | {tc} | {r['tier']} | [profile]({r['url']}) | {r['note'].replace('|','/')} |")
open(NET,"a",encoding="utf-8").write("\n".join(out))
print(f"wrote {len(rows)} targets to NETWORKING.md")
print("tiers:", dict(cc))
print("sample note:", rows[0]['note'])
