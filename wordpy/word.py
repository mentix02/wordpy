"""
author : mentix02
timestamp : Sat Feb  2 16:49:05 2019
"""

import json
import requests

from . import keys
from . import utils
# from . import exceptions

from thesaurus import Word as tWord

BASE_URL = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en'

keys = keys.keys  # load keys for authentications


class Word:
    """
    class "Word" used for 
    extracting definitions 
    and synonyms using APIs
    """

    def __init__(self, word: str):

        # initialise variables
        # with empty values

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

        self.definition = self.get_definition()

    def get_definition(self) -> str:
        return self.senses[0]['definitions'][0]

    def _raw_data(self) -> str:

        # make the actual request
        # with params loaded in the 
        # BASE_URL along with appropriate
        # headers containing authentication keys
        data = requests.get(
            f'{BASE_URL}/{self.word}',
            headers=keys
        )

        # response status code 
        # exception handling below

        if data.status_code == 404:
            # raise exceptions.WordNotFound
            # commented out the exception because it looks ugly
            print(utils.error(f'Word {self.word} was not found'))
            exit(1)
        elif data.status_code == 403:
            # documented over at 
            # https://bit.ly/2UCI7b4
            # to return 403 is API keys 
            # are invalid or expired or
            # have extended the limit usage
            print(utils.error(f'Invalid credentials. Please manually edit ' +
                              '/tmp/keys.json with proper application id.'))
            exit(1)
        elif data.status_code != 200:
            # handling all other errors
            print(utils.error(f'Something went wrong. Please report a ' +
                              'bug at https://github.com/mentix02/wordpy/issues.'))
            exit(1)

        return data.text

    def get_synonyms(self) -> list:
        """
        the design choice to 
        not call this in __init__()
        was consciously made as this
        calls another package that in
        turn makes other requests to a
        different online service thus 
        increasing the total response time
        taken for making a call to the inline
        dictionary API itself. calling this
        function acts like an extension
        to the Word class and should be
        treated like so. not all users want
        to know the synonyms for a word and
        if they do then this is the only 
        function that will be called and 
        the class will never go through the
        __repr__() method at all
        """
        thesaurus = tWord(self.word)
        synonyms = thesaurus.synonyms(0)
        self.synonyms = synonyms
        return synonyms

    def display_synonyms(self):
        """
        calls __repr__() in and
        of itself since the -s flag
        will only call this method &
        nothing else
        """
        self.get_synonyms()
        if len(self.synonyms) == 0:
            print(utils.error(f'No synonyms found for - {self.word}'))
        else:
            print(self)
            print(utils.success('Synonyms'))
            print(', '.join(self.synonyms))
            # print(f'{self.word} - ', ',  '.join(self.synonyms))

    def __repr__(self) -> str:
        """
        for better formatting
        of instances of the Word 
        class displaying the definition
        instead of just the object with 
        it's memory location. arguable,
        it's more developer friendly as well
        """
        return \
            utils.success(f'{self.word.title()} ({self.category.lower()})\n') + f'{self.definition.capitalize()}'
