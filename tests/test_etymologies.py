import json
import unittest

import requests

from wordpy import Word


try:
    with open('./data.json') as data_file:
        data = json.loads(data_file.read())
except FileNotFoundError:
    raw = requests.get('https://pastebin.com/raw/C904cJLK').text
    data = json.loads(raw)


class EtymologyTest(unittest.TestCase):

    def setUp(self):
        self.car = Word('car')
        self.happy = Word('happy')

    def test_get_etymologies(self):
        self.car.get_etymology()
        self.happy.get_etymology()

    def test_origins(self):
        self.assertEqual(data['car']['etymology'], self.car.get_etymology())
        self.assertEqual(data['happy']['etymology'], self.happy.get_etymology())
