from resume_utils import *

def build():
    """
    Cover letter for TotalEnergies — FP&A and Economist (Dubai).
    URL: https://www.linkedin.com/jobs/view/4440531428
    Output: resumes/Muhammed_Ashnad_TotalEnergies_CoverLetter.pdf
    """
    CL_BODY = ParagraphStyle("CLBody", fontName="Helvetica", fontSize=9.5, textColor=DARK,
                             leading=15, spaceAfter=12)
    CL_META = ParagraphStyle("CLMeta", fontName="Helvetica", fontSize=9, textColor=LIGHT,
                             leading=13, spaceAfter=4)
    CL_SIG  = ParagraphStyle("CLSig",  fontName="Helvetica-Bold", fontSize=9.5, textColor=DARK,
                             leading=13, spaceAfter=2)
    CL_SIGD = ParagraphStyle("CLSigD", fontName="Helvetica", fontSize=9, textColor=MID,
                             leading=13, spaceAfter=0)

    story = []
    story.append(Paragraph("Muhammed Ashnad K", NAME))
    story.append(Paragraph("Finance Professional  |  M.Sc. Financial Economics  |  Ex-EY  |  Dubai", HEAD))
    story.append(Paragraph(CONTACT_LINE, CONTACT))
    story.append(Spacer(1, 6))
    story.append(rule())
    story.append(Spacer(1, 10))
    story.append(Paragraph("21 August 2026", CL_META))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Hiring Manager<br/>TotalEnergies<br/>Dubai, UAE", CL_META))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Dear Hiring Manager,", CL_BODY))
    story.append(Paragraph(
        "I am writing to apply for the FP&amp;A and Economist role at TotalEnergies, Dubai. "
        "With an M.Sc. in Financial Economics, Big Four experience at Ernst &amp; Young, and "
        "hands-on financial reporting and ERP implementation experience in an active commercial "
        "environment, I am drawn to a role that combines rigorous financial planning with an "
        "economics dimension — precisely the profile this position requires.",
        CL_BODY
    ))
    story.append(Paragraph(
        "In my current role at Promotech Advertising, Dubai, I prepare monthly financial reports "
        "covering revenue, gross margin, and cost variances for CEO review; run month-end close "
        "including account reconciliations and ledger reviews; and support IFRS-compliant annual "
        "audits through organised, audit-ready documentation. I also monitor cash position and "
        "support liquidity planning across 475 active accounts — work that maps directly to the "
        "monthly P&amp;L analysis, cash flow statement preparation, and actuals-vs-budget reporting "
        "responsibilities outlined in this role. Additionally, I led the full ERP migration from "
        "Tally to Odoo, managing data validation, cross-team coordination, and go-live — giving me "
        "practical experience of the system discipline that large finance functions rely on.",
        CL_BODY
    ))
    story.append(Paragraph(
        "My academic background in Financial Economics — including applied econometrics, monetary "
        "economics (Columbia University), and financial reporting (University of Illinois) — equips "
        "me to engage with the economic analysis and long-term planning elements of this role. "
        "I understand that TotalEnergies operates at the intersection of energy markets, "
        "infrastructure finance, and global capital flows, and I am eager to bring analytical "
        "rigour grounded in both finance operations and economic methodology to your FP&amp;A function.",
        CL_BODY
    ))
    story.append(Paragraph(
        "I would welcome the opportunity to discuss how my background can contribute to "
        "TotalEnergies' financial planning and analysis team. Thank you for your consideration.",
        CL_BODY
    ))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Yours sincerely,", CL_BODY))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Muhammed Ashnad K", CL_SIG))
    story.append(Paragraph("+971 543255352  ·  muhammedashnad@gmail.com  ·  Dubai, UAE", CL_SIGD))
    story.append(Paragraph("linkedin.com/in/muhammed-ashnad-k", CL_SIGD))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_TotalEnergies_CoverLetter.pdf")
