from resume_utils import *

def build():
    """
    Tailored for: ITP Media Group — Assistant Management Accountant
    URL: https://ae.indeed.com/viewjob?jk=76bec186c0f27329
    Output: resumes/Muhammed_Ashnad_ITPMediaGroup_AsstMgmtAccountant.pdf
    """
    story = []
    story += header(
        "Management Accounting &amp; Reporting  |  Variance Analysis  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance professional with M.Sc. Financial Economics and Big Four experience at Ernst &amp; Young, "
        "currently preparing monthly management accounts, variance analysis, and performance packs at "
        "Promotech Advertising, Dubai. Background covers month-end and year-end close, balance sheet "
        "reconciliation, ERP implementation, cash flow monitoring, and direct stakeholder reporting. "
        "Pursuing CMA (US).",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Management Accounting &amp; Financial Reporting",
         "Management Accounts  ·  Variance Analysis &amp; Commentary  ·  Management Reporting  ·  "
         "Budgeting &amp; Forecasting  ·  Cash Flow Analysis  ·  Financial Reporting &amp; MIS  ·  "
         "Month-End &amp; Year-End Close  ·  Balance Sheet Reconciliation"),
        ("Technical Tools",
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  "
         "Odoo ERP  ·  Tally ERP  ·  Microsoft PowerPoint"),
        ("Accounting Foundation",
         "Account Reconciliation  ·  AP/AR Management  ·  ERP Implementation &amp; Migration  ·  "
         "Audit Support  ·  Stakeholder Coordination  ·  Discrepancy Investigation"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Management Accounting &amp; Reporting", SUB))
    story.append(b("Prepare monthly management accounts and CEO-level performance packs covering revenue, gross margin, "
                   "and variance commentary against budget, forecast, and prior period; written analysis explains "
                   "key cost and revenue drivers."))
    story.append(b("Support the budgeting and forecasting process, working closely with budget holders; maintain "
                   "expenditure trackers, monitor actuals versus budget across cost categories, and flag material "
                   "variances for management review."))
    story.append(b("Monitor cash position and support short-term liquidity planning, tracking weekly cash flow, "
                   "scheduling supplier payments based on available funds and payment terms, and assisting in "
                   "cash flow forecast preparation."))
    story.append(b("Run month-end and year-end close: balance sheet account reconciliations, ledger reviews, "
                   "pre/post-closing checks, and discrepancy clearance across all accounts before close date each month."))
    story.append(b("Manage AP/AR across 475 active accounts (319 suppliers, 156 clients); reconcile Statements "
                   "of Account, investigate discrepancies, and follow up on outstanding balances."))
    story.append(b("Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) by liaising with "
                   "internal stakeholders to gather financial information and maintaining audit-ready documentation."))
    story.append(Paragraph("Finance Systems", SUB))
    story.append(b("Led full ERP migration from Tally to Odoo: data validation, inventory database cleansing, "
                   "master data review, and cross-team co-ordination from planning through go-live."))
    story.append(b("Rebuilt finance documentation from scratch, standardising filing and record-keeping; "
                   "document retrieval reduced from days to minutes."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story += ey_tax_analyst_bullets()
    story.append(b("Co-ordinated with EY U.S. teams across time zones to deliver accurate, timely reporting."))

    story.extend(section("Internship Experience"))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Financial Reporting — University of Illinois",
        "Economics of Money and Banking — Columbia University",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_ITPMediaGroup_AsstMgmtAccountant.pdf")
