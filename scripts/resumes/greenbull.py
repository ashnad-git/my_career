from resume_utils import *

def build():
    """
    Tailored for: Greenbull Dubai — Junior Financial Analyst (M&A / Ventures)
    URL: https://ae.indeed.com/viewjob?jk=5470dd9ed1387d64
    NOTE: NOT SUITABLE — French fluency required. Resume built but do not apply.
    Output: resumes/Muhammed_Ashnad_Greenbull_JuniorFinancialAnalyst.pdf
    """
    story = []
    story += header(
        "Financial Analysis &amp; Investment Research  |  "
        "M.Sc. Financial Economics  |  Ex-EY  |  Dubai"
    )

    story.extend(section("Professional Summary"))
    story.append(Paragraph(
        "Finance analyst with M.Sc. Financial Economics, Big Four experience at Ernst &amp; Young in "
        "financial statement analysis, and hands-on valuation and financial modelling work at BB Advisory. "
        "Built an independent financial data analytics platform tracking multi-source market data in real "
        "time, demonstrating portfolio monitoring and quantitative analysis capability. Pursuing a junior "
        "analyst role in M&amp;A and ventures where economics training and analytical discipline contribute "
        "to investment research and deal evaluation.",
        BODY
    ))

    story.extend(section("Core Competencies"))
    for lbl, content in [
        ("Financial Analysis &amp; Investment Research",
         "Financial Modelling  ·  Valuation Analysis  ·  Financial Statement Analysis  ·  "
         "Due Diligence  ·  Market Research  ·  Scenario &amp; Sensitivity Analysis  ·  "
         "KPI Tracking  ·  Investment Research"),
        ("Analytics &amp; Technical",
         "Python (Data Pipelines &amp; Analytics)  ·  "
         "Advanced Excel (Power Query, Pivot Tables, Financial Models)  ·  "
         "Power BI  ·  SQL  ·  Microsoft PowerPoint"),
        ("Finance Foundation",
         "Management Reporting  ·  Variance Analysis  ·  Account Reconciliation  ·  "
         "ERP Systems (Odoo, Tally)"),
    ]:
        story.append(Paragraph(lbl, SKLBL))
        story.append(Paragraph(content, SKBDY))

    story.extend(section("Professional Experience"))
    story.extend(job("Promotech Advertising", "Dubai, UAE", "Accounts and Operations Executive", "Feb 2025 – Present"))
    story.append(b("Prepare monthly financial reports covering revenue, gross margin, and cost variances "
                   "for CEO review; written commentary identifies key performance drivers and business trends."))
    story.append(b("Manage financial data across 475 active accounts, investigating discrepancies, identifying "
                   "patterns, and maintaining accuracy across all reporting inputs."))
    story.append(Spacer(1, 4))

    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "Tax Analyst", "Nov 2023 – May 2024"))
    story.append(b("Conducted financial analysis and review of client financial statements, workpapers, "
                   "and supporting records; identified discrepancies, investigated root causes, and "
                   "coordinated resolution with stakeholders."))
    story.append(b("Reconciled financial data across multiple sources (tax forms, client records, supporting "
                   "schedules), ensuring accuracy and consistency across all reports."))
    story.append(b("Analysed high volumes of financial data across multi-client engagements, identifying "
                   "errors and inconsistencies through disciplined, structured review."))

    story.extend(section("Internship Experience"))
    story.extend(job("BB Advisory", "Bangalore, India", "Financial Analyst Intern", "Jan 2023"))
    story.append(b("Prepared financial analysis reports and valuation models for client engagements, "
                   "supporting investment evaluation and structured financial review."))
    story.append(b("Conducted financial research and competitive analysis, contributing to client-ready "
                   "analytical deliverables on potential acquisition targets and investment opportunities."))
    story.append(b("Supported portfolio reconciliations and compliance reviews, identifying risks, "
                   "discrepancies, and value opportunities across client portfolios."))
    story.append(Spacer(1, 4))
    story.extend(job("Ernst &amp; Young (EY)", "Bangalore, India", "US Tax Intern", "Jan – Apr 2023"))
    story += ey_intern_bullets()

    story.extend(section("Projects"))
    story += proj_row(
        "Financial Data Analytics Platform", "2024 – Present",
        "Built an end-to-end financial data analytics platform: automated ingestion from live market "
        "data APIs, real-time data processing, structured storage, and analytical reporting outputs. "
        "Demonstrates portfolio performance monitoring, multi-source financial data integration, and "
        "quantitative analysis at scale. Built entirely in Python."
    )

    story += education_section()

    story.extend(section("Certifications &amp; Professional Development"))
    for c in [
        "CMA (US) — In Progress",
        "Applied Econometrics — Dr. BR Ambedkar School of Economics",
        "Economics of Money and Banking — Columbia University",
        "Bloomberg Market Concepts — Bloomberg LP",
    ]:
        story.append(cert_line(c))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_Greenbull_JuniorFinancialAnalyst.pdf")
