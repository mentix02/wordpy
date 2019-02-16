"""
test_utils.py
TestCases for utility functions
"""
import string
import unittest

from wordpy import utils

TEST_STRING = string.ascii_letters + string.digits
TEST_STRING_REV = TEST_STRING[::-1]

# noinspection SpellCheckingInspection
STRINGS = {
    'info': [
        '\x1b[1m\x1b[34m[i] abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\x1b[0m',
        'm0[\x1b9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba ]i[m43[\x1bm1[\x1b'
    ],
    'error': [
        '\x1b[1m\x1b[31m[e] abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\x1b[0m',
        'm0[\x1b9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba ]e[m13[\x1bm1[\x1b'
    ],
    'success': [
        '\x1b[1m\x1b[32m[s] abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\x1b[0m',
        'm0[\x1b9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba ]s[m23[\x1bm1[\x1b'
    ],
    'warning': [
        '\x1b[1m\x1b[33m[w] abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\x1b[0m',
        'm0[\x1b9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba ]w[m33[\x1bm1[\x1b'
    ]
}


class UtilsTest(unittest.TestCase):
    """
    test cases for asserting
    basic string utilities to
    check text colors and
    levels of output
    """

    def setUp(self):
        """
        initialize test output
        messages with appropriate levels
        """
        self.info_msg = utils.info(TEST_STRING)
        self.error_msg = utils.error(TEST_STRING)
        self.success_msg = utils.success(TEST_STRING)
        self.warning_msg = utils.warning(TEST_STRING)

    def test_info(self):
        """
        information asserting with blue colouring
        """
        self.assertEqual(self.info_msg, STRINGS['info'][0])
        self.assertEqual(self.info_msg[::-1], STRINGS['info'][1])

    def test_error(self):
        """
        error asserting with red colouring
        """
        self.assertEqual(self.error_msg, STRINGS['error'][0])
        self.assertEqual(self.error_msg[::-1], STRINGS['error'][1])

    def test_success(self):
        """
        success asserting with green colouring
        """
        self.assertEqual(self.success_msg, STRINGS['success'][0])
        self.assertEqual(self.success_msg[::-1], STRINGS['success'][1])

    def test_warning(self):
        """
        warning asserting with yellow colouring
        """
        self.assertEqual(self.warning_msg, STRINGS['warning'][0])
        self.assertEqual(self.warning_msg[::-1], STRINGS['warning'][1])
