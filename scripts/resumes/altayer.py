from resume_utils import *

def build():
    """
    Tailored for: Al Tayer Group — Business Support Analyst, Beauty Distribution (Dubai)
    Output: resumes/Muhammed_Ashnad_AlTayer_BusinessSupportAnalyst.pdf
    """
    story = []
    story += header(
        "Business &amp; Commercial Analyst  |  Data Analysis &amp; Performance Reporting  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance and analytics professional with M.Sc. Financial Economics and Big Four (EY) experience, "
        "currently delivering commercial performance reporting and business insights in a fast-paced "
        "commercial environment in Dubai. I produce monthly management reports analysing revenue "
        "performance, gross margin trends, and cost variances — translating multi-source financial data "
        "into clear, insightful outputs that support stakeholder decision-making. Experienced in ad hoc "
        "data analysis and modelling, variance analysis, and cross-functional stakeholder coordination "
        "across supplier and client accounts. Strong Excel foundation; commercially minded with a "
        "structured, deadline-driven approach.",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Data Analysis &amp; Reporting",
         "Commercial Performance Analysis  ·  Data Analysis &amp; Insights Reporting  ·  "
         "Variance Analysis  ·  Performance Monitoring  ·  Business Planning Support  ·  "
         "Sales &amp; Revenue Analytics  ·  Ad Hoc Financial Modelling  ·  KPI Tracking"),
        ("Technical Tools",
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  "
         "Microsoft PowerPoint  ·  Power BI (Dashboards)  ·  Odoo ERP  ·  Tally ERP"),
        ("Business &amp; Stakeholder Skills",
         "Stakeholder Management  ·  Management Reporting  ·  Financial Reporting &amp; MIS  ·  "
         "Month-End Close  ·  Account Reconciliation  ·  AP/AR Management  ·  Audit Support"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(Paragraph("Commercial Reporting &amp; Data Analysis", SUB))
    story.append(b(
        "Produce monthly management reports analysing revenue performance, gross margin trends, and "
        "cost variances — translating financial and operational data into clear, insightful reporting "
        "for CEO-level business decisions, with written commentary identifying key challenges, "
        "opportunities, and recommended actions."
    ))
    story.append(b(
        "Deliver ad hoc data analysis and financial modelling to support day-to-day business "
        "planning — investigating performance variances, identifying patterns in commercial data, "
        "and presenting findings to stakeholders in structured, decision-ready formats."
    ))
    story.append(b(
        "Track and evaluate commercial performance across 475 active accounts — 319 suppliers and "
        "156 clients — monitoring revenue trends, sales performance patterns, and account-level variances "
        "to support commercial planning and business review processes."
    ))
    story.append(b(
        "Support cross-functional stakeholders including management and finance partners by defining "
        "business reporting requirements, collecting relevant data, and delivering structured "
        "outputs aligned to business planning and performance monitoring cycles."
    ))
    story.append(Paragraph("Finance Operations", SUB))
    story.append(b(
        "Run month-end close: account reconciliations, ledger reviews, pre/post-closing checks, "
        "and discrepancy clearance across all accounts before close date each month."
    ))
    story.append(b(
        "Support IFRS-compliant annual audit (Kreston Menon Chartered Accountants) through "
        "organised, audit-ready documentation and timely stakeholder co-ordination."
    ))
    story.append(b(
        "Led full ERP migration from Tally to Odoo — data validation, master data review, "
        "and cross-team co-ordination from planning through go-live."
    ))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story.append(b(
        "Conducted financial analysis and review of client financial statements and supporting "
        "records across multi-client engagements — identifying discrepancies, investigating root "
        "causes, and coordinating resolution with internal and external stakeholders."
    ))
    story.append(b(
        "Analysed high volumes of financial data applying structured methodology to identify "
        "errors and inconsistencies — developing disciplined analytical and reporting capability "
        "in a high-stakes, deadline-driven environment."
    ))
    story.append(b(
        "Reconciled financial data across multiple sources ensuring accuracy and consistency "
        "across reporting outputs; prepared structured documentation under strict deadlines."
    ))

    story.extend(section("Internship Experience"))
    story.extend(job("BB Advisory", "Bangalore, India", "Financial Analyst Intern", "Jan 2023"))
    story.append(b(
        "Prepared financial analysis reports and valuation models for client engagements; "
        "conducted financial research and contributed to client-ready analytical deliverables."
    ))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Bloomberg Market Concepts — Bloomberg LP",
        "Financial Reporting — University of Illinois",
        "Economics of Money and Banking — Columbia University",
        "Applied Econometrics — Dr. BR Ambedkar School of Economics",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_AlTayer_BusinessSupportAnalyst.pdf")
