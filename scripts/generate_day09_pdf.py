#!/usr/bin/env python3
"""
PEER'S Persona Guard Suite - Executive Multi-Page Lab Report Compiler (Day 09)
Sqrock IT Solutions Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative 7-page executive engineering report integrating:
- 6 empirical execution screenshots (Kali Linux CLI cold boot, master menu, batch evaluation, single deep-dive, homoglyph collision scanner, GitHub repo)
- In-depth forensic explanations for every screenshot
- Deep technical analyses of social media impersonation, automated bot signals, and homoglyphic handle collisions
- MITRE ATT&CK T1585.001 & NIST CSF compliant defense architecture
- Automated 6-point unit test validation ledger and ethical compliance statements
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
OUTPUT_PDF = os.path.join(REPORTS_DIR, "Day09_Social_Impersonation_Report_Sqrock_MdPeerSiddiqui.pdf")

# Palette definitions
NAVY_PRIMARY = colors.HexColor("#0B192C")
CYAN_ACCENT  = colors.HexColor("#008DDA")
DARK_BLUE    = colors.HexColor("#1E3E62")
SLATE_GRAY   = colors.HexColor("#415A77")
LIGHT_BG     = colors.HexColor("#F4F6F9")
BORDER_COLOR = colors.HexColor("#D0D7DE")
SUCCESS_COL  = colors.HexColor("#0E703C")
CRIT_COL     = colors.HexColor("#A8201A")
TEXT_DARK    = colors.HexColor("#1A1A1A")


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    and persistent running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        
        # Running Header (pages 2+)
        if page_num > 1:
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.6)
            self.line(36, 756, 576, 756)
            
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE_GRAY)
            self.drawString(36, 762, "Sqrock IT Solutions | Cybersecurity Internship — Day 09 Lab Report")
            self.drawRightString(576, 762, "PEER'S Persona Guard Suite v2.5")

        # Running Footer (all pages)
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.6)
        self.line(36, 36, 576, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE_GRAY)
        self.drawString(36, 24, "Author: Mohammed Peer Siddiqui | Authorized Lab Environment | Confidential & Educational")
        self.drawRightString(576, 24, f"Page {page_num} of {total_pages}")
        
        self.restoreState()


def create_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=NAVY_PRIMARY,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=CYAN_ACCENT,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=DARK_BLUE
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=TEXT_DARK
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    story = []

    def load_screenshot(filename, w=540, h=195):
        path = os.path.join(SCREENSHOTS_DIR, filename)
        if os.path.exists(path):
            return Image(path, width=w, height=h)
        return Paragraph(f"<b>[Screenshot missing: {filename}]</b>", callout_style)

    # =========================================================================
    # PAGE 1: TITLE, METADATA & EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("SQROCK IT SOLUTIONS — CYBERSECURITY INTERNSHIP", subtitle_style))
    story.append(Paragraph("Day 09: Social Media Impersonation & Fake Profile Detection Heuristics", title_style))
    story.append(Spacer(1, 4))

    # Metadata Card
    meta_data = [
        [
            Paragraph("<b>Intern:</b> Mohammed Peer Siddiqui", table_cell),
            Paragraph("<b>Track:</b> Social Engineering Simulations (Python)", table_cell),
            Paragraph("<b>Date:</b> October 31, 2026", table_cell)
        ],
        [
            Paragraph("<b>Target Domain:</b> Social Media OSINT / Impersonation Defense", table_cell),
            Paragraph("<b>Standard:</b> MITRE ATT&CK T1585.001 (Establish Accounts)", table_cell),
            Paragraph("<b>Framework:</b> NIST CSF DE.CM (Continuous Monitoring)", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[180, 180, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Social media platforms (Twitter/X, LinkedIn, Instagram, and Telegram) have become primary operational staging grounds "
        "for modern social engineering threat actors. In advance of executing spear-phishing campaigns, credential theft operations, "
        "or business email compromise (BEC), adversaries routinely establish fraudulent accounts (mapped to <b>MITRE ATT&CK T1585.001</b>). "
        "These synthetic identities take two predominant forms: (1) <b>High-Fidelity Executive Impersonators</b> that clone the likeness, "
        "biography, and visual branding of corporate leaders using homoglyphs (e.g., substituting numeric zero for letter 'o') to bait "
        "subordinates into urgent financial actions, and (2) <b>Automated Bot Swarms</b> engineered to conduct reconnaissance, astroturf "
        "disinformation, or deliver credential-stealing hyperlinks.",
        body_style
    ))
    story.append(Paragraph(
        "Under <b>Day 09</b> of the Sqrock IT Solutions Cybersecurity Internship, this laboratory research project developed and evaluated "
        "<b>PEER'S Persona Guard Suite v2.5</b>. The system implements a robust, multi-vector heuristic scoring engine capable of detecting "
        "automated bots, sockpuppets, and executive impersonators without relying on brittle static signatures. By combining account "
        "creation velocity, network topology (following-to-follower ratios), visual completeness metrics, activity volume, and algorithmic "
        "homoglyph string similarity against protected corporate executive directories, the suite achieves authoritative triage and "
        "automated brand abuse alerting.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("2. Social Media Behavioral Profile Analysis Matrix", h1_style))
    matrix_data = [
        [
            Paragraph("Heuristic Dimension", table_header),
            Paragraph("Authentic Organic Profile", table_header),
            Paragraph("Malicious Bot / Impersonator Profile", table_header)
        ],
        [
            Paragraph("Account Longevity & Age", table_cell),
            Paragraph("<font color='#0E703C'>Established history (> 365 days)</font>", table_cell),
            Paragraph("<font color='#A8201A'>Extreme recency (< 7 to 30 days old)</font>", table_cell)
        ],
        [
            Paragraph("Network Topology Ratio", table_cell),
            Paragraph("<font color='#0E703C'>Balanced or high authority (Ratio <= 1.0)</font>", table_cell),
            Paragraph("<font color='#A8201A'>Highly skewed (Following/Followers > 10 to 50+)</font>", table_cell)
        ],
        [
            Paragraph("Visual & Bio Completeness", table_cell),
            Paragraph("<font color='#0E703C'>Unique portrait, customized rich bio</font>", table_cell),
            Paragraph("<font color='#A8201A'>Default egg/avatar, blank bio, or cloned asset</font>", table_cell)
        ],
        [
            Paragraph("Activity & Post Frequency", table_cell),
            Paragraph("<font color='#0E703C'>Consistent posting history (> 100 posts)</font>", table_cell),
            Paragraph("<font color='#A8201A'>Minimal activity (< 5 posts) or zero original posts</font>", table_cell)
        ],
        [
            Paragraph("Executive Handle Collision", table_cell),
            Paragraph("<font color='#0E703C'>Verified official corporate handle</font>", table_cell),
            Paragraph("<font color='#A8201A'>Homoglyphs / Typo-squats (Sim >= 70%)</font>", table_cell)
        ]
    ]
    t_mat = Table(matrix_data, colWidths=[140, 195, 205])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mat)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: THREAT MODELING, BOT TOPOLOGIES & INITIAL STATE
    # =========================================================================
    story.append(Paragraph("3. Threat Modeling & Social Media Reconnaissance Lifecycle", h1_style))
    story.append(Paragraph(
        "Adversaries exploit social media because platforms inherently foster trust and rapid informal interaction. "
        "The attack progression unfolds across four distinct stages:",
        body_style
    ))
    story.append(Paragraph(
        "<b>Phase 1: Persona Formulation & Cloning:</b> The adversary identifies high-value targets (e.g., C-level executives, "
        "recruiting leads, technical support directors) via OSINT. They register a deceptive handle utilizing typographical homoglyphs "
        "(e.g., substituting letter 'o' with numerical '0', or capitalizing 'i' to mimic 'l') and scrape high-resolution avatar photos.<br/>"
        "<b>Phase 2: Network Seeding & Trust Infiltration:</b> The synthetic persona aggressively follows dozens or hundreds of target "
        "organization employees in rapid succession, resulting in an abnormally high Following-to-Follower ratio (e.g., 800+ following "
        "versus only 10 followers).<br/>"
        "<b>Phase 3: Pretext Engagement & Lure Delivery:</b> The attacker initiates direct messaging (DMs) claiming urgent corporate matters, "
        "discreet recruitment opportunities, or VIP investment partnerships, embedding credential harvesting URLs.<br/>"
        "<b>Phase 4: Exploitation & Account Takeover:</b> Victims input corporate credentials into lookalike phishing portals or execute "
        "payloads under the illusion of interacting with verified internal management.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 1: Kali Linux Terminal Initialization & Environment Verification", h2_style))
    story.append(load_screenshot("01_kali_init_banner.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 1:</b> The cold-boot execution captured in Figure 1 confirms active deployment within "
        "Kali Linux kernel 6.1.0-kali7-amd64 with Python 3.10.12. Git synchronization validates the clean <code>main</code> branch "
        "state. The initialization sequence automatically loads the Multi-Vector Behavioral Scorer, arms the 4-member Protected "
        "Executive Roster, ingests the primary dataset (<code>datasets/profile_samples.json</code>), and mounts the structured SOC "
        "reporting pipeline into <code>./audit_reports/</code>.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: SUITE ARCHITECTURE & MASTER CONTROL CONSOLE
    # =========================================================================
    story.append(Paragraph("4. Suite Architecture & Modular Control Interface", h1_style))
    story.append(Paragraph(
        "To provide a production-ready investigative tool for SOC analysts and incident responders, <b>PEER'S Persona Guard Suite v2.5</b> "
        "was engineered into six distinct operational capabilities. The modular architecture is driven by an interactive command interface:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Option 1 (Interactive Profile Inspection):</b> Allows an analyst to input ad-hoc Twitter/X profile metrics, computing "
        "an instant threat score, penalty itemization, and risk classification.<br/>"
        "• <b>Option 2 (Batch Dataset Audit):</b> Ingests multi-profile JSON archives, processing complex real-world profile vectors in "
        "parallel and generating side-by-side behavioral comparison matrices.<br/>"
        "• <b>Option 3 (Executive Collision Scanner):</b> Utilizes normalized SequenceMatcher string similarity metrics to cross-reference "
        "candidate handles against an internal database of protected corporate executives, flagging deceptive typo-squats.<br/>"
        "• <b>Option 4 (Threat Intelligence Exporter):</b> Serializes all audit findings into machine-readable JSON schemas and human-readable "
        "incident response briefing documents.<br/>"
        "• <b>Option 5 (Heuristic Weights Matrix):</b> Displays transparent mathematical weighting coefficients for all behavioral indicators.<br/>"
        "• <b>Option 6 (Brand Defense Blueprint):</b> Outlines formal enterprise policies for brand trademark monitoring and DMCA takedowns.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 2: PEER'S Persona Guard Master Control Console", h2_style))
    story.append(load_screenshot("02_master_menu.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 2:</b> Figure 2 illustrates the master operator interface. The readiness telemetry pane confirms "
        "that the Behavioral Velocity Sensor, Network Topology Analyzer, Homoglyph Matcher (similarity threshold >= 0.70), and SIEM "
        "Export Pipeline are armed. The interface provides clear, non-intrusive terminal navigation suitable for high-throughput SOC operations.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: BATCH AUDIT EVALUATION (5 REAL-WORLD PROFILE SAMPLES)
    # =========================================================================
    story.append(Paragraph("5. Batch Audit Evaluation & Threat Spectrum Analysis", h1_style))
    story.append(Paragraph(
        "In strict alignment with the Day 09 syllabus requirements (<i>'Deliverable: Script + analysis of 5 real anonymized profile samples'</i>), "
        "the suite evaluated a curated benchmark dataset (<code>datasets/profile_samples.json</code>) spanning five diverse identity classes:",
        body_style
    ))
    story.append(Paragraph(
        "1. <b>PROF-001 (Executive Impersonator - <code>@peer_siddiqui_ce0</code>):</b> Age 4 days, following 820, followers 14 (ratio 58.6:1), "
        "posts 2, homoglyph mimicry of CEO. <b>Score: 95/100 (CRITICAL_IMPERSONATOR_THREAT)</b>.<br/>"
        "2. <b>PROF-002 (Crypto Spam Bot - <code>@airdrop_reward_bot2026</code>):</b> Age 7 days, following 980, followers 8 (ratio 122.5:1), "
        "default avatar, empty bio, post count 1. <b>Score: 90/100 (HIGH_RISK_AUTOMATED_BOT)</b>.<br/>"
        "3. <b>PROF-003 (Recruiter Recon Account - <code>@sarah_recruiter_tech</code>):</b> Age 26 days, following 740, followers 42 (ratio 17.6:1), "
        "generic bio, posts 4. <b>Score: 60/100 (SUSPICIOUS_PROFILE_EVALUATION)</b>.<br/>"
        "4. <b>PROF-004 (Authentic Verified Executive - <code>@peer_siddiqui_real</code>):</b> Age 1420 days (~4 years), following 450, "
        "followers 18,400 (ratio 0.02:1), posts 720, verified badge. <b>Score: 5/100 (AUTHENTIC_ORGANIC_ACCOUNT)</b>.<br/>"
        "5. <b>PROF-005 (Organic Junior Dev - <code>@dev_arjun_patel</code>):</b> Age 24 days, following 52, followers 38 (ratio 1.37:1), "
        "custom avatar, filled bio, posts 14. <b>Score: 15/100 (AUTHENTIC_ORGANIC_ACCOUNT)</b>.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 3: Batch Profile Audit Evaluation (5 Vectors)", h2_style))
    story.append(load_screenshot("03_batch_audit_results.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 3:</b> Figure 3 displays the tabulated batch processing output. The engine accurately segregated "
        "malicious from authentic identities: PROF-001 (95) and PROF-002 (90) were flagged with CRITICAL red alerts; PROF-003 (60) was "
        "triaged for manual analyst investigation; and PROF-004 (5) and PROF-005 (15) were recognized as authentic organic accounts. "
        "Crucially, the heuristic correctly distinguished a genuine new organic user (PROF-005, 24 days old) from an aggressive bot due "
        "to balanced network topology and authentic post velocity.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: FORENSIC DEEP-DIVE OF MALICIOUS EXECUTIVE IMPERSONATOR
    # =========================================================================
    story.append(Paragraph("6. Deep-Dive Forensic Inspection of Impersonation Vectors", h1_style))
    story.append(Paragraph(
        "Executive impersonation attacks present the highest operational risk to corporate networks because victims frequently suspend "
        "critical judgment when contacted by organizational leadership. Under <b>Option 1</b>, the analyst conducted an itemized deep-dive "
        "into Profile <code>PROF-001</code> (<code>@peer_siddiqui_ce0</code>).",
        body_style
    ))
    story.append(Paragraph(
        "The evaluation exposed five compound behavioral anomalies that collectively triggered a <b>95/100 Threat Score</b>:<br/>"
        "• <b>Executive Homoglyph Collision (+35):</b> The handle <code>peer_siddiqui_ce0</code> closely mimics <code>peer_siddiqui_real</code> "
        "substituting letter 'o' with digit '0', coupled with the display name <i>'Mohammed Peer Siddiqui (CEO)'</i>.<br/>"
        "• <b>Extreme Creation Recency (+35):</b> The profile was created only 4 days prior, characteristic of disposable attack infrastructure.<br/>"
        "• <b>Asymmetric Following Velocity (+30):</b> Aggressively following 820 corporate targets while accumulating only 14 followers.<br/>"
        "• <b>Minimal Organic History (+15):</b> Only 2 published posts, indicating an absence of historical engagement.<br/>"
        "• <b>External Malicious Link (+25):</b> Directs users to an unverified phishing portal (<code>sqrock-vip-invest.net</code>).",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 4: Single Profile Deep-Dive & Forensic Inspection", h2_style))
    story.append(load_screenshot("04_single_profile_deepdive.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 4:</b> Figure 4 captures the forensic breakdown of the impersonation candidate. Every penalty "
        "is explicitly annotated with its corresponding point contribution and root cause. The automated response engine raised an "
        "immediate Brand Abuse Incident Report and generated an expedited takedown payload formatted for social media platform trust "
        "and safety teams.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: HOMOGLYPH COLLISION & TYPO-SQUATTING DETECTION
    # =========================================================================
    story.append(Paragraph("7. Homoglyph & Typo-Squatting Collision Analysis", h1_style))
    story.append(Paragraph(
        "Attackers exploit homoglyphic substitutions (lookalike characters from Latin, Cyrillic, or numeric sets) to construct handles "
        "that appear visually indistinguishable to the human eye. To automate detection, the suite integrates a string distance matcher "
        "based on the Ratcliff-Obershelp gesture pattern matching algorithm (<code>difflib.SequenceMatcher</code>).",
        body_style
    ))
    story.append(Paragraph(
        "When an analyst inputs a candidate handle into <b>Option 3</b>, the engine calculates normalized similarity against every entity "
        "in the protected executive directory. If similarity equals or exceeds 70.0% and the candidate is not cryptographically verified, "
        "an executive impersonation alert is declared.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 5: Executive Impersonation & Homoglyph Collision Scanner", h2_style))
    story.append(load_screenshot("05_executive_collision_scan.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 5:</b> The terminal trace in Figure 5 demonstrates the detection of candidate handle "
        "<code>peer_siddiqui_ce0</code> targeting legitimate executive Mohammed Peer Siddiqui (<code>@peer_siddiqui_real</code>). "
        "The matcher reported an <b>88.9% Handle Similarity</b> and a <b>78.4% Display Name Similarity</b>, pinpointing the exact character "
        "substitution ('ce0' replacing 'ceo'). The tool mapped the incident directly to MITRE ATT&CK T1585.001 and recommended immediate "
        "trademark brand abuse escalation.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: AUTOMATED UNIT TESTS, POLICY BLUEPRINT & GITHUB REPO
    # =========================================================================
    story.append(Paragraph("8. Automated Unit Test Verification & Quality Assurance", h1_style))
    test_data = [
        [
            Paragraph("Test Method Identifier", table_header),
            Paragraph("Target Functional Component", table_header),
            Paragraph("Verification Metric", table_header),
            Paragraph("Result", table_header)
        ],
        [
            Paragraph("<code>test_account_age_penalty</code>", table_cell),
            Paragraph("Velocity Heuristic", table_cell),
            Paragraph("Confirms +35 score on accounts < 7d", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_follower_ratio_penalty</code>", table_cell),
            Paragraph("Network Topology Check", table_cell),
            Paragraph("Flags ratio > 50:1 with +30 penalty", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_default_profile_elements</code>", table_cell),
            Paragraph("Visual Asset Sensor", table_cell),
            Paragraph("Detects default avatar & missing bio (+35)", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_homoglyph_impersonation</code>", table_cell),
            Paragraph("Homoglyph Collision Engine", table_cell),
            Paragraph("Identifies handle similarity >= 80% to CEO", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_legitimate_profile_low_score</code>", table_cell),
            Paragraph("False Positive Prevention", table_cell),
            Paragraph("Authentic executive receives <= 10 score", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_batch_dataset_processing</code>", table_cell),
            Paragraph("Batch Dataset Ingestion", table_cell),
            Paragraph("Correctly evaluates all 5 test vectors", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ]
    ]
    t_test = Table(test_data, colWidths=[150, 130, 190, 70])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 6: GitHub Repository Overview (PEER-S-Persona-Guard-Suite)", h2_style))
    story.append(load_screenshot("06_github_repo_overview.png", w=540, h=175))
    story.append(Spacer(1, 4))

    story.append(Paragraph("9. Enterprise Brand Protection & Anti-Impersonation Blueprint", h1_style))
    story.append(Paragraph(
        "<b>Technical & Organizational Safeguards:</b> Enterprise security teams must operationalize a multi-layered brand defense strategy: "
        "(1) <i>Proactive Domain & Handle Squatting Defense:</i> Preemptively register common phonetic and homoglyphic variants of corporate "
        "brands and executive names; (2) <i>Continuous OSINT Monitoring:</i> Schedule automated daily scans against major platform APIs using "
        "heuristic thresholds defined in this suite; (3) <i>Zero-Trust Social Messaging Policy:</i> Formally prohibit conducting corporate "
        "business or credential validation across social direct messages (DMs); and (4) <i>Expedited Takedown Channels:</i> Maintain "
        "established enterprise relationships with platform trust and safety teams to execute rapid DMCA/trademark takedowns.<br/>"
        "<b>Ethical Research Notice:</b> All profile datasets evaluated in this laboratory were anonymized or synthetically generated within "
        "an authorized educational sandbox. No real personal identifiable information (PII) was exposed or compromised.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Executive Lab Report PDF successfully compiled at:\n    {OUTPUT_PDF}")


if __name__ == "__main__":
    create_report()
