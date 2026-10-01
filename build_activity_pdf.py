from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "pdf" / "student-tech-program-strategy.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)
W, H = A4
NAVY = colors.HexColor("#14213D")
BLUE = colors.HexColor("#2563EB")
TEAL = colors.HexColor("#0F766E")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#64748B")
LINE = colors.HexColor("#D9E2EC")
PALE_BLUE = colors.HexColor("#EFF6FF")
PALE_TEAL = colors.HexColor("#ECFDF5")
PALE_GREY = colors.HexColor("#F8FAFC")

ss = getSampleStyleSheet()
ss.add(ParagraphStyle(name="TitleX", parent=ss["Title"], fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=NAVY, spaceAfter=3))
ss.add(ParagraphStyle(name="SubX", parent=ss["Normal"], fontName="Helvetica", fontSize=7.6, leading=9.4, textColor=MUTED, spaceAfter=5))
ss.add(ParagraphStyle(name="SectionX", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=9.4, leading=11, textColor=NAVY, spaceBefore=4, spaceAfter=2))
ss.add(ParagraphStyle(name="BodyX", parent=ss["BodyText"], fontName="Helvetica", fontSize=7.05, leading=8.65, textColor=INK, spaceAfter=2))
ss.add(ParagraphStyle(name="SmallX", parent=ss["BodyText"], fontName="Helvetica", fontSize=6.35, leading=7.55, textColor=INK))
ss.add(ParagraphStyle(name="TinyX", parent=ss["BodyText"], fontName="Helvetica", fontSize=5.65, leading=6.8, textColor=MUTED))
ss.add(ParagraphStyle(name="CellX", parent=ss["BodyText"], fontName="Helvetica", fontSize=5.95, leading=7.15, textColor=INK))
ss.add(ParagraphStyle(name="CellBoldX", parent=ss["BodyText"], fontName="Helvetica-Bold", fontSize=5.95, leading=7.15, textColor=NAVY))
ss.add(ParagraphStyle(name="HeadX", parent=ss["BodyText"], fontName="Helvetica-Bold", fontSize=6.05, leading=7.15, textColor=colors.white))


def p(text, style="BodyX"):
    return Paragraph(text, ss[style])


def section(title, accent=BLUE):
    t = Table([[p(title, "SectionX")]], colWidths=[W - 34 * mm])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.4, accent), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(17 * mm, 12.5 * mm, W - 17 * mm, 12.5 * mm)
    canvas.setFont("Helvetica", 5.9)
    canvas.setFillColor(MUTED)
    canvas.drawString(17 * mm, 8.2 * mm, "Student Tech-Program Strategy | verified 1 Oct 2026")
    canvas.drawRightString(W - 17 * mm, 8.2 * mm, f"Page {doc.page} of 2")
    canvas.restoreState()


doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm, topMargin=13 * mm, bottomMargin=16 * mm, title="Student Technology Program Strategy", author="Codex")
doc.addPageTemplates([PageTemplate(id="all", frames=Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal"), onPage=footer)])
story = []

# Page 1: research and readiness
story += [
    p("Student Technology Program Strategy", "TitleX"),
    p("Target pathways: GitHub Campus Experts + Linux Foundation LFX Mentorship &nbsp;|&nbsp; Profile basis: supplied React/TypeScript visual portfolio repository &nbsp;|&nbsp; Official pages checked 1 October 2026.", "SubX"),
]
intro = Table([[p("<b>Best-fit direction.</b> The supplied portfolio shows a strong web/visual engineering base: React/TypeScript components, shader/3D scenes, packaged landing pages, and reusable UI systems. The next step is to convert that craft into public evidence of collaboration: documented issues, reviewed pull requests, technical writing, and a small community event.")]], colWidths=[doc.width])
intro.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFDBFE")), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
story += [intro, Spacer(1, 2), section("1. Comparative matrix", BLUE)]

matrix = [
    [p("Dimension", "HeadX"), p("GitHub Campus Experts", "HeadX"), p("LFX Mentorship", "HeadX")],
    [p("Eligibility / year", "CellBoldX"), p("18+; enrolled in formal higher education; GitHub user for 6+ months; verified Student Developer Pack; more than 1 year left before graduation.", "CellX"), p("18+ by program start; individual applicant; eligible to work where participating; not a prior/active LF mentee; must meet project-specific rules.", "CellX")],
    [p("Technical prerequisites", "CellBoldX"), p("No single language requirement. Evidence of GitHub use, motivation, campus-community problem awareness, and potential to create impact; application form + video resume.", "CellX"), p("Project-specific skills. Prepare a mentee profile, current resume/cover letter, relevant work samples, and sometimes a code challenge or open-source evidence. Up to 3 projects per term.", "CellX")],
    [p("Cycle / next target", "CellBoldX"), p("Applications open every July for one month. The 2026 window is closed; target July 2027 and verify exact dates when the form reopens.", "CellX"), p("Recurring Spring/Summer/Fall terms. Official schedule says projects become visible around mid-Jan / mid-Apr / mid-Jul, with applications about 4 weeks; target Spring 2027, exact dates vary.", "CellX")],
    [p("Benefits", "CellBoldX"), p("Training to build technical communities; GitHub resources/support; possible swag, sponsorship, and event opportunities such as GitHub Universe.", "CellX"), p("Structured 12-week full-time or 24-week part-time project, mentor guidance, open-source contribution experience, and project-determined stipend/incentives; stipend rules are location-based.", "CellX")],
    [p("Career track / fit", "CellBoldX"), p("Developer relations, community leadership, technical evangelism, open-source advocacy, and collaborative engineering. Strong fit if the portfolio becomes a learning resource or workshop.", "CellX"), p("Open-source software engineering, Linux/cloud infrastructure, tooling, security, and maintainer-track development. Strong fit for turning front-end craft into production-quality collaboration.", "CellX")],
]
mt = Table(matrix, colWidths=[23 * mm, 74 * mm, 73 * mm], repeatRows=1)
mt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 1), (0, -1), PALE_GREY), ("GRID", (0, 0), (-1, -1), 0.3, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
story += [mt, section("2. Readiness and gap analysis", TEAL)]

gaps = Table([
    [p("Current evidence / strengths", "HeadX"), p("Gaps to close before applying", "HeadX")],
    [p("<b>GitHub Campus Experts</b><br/>&#8226;&nbsp;Strong visual communication and polished web artifact.<br/>&#8226;&nbsp;React/TypeScript and reusable UI systems are visible.<br/>&#8226;&nbsp;Portfolio can become a workshop/demo asset.", "CellX"), p("<b>Not evidenced in the supplied workspace:</b> student verification, 6+ months of GitHub use, 1+ year before graduation, campus leadership, event history, and public technical posts. Create one peer event, publish a facilitator guide, and prepare the video-resume story.", "CellX")],
    [p("<b>LFX Mentorship</b><br/>&#8226;&nbsp;Technical foundation supports front-end or developer-tool projects.<br/>&#8226;&nbsp;Existing code gives a credible project narrative and demo surface.<br/>&#8226;&nbsp;Visual polish can support docs, dashboards, or onboarding.", "CellX"), p("<b>Not evidenced in the supplied workspace:</b> public open-source issues/PRs, maintainer interaction, Linux/cloud/testing depth, resume/cover letter, and project-specific samples. Start with good-first-issue work, tests/docs, and a short contribution log; confirm age/work-authorization rules.", "CellX")],
], colWidths=[86 * mm, 84 * mm])
gaps.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), TEAL), ("BACKGROUND", (1, 0), (1, 0), NAVY), ("BACKGROUND", (0, 1), (0, -1), PALE_TEAL), ("BACKGROUND", (1, 1), (1, -1), PALE_BLUE), ("BOX", (0, 0), (-1, -1), 0.4, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4.5), ("RIGHTPADDING", (0, 0), (-1, -1), 4.5), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story += [gaps, Spacer(1, 2), p("<b>Readiness verdict:</b> Apply after the four-week sprint only if the eligibility checks are true. The portfolio is a credible starting artifact, not yet sufficient evidence for either selection process.", "SmallX"), PageBreak()]

# Page 2: plan, essay, sources
story += [p("Execution plan + application draft", "TitleX"), p("A four-week sprint designed to produce visible evidence, not just course completion.", "SubX"), section("3. Four-week preparation timeline", BLUE)]
plan = [
    [p("Week", "HeadX"), p("GitHub Campus Experts", "HeadX"), p("LFX Mentorship", "HeadX")],
    [p("1<br/><font color='#64748B'>Position</font>", "CellBoldX"), p("Verify age, enrollment, Student Developer Pack, GitHub account age, and graduation runway. Rewrite GitHub bio/readme around visual engineering + community learning. Pick a campus audience and one workshop topic.", "CellX"), p("Choose 2-3 LFX project families (web tooling, docs, cloud-native, or developer experience). Read contribution guides and codes of conduct. Create a one-page resume and project-fit notes.", "CellX")],
    [p("2<br/><font color='#64748B'>Contribute</font>", "CellBoldX"), p("Open-source setup/demo notes or a small reusable UI/shader component. File one issue or documentation improvement in a relevant public repo; request review politely.", "CellX"), p("Make one small, reviewable contribution: docs, test, bug reproduction, or beginner issue. Keep a dated contribution log with links, feedback, and what changed after review.", "CellX")],
    [p("3<br/><font color='#64748B'>Lead + write</font>", "CellBoldX"), p("Run a 30-45 minute peer session on Git/GitHub or creative coding for 3+ students. Publish slides/notes and a short reflection. Capture one measurable outcome.", "CellX"), p("Deepen one contribution and add tests or screenshots. Publish a 500-word technical note explaining the problem, trade-offs, and setup. Ask a maintainer or peer to review.", "CellX")],
    [p("4<br/><font color='#64748B'>Package</font>", "CellBoldX"), p("Record a concise video resume: motivation, community problem, planned impact, and evidence from the workshop. Pin the strongest repo and draft motivation/growth/contribution answers.", "CellX"), p("Select up to 3 target projects. Tailor resume + cover letter to each. Assemble portfolio links, contribution log, technical note, and a 90-second project pitch. Calendar the next official window.", "CellX")],
]
pt = Table(plan, colWidths=[19 * mm, 76 * mm, 75 * mm], repeatRows=1)
pt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 1), (0, -1), PALE_GREY), ("GRID", (0, 0), (-1, -1), 0.3, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5), ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]))
story += [pt, Spacer(1, 3), section("4. Draft application material | motivation essay (~250 words)", TEAL)]
essay = ("I am building toward a career in collaborative software engineering, with a particular interest in the space where developer tools, visual interfaces, and open source meet. My current portfolio is a React/TypeScript project containing reusable landing-page systems, shader-based scenes, and carefully documented UI experiments. It has taught me how to turn an idea into a polished artifact; my next goal is to learn how to make that work useful to a community of contributors.\n\n"
         "GitHub Campus Experts appeals to me because technical growth is stronger when it is shared. I want to run approachable sessions on Git, creative coding, and practical portfolio engineering, especially for students who may feel that open source is only for experienced developers. I can contribute visual communication, workshop demos, clear setup guides, and the patience to help beginners take a first step.\n\n"
         "In parallel, LFX Mentorship would help me develop the habits that production open source requires: reading contribution guides, making small reviewable changes, writing tests and documentation, responding to maintainer feedback, and communicating consistently across time zones. I am prepared to start with documentation or a focused issue, learn the project’s standards, and build toward deeper technical work.\n\n"
         "These pathways align with my long-term goal of becoming an engineer who ships reliable software and also strengthens the communities around it. I would bring curiosity, visual craft, and a bias toward making complex tools easier for other students to understand and use.")
story.append(p(essay.replace("\n\n", "<br/><br/>"), "SmallX"))
story += [Spacer(1, 3), section("Official sources used for verification", BLUE)]
sources = [
    "GitHub Campus Experts overview and eligibility: https://github.com/campus-experts",
    "GitHub application steps and July cycle: https://docs.github.com/en/education/about-github-education/use-github-at-your-educational-institution/applying-to-be-a-github-campus-expert",
    "Linux Foundation Mentorship overview and term windows: https://www.linuxfoundation.org/about/mentorship-programs/",
    "LFX eligibility rules: https://docs.linuxfoundation.org/lfx/mentorship/mentee-guide/am-i-eligible",
    "LFX schedules and program structure: https://docs.linuxfoundation.org/lfx/mentorship/mentorship-program-timelines",
    "LFX stipend guidance: https://docs.linuxfoundation.org/lfx/mentorship/mentee-stipends",
]
story += [p("<br/>".join(f"{i + 1}. {s}" for i, s in enumerate(sources)), "TinyX"), Spacer(1, 1), p("Note: Dates, project availability, eligibility, and benefits can change by cycle. Re-check the official application page immediately before submitting.", "TinyX")]

doc.build(story)
print(OUT)
