#!/usr/bin/env python3

import unittest
import challenge0

class tests_challenge0(unittest.TestCase):
    """Tests for challenge0"""
    def test_exponentiate(self):
        self.assertEqual(challenge0.exponentiate(2,38), int(274877906944))

if __name__ == "__main__":
    unittest.main()

