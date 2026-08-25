from resume_utils import *

def build():
    """
    Tailored for: NAFFCO — FP&A (Financial Planning & Analysis) Analyst
    URL: https://www.linkedin.com/jobs/view/4450359617
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
    story += proj_row(
        "Personal Financial Data Analytics System", "2024 – Present",
        "Building FP&amp;A analytical portfolio in Advanced Excel and Power BI: budgeting and rolling "
        "forecast models, budget-vs-actual variance dashboards, and management reporting templates "
        "using real company financial data. Supporting financial data workflows with Python automation."
    )

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Financial Reporting — University of Illinois",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_NAFFCO_FPnA_Analyst.pdf")
