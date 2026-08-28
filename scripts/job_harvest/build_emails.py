#!/usr/bin/env python3
"""Merge harvested emails (jobspy CSV + JD files) -> deduped cold-email contact list
with company context + humanized cold-email drafts. Writes COLD_EMAILS.md."""
import csv, re, os, json, glob

ROOT="/Users/ashnad/my_career"
EMAIL_RE=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
JUNK=re.compile(r'example|sentry|wixpress|@2x|\.png|\.jpg|domain\.com|test@|yourcompany|noreply|no-reply', re.I)

contacts={}  # email -> {email, company, source, context}

def add(email, company, source, context=""):
    email=email.strip().lower().rstrip('.').replace('.ltdwith','.ltd')
    if not EMAIL_RE.fullmatch(email) or JUNK.search(email): return
    if email.endswith(('.png','.jpg','.gif')): return
    if email not in contacts:
        contacts[email]={"email":email,"company":company or "","source":source,"context":context}
    elif company and not contacts[email]["company"]:
        contacts[email]["company"]=company

# 1) jobspy CSV
csvp=os.path.join(ROOT,"scratchpad/jobpipe/harvested_emails.csv")
if os.path.exists(csvp):
    for r in csv.DictReader(open(csvp)):
        raw=r.get("email","")
        comp=r.get("company","") or ""
        title=r.get("title","") or ""
        for e in EMAIL_RE.findall(raw):
            add(e, comp, "job posting (Indeed)", title)

# 2) JD files
for f in glob.glob(os.path.join(ROOT,"jds","*.md")):
    txt=open(f,encoding="utf-8",errors="ignore").read()
    cm=re.search(r'\*\*Company:\*\*\s*(.+)',txt); comp=cm.group(1).strip() if cm else ""
    for e in set(EMAIL_RE.findall(txt)):
        add(e, comp, "job posting (JD archive)")

rows=list(contacts.values())

def company_from_email(e):
    dom=e.split('@')[1]
    base=dom.split('.')[0]
    return base

def draft(c):
    comp=c["company"].strip()
    e=c["email"]
    local=e.split('@')[0].lower()
    # generic inbox vs named person
    generic = any(k in local for k in ["hr","recruit","career","talent","info","jobs","cv","partner","hrd","hiring"])
    name= comp if comp and comp.lower() not in ("nan","confidential","") else company_from_email(e).title()
    if generic:
        body=(f"Subject: Finance Analyst / FP&A - CV\n\n"
              f"Hi,\n\n"
              f"I'm looking to move into an FP&A or finance analyst role in Dubai and wanted to send my CV across in case there's anything suitable at {name}.\n\n"
              f"Quick background: I've got an accounting foundation from EY plus an M.Sc. in Financial Economics, and I've built out budgeting, forecasting and variance models along with an ERP migration from Tally to Odoo. I'm comfortable in Excel and building out Power BI dashboards.\n\n"
              f"CV is attached. Happy to share more if useful.\n\n"
              f"Thanks,\nMuhammed Ashnad\n+971 54 325 5352")
    else:
        first=local.split('.')[0].title() if '.' in local else ''
        greet=f"Hi {first}," if first and len(first)>1 else "Hi,"
        body=(f"Subject: FP&A / Finance Analyst in Dubai\n\n"
              f"{greet}\n\n"
              f"Came across your details while looking at finance roles in Dubai. I'm moving into FP&A from an accounting background and wanted to send my CV over in case you're working on anything relevant"
              + (f" at {name}" if comp and comp.lower() not in ('nan','confidential') else "") + ".\n\n"
              f"Short version: EY accounting background, M.Sc. Financial Economics, and hands-on work building budgeting/forecasting models plus a Tally to Odoo ERP migration. Strong Excel, learning Power BI.\n\n"
              f"CV attached. Would be glad to talk if there's a fit.\n\n"
              f"Thanks,\nMuhammed Ashnad\n+971 54 325 5352")
    return body

# order: named recruiter/agency first, then hr/recruitment inboxes, then info/generic
def rank(c):
    l=c["email"].split('@')[0]
    if any(k in l for k in ["recruit","talent"]): return 0
    if "hr" in l or "career" in l or "jobs" in l or "cv" in l: return 1
    if "." in l and not any(k in l for k in ["info","hr","jobs"]): return 0  # named person
    return 2
rows.sort(key=rank)

json.dump(rows, open(os.path.join(ROOT,"scratchpad/jobpipe/emails_master.json"),"w"), indent=1)

out=[]
out.append("# Cold Email Contacts — 2026-08-28\n")
out.append(f"**{len(rows)} real employer / recruiter emails** harvested from live UAE finance job postings (Indeed `emails` field + JD archive). All are addresses the employer/agency published on the posting.\n")
out.append("**Sending is Ashnad's action.** Attach the master CV (`resumes/Muhammed_Ashnad_Resume.pdf`). Send in small batches, personalise the company line where it says a generic name. Humanized drafts below follow the repo writing rules (no em dashes, no AI openers).\n")
out.append("## Contact list\n")
out.append("| # | Email | Company | Source |")
out.append("|---|---|---|---|")
for i,c in enumerate(rows,1):
    out.append(f"| {i} | {c['email']} | {c['company'] or company_from_email(c['email']).title()} | {c['source']} |")
out.append("\n---\n\n## Draft templates\n")
out.append("Two humanized drafts are used depending on whether the address is a generic inbox (hr@/careers@) or a named person. Examples:\n")
out.append("### Generic inbox (hr@ / careers@ / recruitment@)\n```\n"+draft({"email":"hr@example.com","company":"[Company]"})+"\n```\n")
out.append("### Named recruiter / person\n```\n"+draft({"email":"jane.doe@example.com","company":"[Company]"})+"\n```\n")
open(os.path.join(ROOT,"COLD_EMAILS.md"),"w",encoding="utf-8").write("\n".join(out))
print(f"wrote {len(rows)} contacts to COLD_EMAILS.md")
gen=sum(1 for c in rows if any(k in c['email'].split('@')[0] for k in ['hr','recruit','career','talent','info','jobs','cv']))
print("generic inboxes:",gen," named/other:",len(rows)-gen)
