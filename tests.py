#!/usr/bin/env python3

import unittest
import challenge0
import challenge1

class tests_challenge0(unittest.TestCase):
    """Tests for challenge0"""
    def test_exponentiate(self):
        self.assertEqual(challenge0.exponentiate(2,38), int(274877906944))

class tests_challenge1(unittest.TestCase):
    """Tests for challenge1"""
    def test_exponentiate(self):
        self.assertEqual(challenge1.decipher("""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""), str("""i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's
why this text is so long. using string.maketrans() is recommended. now apply on the url."""))

if __name__ == "__main__":
    unittest.main()

