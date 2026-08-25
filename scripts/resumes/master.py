from resume_utils import *

def build():
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
    story += proj_row(
        "Personal Financial Data Analytics System", "2024 – Present",
        "Independently built an end-to-end financial data pipeline: automated ingestion from "
        "multiple live market data APIs, real-time processing, structured data storage, and "
        "analytical reporting outputs. Built entirely in Python."
    )

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "ESG Certificate — Bloomberg LP",
        "Financial Reporting — University of Illinois",
        "Economics of Money and Banking — Columbia University",
        "Bloomberg &amp; NSMART Certification — IIM Bengaluru",
        "Applied Econometrics — Dr. BR Ambedkar School of Economics",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/Muhammed_Ashnad_Resume.pdf")
