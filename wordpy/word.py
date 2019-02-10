"""
author : mentix02
timestamp : Sat Feb  2 16:49:05 2019
"""

import os
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
        self.antonyms = []
        self.etymology = ''
        self.definition = ''
        self.thesaurus: tWord = ''

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
            print(utils.error(f'Word `{self.word}` was not found'))
            exit(1)
        elif data.status_code == 403:
            # documented over at 
            # https://bit.ly/2UCI7b4
            # to return 403 is API keys 
            # are invalid or expired or
            # have extended the limit usage
            print(utils.error(f'Invalid credentials. Please manually edit ' +
                              '/tmp/keys.json with proper application id.'))
            return_code = os.system(f'{os.getenv('EDITOR')} /tmp/keys.json')
            if return_code != 0:
                print(utils.error('Please set a default $EDITOR variable for shell.'))
            exit(1)
        elif data.status_code != 200:
            # handling all other errors
            print(utils.error(f'Something went wrong. Please report a ' +
                              'bug at https://github.com/mentix02/wordpy/issues.'))
            exit(1)

        return data.text

    def get_thesaurus(self) -> tWord:
        """
        load tWord module if any
        flags for synonyms or
        antonyms is provided for
        the specific self.word
        """
        self.thesaurus = tWord(self.word)
        return self.thesaurus

    def fill_empty_thesaurus(self):
        """
        check if the thesaurus
        object has been initialized
        """
        try:
            if self.thesaurus == '':
                self.get_thesaurus()
        except Exception as e:
            print(utils.error(e))
            exit(1)

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

        self.fill_empty_thesaurus()

        self.synonyms = self.thesaurus.synonyms(0)
        return self.synonyms

    def get_antonyms(self) -> list:
        """
        reasons for not including
        this in __init__() are the
        same as self.get_synonyms()
        """

        self.fill_empty_thesaurus()

        self.antonyms = self.thesaurus.antonyms(0)
        return self.antonyms

    def get_etymology(self) -> str:
        """
        get_<pattern> syntax
        follows over here as well
        """

        self.fill_empty_thesaurus()

        self.etymology = self.thesaurus.origin()
        return self.etymology

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
            print(utils.success('Synonyms'))
            print(utils.p_list(self.synonyms))

    def display_antonyms(self):
        """
        same as self.display_synonyms()
        in regards to calling __repr__()
        """
        self.get_antonyms()

        if len(self.antonyms) == 0:
            print(utils.error(f'No antonyms found for - {self.word}'))
        else:
            print(utils.success('Antonyms'))
            print(utils.p_list(self.antonyms))

    def display_etymology(self):
        """
        same reasons follow for
        as self.display_synonyms()
        """
        self.get_etymology()

        if len(self.etymology) == '':
            print(utils.error(f'No etymology found for - {self.word}'))
        else:
            print(utils.success('Etymology'))
            print(self.etymology)

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
