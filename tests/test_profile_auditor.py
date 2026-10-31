#!/usr/bin/env python3
"""
================================================================================
Automated Unit Verification Suite for PEER'S Persona Guard Suite
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
================================================================================
"""

import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from profile_auditor import (
    evaluate_profile,
    check_executive_collision,
    compute_string_similarity,
    load_dataset
)


class TestPersonaGuardSuite(unittest.TestCase):
    """Test suite covering behavioral scoring, homoglyph detection, and batch audit."""

    def test_account_age_penalty(self):
        """Verify young accounts (<7d and <30d) incur appropriate velocity penalties."""
        profile_young = {
            "username": "brand_new_user",
            "account_age_days": 3,
            "followers": 100,
            "following": 100,
            "posts": 50
        }
        res = evaluate_profile(profile_young)
        self.assertGreaterEqual(res["threat_score"], 35)
        self.assertTrue(any("EXTREME_ACCOUNT_VELOCITY" in p for p in res["penalties"]))

    def test_follower_ratio_penalty(self):
        """Verify skewed following-to-follower ratio triggers penalty."""
        profile_ratio = {
            "username": "follow_spammer",
            "account_age_days": 100,
            "followers": 10,
            "following": 600,  # 60:1 ratio
            "posts": 50
        }
        res = evaluate_profile(profile_ratio)
        self.assertGreaterEqual(res["threat_score"], 30)
        self.assertTrue(any("EXTREME_FOLLOW_RATIO" in p for p in res["penalties"]))

    def test_default_profile_elements(self):
        """Verify default avatar and missing bio triggers visual incompleteness penalties."""
        profile_blank = {
            "username": "ghost_account",
            "account_age_days": 100,
            "followers": 100,
            "following": 100,
            "no_profile_pic": True,
            "has_default_bio": True,
            "posts": 50
        }
        res = evaluate_profile(profile_blank)
        self.assertGreaterEqual(res["threat_score"], 35)
        self.assertTrue(any("DEFAULT_AVATAR" in p for p in res["penalties"]))
        self.assertTrue(any("INCOMPLETE_BIO" in p for p in res["penalties"]))

    def test_homoglyph_impersonation_detection(self):
        """Verify executive impersonator handles trigger homoglyph collision alerts."""
        collisions = check_executive_collision("peer_siddiqui_ce0", "Mohammed Peer Siddiqui (CEO)")
        self.assertTrue(len(collisions) > 0)
        self.assertEqual(collisions[0]["target_handle"], "@peer_siddiqui_real")
        self.assertGreaterEqual(collisions[0]["handle_similarity"], 80.0)

    def test_legitimate_profile_low_score(self):
        """Verify authentic corporate profile receives low threat score (<= 10)."""
        legit_profile = {
            "username": "peer_siddiqui_real",
            "display_name": "Mohammed Peer Siddiqui",
            "account_age_days": 1420,
            "followers": 18400,
            "following": 450,
            "no_profile_pic": False,
            "has_default_bio": False,
            "bio": "Lead Security Researcher @ Sqrock IT Solutions",
            "posts": 720,
            "is_verified": True
        }
        res = evaluate_profile(legit_profile)
        self.assertLessEqual(res["threat_score"], 10)
        self.assertEqual(res["risk_tier"], "LOW")
        self.assertEqual(res["verdict"], "AUTHENTIC_ORGANIC_ACCOUNT")

    def test_batch_dataset_processing(self):
        """Verify all 5 dataset profile samples are properly loaded and evaluated."""
        dataset = load_dataset()
        self.assertEqual(len(dataset), 5)
        
        results = [evaluate_profile(p) for p in dataset]
        self.assertEqual(len(results), 5)
        
        # Verify Profile 1 is flagged as high/critical threat
        p1_res = next(r for r in results if r["profile_id"] == "PROF-001")
        self.assertGreaterEqual(p1_res["threat_score"], 80)
        self.assertIn("CRITICAL", p1_res["risk_tier"])

        # Verify Profile 4 is flagged as low risk
        p4_res = next(r for r in results if r["profile_id"] == "PROF-004")
        self.assertLessEqual(p4_res["threat_score"], 10)


if __name__ == "__main__":
    unittest.main()
