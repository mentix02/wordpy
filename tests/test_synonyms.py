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
        self.happy = Word('happy')

    def test_get_synonyms(self):
        self.car.get_synonyms()
        self.happy.get_synonyms()

    def test_synonyms(self):
        self.assertEqual(data['car']['synonyms'], self.car.get_synonyms())
        self.assertEqual(data['happy']['synonyms'], self.happy.get_synonyms())
