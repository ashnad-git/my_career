from resume_utils import *

def build():
    """
    Tailored for: NEP Singapore, India & MENA — Commercial Finance Analyst
    URL: https://ae.indeed.com/viewjob?jk=4c8377bbab0ef6c5
    Output: resumes/Muhammed_Ashnad_NEP_CommercialFinanceAnalyst.pdf
    """
    story = []
    story += header(
        "Commercial Finance &amp; FP&amp;A  |  Management Reporting &amp; Variance Analysis  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance professional with M.Sc. Financial Economics and Big Four experience at Ernst &amp; Young, "
        "currently delivering commercial finance reporting, variance analysis, and management packs in the "
        "media and advertising sector at Promotech Advertising in Dubai. Background covers budgeting and "
        "reforecasting, month-end close including accruals and cost centre reviews, business partnering "
        "with commercial stakeholders to consolidate inputs and drive reforecasting cycles, and presenting "
        "findings directly to CEO and senior leadership. Pursuing CMA (US).",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Commercial Finance &amp; FP&amp;A",
         "Management Reporting  ·  Variance Analysis  ·  Commercial Finance  ·  "
         "Budgeting &amp; Reforecasting  ·  Financial Modelling  ·  P&amp;L Analysis  ·  "
         "KPI Tracking  ·  Scenario Analysis  ·  Cash Flow Analysis"),
        ("Technical Tools",
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  "
         "Power BI (Dashboards, DAX)  ·  Odoo ERP  ·  Tally ERP  ·  Microsoft PowerPoint"),
        ("Accounting Foundation",
         "Month-End Close  ·  Accruals &amp; Prepayments  ·  Cost Centre Reviews  ·  "
         "Account Reconciliation  ·  ERP Implementation  ·  Audit Support"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Commercial Finance &amp; Reporting", SUB))
    story.append(b("Prepare monthly commercial finance reports and management packs for a media and "
                   "advertising business covering revenue performance, gross margin analysis, and operating "
                   "cost variance against budget and forecast; present written variance commentary and risk "
                   "narrative directly to CEO and senior leadership."))
    story.append(b("Partner with operational stakeholders across the business to gather financial inputs, "
                   "challenge assumptions, and consolidate data for monthly reporting and reforecasting cycles."))
    story.append(b("Produce account-level revenue performance analysis across 475+ active client accounts, "
                   "tracking billing, collection risk, and revenue trends by account and service category."))
    story.append(b("Support budgeting and quarterly reforecasting: maintain expenditure trackers, monitor "
                   "actuals versus budget across cost categories, and flag material variances for "
                   "management review."))
    story.append(b("Run month-end close including accruals, prepayments, cost centre reviews, account "
                   "reconciliations, and ledger clearance; all open items resolved before close date "
                   "each month."))
    story.append(b("Track and report commercial KPIs across accounts and cost categories, identifying "
                   "risks, opportunities, and areas requiring corrective action for management review."))
    story.append(Paragraph("Finance Systems", SUB))
    story.append(b("Led full ERP migration from Tally to Odoo: data validation, inventory cleansing, "
                   "master data review, and cross-team co-ordination from planning through go-live; "
                   "rebuilt finance documentation and reporting templates from scratch."))
    story.append(b("Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
                   "audit-ready documentation and timely stakeholder co-ordination."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story += ey_tax_analyst_bullets()
    story.append(b("Prepared structured financial analysis and reporting deliverables under strict "
                   "deadlines, co-ordinating with EY U.S. teams across time zones to ensure accuracy "
                   "and timely completion."))

    story.extend(section("Internship Experience"))
    story.extend(job("BB Advisory", "Bangalore, India", "Financial Analyst Intern", "Jan 2023"))
    story.append(b("Prepared financial analysis reports and valuation models for client engagements."))
    story.append(b("Supported financial research and contributed to client-ready analytical deliverables."))
    story.append(Spacer(1, 4))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story.extend(section("Projects"))
    for title, dates, desc in [
        ("FP&amp;A Financial Model (Excel)", "In progress — 2026",
         "Building a comprehensive driver-based financial model covering revenue forecasting, COGS and "
         "operating cost modelling, budgeting, variance analysis, and scenario modelling. Includes scenario "
         "and sensitivity analysis tabs demonstrating ROI and reforecast impact under varying assumptions. "
         "Designed to demonstrate the planning and analysis deliverables of a commercial finance function. "
         "Built in Excel using UAE retail sector financial data."),
        ("Financial Data Analytics Platform", "2024 – Present",
         "Built an end-to-end financial data pipeline: automated ingestion from multiple live market "
         "data APIs, real-time processing, structured data storage, and analytical reporting outputs. "
         "Built in Python."),
    ]:
        story += proj_row(title, dates, desc)

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Financial Reporting — University of Illinois",
        "Economics of Money and Banking — Columbia University",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_NEP_CommercialFinanceAnalyst.pdf")
