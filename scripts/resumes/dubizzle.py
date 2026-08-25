from resume_utils import *

def build():
    """
    Tailored for: dubizzle (Bayut) — Associate Commercial Analyst
    Output: resumes/Muhammed_Ashnad_Dubizzle_AssociateCommercialAnalyst.pdf
    """
    story = header(
        "Commercial &amp; Financial Analyst  |  Business Analytics  |  "
        "Python · SQL · Power BI  |  M.Sc. Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance and analytics professional with M.Sc. Financial Economics and 3+ years building "
        "performance dashboards, financial reporting systems, and data automation pipelines in "
        "commercial environments. At Promotech, I produce monthly CEO reporting packs covering "
        "revenue, margin, cost variance, and operational KPIs — performing deep-dive analysis on "
        "multi-source financial and operational data to surface actionable business insights. "
        "I independently built a production-grade Python data platform (multi-API ingestion, "
        "automated processing, structured analytical output) and am SQL-proficient — bringing a "
        "rare combination of economics training, automation capability, and commercial finance "
        "exposure to a data-driven digital analytics role.",
        BODY
    ))

    story.extend(section("Core Skills"))
    story.append(Paragraph("Analytics &amp; Data Tools", SKLBL))
    story.append(Paragraph(
        "SQL  |  Python (Automation, Data Pipelines &amp; Analytics)  |  Power BI (Dashboards, DAX)  |  "
        "Advanced Excel (Power Query, Pivot Tables, Financial Models)  |  Microsoft PowerPoint",
        SKBDY
    ))
    story.append(Paragraph("Business &amp; Financial Analysis", SKLBL))
    story.append(Paragraph(
        "Business Performance Analysis  |  P&amp;L Analysis  |  KPI Tracking  |  "
        "Revenue &amp; Cost Analytics  |  Variance Analysis  |  Budgeting &amp; Forecasting  |  "
        "Financial Reporting &amp; MIS  |  Management Reporting  |  Scenario Analysis",
        SKBDY
    ))
    story.append(Paragraph("Commercial &amp; Operational", SKLBL))
    story.append(Paragraph(
        "Month-End Close  |  Account Reconciliation  |  ERP Systems (Odoo, Tally)  |  "
        "Audit Support  |  Stakeholder Coordination",
        SKBDY
    ))

    story.extend(section("Professional Experience"))
    story += job("Promotech Advertising", "Dubai, UAE",
                 "Accounts and Operations Executive", "Feb 2025 – Present")
    story.append(Paragraph("Business Performance Reporting &amp; Analytics", SUB))
    story.append(b(
        "Build and deliver monthly performance dashboards and management reporting packs for the "
        "CEO — covering revenue, gross margin, cost variance, and operational KPI trends; perform "
        "deep-dive analysis on financial and operational data to surface actionable business insights "
        "with written commentary."
    ))
    story.append(b(
        "Perform month-end financial close: account reconciliations, ledger reviews, discrepancy "
        "investigation, and pre/post-closing validation across all accounts — ensuring data "
        "accuracy and completeness before each reporting cycle."
    ))
    story.append(b(
        "Track and analyse commercial performance metrics across 475 active supplier and client "
        "accounts — consolidating multi-source financial data into structured reporting for "
        "operational decision-making."
    ))
    story.append(b(
        "Monitor monthly cash position and working capital trends; produce weekly liquidity "
        "analysis for management — translating operational data into actionable cash management "
        "and payment scheduling decisions."
    ))
    story.append(b(
        "Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
        "organised, audit-ready documentation and timely resolution of review queries."
    ))
    story.append(Paragraph("Finance Systems &amp; Automation", SUB))
    story.append(b(
        "Drove full ERP migration from Tally to Odoo — data validation, inventory database "
        "cleansing, master data review, and cross-team coordination from planning through go-live."
    ))
    story.append(b(
        "Rebuilt finance function documentation from scratch; reduced document retrieval time "
        "from days to minutes through structured filing and process redesign."
    ))

    story += job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024")
    story.append(b(
        "Performed structured financial analysis across multi-client engagements — analysing "
        "high-volume financial datasets, identifying discrepancies, investigating root causes, "
        "and coordinating resolution with internal and client stakeholders."
    ))
    story.append(b(
        "Reconciled financial data across multiple sources (tax forms, client records, supporting "
        "schedules) — ensuring accuracy and consistency across reporting outputs at scale."
    ))
    story.append(b(
        "Built and maintained audit-ready analytical documentation under strict deadlines; "
        "coordinated with EY U.S. teams across time zones, developing cross-functional "
        "communication and deadline management capability."
    ))

    story.extend(section("Internship Experience"))
    story += job("BB Advisory", "Bangalore, India", "Financial Analyst Intern", "Jan 2023")
    story.append(b(
        "Prepared financial analysis reports and valuation models for client engagements; "
        "contributed to portfolio reconciliations and client-ready analytical deliverables."
    ))
    story += job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan 2023 – Apr 2023")
    story.extend(ey_intern_bullets())

    story.extend(section("Projects"))
    story += proj_row(
        "Multi-Source Financial Data Analytics Platform", "2024 – Present",
        "Built to reduce manual reporting overhead and enable scalable analytics at volume — "
        "production-grade automated data pipeline integrating multiple live market data APIs: "
        "real-time data ingestion, processing, validation, and structured analytical reporting "
        "outputs. Demonstrates capability in large-dataset automation, multi-source data "
        "integration, and programmatic reporting — directly applicable to commercial analytics "
        "and business intelligence workflows. Built entirely in Python."
    )

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — Pursuing",
        "Applied Econometrics — Dr. BR Ambedkar School of Economics  (quantitative methods, economic modelling)",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Economics of Money and Banking — Columbia University",
        "Financial Reporting — University of Illinois",
        "Bloomberg &amp; NSMART Certification — IIM Bengaluru",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_Dubizzle_AssociateCommercialAnalyst.pdf")
