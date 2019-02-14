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

    def setUp(self):
        self.infoMsg = utils.info(TEST_STRING)
        self.errorMsg = utils.error(TEST_STRING)
        self.successMsg = utils.success(TEST_STRING)
        self.warningMsg = utils.warning(TEST_STRING)

    def test_info(self):
        self.assertEqual(self.infoMsg, STRINGS['info'][0])
        self.assertEqual(self.infoMsg[::-1], STRINGS['info'][1])

    def test_error(self):
        self.assertEqual(self.errorMsg, STRINGS['error'][0])
        self.assertEqual(self.errorMsg[::-1], STRINGS['error'][1])

    def test_success(self):
        self.assertEqual(self.successMsg, STRINGS['success'][0])
        self.assertEqual(self.successMsg[::-1], STRINGS['success'][1])

    def test_warning(self):
        self.assertEqual(self.warningMsg, STRINGS['warning'][0])
        self.assertEqual(self.warningMsg[::-1], STRINGS['warning'][1])
