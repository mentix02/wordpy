"""
dict : mentix02
timestamp : Sat Feb  2 16:49:05 2019
"""

import json
import requests

import utils

from thesaurus import Word as tWord

BASE_URL = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en'

with open('/tmp/keys.json') as data:
    """
    derive keys from file
    stores in keys.json
    """
    keys = json.loads(data.read())


class Word:
    """
    class "Word" used for 
    extracting definitions 
    and synonyms using APIs
    """

    def __init__(self, word: str):
        
        self._data = ''
        self._json = {}
        self.category = ''
        self.synonyms = []
        self.definition = ''

        self.word = str(word).lower()

        self._data = self._raw_data()
        self._json = json.loads(self._data)
        self.lexicalEntries = self._json['results'][0]['lexicalEntries']

        self.category = self.lexicalEntries[0]['lexicalCategory']
        self.senses = self.lexicalEntries[0]['entries'][0]['senses']

        self.definition = self.senses[0]['definitions'][0]

    def _raw_data(self) -> str:

        data =  requests.get(
            f'{BASE_URL}/{self.word}',
            headers = keys
        )

        return data.text

    def get_synonyms(self) -> list:
        thesaurus = tWord(self.word)
        synonyms = thesaurus.synonyms(0)
        self.synonyms = synonyms
        return synonyms

    def __repr__(self) -> str:
        return utils.success(f'{self.word.title()}({self.category.lower()})\n') + \
            f'{self.definition.capitalize()}'


apple = Word('car')
print(apple)
