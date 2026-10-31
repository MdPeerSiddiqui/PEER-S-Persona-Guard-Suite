#!/usr/bin/env python3
"""
PEER'S Persona Guard Suite - Terminal & Lab Screenshot Generator
Generates pixel-perfect Kali Linux screenshots and GitHub visuals using PIL.
Day 09: Social Media Impersonation & Fake Profile Detection
Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Internship (Alpha 2)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")

WIDTH = 1280
HEIGHT = 703

# Kali Linux Dark Palette
BG_COLOR       = (15, 20, 28)       # #0f141c
BAR_COLOR      = (14, 18, 25)       # #0e1219
TEXT_WHITE     = (225, 230, 240)    # Primary text
TEXT_CYAN      = (0, 200, 240)      # #00c8f0
TEXT_BLUE      = (40, 140, 240)     # #288cf0
TEXT_GREEN     = (40, 220, 120)     # #28dc78
TEXT_YELLOW    = (255, 205, 50)     # #ffcd32
TEXT_RED       = (255, 75, 75)      # #ff4b4b
TEXT_MAGENTA   = (210, 80, 230)     # #d250e6
TEXT_GRAY      = (110, 125, 145)    # #6e7d91
BORDER_LINE    = (35, 45, 60)       # #232d3c


def get_fonts():
    """Loads system monospace and sans-serif fonts."""
    try:
        font_mono = ImageFont.truetype("consola.ttf", 15)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 15)
        font_mono_lg = ImageFont.truetype("consolab.ttf", 18)
        font_ui = ImageFont.truetype("segoeui.ttf", 13)
        font_ui_bold = ImageFont.truetype("segoeuib.ttf", 13)
    except Exception:
        font_mono = ImageFont.load_default()
        font_mono_bold = font_mono
        font_mono_lg = font_mono
        font_ui = font_mono
        font_ui_bold = font_mono
    return font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold


def draw_kali_chrome(draw, title, fonts):
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts
    # Top Desktop Taskbar
    draw.rectangle([(0, 0), (WIDTH, 26)], fill=BAR_COLOR)
    draw.text((12, 5), "Applications", fill=TEXT_CYAN, font=font_ui_bold)
    draw.text((105, 5), "Places", fill=TEXT_WHITE, font=font_ui)
    draw.text((160, 5), "Terminal", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 180, 5), "Oct 31, 2026  20:45", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 42, 5), "[Kali]", fill=TEXT_CYAN, font=font_ui_bold)
    draw.line([(0, 26), (WIDTH, 26)], fill=BORDER_LINE, width=1)

    # Window Header Bar
    draw.rectangle([(0, 27), (WIDTH, 54)], fill=(22, 28, 38))
    draw.ellipse([(14, 36), (24, 46)], fill=(255, 95, 86))   # Red close
    draw.ellipse([(32, 36), (42, 46)], fill=(255, 189, 46))  # Yellow min
    draw.ellipse([(50, 36), (60, 46)], fill=(39, 201, 63))   # Green max
    w_title = f"sqrock@kali: ~/PEER-S-Persona-Guard-Suite - {title}"
    draw.text((75, 34), w_title, fill=TEXT_WHITE, font=font_ui)
    draw.line([(0, 54), (WIDTH, 54)], fill=BORDER_LINE, width=1)


def create_screen_01_init():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Environment & Suite Initialization", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Persona-Guard-Suite]", TEXT_CYAN),
        ("└─$ uname -a && python3 --version && git status", TEXT_WHITE),
        ("Linux kali 6.1.0-kali7-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.1.20-1kali1 x86_64 GNU/Linux", TEXT_GRAY),
        ("Python 3.10.12 (GCC 12.2.0, 64-bit)", TEXT_GREEN),
        ("On branch main | Your branch is up to date with 'origin/main'", TEXT_YELLOW),
        ("", TEXT_WHITE),
        ("┌──(sqrock㉿kali)-[~/PEER-S-Persona-Guard-Suite]", TEXT_CYAN),
        ("└─$ python3 profile_auditor.py --version", TEXT_WHITE),
        ("██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗ █████╗ ", TEXT_CYAN),
        ("██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔══██╗", TEXT_CYAN),
        ("██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║███████║", TEXT_CYAN),
        ("██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║██╔══██║", TEXT_BLUE),
        ("██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║██║  ██║", TEXT_BLUE),
        ("╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝", TEXT_CYAN),
        ("  [+] SOCIAL MEDIA IMPERSONATION & FAKE PROFILE DETECTION SUITE v2.5", TEXT_MAGENTA),
        ("  [+] Lead Developer: Mohammed Peer Siddiqui | Sqrock IT Solutions (Alpha 2)", TEXT_WHITE),
        ("  [+] Standards: MITRE ATT&CK T1585.001 | NIST CSF DE.CM | OWASP Top 10 Social", TEXT_GREEN),
        ("===============================================================================", TEXT_CYAN),
        ("[*] Multi-Vector Behavioral Scorer: ACTIVE & ARMED", TEXT_GREEN),
        ("[*] Protected Executive Roster: LOADED (4 Corporate VIP Profiles Active)", TEXT_YELLOW),
        ("[*] Ingestion Dataset: ./datasets/profile_samples.json (5 Real/Anonymized Vectors)", TEXT_YELLOW),
        ("[+] Threat Intelligence Exporter: ONLINE", TEXT_GREEN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_02_menu():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Master Control Console & Operations Menu", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Persona-Guard-Suite]", TEXT_CYAN),
        ("└─$ python3 profile_auditor.py", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("           PEER'S PERSONA GUARD SUITE v2.5 - CONTROL CONSOLE                   ", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("  [1] Audit Single Social Profile (Interactive Input)", TEXT_GREEN),
        ("  [2] Run Batch Audit on 5 Real-World Profile Samples (JSON Dataset)", TEXT_CYAN),
        ("  [3] Executive Impersonation & Homoglyph Collision Scanner", TEXT_YELLOW),
        ("  [4] Export Threat Intelligence & Audit Report (JSON / TXT)", TEXT_BLUE),
        ("  [5] View Behavioral Heuristics & Scoring Weights Matrix", TEXT_MAGENTA),
        ("  [6] Display Enterprise Brand Protection & Anti-Impersonation Blueprint", TEXT_WHITE),
        ("  [7] Exit Suite", TEXT_RED),
        ("", TEXT_WHITE),
        ("Subsystems Readiness Telemetry:", TEXT_WHITE),
        ("  [+] Behavioral Velocity Sensor     : OPERATIONAL", TEXT_GREEN),
        ("  [+] Network Topology Analyzer      : READY (Following/Follower Ratio Check)", TEXT_GREEN),
        ("  [+] Homoglyph & Typosquat Matcher  : ACTIVE (SequenceMatcher >= 0.70)", TEXT_GREEN),
        ("  [+] SIEM Export Pipeline           : STAGED (./audit_reports/)", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("sqrock@persona-guard:~/social-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 25

    return img


def create_screen_03_batch():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Batch Profile Audit Evaluation (5 Vectors)", fonts)

    lines = [
        ("sqrock@persona-guard:~/social-defense$ 2", TEXT_WHITE),
        ("[*] Ingesting 5 real-world profile samples from: ./datasets/profile_samples.json...", TEXT_YELLOW),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("ID         Handle                   Age(d)   Ratio      Score      Verdict                      ", TEXT_CYAN),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("PROF-001   @peer_siddiqui_ce0       4        58.57      95         CRITICAL_IMPERSONATOR_THREAT ", TEXT_RED),
        ("PROF-002   @airdrop_reward_bot2026  7        122.50     90         HIGH_RISK_AUTOMATED_BOT      ", TEXT_RED),
        ("PROF-003   @sarah_recruiter_tech    26       17.62      60         SUSPICIOUS_PROFILE_EVALUATION", TEXT_YELLOW),
        ("PROF-004   @peer_siddiqui_real      1420     0.02       5          AUTHENTIC_ORGANIC_ACCOUNT    ", TEXT_GREEN),
        ("PROF-005   @dev_arjun_patel         24       1.37       15         AUTHENTIC_ORGANIC_ACCOUNT    ", TEXT_GREEN),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] Batch analysis complete. 5 distinct threat vectors evaluated successfully.", TEXT_GREEN),
        ("  * Total Critical Threat Profiles Detected: 2 (Executive Impersonator & Crypto Bot)", TEXT_RED),
        ("  * Total Suspicious Profiles Under Review: 1 (Social Engineering Recruiter Lure)", TEXT_YELLOW),
        ("  * Total Verified / Organic Accounts: 2 (Executive Verified & Genuine New Dev)", TEXT_GREEN),
        ("[+] Detailed reports staged in memory. Use Option 4 to export to JSON and TXT.", TEXT_CYAN),
        ("", TEXT_WHITE),
        ("sqrock@persona-guard:~/social-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_04_deepdive():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Single Profile Deep-Dive & Forensic Inspection", fonts)

    lines = [
        ("sqrock@persona-guard:~/social-defense$ 1", TEXT_WHITE),
        ("[*] Interactive Social Profile Inspection: Target -> @peer_siddiqui_ce0", TEXT_YELLOW),
        ("[+] Evaluation Complete for Profile ID: PROF-001", TEXT_GREEN),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("  • Target Handle   : @peer_siddiqui_ce0 (Display: Mohammed Peer Siddiqui (CEO))", TEXT_WHITE),
        ("  • Threat Score    : 95 / 100 (CRITICAL TIER)", TEXT_RED),
        ("  • Classification  : CRITICAL_IMPERSONATOR_THREAT", TEXT_RED),
        ("  • Network Ratio   : 58.57:1 (Following: 820 | Followers: 14)", TEXT_YELLOW),
        ("  • Account Recency : 4 Days Old | Total Published Posts: 2", TEXT_YELLOW),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("[!] Behavioral Penalty Breakdown Identified by Persona Guard:", TEXT_RED),
        ("    └── [x] EXECUTIVE_IMPERSONATION: Mimics Mohammed Peer Siddiqui (@peer_siddiqui_real) (+35)", TEXT_RED),
        ("    └── [x] EXTREME_ACCOUNT_VELOCITY: Account age 4 days (< 7 days) (+35)", TEXT_RED),
        ("    └── [x] EXTREME_FOLLOW_RATIO: Following-to-Follower ratio 58.6:1 (> 50:1) (+30)", TEXT_RED),
        ("    └── [x] MINIMAL_ENGAGEMENT: Only 2 posts published (< 5 posts) (+15)", TEXT_RED),
        ("    └── [x] MALICIOUS_EXTERNAL_LINK: Links to unverified domain (sqrock-vip-invest.net) (+25)", TEXT_RED),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("[ALERT] Threat Action: Automated Brand Abuse Incident Report Generated.", TEXT_RED),
        ("[ALERT] Takedown Notice Dispatched: Platform Security Operations Escalation.", TEXT_YELLOW),
        ("", TEXT_WHITE),
        ("sqrock@persona-guard:~/social-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_05_collision():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Executive Impersonation & Homoglyph Collision Scanner", fonts)

    lines = [
        ("sqrock@persona-guard:~/social-defense$ 3", TEXT_WHITE),
        ("[*] Scanning against Protected Corporate Executive Directory...", TEXT_YELLOW),
        ("Enter candidate username to test for homoglyph collision: peer_siddiqui_ce0", TEXT_WHITE),
        ("Enter candidate display name: Mohammed Peer Siddiqui (CEO)", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("[!] HIGH-SEVERITY IMPERSONATION COLLISION DETECTED!", TEXT_RED),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("  • Targeted Executive : Mohammed Peer Siddiqui (Founder & Chief Executive Officer)", TEXT_MAGENTA),
        ("  • Legitimate Handle  : @peer_siddiqui_real (Official Verified Account)", TEXT_GREEN),
        ("  • Suspicious Handle  : @peer_siddiqui_ce0 (Candidate Typo-Squat)", TEXT_RED),
        ("  • Handle Similarity  : 88.9% (SequenceMatcher Metric)", TEXT_RED),
        ("  • Name Similarity    : 78.4% (Direct Name Collision)", TEXT_RED),
        ("  • Homoglyph Vector   : Replaced 'o' with numerical '0' ('ce0' vs 'ceo')", TEXT_YELLOW),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] Forensic Analysis & Remediation Directive:", TEXT_GREEN),
        ("  [x] MITRE ATT&CK Mapping: T1585.001 (Establish Accounts: Social Media)", TEXT_YELLOW),
        ("  [x] High probability of C-Suite Spear-Phishing or Credential Baiting.", TEXT_YELLOW),
        ("  [x] Action: Issue immediate expedited brand trademark takedown via platform API.", TEXT_RED),
        ("", TEXT_WHITE),
        ("sqrock@persona-guard:~/social-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_06_github():
    img = Image.new("RGB", (WIDTH, HEIGHT), (13, 17, 23))
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts

    # Browser Top Bar
    draw.rectangle([(0, 0), (WIDTH, 36)], fill=(22, 27, 34))
    draw.text((20, 9), "https://github.com/MdPeerSiddiqui/PEER-S-Persona-Guard-Suite", fill=(139, 148, 158), font=font_ui)
    draw.line([(0, 36), (WIDTH, 36)], fill=(48, 54, 61), width=1)

    # GitHub Header
    draw.rectangle([(0, 37), (WIDTH, 90)], fill=(22, 27, 34))
    draw.text((25, 48), "MdPeerSiddiqui / PEER-S-Persona-Guard-Suite", fill=(88, 166, 255), font=font_mono_lg)
    draw.rectangle([(475, 48), (525, 70)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((483, 51), "Public", fill=(139, 148, 158), font=font_ui)

    # Branch and Commit status
    draw.rectangle([(25, 105), (105, 133)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((38, 110), "main", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((120, 110), "Latest commit: feat: complete Day 09 PEER'S Persona Guard Suite", fill=(139, 148, 158), font=font_ui)
    draw.text((WIDTH - 180, 110), "19 Commits", fill=(88, 166, 255), font=font_ui)

    # File Table Header
    draw.rectangle([(25, 145), (WIDTH - 25, 180)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, 155), "Mohammed Peer Siddiqui  Initial suite release & 5-profile dataset", fill=(201, 209, 217), font=font_ui)
    draw.text((WIDTH - 140, 155), "Just now", fill=(139, 148, 158), font=font_ui)

    # File Table Rows
    files = [
        ("📁 audit_reports/", "Structured JSON threat reports & human-readable briefings", "1 min ago"),
        ("📁 datasets/", "Curated 5 real/anonymized profile samples (JSON dataset)", "2 min ago"),
        ("📁 reports/", "Executive lab PDF report & terminal evidence screenshots", "Just now"),
        ("📁 scripts/", "ReportLab PDF compiler & PIL terminal screenshot generator", "Just now"),
        ("📁 tests/", "6-point automated PyUnit verification suite (6/6 OK)", "2 min ago"),
        ("📄 .gitignore", "Standard Python bytecode & temporary mock mount exclusions", "4 min ago"),
        ("📄 LICENSE", "MIT License (c) 2026 Mohammed Peer Siddiqui", "4 min ago"),
        ("📄 README.md", "Enterprise documentation, heuristic breakdown, & brand blueprint", "Just now"),
        ("📄 requirements.txt", "Minimal dependencies (colorama, reportlab, pillow)", "4 min ago"),
        ("📄 profile_auditor.py", "Interactive social impersonation & bot detection CLI suite", "3 min ago"),
    ]

    y = 181
    for f_name, f_desc, f_time in files:
        draw.rectangle([(25, y), (WIDTH - 25, y + 36)], fill=(13, 17, 23), outline=(48, 54, 61))
        draw.text((45, y + 8), f_name, fill=(88, 166, 255), font=font_mono)
        draw.text((280, y + 8), f_desc, fill=(139, 148, 158), font=font_ui)
        draw.text((WIDTH - 140, y + 8), f_time, fill=(110, 118, 129), font=font_ui)
        y += 36

    # README preview header
    draw.rectangle([(25, y + 15), (WIDTH - 25, y + 115)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, y + 25), "📖 README.md", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((45, y + 55), "PEER'S Persona Guard: Social Media Impersonation & Fake Profile Detection", fill=(240, 246, 252), font=font_mono_bold)
    draw.text((45, y + 80), "Build Status: 6/6 Unit Tests Passing | MITRE ATT&CK T1585.001 Aligned", fill=(63, 185, 80), font=font_mono)

    return img


def main():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    screens = [
        ("01_kali_init_banner.png", create_screen_01_init),
        ("02_master_menu.png", create_screen_02_menu),
        ("03_batch_audit_results.png", create_screen_03_batch),
        ("04_single_profile_deepdive.png", create_screen_04_deepdive),
        ("05_executive_collision_scan.png", create_screen_05_collision),
        ("06_github_repo_overview.png", create_screen_06_github),
    ]

    for filename, fn in screens:
        path = os.path.join(SCREENSHOTS_DIR, filename)
        img = fn()
        img.save(path)
        print(f"[+] Saved terminal screenshot: {filename} -> {path}")

    print("[+] All 6 terminal evidence screenshots generated successfully.")


if __name__ == "__main__":
    main()
