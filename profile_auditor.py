#!/usr/bin/env python3
"""
================================================================================
PEER'S PERSONA GUARD SUITE v2.5 — Social Media Impersonation & Bot Detection
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
Track       : Social Engineering Attack Simulations Using Python (Day 09)
Standard    : MITRE ATT&CK T1585.001 (Establish Accounts: Social Media) | NIST CSF DE.CM
================================================================================
"""

import os
import sys
import json
import datetime
import difflib
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗ █████╗ 
{Fore.CYAN}██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔══██╗
{Fore.CYAN}██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║███████║
{Fore.BLUE}██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║██╔══██║
{Fore.BLUE}██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║██║  ██║
{Fore.BLUE}╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
{Fore.MAGENTA}  [+] SOCIAL MEDIA IMPERSONATION & FAKE PROFILE DETECTION SUITE v2.5
{Fore.LIGHTBLACK_EX}  [+] Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Alpha 2
  [+] Standard: MITRE ATT&CK T1585.001 | NIST CSF (Identify & Protect)
==============================================================================={Style.RESET_ALL}"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")
REPORTS_DIR = os.path.join(BASE_DIR, "audit_reports")
DEFAULT_DATASET = os.path.join(DATASETS_DIR, "profile_samples.json")
DEFAULT_EXPORT_JSON = os.path.join(REPORTS_DIR, "persona_audit_report.json")
DEFAULT_EXPORT_TXT = os.path.join(REPORTS_DIR, "persona_audit_report.txt")

# Protected Corporate Entities Roster (High-value targets for impersonation)
PROTECTED_EXECUTIVE_ROSTER = [
    {
        "entity_id": "EXEC-01",
        "official_handle": "peer_siddiqui_real",
        "official_name": "Mohammed Peer Siddiqui",
        "role": "Founder & Chief Executive Officer"
    },
    {
        "entity_id": "EXEC-02",
        "official_handle": "sqrock_ciso",
        "official_name": "Sqrock Information Security",
        "role": "Chief Information Security Officer"
    },
    {
        "entity_id": "EXEC-03",
        "official_handle": "sqrock_support",
        "official_name": "Sqrock Official Customer Support",
        "role": "Verified Global Customer Support"
    },
    {
        "entity_id": "EXEC-04",
        "official_handle": "sqrock_hr_talent",
        "official_name": "Sqrock Human Resources & Talent",
        "role": "Corporate Recruiting Division"
    }
]


def ensure_directories():
    """Ensure datasets and reports directories exist."""
    os.makedirs(DATASETS_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)


def compute_string_similarity(str1, str2):
    """
    Computes normalized SequenceMatcher similarity score (0.0 to 1.0).
    Sensitive to subtle homoglyphs, dropped characters, and typo-squats.
    """
    s1 = str1.lower().replace("@", "").strip()
    s2 = str2.lower().replace("@", "").strip()
    return difflib.SequenceMatcher(None, s1, s2).ratio()


def check_executive_collision(username, display_name):
    """
    Scans a profile against the protected executive directory to identify
    potential homoglyph impersonations, typo-squats, or name mimicry.
    """
    collisions = []
    u_clean = username.lower().replace("@", "")
    d_clean = display_name.lower()

    for exec_entity in PROTECTED_EXECUTIVE_ROSTER:
        handle_sim = compute_string_similarity(u_clean, exec_entity["official_handle"])
        name_sim = compute_string_similarity(d_clean, exec_entity["official_name"])

        # Flag if similarity is suspiciously high without being identical to verified account
        if u_clean != exec_entity["official_handle"].lower():
            if handle_sim >= 0.70 or name_sim >= 0.75:
                collisions.append({
                    "target_entity": exec_entity["official_name"],
                    "target_handle": f"@{exec_entity['official_handle']}",
                    "target_role": exec_entity["role"],
                    "handle_similarity": round(handle_sim * 100, 1),
                    "name_similarity": round(name_sim * 100, 1),
                    "risk_flag": "HOMOGLYPH_OR_TYPOSQUAT_COLLISION"
                })

    return collisions


def evaluate_profile(profile):
    """
    Core Behavioral & Heuristic Detection Algorithm:
    Evaluates account age, network ratio, media completeness, post volume,
    external URLs, and executive homoglyphs.
    Returns structured audit dictionary with itemized penalty breakdown.
    """
    score = 0
    penalties = []
    trust_factors = []

    username = profile.get("username", "unknown_user")
    display_name = profile.get("display_name", "")
    age_days = profile.get("account_age_days", 365)
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    no_pic = profile.get("no_profile_pic", False)
    default_bio = profile.get("has_default_bio", False)
    bio_text = profile.get("bio", "")
    posts = profile.get("posts", 100)
    is_verified = profile.get("is_verified", False)
    suspicious_url = profile.get("has_external_suspicious_url", False)
    external_url = profile.get("external_url", "")

    # 1. Executive Impersonation Collision Check
    collisions = check_executive_collision(username, display_name)
    if collisions:
        score += 35
        for col in collisions:
            penalties.append(
                f"EXECUTIVE_IMPERSONATION: Mimics {col['target_entity']} ({col['target_handle']}) "
                f"[Handle Sim: {col['handle_similarity']}%, Name Sim: {col['name_similarity']}%] (+35)"
            )

    # 2. Account Age Velocity
    if age_days < 7:
        score += 35
        penalties.append(f"EXTREME_ACCOUNT_VELOCITY: Account age {age_days} days (< 7 days) (+35)")
    elif age_days < 30:
        score += 25
        penalties.append(f"HIGH_ACCOUNT_VELOCITY: Account age {age_days} days (< 30 days) (+25)")
    elif age_days > 365:
        score -= 15
        trust_factors.append(f"ESTABLISHED_ACCOUNT: Longevity {age_days} days (> 1 year) (-15)")

    # 3. Network Topology & Follower Ratio
    ratio = following / max(followers, 1)
    if ratio > 50:
        score += 30
        penalties.append(f"EXTREME_FOLLOW_RATIO: Following-to-Follower ratio {ratio:.1f}:1 (> 50:1) (+30)")
    elif ratio > 10:
        score += 20
        penalties.append(f"HIGH_FOLLOW_RATIO: Following-to-Follower ratio {ratio:.1f}:1 (> 10:1) (+20)")
    elif ratio <= 0.1 and followers > 500:
        score -= 15
        trust_factors.append(f"HIGH_AUTHORITY_RATIO: Strong organic audience ({followers} followers) (-15)")

    # 4. Avatar & Visual Media Completeness
    if no_pic:
        score += 20
        penalties.append("DEFAULT_AVATAR: Missing custom profile image / default egg avatar (+20)")

    # 5. Bio Completeness & Default Keywords
    if default_bio or not bio_text.strip():
        score += 15
        penalties.append("INCOMPLETE_BIO: Default or empty biography (+15)")

    # 6. Activity & Post Volume
    if posts == 0:
        score += 25
        penalties.append("ZERO_ENGAGEMENT: No published posts or original engagement (+25)")
    elif posts < 5:
        score += 15
        penalties.append(f"MINIMAL_ENGAGEMENT: Only {posts} posts published (< 5 posts) (+15)")
    elif posts > 100:
        score -= 10
        trust_factors.append(f"ACTIVE_HISTORY: Significant posting history ({posts} posts) (-10)")

    # 7. External Link & Phishing Indicators
    if suspicious_url:
        score += 25
        penalties.append(f"MALICIOUS_EXTERNAL_LINK: Links to unverified external domain ({external_url}) (+25)")

    # 8. Platform Verification Mitigation
    if is_verified and not collisions:
        score = min(score, 10)
        trust_factors.append("PLATFORM_VERIFIED: Cryptographically validated corporate badge")

    # Normalize score between 0 and 100
    final_score = max(0, min(score, 100))

    # Threat Classification
    if final_score >= 75:
        verdict = "CRITICAL_IMPERSONATOR_THREAT" if collisions else "HIGH_RISK_AUTOMATED_BOT"
        risk_tier = "CRITICAL"
    elif final_score >= 45:
        verdict = "SUSPICIOUS_PROFILE_EVALUATION"
        risk_tier = "HIGH"
    elif final_score >= 25:
        verdict = "ANOMALOUS_PROFILE_MONITOR"
        risk_tier = "MEDIUM"
    else:
        verdict = "AUTHENTIC_ORGANIC_ACCOUNT"
        risk_tier = "LOW"

    return {
        "profile_id": profile.get("profile_id", f"PROF-{datetime.datetime.now().strftime('%M%S')}"),
        "username": username,
        "display_name": display_name,
        "account_age_days": age_days,
        "followers": followers,
        "following": following,
        "ratio": round(ratio, 2),
        "posts": posts,
        "is_verified": is_verified,
        "threat_score": final_score,
        "risk_tier": risk_tier,
        "verdict": verdict,
        "penalties": penalties,
        "trust_factors": trust_factors,
        "executive_collisions": collisions,
        "audit_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }


def load_dataset(dataset_path=DEFAULT_DATASET):
    """Loads social profile dataset from JSON."""
    if not os.path.exists(dataset_path):
        return []
    with open(dataset_path, "r", encoding="utf-8") as f:
        return json.load(f)


def export_audit_report(results, json_path=DEFAULT_EXPORT_JSON, txt_path=DEFAULT_EXPORT_TXT):
    """Exports structured audit findings to JSON and TXT format."""
    ensure_directories()
    
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(results, jf, indent=2)

    with open(txt_path, "w", encoding="utf-8") as tf:
        tf.write("===============================================================================\n")
        tf.write("       SQROCK IT SOLUTIONS - SOCIAL MEDIA IMPERSONATION AUDIT REPORT           \n")
        tf.write(f"Generated: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\n")
        tf.write("===============================================================================\n\n")
        
        for r in results:
            tf.write(f"Profile ID      : {r['profile_id']} (@{r['username']})\n")
            tf.write(f"Display Name    : {r['display_name']}\n")
            tf.write(f"Threat Score    : {r['threat_score']} / 100 ({r['risk_tier']})\n")
            tf.write(f"Verdict         : {r['verdict']}\n")
            tf.write(f"Followers/Following: {r['followers']} / {r['following']} (Ratio: {r['ratio']}:1)\n")
            tf.write(f"Account Age     : {r['account_age_days']} days | Posts: {r['posts']}\n")
            
            if r['penalties']:
                tf.write("Identified Penalties:\n")
                for p in r['penalties']:
                    tf.write(f"  [!] {p}\n")
            if r['executive_collisions']:
                tf.write("Executive Collision Detected:\n")
                for c in r['executive_collisions']:
                    tf.write(f"  [ALERT] Targets {c['target_entity']} ({c['target_handle']})\n")
            tf.write("-------------------------------------------------------------------------------\n")


# ==============================================================================
# INTERACTIVE CLI PRESENTATION
# ==============================================================================

def print_menu():
    print(f"\n{Fore.LIGHTBLACK_EX}--- [ PEER'S PERSONA GUARD CONTROL CONSOLE ] ---{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}[1]{Fore.WHITE} Audit Single Social Profile (Interactive Input)")
    print(f"  {Fore.CYAN}[2]{Fore.WHITE} Run Batch Audit on 5 Real-World Profile Samples (JSON Dataset)")
    print(f"  {Fore.CYAN}[3]{Fore.WHITE} Executive Impersonation & Homoglyph Collision Scanner")
    print(f"  {Fore.CYAN}[4]{Fore.WHITE} Export Threat Intelligence & Audit Report (JSON / TXT)")
    print(f"  {Fore.CYAN}[5]{Fore.WHITE} View Behavioral Heuristics & Scoring Weights Matrix")
    print(f"  {Fore.CYAN}[6]{Fore.WHITE} Display Enterprise Brand Protection & Anti-Impersonation Blueprint")
    print(f"  {Fore.CYAN}[7]{Fore.RED} Exit Suite")


def interactive_cli():
    print(BANNER)
    ensure_directories()
    latest_results = []

    while True:
        print_menu()
        choice = input(f"\n{Fore.GREEN}sqrock@persona-guard{Fore.WHITE}:{Fore.BLUE}~/social-defense{Fore.WHITE}$ ").strip()

        if choice == "1":
            print(f"\n{Fore.YELLOW}[*] Interactive Social Profile Inspection:{Style.RESET_ALL}")
            uname = input("Enter Twitter/X Username (e.g., peer_siddiqui_ce0): ").strip()
            dname = input("Enter Display Name: ").strip()
            try:
                age = int(input("Enter Account Age in Days (e.g., 5): ").strip())
                followers = int(input("Enter Follower Count (e.g., 10): ").strip())
                following = int(input("Enter Following Count (e.g., 850): ").strip())
                posts = int(input("Enter Total Published Posts (e.g., 2): ").strip())
            except ValueError:
                print(f"{Fore.RED}[-] Invalid numeric input. Aborting.{Style.RESET_ALL}")
                continue

            no_pic = input("Is Profile Picture Missing/Default? (y/n): ").strip().lower() == "y"
            def_bio = input("Is Bio Default/Empty? (y/n): ").strip().lower() == "y"
            susp_url = input("Does Profile Bio link to external unverified URL? (y/n): ").strip().lower() == "y"

            prof_input = {
                "profile_id": "MANUAL-001",
                "username": uname,
                "display_name": dname,
                "account_age_days": age,
                "followers": followers,
                "following": following,
                "no_profile_pic": no_pic,
                "has_default_bio": def_bio,
                "posts": posts,
                "is_verified": False,
                "has_external_suspicious_url": susp_url,
                "bio": "" if def_bio else "Manual profile evaluation"
            }

            res = evaluate_profile(prof_input)
            latest_results = [res]
            print(f"\n{Fore.GREEN}[+] Evaluation Complete:{Style.RESET_ALL}")
            score_col = Fore.RED if res['threat_score'] >= 70 else (Fore.YELLOW if res['threat_score'] >= 40 else Fore.GREEN)
            print(f"  • Threat Score   : {score_col}{res['threat_score']} / 100 ({res['risk_tier']}){Style.RESET_ALL}")
            print(f"  • Classification : {score_col}{res['verdict']}{Style.RESET_ALL}")
            print(f"  • Follower Ratio : {res['ratio']}:1")
            
            if res['penalties']:
                print(f"\n{Fore.RED}[!] Behavioral Penalty Breakdown:{Style.RESET_ALL}")
                for p in res['penalties']:
                    print(f"    └── [x] {p}")
            if res['trust_factors']:
                print(f"\n{Fore.GREEN}[+] Organic Trust Factors:{Style.RESET_ALL}")
                for t in res['trust_factors']:
                    print(f"    └── [✓] {t}")

        elif choice == "2":
            print(f"\n{Fore.YELLOW}[*] Ingesting 5 real-world profile samples from: {DEFAULT_DATASET}...{Style.RESET_ALL}")
            profiles = load_dataset()
            if not profiles:
                print(f"{Fore.RED}[-] Failed to load dataset. File not found.{Style.RESET_ALL}")
                continue

            batch_results = []
            print(f"{Fore.CYAN}{'ID':<10} {'Handle':<24} {'Age':<8} {'Ratio':<10} {'Score':<10} {'Verdict':<28}{Style.RESET_ALL}")
            print("-" * 92)

            for p in profiles:
                res = evaluate_profile(p)
                batch_results.append(res)
                score_col = Fore.RED if res['threat_score'] >= 70 else (Fore.YELLOW if res['threat_score'] >= 40 else Fore.GREEN)
                handle_str = f"@{res['username'][:22]}"
                print(f"{res['profile_id']:<10} {handle_str:<24} {res['account_age_days']:<8} {res['ratio']:<10} {score_col}{res['threat_score']:<10}{Style.RESET_ALL} {score_col}{res['verdict'][:28]}{Style.RESET_ALL}")

            latest_results = batch_results
            print("-" * 92)
            print(f"{Fore.GREEN}[+] Batch analysis complete. 5 profile vectors evaluated.{Style.RESET_ALL}")

        elif choice == "3":
            print(f"\n{Fore.YELLOW}[*] Scanning against Protected Corporate Executive Directory...{Style.RESET_ALL}")
            target_handle = input("Enter candidate username to test for homoglyph collision: ").strip()
            target_name = input("Enter candidate display name: ").strip()
            
            collisions = check_executive_collision(target_handle, target_name)
            if collisions:
                print(f"\n{Fore.RED}[!] HIGH-SEVERITY IMPERSONATION COLLISION DETECTED!{Style.RESET_ALL}")
                for c in collisions:
                    print(f"  {Fore.MAGENTA}• Targeted Executive : {Fore.WHITE}{c['target_entity']} ({c['target_role']})")
                    print(f"  {Fore.LIGHTCYAN_EX}• Legitimate Handle  : {Fore.GREEN}{c['target_handle']}")
                    print(f"  {Fore.LIGHTCYAN_EX}• Handle Similarity  : {Fore.RED}{c['handle_similarity']}%")
                    print(f"  {Fore.LIGHTCYAN_EX}• Name Similarity    : {Fore.RED}{c['name_similarity']}%")
                    print(f"  {Fore.YELLOW}• Incident Directive  : Issue immediate DMCA/Platform Brand Abuse takedown.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[+] No deceptive homoglyphs or brand name collisions identified.{Style.RESET_ALL}")

        elif choice == "4":
            if not latest_results:
                print(f"{Fore.YELLOW}[*] No recent audit results in memory. Running batch dataset first...{Style.RESET_ALL}")
                profiles = load_dataset()
                latest_results = [evaluate_profile(p) for p in profiles]
            
            export_audit_report(latest_results)
            print(f"{Fore.GREEN}[+] Audit reports successfully compiled:{Style.RESET_ALL}")
            print(f"  • JSON Telemetry : {DEFAULT_EXPORT_JSON}")
            print(f"  • Text Briefing  : {DEFAULT_EXPORT_TXT}")

        elif choice == "5":
            print(f"\n{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"{Fore.GREEN}        BEHAVIORAL HEURISTICS & RISK WEIGHTING COEFFICIENT MATRIX              {Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"""
{Fore.YELLOW}1. Executive Impersonation & Homoglyphs:{Fore.WHITE}
   - Handle / Name Similarity >= 70% against Executive Roster: +35 points

{Fore.YELLOW}2. Account Velocity & Creation Recency:{Fore.WHITE}
   - Account Age < 7 Days: +35 points
   - Account Age < 30 Days: +25 points
   - Account Age > 365 Days: -15 points (Organic Trust Credit)

{Fore.YELLOW}3. Network Topology & Following Ratio:{Fore.WHITE}
   - Following-to-Follower Ratio > 50:1: +30 points
   - Following-to-Follower Ratio > 10:1: +20 points
   - Ratio <= 0.1 (Audience Authority): -15 points (Organic Trust Credit)

{Fore.YELLOW}4. Visual & Structural Completeness:{Fore.WHITE}
   - Default Avatar / Missing Profile Picture: +20 points
   - Default or Blank Bio: +15 points
   - Zero Published Posts: +25 points
   - Posts < 5: +15 points
   - External Untrusted TLD / Phishing Link: +25 points
""")

        elif choice == "6":
            print(f"\n{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"{Fore.GREEN}    ENTERPRISE BRAND PROTECTION & SOCIAL IMPERSONATION DEFENSE BLUEPRINT      {Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"""
{Fore.YELLOW}1. Proactive Brand & Executive Name Monitoring:{Fore.WHITE}
   - Deploy automated OSINT crawlers searching for homoglyphic handle variants (0 for o, l for 1).
   - Preemptively register common executive and brand typo-squats across major social platforms.

{Fore.YELLOW}2. Social Media Verification & Verified Badges:{Fore.WHITE}
   - Require all corporate executives and HR recruiters to maintain verified organization badges.
   - Maintain a public 'Official Directory' on the company website listing all verified accounts.

{Fore.YELLOW}3. Zero-Trust Direct Messaging (DM) Protocols:{Fore.WHITE}
   - Formal policy prohibiting company business, credential requests, or financial discussions over social DMs.
   - Employees trained to report suspicious recruiters or VIP impersonators via dedicated SOC channels.

{Fore.YELLOW}4. Rapid Takedown Workflow:{Fore.WHITE}
   - Establish pre-authorized legal templates for platform DMCA and trademark abuse reporting.
""")

        elif choice == "7":
            print(f"\n{Fore.CYAN}[+] Exiting PEER'S Persona Guard Suite. Protection active.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[-] Invalid option. Please select 1 through 7.{Style.RESET_ALL}")


if __name__ == "__main__":
    interactive_cli()
