"""
Shared utilities for all resume PDF builds.
Import everything with: from resume_utils import *
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

# ── Colours ───────────────────────────────────────────────────────────────────
DARK  = HexColor("#1a1a1a")
MID   = HexColor("#444444")
LIGHT = HexColor("#888888")
RULE  = HexColor("#cccccc")
BLUE  = HexColor("#1e3a5f")

LINKEDIN     = "linkedin.com/in/muhammed-ashnad-k"
CONTACT_LINE = f"+971 543255352  ·  muhammedashnad@gmail.com  ·  Dubai, UAE  ·  {LINKEDIN}"

# ── Styles ────────────────────────────────────────────────────────────────────
def st(name, **kw):
    d = dict(fontName="Helvetica", fontSize=9, textColor=DARK, leading=12, spaceAfter=0, spaceBefore=0)
    d.update(kw)
    return ParagraphStyle(name, **d)

NAME    = st("Name",   fontName="Helvetica-Bold",       fontSize=20, textColor=BLUE,  leading=24, spaceAfter=2)
HEAD    = st("Head",   fontName="Helvetica",             fontSize=9,  textColor=MID,   leading=12, spaceAfter=2)
CONTACT = st("Cont",   fontName="Helvetica",             fontSize=8.5,textColor=LIGHT, leading=11, spaceAfter=0)
SECTION = st("Sec",    fontName="Helvetica-Bold",        fontSize=8.5,textColor=BLUE,  leading=11, spaceBefore=8, spaceAfter=2)
EMPLOYER= st("Emp",    fontName="Helvetica-Bold",        fontSize=9.5,textColor=DARK,  leading=12, spaceBefore=6, spaceAfter=0)
ROLE    = st("Role",   fontName="Helvetica-BoldOblique", fontSize=8.5,textColor=MID,   leading=11, spaceAfter=2)
DATE_ST = st("Date",   fontName="Helvetica-Oblique",     fontSize=8.5,textColor=LIGHT, leading=12)
SUB     = st("Sub",    fontName="Helvetica-Bold",        fontSize=8.5,textColor=DARK,  leading=11, spaceBefore=3, spaceAfter=1)
BULLET  = st("Bul",    fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=11.5, leftIndent=10, firstLineIndent=-10, spaceAfter=1.5)
BODY    = st("Body",   fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=12, spaceAfter=4)
SKLBL   = st("SklLbl", fontName="Helvetica-Bold",        fontSize=8.5,textColor=MID,   leading=11, spaceAfter=1)
SKBDY   = st("SklBdy", fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=11.5,spaceAfter=3)
EDU_DEG = st("EduDeg", fontName="Helvetica-Bold",        fontSize=9,  textColor=DARK,  leading=12, spaceBefore=4, spaceAfter=0)
EDU_INS = st("EduIns", fontName="Helvetica",             fontSize=8.5,textColor=MID,   leading=11, spaceAfter=3)
CERT    = st("Cert",   fontName="Helvetica",             fontSize=8.5,textColor=DARK,  leading=12, leftIndent=10, firstLineIndent=-10, spaceAfter=1.5)

# ── Helpers ───────────────────────────────────────────────────────────────────
def rule():
    return HRFlowable(width="100%", thickness=0.4, color=RULE, spaceAfter=3, spaceBefore=0)

def b(text):
    return Paragraph(f"• {text}", BULLET)

def cert_line(text):
    return Paragraph(f"• {text}", CERT)

def section(title):
    return [Paragraph(title, SECTION), rule()]

def job(company, loc, role_title, dates):
    left = f"<b>{company}</b>  <font color='#888888' size='7.5'>— {loc}</font>"
    t = Table(
        [[Paragraph(left, EMPLOYER), Paragraph(dates, DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "BOTTOM"),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    return [t, Paragraph(role_title, ROLE)]

def edu_row(degree, institution, location, year):
    t = Table(
        [[Paragraph(f"<b>{degree}</b>", EDU_DEG), Paragraph(year, DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    return [t, Paragraph(f"{institution}  ·  {location}", EDU_INS)]

def proj_row(title, dates, desc):
    t = Table(
        [[Paragraph(f"<b>{title}</b>", EDU_DEG), Paragraph(dates, DATE_ST)]],
        colWidths=["76%", "24%"],
    )
    t.setStyle(TableStyle([
        ("ALIGN",         (0,0), (0,0),   "LEFT"),
        ("ALIGN",         (1,0), (1,0),   "RIGHT"),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("LEFTPADDING",   (0,0), (0,0),   0),
        ("RIGHTPADDING",  (1,0), (1,0),   0),
    ]))
    return [t, Paragraph(desc, EDU_INS)]

def header(headline):
    return [
        Paragraph("Muhammed Ashnad K", NAME),
        Paragraph(headline, HEAD),
        Paragraph(CONTACT_LINE, CONTACT),
        Spacer(1, 5),
        rule(),
    ]

def build_pdf(story, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=17*mm, rightMargin=17*mm,
        topMargin=14*mm,  bottomMargin=14*mm,
        title="Muhammed Ashnad K — Resume",
        author="Muhammed Ashnad K",
    )
    doc.build(story)
    print(f"PDF saved: {output_path}")

# ── Shared content (used across multiple resumes) ─────────────────────────────
def ey_tax_analyst_bullets():
    return [
        b("Conducted financial analysis and review of client financial statements, workpapers, "
          "and supporting records; identified discrepancies, investigated root causes, and "
          "coordinated resolution with stakeholders."),
        b("Reconciled financial data across multiple sources (tax forms, client records, supporting "
          "schedules), ensuring accuracy and consistency across all reports."),
        b("Analysed high volumes of financial data across multi-client engagements, identifying "
          "errors and inconsistencies through disciplined, structured review."),
        b("Prepared and reviewed client financial filings; maintained audit-ready documentation "
          "under strict filing deadlines."),
    ]

def ey_intern_bullets():
    return [
        b("Reviewed financial documents and supporting schedules for accuracy and compliance; "
          "validated client statements and reconciled supporting data."),
        b("Supported documentation and financial reporting workflows requiring strong analytical "
          "attention to detail and cross-team coordination."),
    ]

def education_section():
    s = section("Education")
    s += edu_row("M.Sc. Financial Economics",
                 "Manipal Academy of Higher Education", "Manipal, India", "2021 – 2023")
    s += edu_row("BBA — Finance (Major)",
                 "St. Aloysius College", "Mangalore, India", "2017 – 2020")
    return s
