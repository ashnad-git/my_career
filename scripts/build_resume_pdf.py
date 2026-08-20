"""
Resume PDF Builder — Muhammed Ashnad K
======================================
Builds any resume (master or tailored) as a professionally formatted PDF.
Uses reportlab — same output every time. NO Chrome, NO pandoc, NO HTML.

HOW TO USE
----------
Master resume (regenerate from scratch):
    python3 scripts/build_resume_pdf.py master

Tailored resume for a specific job:
    python3 scripts/build_resume_pdf.py chalhoub
    python3 scripts/build_resume_pdf.py <key>   ← add new keys in RESUMES dict below

HOW TO ADD A NEW TAILORED RESUME
---------------------------------
1. Build the tailored content (summary, bullets, skills) in resumes/<Company>_<Role>.md
2. Copy the relevant RESUME_* function below, rename it, edit the content
3. Add the key → function mapping in RESUMES dict
4. Run: python3 scripts/build_resume_pdf.py <your_key>

STYLE REFERENCE
---------------
- Font: Helvetica (name bold 20pt blue, section bold 8.5pt blue, bullets 8.5pt)
- Blue: #1e3a5f  Dark: #1a1a1a  Mid: #444444  Light: #888888  Rule: #cccccc
- Margins: left/right 17mm, top/bottom 14mm
- ATS-safe: single column, all text selectable, no images
- Page size: A4
"""

import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

# ── Colours ───────────────────────────────────────────────────────────────────
DARK  = HexColor("#1a1a1a")
MID   = HexColor("#444444")
LIGHT = HexColor("#888888")
RULE  = HexColor("#cccccc")
BLUE  = HexColor("#1e3a5f")

LINKEDIN = "linkedin.com/in/muhammed-ashnad-k"
CONTACT_LINE = f"+971 562303121  ·  muhammedashnad@gmail.com  ·  Dubai, UAE  ·  {LINKEDIN}"

# ── Styles (shared across all resumes) ────────────────────────────────────────
def st(name, **kw):
    d = dict(fontName="Helvetica", fontSize=9, textColor=DARK, leading=12, spaceAfter=0, spaceBefore=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME    = st("Name",   fontName="Helvetica-Bold",       fontSize=20, textColor=BLUE,  leading=24, spaceAfter=2)
HEAD    = st("Head",   fontName="Helvetica",             fontSize=9,  textColor=MID,   leading=12, spaceAfter=2)
CONTACT = st("Cont",   fontName="Helvetica",             fontSize=8.5,textColor=LIGHT, leading=11, spaceAfter=0)
SECTION = st("Sec",    fontName="Helvetica-Bold",        fontSize=8.5,textColor=BLUE,  leading=11, spaceBefore=8, spaceAfter=2)
EMPLOYER= st("Emp",    fontName="Helvetica-Bold",        fontSize=9.5,textColor=DARK,  leading=12, spaceBefore=6, spaceAfter=0)
ROLE    = st("Role",   fontName="Helvetica-BoldOblique", fontSize=8.5,textColor=MID,   leading=11, spaceAfter=2)
DATE_ST = st("Date",   fontName="Helvetica-Oblique",     fontSize=8.5,textColor=LIGHT, leading=12)
SUB     = st("Sub",    fontName="Helvetica-Bold",        fontSize=8.5,textColor=DARK,  leading=11, spaceBefore=3, spaceAfter=1)
BULLET  = st("Bul",    fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=11.5, leftIndent=10, firstLineIndent=-10, spaceAfter=1.5)
BODY    = st("Body",   fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=12, spaceAfter=4)
SKLBL   = st("SklLbl", fontName="Helvetica-Bold",        fontSize=8.5,textColor=MID,   leading=11, spaceAfter=1)
SKBDY   = st("SklBdy", fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=11.5,spaceAfter=3)
EDU_DEG = st("EduDeg", fontName="Helvetica-Bold",        fontSize=9,  textColor=DARK,  leading=12, spaceBefore=4, spaceAfter=0)
EDU_INS = st("EduIns", fontName="Helvetica",             fontSize=8.5,textColor=MID,   leading=11, spaceAfter=3)
CERT    = st("Cert",   fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=12, leftIndent=10, firstLineIndent=-10, spaceAfter=1.5)

# ── Helpers ───────────────────────────────────────────────────────────────────
def rule():
    return HRFlowable(width="100%", thickness=0.4, color=RULE, spaceAfter=3, spaceBefore=0)

def b(text):
    return Paragraph(f"• {text}", BULLET)

def cert_line(text):
    return Paragraph(f"• {text}", CERT)

def section(title):
    return [Paragraph(title, SECTION), rule()]

def job(company, loc, role_title, dates):
    left = f"<b>{company}</b>  <font color='#888888' size='7.5'>— {loc}</font>"
    t = Table(
        [[Paragraph(left, EMPLOYER), Paragraph(dates, DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "BOTTOM"),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    return [t, Paragraph(role_title, ROLE)]

def edu_row(degree, institution, location, year):
    t = Table(
        [[Paragraph(f"<b>{degree}</b>", EDU_DEG), Paragraph(year, DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    return [t, Paragraph(f"{institution}  ·  {location}", EDU_INS)]

def header(headline):
    return [
        Paragraph("Muhammed Ashnad K", NAME),
        Paragraph(headline, HEAD),
        Paragraph(CONTACT_LINE, CONTACT),
        Spacer(1, 5),
        rule(),
    ]

def build_pdf(story, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=17*mm, rightMargin=17*mm,
        topMargin=14*mm,  bottomMargin=14*mm,
        title="Muhammed Ashnad K — Resume",
        author="Muhammed Ashnad K",
    )
    doc.build(story)
    print(f"PDF saved: {output_path}")

# ── SHARED SECTIONS (used in multiple resumes) ────────────────────────────────

def ey_tax_analyst_bullets():
    """EY Tax Analyst bullets — standard version used in most resumes."""
    return [
        b("Conducted financial analysis and review of client financial statements, workpapers, "
          "and supporting records; identified discrepancies, investigated root causes, and "
          "coordinated resolution with stakeholders."),
        b("Reconciled financial data across multiple sources (tax forms, client records, supporting "
          "schedules) — ensuring accuracy and consistency across reporting outputs."),
        b("Analysed high volumes of financial data across multi-client engagements, applying "
          "structured investigation methodology to identify errors and inconsistencies."),
        b("Prepared and reviewed client financial filings; maintained audit-ready documentation "
          "under strict reporting deadlines."),
    ]

def ey_intern_bullets():
    """EY US Tax Intern bullets — standard version."""
    return [
        b("Reviewed financial documents and supporting schedules for accuracy and compliance; "
          "validated client statements and reconciled supporting data."),
        b("Supported documentation and financial reporting workflows requiring strong analytical "
          "attention to detail and cross-team coordination."),
    ]

def education_section():
    """Standard education section — same across all resumes."""
    s = section("Education")
    s += edu_row("M.Sc. Financial Economics",
                 "Manipal Academy of Higher Education", "Manipal, India", "2021 – 2023")
    s += edu_row("BBA — Finance (Major)",
                 "St. Aloysius College", "Mangalore, India", "2017 – 2020")
    return s

# ── MASTER RESUME ─────────────────────────────────────────────────────────────

def build_master():
    """
    Master resume — broad FP&A/Finance positioning.
    Output: Muhammed_Ashnad_Resume.pdf
    Source: Muhammed_Ashnad_Resume.md
    """
    story = []
    story += header(
        "Finance Professional  |  Financial Analysis &amp; FP&amp;A  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance professional with M.Sc. Financial Economics and Big Four experience at Ernst &amp; Young, "
        "currently managing financial reporting and operational finance at Promotech Advertising, Dubai. "
        "My background spans financial statement analysis, multi-source reconciliation, and structured "
        "client documentation at EY, through to management reporting, account reconciliation, ERP "
        "implementation, and month-end close in an active business environment. "
        "Pursuing CMA (US).",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Financial Analysis &amp; FP&amp;A",
         "Financial Reporting  ·  Management Reporting  ·  Variance Analysis  ·  P&amp;L Analysis  ·  "
         "Financial Statement Analysis  ·  Budgeting &amp; Forecasting  ·  Cash Flow Analysis  ·  "
         "KPI Tracking  ·  Scenario Analysis"),
        ("Technical Tools",
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  Power BI (DAX, Dashboards)  ·  "
         "SQL  ·  Python (automation &amp; data pipelines)  ·  Odoo ERP  ·  Tally ERP"),
        ("Accounting Foundation",
         "Month-End Close  ·  Account Reconciliation  ·  AP/AR Management  ·  "
         "ERP Implementation  ·  Audit Support  ·  Discrepancy Investigation"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Finance Operations &amp; Systems", SUB))
    story.append(b("Designed and implemented a finance documentation framework from scratch — established "
                   "standardized filing, record-keeping, and audit-trail processes, reducing document "
                   "retrieval time from days to minutes."))
    story.append(b("Led full ERP migration from Tally to Odoo: managed data validation, inventory database "
                   "cleansing, master data review, and cross-team co-ordination from planning through go-live."))
    story.append(b("Co-ordinate with ERP partners on system support, data reconciliations, and ongoing updates."))
    story.append(Paragraph("Financial Reporting &amp; Analysis", SUB))
    story.append(b("Prepare monthly financial reports, management summaries, and performance packs for the CEO — "
                   "covering revenue, gross margin, cost variances, and key operational metrics."))
    story.append(b("Run month-end close: account reconciliations, ledger reviews, and pre/post-closing checks; "
                   "clear all open items and discrepancies before close date each month."))
    story.append(b("Manage AP/AR across 475 active accounts — 319 suppliers and 156 clients; review Statements "
                   "of Account, investigate discrepancies, and follow up on outstanding balances."))
    story.append(b("Co-ordinate supplier and vendor payments while maintaining complete supporting documentation; "
                   "process 1,000+ payment transactions per year."))
    story.append(b("Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
                   "organized, audit-ready documentation and timely stakeholder co-ordination."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story += ey_tax_analyst_bullets()
    story.append(b("Co-ordinated with EY U.S. teams across time zones to support timely completion of "
                   "financial and documentation requirements under strict deadlines."))

    story.extend(section("Internship Experience"))
    story.extend(job("BB Advisory", "Bangalore, India", "Financial Analyst Intern", "Jan 2023"))
    story.append(b("Assisted in preparing financial analysis reports and valuation models for client engagements."))
    story.append(b("Reviewed financial data and compliance-related documentation to address relevant stakeholder requirements."))
    story.append(b("Supported financial research and contributed to structured, client-ready financial reporting."))
    story.append(Spacer(1, 4))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story.extend(section("Projects"))
    proj_t = Table(
        [[Paragraph("<b>Personal Financial Data Analytics System</b>", EDU_DEG),
          Paragraph("2024 – Present", DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    proj_t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    story.append(proj_t)
    story.append(Paragraph(
        "Independently built an end-to-end financial data pipeline: automated ingestion from "
        "multiple live market data APIs, real-time processing, structured data storage, and "
        "analytical reporting outputs. Built entirely in Python.",
        EDU_INS
    ))

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US / IMA) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "ESG Certificate — Bloomberg LP",
        "Financial Reporting — University of Illinois",
        "Economics of Money and Banking — Columbia University",
        "Bloomberg &amp; NSMART Certification — IIM Bengaluru",
        "Applied Econometrics — Dr. BR Ambedkar School of Economics",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/Muhammed_Ashnad_Resume.pdf")


# ── CHALHOUB — FP&A Associate I (Zimmermann) ─────────────────────────────────

def build_chalhoub():
    """
    Tailored for: Chalhoub Group — FP&A Associate I (Zimmermann)
    URL: https://www.linkedin.com/jobs/view/4452830346
    Key changes vs master:
    - Headline: FP&A & Commercial Finance (mirrors JD language)
    - Summary: Names Chalhoub explicitly
    - Promotech: Reporting section leads (not ERP); 3 new bullets:
        variance commentary, budget trackers, VAT support
    - Core skills: No SQL/Python/Power BI (not in JD); VAT added
    - BB Advisory: Removed (1-month internship adds nothing here)
    - Certs: Trimmed to 4 (removed academic-only entries)
    Output: resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf
    """
    story = []
    story += header(
        "FP&amp;A &amp; Commercial Finance  |  Management Reporting  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance professional with M.Sc. Financial Economics and Big Four experience at Ernst &amp; Young, "
        "seeking to join Chalhoub Group's FP&amp;A team in a brand-level analytical role. "
        "I bring hands-on experience in management reporting, P&amp;L variance analysis, month-end close, "
        "and ERP-driven operational finance — with direct exposure to producing monthly financial packs "
        "for executive stakeholders and supporting annual audit and indirect tax processes. "
        "Pursuing CMA (US).",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Financial Analysis &amp; FP&amp;A",
         "Management Reporting  ·  Variance Analysis &amp; Commentary  ·  P&amp;L Analysis  ·  "
         "Budgeting &amp; Cost Tracking  ·  Financial Reporting &amp; MIS  ·  KPI Tracking  ·  "
         "Financial Statement Analysis  ·  Cash Flow Analysis"),
        ("Technical Tools",
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  "
         "Odoo ERP  ·  Tally ERP  ·  Microsoft PowerPoint"),
        ("Accounting Foundation",
         "Month-End Close  ·  Account Reconciliation  ·  AP/AR Management  ·  "
         "ERP Implementation &amp; Migration  ·  VAT &amp; Indirect Tax Support  ·  "
         "Audit Support  ·  Stakeholder Coordination"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Financial Reporting &amp; Analysis", SUB))
    story.append(b("Prepare monthly P&amp;L reports, management summaries, and board-ready performance packs for "
                   "CEO review — analysing revenue, gross margin, and cost variances versus prior periods, with "
                   "written variance commentary explaining key drivers."))
    story.append(b("Maintain budget trackers for operational expenditure; monitor actuals versus budget across "
                   "cost categories and flag material variances for management review."))
    story.append(b("Assist in UAE VAT calculations and indirect tax filings in coordination with line manager; "
                   "support reconciliation of tax positions ahead of filing deadlines."))
    story.append(b("Run month-end close: account reconciliations, ledger reviews, pre/post-closing checks, "
                   "and discrepancy clearance across all accounts before close date each month."))
    story.append(b("Manage AP/AR across 475 active accounts — 319 suppliers and 156 clients; investigate "
                   "discrepancies and follow up on outstanding balances."))
    story.append(b("Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
                   "organised, audit-ready documentation and timely issue resolution."))
    story.append(Paragraph("Finance Systems Transformation", SUB))
    story.append(b("Led full ERP migration from Tally to Odoo: data validation, inventory database cleansing, "
                   "master data review, and cross-team co-ordination from planning through go-live — directly "
                   "comparable to ERP system transitions in enterprise environments."))
    story.append(b("Took over a finance function with no filing system or documentation; rebuilt the entire "
                   "structure from scratch — document retrieval reduced from days to minutes."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story += ey_tax_analyst_bullets()

    story.extend(section("Internship Experience"))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US / IMA) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "ESG Certificate — Bloomberg LP",
        "Financial Reporting — University of Illinois",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf")


# ── NAFFCO — FP&A Analyst ─────────────────────────────────────────────────────

def build_naffco():
    """
    Tailored for: NAFFCO — FP&A (Financial Planning & Analysis) Analyst
    URL: https://www.linkedin.com/jobs/view/4450359617
    Deadline: Aug 22, 2026
    Key changes vs master:
    - Headline: FP&A Analyst | Budgeting & Variance Analysis (mirrors JD title)
    - Summary: Names NAFFCO; uses rolling forecasts, variance analysis, cost control language
    - Skills: Lead with budgeting/forecasting/variance; add Power BI; keep Odoo ERP
    - Promotech: Financial Reporting leads; budget-to-actual / YoY / cost control language throughout
    - BB Advisory: Removed (space; adds nothing for industrial FP&A)
    - Certs: 3 items only
    Output: resumes/Muhammed_Ashnad_NAFFCO_FPnA_Analyst.pdf
    """
    story = []
    story += header(
        "FP&amp;A Analyst  |  Budgeting &amp; Variance Analysis  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance professional with M.Sc. Financial Economics and Big Four (EY) experience, currently leading "
        "financial reporting, budget-to-actual variance analysis, and cost control for a commercial enterprise "
        "in Dubai. I prepare monthly management reports with written variance commentary, run month-end close, "
        "track departmental expenditure against rolling targets, and support ERP-driven finance operations — "
        "building the analytical foundation an FP&amp;A function requires. Pursuing CMA (US).",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Financial Analysis &amp; FP&amp;A",
         "Budgeting &amp; Rolling Forecasts  ·  Variance Analysis (Budget vs Actual, YoY)  ·  "
         "Management Reporting &amp; MIS  ·  Cash Flow Analysis  ·  KPI Tracking  ·  "
         "Financial Modelling  ·  Scenario Analysis  ·  P&amp;L Analysis"),
        ("Technical Tools",
         "Advanced Excel (Pivot Tables, VLOOKUP/XLOOKUP, Financial Models, Power Query)  ·  "
         "Power BI (Dashboards, DAX)  ·  Odoo ERP  ·  Tally ERP  ·  Microsoft PowerPoint"),
        ("Accounting Foundation",
         "Month-End Close  ·  Account Reconciliation  ·  AP/AR Management  ·  "
         "ERP Implementation &amp; Migration  ·  Cost Monitoring  ·  Audit Support"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Financial Reporting &amp; Analysis", SUB))
    story.append(b("Prepare monthly management reports, dashboards, and performance packs for CEO review — "
                   "analysing revenue, gross margin, and cost variances versus budget and prior year, "
                   "with written commentary explaining key drivers and recommending corrective actions."))
    story.append(b("Track departmental and operational expenditure against rolling budget targets; "
                   "investigate material variances and escalate cost control issues with actionable "
                   "recommendations to management."))
    story.append(b("Run month-end close: account reconciliations, ledger reviews, pre/post-closing checks, "
                   "and discrepancy clearance across all accounts before close date each month."))
    story.append(b("Collect, validate, and consolidate financial and operational data from multiple business "
                   "units and departments to support monthly reporting cycles — managing data accuracy and "
                   "completeness across all inputs before each close."))
    story.append(b("Monitor weekly cash position and prepare cash flow analysis for management review; "
                   "support liquidity planning and prioritise supplier payment scheduling based on available "
                   "funds and payment terms."))
    story.append(b("Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
                   "organised, audit-ready documentation and timely issue resolution."))
    story.append(Paragraph("Finance Systems &amp; ERP", SUB))
    story.append(b("Led full ERP migration from Tally to Odoo: managed data validation, inventory database "
                   "cleansing, master data review, and cross-team co-ordination from planning through go-live "
                   "— building hands-on ERP implementation experience directly applicable to Oracle/Dynamics environments."))
    story.append(b("Rebuilt finance documentation framework from scratch — standardised filing, record-keeping, "
                   "and audit-trail processes; document retrieval reduced from days to minutes."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story.append(b("Conducted financial analysis and review of client financial statements, workpapers, "
                   "and supporting records; identified discrepancies, investigated root causes, and "
                   "coordinated resolution with stakeholders."))
    story.append(b("Reconciled financial data across multiple sources — ensuring accuracy and consistency "
                   "across all reporting outputs under strict deadline pressure."))
    story.append(b("Analysed high volumes of financial data across multi-client engagements, applying "
                   "structured investigation methodology to identify errors and inconsistencies."))
    story.append(b("Produced structured financial analysis and reporting deliverables across multi-client "
                   "engagements — developing disciplined analytical processes for data accuracy, deadline "
                   "adherence, and financial controls."))

    story.extend(section("Internship Experience"))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story.extend(section("Projects"))
    proj_t = Table(
        [[Paragraph("<b>Personal Financial Data Analytics System</b>", EDU_DEG),
          Paragraph("2024 – Present", DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    proj_t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    story.append(proj_t)
    story.append(Paragraph(
        "Building FP&amp;A analytical portfolio in Advanced Excel and Power BI: budgeting and rolling "
        "forecast models, budget-vs-actual variance dashboards, and management reporting templates "
        "using real company financial data. Supporting financial data workflows with Python automation.",
        EDU_INS
    ))

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US / IMA) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Financial Reporting — University of Illinois",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_NAFFCO_FPnA_Analyst.pdf")


# ── DISPATCH ──────────────────────────────────────────────────────────────────

RESUMES = {
    "master":    build_master,
    "chalhoub":  build_chalhoub,
    "naffco":    build_naffco,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/build_resume_pdf.py <key>")
        print(f"Available: {', '.join(RESUMES.keys())}")
        sys.exit(1)
    key = sys.argv[1].lower()
    if key not in RESUMES:
        print(f"Unknown resume key: '{key}'. Available: {', '.join(RESUMES.keys())}")
        sys.exit(1)
    RESUMES[key]()
