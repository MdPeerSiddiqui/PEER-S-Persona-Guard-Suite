# PEER'S Persona Guard Suite: Social Media Impersonation & Fake Profile Detection

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/MITRE%20ATT%26CK-T1585.001-red.svg?style=for-the-badge&logo=mitre-attack)](https://attack.mitre.org/techniques/T1585/001/)
[![Standard](https://img.shields.io/badge/NIST%20CSF-DE.CM--1-orange.svg?style=for-the-badge)](https://www.nist.gov/cyberframework)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-6%2F6%20Passed-brightgreen.svg?style=for-the-badge)](tests/test_profile_auditor.py)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-black.svg?style=for-the-badge&logo=linux)](https://www.kali.org/)

> **Day 09 Cybersecurity Internship Deliverable**  
> **Company:** Sqrock IT Solutions  
> **Specialization:** Social Engineering & Authentication Security Simulations Using Python  
> **Developer:** Mohammed Peer Siddiqui  
> **Repository:** [https://github.com/MdPeerSiddiqui/PEER-S-Persona-Guard-Suite](https://github.com/MdPeerSiddiqui/PEER-S-Persona-Guard-Suite)

---

## 📌 Executive Overview

Social media platforms (Twitter/X, LinkedIn, Telegram, and Instagram) have become primary operational staging grounds for modern social engineering threat actors. In advance of executing spear-phishing campaigns, credential theft operations, or business email compromise (BEC), adversaries routinely establish fraudulent accounts (mapped to **MITRE ATT&CK T1585.001: Establish Accounts - Social Media**).

**PEER'S Persona Guard Suite v2.5** is an enterprise-grade social media impersonation detection, bot behavioral analysis, and brand protection suite developed for **Day 09** of the Sqrock IT Solutions Cybersecurity Internship. It delivers a multi-vector scoring architecture that correlates:
1. **Creation Velocity & Account Longevity:** Flags disposable accounts created under 7–30 days.
2. **Network Topology Anomalies:** Detects skewed Following-to-Follower ratios (`following / followers > 10.0 to 50.0+`).
3. **Visual & Bio Completeness:** Identifies default avatars, blank descriptions, or scraped asset templates.
4. **Activity & Engagement Velocity:** Analyzes publication volume and flags accounts with `< 5 posts`.
5. **Algorithmic Homoglyph & Executive Collision:** Calculates normalized string similarity against a protected directory of corporate executives to catch lookalike handles (e.g., substituting numeric zero for letter 'o').

```
+========================================================================+
|             PEER'S PERSONA GUARD SUITE v2.5 - ARCHITECTURE             |
+========================================================================+
|                                                                        |
|  [Suspicious Social Media Profile Candidate]                           |
|          |                                                             |
|          v                                                             |
|  [Persona Guard Behavioral Inspection Engine]                          |
|          |                                                             |
|   +------+----------------------------------------------------------+  |
|   | Multi-Vector Scoring & Threat Correlation Pipeline              |  |
|   |                                                                 |  |
|   |  1. Executive Impersonation & Homoglyph Matcher                 |  |
|   |     * Cross-references Protected Corporate Executive Roster     |  |
|   |     * SequenceMatcher similarity >= 70% -> Flag +35 Points      |  |
|   |                                                                 |  |
|   |  2. Account Age & Creation Velocity Sensor                      |  |
|   |     * Age < 7 Days: +35 Points | Age < 30 Days: +25 Points      |  |
|   |     * Age > 365 Days: -15 Points (Organic Longevity Credit)     |  |
|   |                                                                 |  |
|   |  3. Network Topology & Following Ratio Analyzer                 |  |
|   |     * Ratio > 50:1: +30 Points | Ratio > 10:1: +20 Points       |  |
|   |     * Ratio <= 0.1 (Audience Authority): -15 Points             |  |
|   |                                                                 |  |
|   |  4. Visual Asset & Bio Incompleteness Detector                  |  |
|   |     * Default Avatar / Missing Picture: +20 Points              |  |
|   |     * Blank or Default Bio: +15 Points                          |  |
|   |     * Minimal Activity (< 5 posts): +15 Points                  |  |
|   |     * External Malicious / Phishing URL: +25 Points             |  |
|   |                                                                 |  |
|   |  5. Normalized Threat Score (0 - 100) & Classification          |  |
|   |     * Score >= 75: CRITICAL_IMPERSONATOR / HIGH_RISK_BOT        |  |
|   |     * Score >= 45: SUSPICIOUS_PROFILE_EVALUATION                |  |
|   |     * Score < 45 : AUTHENTIC_ORGANIC_ACCOUNT                    |  |
|   +-----------------------------------------------------------------+  |
+========================================================================+
```

---

## 🛡️ Core Capabilities

1. **Multi-Vector Behavioral Heuristic Scorer (`profile_auditor.py`)**
   - Evaluates profiles on continuous mathematical scales rather than rigid boolean rules.
   - Accurately balances suspicious indicators against positive trust factors (e.g., account age > 1 year, verified badge, organic audience size).
   - Prevents false positives by distinguishing genuine new organic users from aggressive bots.

2. **Executive Collision & Homoglyph Detector**
   - Automatically cross-references incoming handles and display names against a protected corporate executive database.
   - Detects character substitutions (e.g., `@peer_siddiqui_ce0` mimicking `@peer_siddiqui_real`), dropped letters, and brand name mimicry using normalized gesture pattern matching (`difflib.SequenceMatcher`).

3. **5 Curated Real-World Profile Test Vectors (`datasets/profile_samples.json`)**
   - Rigorously benchmarks the detection engine across five diverse identity archetypes:
     - `PROF-001`: Malicious C-Suite Impersonator (`Score: 95/100 -> CRITICAL`)
     - `PROF-002`: Automated Crypto Phishing Bot (`Score: 90/100 -> CRITICAL`)
     - `PROF-003`: Social Engineering Recruiter Account (`Score: 60/100 -> SUSPICIOUS`)
     - `PROF-004`: Authentic Corporate Executive (`Score: 5/100 -> AUTHENTIC`)
     - `PROF-005`: Genuine New Organic Developer (`Score: 15/100 -> AUTHENTIC`)

4. **SIEM Telemetry & Threat Intelligence Export**
   - Serializes audit results into structured JSON (`audit_reports/persona_audit_report.json`) and human-readable SOC briefings (`audit_reports/persona_audit_report.txt`).

---

## 📂 Repository Structure

```
PEER-S-Persona-Guard-Suite/
├── profile_auditor.py            # Interactive social impersonation & bot detection CLI suite
├── requirements.txt              # Core project dependencies (colorama, reportlab, pillow)
├── LICENSE                       # MIT License
├── README.md                     # Technical documentation & usage guide
├── datasets/
│   └── profile_samples.json      # 5 curated real-world profile test vectors
├── audit_reports/
│   ├── persona_audit_report.json # Structured JSON threat intelligence export
│   └── persona_audit_report.txt  # Human-readable executive SOC incident briefing
├── tests/
│   └── test_profile_auditor.py   # 6-point automated PyUnit verification suite
├── scripts/
│   ├── generate_terminal_screens.py # Headless PIL terminal screenshot generator
│   └── generate_day09_pdf.py     # ReportLab multi-page executive report compiler
└── reports/
    ├── Day09_Social_Impersonation_Report_Sqrock_MdPeerSiddiqui.pdf # 7-page executive lab report
    └── screenshots/              # High-fidelity terminal evidence
        ├── 01_kali_init_banner.png
        ├── 02_master_menu.png
        ├── 03_batch_audit_results.png
        ├── 04_single_profile_deepdive.png
        ├── 05_executive_collision_scan.png
        └── 06_github_repo_overview.png
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- Git
- Kali Linux, Ubuntu, Debian, or Windows 10/11

### 2. Clone the Repository
```bash
git clone https://github.com/MdPeerSiddiqui/PEER-S-Persona-Guard-Suite.git
cd PEER-S-Persona-Guard-Suite
```

### 3. Create and Activate Virtual Environment
```bash
# On Linux / macOS / Kali:
python3 -m venv .venv
source .venv/bin/activate

# On Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Execution & Usage Guide

Launch the master interactive console:
```bash
python profile_auditor.py
```

### Operational Modes:
- **`[1] Audit Single Social Profile`**  
  Prompts for handle, age, follower ratio, bio status, and external links; returns an itemized penalty breakdown and threat tier.
- **`[2] Run Batch Audit on 5 Real-World Profile Samples`**  
  Ingests the complete benchmark dataset (`datasets/profile_samples.json`) and generates a side-by-side threat comparison table.
- **`[3] Executive Impersonation & Homoglyph Collision Scanner`**  
  Tests candidate handles and display names against protected corporate executives to detect typosquats and lookalike characters.
- **`[4] Export Threat Intelligence & Audit Report`**  
  Compiles and saves audit records to `audit_reports/persona_audit_report.json` and `.txt`.
- **`[5] View Behavioral Heuristics & Scoring Weights Matrix`**  
  Displays the transparent scoring breakdown and point allocations.
- **`[6] Display Enterprise Brand Protection & Anti-Impersonation Blueprint`**  
  Presents corporate brand monitoring strategies, DMCA takedown policies, and zero-trust social messaging protocols.

---

## 🧪 Automated Unit Verification

A comprehensive 6-point test suite is included in `tests/test_profile_auditor.py`:

```bash
python -m unittest tests/test_profile_auditor.py -v
```

### Test Suite Results:
| Test Method | Target Component | Status |
| :--- | :--- | :---: |
| `test_account_age_penalty` | Creation Velocity Heuristic Sensor | `PASSED` |
| `test_follower_ratio_penalty` | Network Topology Ratio Analyzer | `PASSED` |
| `test_default_profile_elements` | Visual Asset & Bio Incompleteness Sensor | `PASSED` |
| `test_homoglyph_impersonation_detection` | Executive Homoglyph Collision Engine | `PASSED` |
| `test_legitimate_profile_low_score` | Organic Trust Factor & False Positive Prevention | `PASSED` |
| `test_batch_dataset_processing` | Multi-Vector Dataset Batch Processing | `PASSED` |

**Verification Result: 6/6 Tests Passed (100% OK).**

---

## 📊 Benchmark Dataset Evaluation (5 Profile Samples)

| Profile ID | Handle | Age (Days) | Follower Ratio | Threat Score | Verdict |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **PROF-001** | `@peer_siddiqui_ce0` | 4 | 58.6:1 | **95 / 100** | `CRITICAL_IMPERSONATOR_THREAT` |
| **PROF-002** | `@airdrop_reward_bot2026` | 7 | 122.5:1 | **90 / 100** | `HIGH_RISK_AUTOMATED_BOT` |
| **PROF-003** | `@sarah_recruiter_tech` | 26 | 17.6:1 | **60 / 100** | `SUSPICIOUS_PROFILE_EVALUATION` |
| **PROF-004** | `@peer_siddiqui_real` | 1420 | 0.02:1 | **5 / 100** | `AUTHENTIC_ORGANIC_ACCOUNT` |
| **PROF-005** | `@dev_arjun_patel` | 24 | 1.37:1 | **15 / 100** | `AUTHENTIC_ORGANIC_ACCOUNT` |

---

## 📜 Compliance & Industry Standards

- **MITRE ATT&CK T1585.001:** Establish Accounts: Social Media.
- **NIST CSF DE.CM-1:** The network and perimeter are monitored to detect potential cybersecurity events.
- **OWASP Social Engineering Heuristics:** Profile verification and trust-building countermeasures.

---

## 👤 Author & Acknowledgments

- **Lead Developer:** Mohammed Peer Siddiqui
- **Internship Organization:** Sqrock IT Solutions
- **Track:** Social Engineering Attack Simulations Using Python (Alpha 2 Cohort)
- **LinkedIn:** [Mohammed Peer Siddiqui](https://www.linkedin.com)
- **GitHub:** [@MdPeerSiddiqui](https://github.com/MdPeerSiddiqui)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.
