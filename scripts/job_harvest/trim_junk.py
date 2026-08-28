#!/usr/bin/env python3
"""Remove TODAY's clerical/junior junk that slipped via the broad 'accountant' keyword.
Keeps genuine adjacent roles (senior/general/management/cost/financial/chief accountant,
finance officer, analyst/FP&A). Only touches 2026-08-28 files."""
import os, re, glob
JD="/Users/ashnad/my_career/jds"; TODAY="2026-08-28"

# reject if TITLE matches any (clerical / junior / below-level / nationality-gated clerical)
JUNK = re.compile(r'''(
   junior\s+account | assistant\s+account | account\w*\s*(cum|&|/|-|–)\s*(admin|office|recep|purchase|data|coordinator|store|warehouse|invoic|document|hr|sales|cashier)
 | (admin|office|recep|purchase|data\s*entry|coordinator|store|warehouse|document\s*control|cashier)\s*(cum|&|/|-|–)\s*account
 | \bintern\b | \btrainee\b(?!\s+cost\s+analyst) | \bcashier\b | \bclerk\b | bookkeep | data\s*entry
 | spouse\s*visa | philippine\s*national | russian\s*speaking | \(arabic\) | female\s*only
 | receptionist | \bteller\b | collection\s+officer | document\s*controller
 | assistant\s+account | account\w*\s*admin | admin\s+account | accounts?\s+(payable|receivable)\b
 | fresh\s*graduate | \bhelper\b | office\s+administrator
)''', re.I | re.X)

# always KEEP if title has a clear analyst/senior-finance token even if 'account' present
KEEP = re.compile(r'financial analyst|finance analyst|fp&a|fpa|financial planning|budget analyst|'
                  r'commercial|revenue analyst|management report|business partner|reporting analyst|'
                  r'senior account|general account|management account|cost account|financial account|'
                  r'chief account|finance officer|financial controller|cost controller|modeller|modeler|'
                  r'planning analyst|treasury', re.I)

removed=[]
for f in sorted(glob.glob(JD+"/*"+TODAY+"*.md")):
    txt=open(f,encoding="utf-8",errors="ignore").read()
    m=re.search(r'^#\s+(.+)',txt,re.M); title=m.group(1).strip() if m else ""
    if KEEP.search(title):
        continue
    if JUNK.search(title):
        removed.append((os.path.basename(f),title)); os.remove(f)
print(f"removed {len(removed)} clerical/junior junk files")
for b,t in removed: print("  -",t)
print("today remaining:", len(glob.glob(JD+"/*"+TODAY+"*.md")))
