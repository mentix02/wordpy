import json
import unittest

import requests

from wordpy import Word


try:
    with open('./data.json') as data_file:
        data = json.loads(data_file.read())
except FileNotFoundError:
    raw = requests.get('https://pastebin.com/raw/VatVLSLQ').text
    data = json.loads(raw)


class SynonymTest(unittest.TestCase):

    def setUp(self):
        self.car = Word('car')
        self.airplane = Word('airplane')

    def test_getting_synonyms(self):
        self.car.get_synonyms()
        self.airplane.get_synonyms()

    def test_synonyms(self):
        self.assertEqual(data['car'][1], self.car.get_synonyms())
        self.assertEqual(data['airplane'][1], self.airplane.get_synonyms())


if __name__ == '__main__':
    unittest.main()
