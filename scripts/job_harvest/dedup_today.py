#!/usr/bin/env python3
"""SAFE dedup: only removes TODAY's (2026-08-28) scraped files that duplicate an
earlier-dated archive file or an earlier today's file. Never deletes archive files."""
import os, re, unicodedata as ud
JD="/Users/ashnad/my_career/jds"; TODAY="2026-08-28"

def norm(s):
    s=ud.normalize("NFKD",s or ""); return re.sub(r'[^a-z0-9]','',s.lower())
def cnorm(s):
    return re.sub(r'(llc|fzco|fze|pjsc|llp|ltd|limited|group|international)$','',norm(s))
def tnorm(s):
    t=norm(s); t=re.sub(r'^jd','',t)
    for loc in ["dubai","abudhabi","sharjah","uae","unitedarabemirates"]: t=t.replace(loc,"")
    return t[:22]
def meta(f):
    txt=open(os.path.join(JD,f),encoding="utf-8",errors="ignore").read()
    u=re.search(r'URL:\s*(\S+)',txt); url=u.group(1).strip().lower() if u else ""
    if not url.startswith("http"): url=""
    c=re.search(r'\*\*Company:\*\*\s*(.+)',txt); comp=c.group(1).strip() if c else ""
    t=re.search(r'^#\s+(.+)',txt,re.M); title=t.group(1).strip() if t else ""
    d=re.search(r'Date Found:\s*(\S+)',txt); date=d.group(1) if d else "0000-00-00"
    return url,comp,title,date

files=sorted(f for f in os.listdir(JD) if f.endswith(".md"))
recs=[(f,)+meta(f) for f in files]
# process archive first (earlier dates) to seed seen-sets
recs.sort(key=lambda r:(r[4], r[0]))
seen_url=set(); seen_ct=set(); drop=[]
for f,url,comp,title,date in recs:
    ck=(cnorm(comp),tnorm(title))
    isdup = (url and url in seen_url) or (ck[0] and ck in seen_ct)
    if isdup and date==TODAY:
        drop.append(f); continue
    if isdup and date!=TODAY:
        # archive internal dup - leave it, just don't re-add
        continue
    if url: seen_url.add(url)
    if ck[0]: seen_ct.add(ck)
for f in drop:
    os.remove(os.path.join(JD,f))
print(f"removed {len(drop)} today-dups")
for f in drop: print("  -",f)
import glob
print("today remaining:", len(glob.glob(JD+"/*"+TODAY+"*.md")))
print("total jds:", len([f for f in os.listdir(JD) if f.endswith('.md')]))
