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


class DefinitionTest(unittest.TestCase):

    def setUp(self):
        self.car = Word('car')
        self.airplane = Word('airplane')

    def test_definitions(self):
        self.assertEqual(data['car'][0], self.car.get_definition())
        self.assertEqual(data['airplane'][0], self.airplane.get_definition())


if __name__ == '__main__':
    unittest.main()
