#!/usr/bin/env python3
"""Remove junk JDs that slipped through the broad finance/analyst keyword net.
Keeps genuine FP&A, Financial Analyst, Management Reporting, Commercial Finance roles.

Usage:
  python3 trim_junk.py          # today's files only (pipeline default)
  python3 trim_junk.py --all    # full archive (use after tightening rules)

Also importable: from trim_junk import should_remove
"""
import os, re, glob, sys, datetime

JD = "/Users/ashnad/my_career/jds"
TODAY = datetime.date.today().isoformat()

# ── Hard junk: remove regardless of KEEP ──────────────────────────────────────
HARD_JUNK = re.compile(r'''(
    night\s+auditor
  | cctv
  | security\s+guard
  | \bpeon\b
  | \bpacker\b
  | arabic\s+nationality
  | arabic\s+speak(?:er|ing)(?!\s+preferred)
  | arabic\s+speaking\s+only
  | arabic\s+speaker\s+(?:required|only|mandatory|essential)
  | \bit[\s-]?audit\b                          # IT Audit in any form
  | income\s+audit(?:or|s)?\b
  | income\s+audit\s+clerk
  | \bstore\s+auditor\b
  | \bbiosecurity\b
  | data\s+auditor
  | \bsevp\b
  | credit\s+review
  | trading\s+risk
  | treasury\s+credit\s+risk
  | traded\s+.*\s+credit\s+risk
  | tax\s+audit(?:or)?\b
  | auditor\s+.*\btax\b
  | hotel.*audit.*clerk
  | cluster.*audit.*clerk
  | geopolitic(?:al)?\s+risk
  | ot\s+cybersecurity
  | cybersecurity.*compliance
  | accounts?\s+(payable|receivable)\b         # AP/AR clerk roles
  | \bcashier\b | \bteller\b | \bclerk\b | bookkeep
  | receptionist | \bdriver\b | \bnurse\b | \bwarehouse\b
  | \buaen\b                                   # UAE National abbreviated
  | \bmale\s+account                           # gender-gated
  | account\w*[–\-\s]+(?:male|female)\b        # gender-gated suffix
  | \(male\)\s*$ | \(female\)\s*$              # (MALE) or (FEMALE) at end of title
  | secretary\s+(?:cum|and|&)\s+account | account\w*\s+(?:cum|and|&)\s+secretary
  | collector\s+(?:cum|and|&)\s+account | account\w*\s+(?:cum|and|&)\s+collector
  | account\w*\s*(?:cum|&)\s*(?:typist|biller(?!\s+analyst)|peon)
  | account\w*\s*(?:&|and)\s*pro\b            # accountant & PRO (public relations officer)
  | (admin|office|recep|purchase|data\s*entry|coordinator|store|warehouse|document\s*control|cashier|front\s*office)
    \s*(cum|&|/|-|–)\s*account
  | account\w*\s*(cum|&|/|-|–)\s*(admin|office|recep|purchase|data|coordinator|store|warehouse|invoic|document|hr|sales|cashier|front\s*office)
  | unpaid\s+intern                            # unpaid internship roles
  | papua\s+new\s+guinea                       # non-UAE location
  | \btagalog\b | \btamil\b(?!\s+nadu)        # language-gated
  | french[\s-]speaking | french[\s-]speaker   # language-gated
)''', re.I | re.X)

# ── JUNK: remove unless KEEP overrides ────────────────────────────────────────
JUNK = re.compile(r'''(
    \bjunior\s+account | \bjr\.?\s+account | \bassistant\s+account
  | \baudit\s+(intern|associate|assistant)\b
  | \bauditor\s+assistant\b
  | \binformation\s+security\s+(audit|risk)\b
  | credit\s+(risk\s+)?analyst
  | senior\s+(?:specialist|auditor).*credit\s+risk
  | market\s+risk\s+analyst
  | market\s+surveillance
  | \bfraud\s+analyst\b
  | banking\s+card\s+fraud
  | actuar
  | underwriting
  | \bclaims\b
  | data\s+analyst
  | data\s+scientist
  | penetration\s+test
  | cyber\s*security\s+analyst
  | cybersecurity\b
  | security\s+(?:audit|consultant|assurance|specialist|risk\s+management)\b
  | \binfosec\b
  | technology\s+(?:audit|risk|compliance)\b
  | tech\s+(?:audit|risk)\b
  | it\s+(?:risk|compliance)\b
  | \bsales\b
  | business\s+development
  | \bmarketing\b
  | \bprocurement\b
  | supply\s+chain
  | \bhr\s+analyst\b | human\s+resource\s+analyst
  | \brecrui(?:ter|tment)\b
  | teacher | instructor | trainer\b(?!\s+(?:finance|financial))
  | mechanical | civil\s+engineer | electrical\s+engineer
  | product\s+manager | product\s+management
  | \bseo\b
  | spouse\s*visa
  | philippine\s*national | philipino | filipino\s+(?:only|national|speaker)
  | arabic\s+account                           # Arabic-speaking accountant required
  | russian\s*speak(?:er|ing)
  | chinese\s*speak(?:er|ing)
  | mandarin\s*speak(?:er|ing)
  | cantonese\s*speak(?:er|ing)
  | female\s*only | male\s*only
  | external\s+audit(?:or|s)?\b
  | audit\s+(?:semi\s+)?senior\b
  | audit\s+associate\b | associate\s+auditor\b
  | quantitative\s+analyst | quant(?:itative)?\s+risk
  | \brisk\s+analyst\b | senior\s+risk\s+analyst\b
  | geopolitic
  | wealth\s+product\s+risk
  | technical\s+compliance\s+specialist
  | \bavp\s*,?\s+infosec\b
  | \bpayroll\b(?!\s+.*financial)
  | \bfresh\s*graduate\b | \bentry\s+level\b(?=.*non.finance)
  | \bhelper\b | office\s+administrator
  | data\s+entry | \bdocument\s*controller\b
  | insurance\s+analyst | actuarial\s+analyst
  | valuation\s+analyst(?!.*finance) | investment\s+analyst(?!.*finance)
  | \bportfolio\s+manager\b(?!.*finance)
)''', re.I | re.X)

# ── Body-level filters (check full file text) ─────────────────────────────────
NATIONAL_BODY = re.compile(
    r'uae\s+national(s)?\s+(only|preferred|required)'
    r'|emirati\s+(only|candidates|preferred)'
    r'|exclusively\s+(emirati|uae\s+national)'
    r'|\buaen\s+only\b'
    r'|emiratisation\s+(role|position|requirement)',
    re.I
)

DESC_DISQUALIFY = re.compile(r'''(
    \b(?:arabic|mandarin|cantonese|russian|french)\s+(?:is\s+)?(?:a\s+)?(?:must|mandatory|required|essential|prerequisite)\b
  | must\s+(?:speak|read|write)\s+arabic
  | native\s+arabic\s+speaker
  | \bcisa\b.*(?:mandatory|required|essential|must|prerequisite)
  | (?:mandatory|required|essential|must|prerequisite).*\bcisa\b
  | \bcissp\b.*(?:mandatory|required|essential|must|prerequisite)
  | engineering\s+degree\s+(?:required|mandatory|essential)
  | b\.?\s*e\.?\/b\.?\s*tech\s+(?:required|mandatory|essential)
  | minimum\s+(?:of\s+)?(?:8|9|10|11|12|13|14|15)\s+years
  | at\s+least\s+(?:8|9|10|11|12|13|14|15)\s+years
)''', re.I | re.X)

# ── KEEP: these title patterns always pass (HARD_JUNK still overrides) ────────
KEEP = re.compile(r'''(
    financial\s+analyst | finance\s+analyst
  | fp&?a | financial\s+planning
  | budget\s+analyst | budgeting\s+analyst
  | commercial\s+(?:analyst|finance)
  | management\s+report(?:ing)?
  | management\s+account
  | cost\s+analyst | cost\s+account | cost\s+controller
  | revenue\s+analyst
  | finance\s+business\s+partner | business\s+finance\s+partner
  | financial\s+report(?:ing)?
  | financial\s+controller | finance\s+controller
  | financial\s+modell?(?:er|ing)
  | pricing\s+analyst
  | treasury\s+analyst
  | planning\s+analyst | forecasting\s+analyst
  | decision\s+support\s+analyst
  | consolidation\s+analyst | group\s+report(?:ing)?
  | profitability\s+analyst | margin\s+analyst
  | business\s+performance\s+analyst | financial\s+performance\s+analyst
  | business\s+support\s+analyst
  | senior\s+account(?:ant)? | general\s+account(?:ant)?
  | financial\s+account(?:ant)? | chief\s+account(?:ant)?
  | finance\s+officer | finance\s+associate
  | variance\s+analysis | p&l\s+analyst
)''', re.I | re.X)


def should_remove(title: str, body: str = "") -> tuple[bool, str]:
    """Return (remove, reason). Pure function — no file I/O."""
    # 1. Hard junk wins over everything
    if HARD_JUNK.search(title):
        return True, "hard junk"

    # 2. Nationality-gated in body
    if NATIONAL_BODY.search(body):
        return True, "nationality-gated (body)"

    # 3. Description disqualifiers (only when body is available)
    if body and DESC_DISQUALIFY.search(body):
        return True, "description disqualifier"

    # 4. KEEP overrides JUNK
    if KEEP.search(title):
        return False, "keep"

    # 5. JUNK
    if JUNK.search(title):
        return True, "junk title"

    return False, "ok"


def _run(files):
    removed = []
    for f in sorted(files):
        txt = open(f, encoding="utf-8", errors="ignore").read()
        m = re.search(r'^#\s+(.+)', txt, re.M)
        title = m.group(1).strip() if m else ""
        drop, reason = should_remove(title, txt)
        if drop:
            removed.append((os.path.basename(f), title, reason))
            os.remove(f)
    return removed


if __name__ == "__main__":
    all_files = "--all" in sys.argv
    if all_files:
        files = glob.glob(JD + "/*.md")
        label = "FULL ARCHIVE"
    else:
        files = glob.glob(JD + "/*" + TODAY + "*.md")
        label = "today"

    removed = _run(files)
    print(f"Removed {len(removed)} junk files ({label})")
    for item in removed:
        print(f"  - [{item[2]}] {item[1]}")
    remaining = len([f for f in os.listdir(JD) if f.endswith('.md')])
    print(f"Total JDs in archive: {remaining}")
