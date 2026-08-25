from resume_utils import *

def build():
    """
    Cover letter for Al Tayer Group — Business Support Analyst, Beauty Distribution.
    Output: resumes/Muhammed_Ashnad_AlTayer_CoverLetter.pdf
    """
    CL_BODY = ParagraphStyle("CLBody2", fontName="Helvetica", fontSize=9.5, textColor=DARK,
                             leading=15, spaceAfter=12)
    CL_META = ParagraphStyle("CLMeta2", fontName="Helvetica", fontSize=9, textColor=LIGHT,
                             leading=13, spaceAfter=4)
    CL_SIG  = ParagraphStyle("CLSig2",  fontName="Helvetica-Bold", fontSize=9.5, textColor=DARK,
                             leading=13, spaceAfter=2)
    CL_SIGD = ParagraphStyle("CLSigD2", fontName="Helvetica", fontSize=9, textColor=MID,
                             leading=13, spaceAfter=0)

    story = []
    story.append(Paragraph("Muhammed Ashnad K", NAME))
    story.append(Paragraph(
        "Business &amp; Commercial Analyst  |  M.Sc. Financial Economics  |  Ex-EY  |  Dubai", HEAD))
    story.append(Paragraph(CONTACT_LINE, CONTACT))
    story.append(Spacer(1, 6))
    story.append(rule())
    story.append(Spacer(1, 10))
    story.append(Paragraph("23 August 2026", CL_META))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Hiring Manager<br/>Al Tayer Group — Al Tayer Insignia<br/>Dubai, UAE", CL_META))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Dear Hiring Manager,", CL_BODY))
    story.append(Paragraph(
        "I am writing to apply for the Business Support Analyst role within Al Tayer Insignia's "
        "Beauty Distribution function. Al Tayer Insignia's position as the luxury retail leader "
        "across Beauty, Fashion, and Home in the Middle East — representing brands including "
        "Armani, Harvey Nichols, and Bloomingdale's — makes this an environment where commercial "
        "analytics and performance insight genuinely matter. I am drawn to a role where I can "
        "translate sales and financial data into decisions that drive a premium business.",
        CL_BODY
    ))
    story.append(Paragraph(
        "In my current role at Promotech Advertising, Dubai, I produce monthly commercial "
        "performance reports for CEO-level review — analysing revenue trends, gross margin "
        "variances, and cost performance across 475 active supplier and client accounts, with "
        "written commentary identifying key challenges, opportunities, and recommended actions. "
        "I also deliver ad hoc data analysis and financial modelling to support day-to-day "
        "business planning, and track account-level sales performance patterns against prior "
        "periods. This is exactly the work described in this role — commercial reporting, "
        "variance analysis, KPI tracking, and business planning support — applied in a live "
        "commercial environment under real deadline pressure.",
        CL_BODY
    ))
    story.append(Paragraph(
        "My M.Sc. in Financial Economics, Big Four experience at Ernst &amp; Young, and hands-on "
        "background in performance monitoring and stakeholder reporting give me the analytical "
        "foundation and commercial mindset this role requires. I am confident in translating "
        "complex data into clear, actionable insights and in working across functions — finance, "
        "commercial, and operations — to deliver reporting that supports business decisions. "
        "I would welcome the opportunity to bring this capability to Al Tayer's Beauty Distribution team.",
        CL_BODY
    ))
    story.append(Paragraph(
        "Thank you for considering my application. I look forward to the opportunity to discuss "
        "how my background aligns with the needs of this role.",
        CL_BODY
    ))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Yours sincerely,", CL_BODY))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Muhammed Ashnad K", CL_SIG))
    story.append(Paragraph("+971 543255352  ·  muhammedashnad@gmail.com  ·  Dubai, UAE", CL_SIGD))
    story.append(Paragraph("linkedin.com/in/muhammed-ashnad-k", CL_SIGD))

    build_pdf(story, "/Users/ashnad/my_career/resumes/Muhammed_Ashnad_AlTayer_CoverLetter.pdf")
