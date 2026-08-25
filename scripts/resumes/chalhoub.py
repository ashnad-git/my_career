from resume_utils import *

def build():
    """
    Tailored for: Chalhoub Group — FP&A Associate I (Zimmermann)
    URL: https://www.linkedin.com/jobs/view/4452830346
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
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "ESG Certificate — Bloomberg LP",
        "Financial Reporting — University of Illinois",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_Chalhoub_FPnA_Associate.pdf")
