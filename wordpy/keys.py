"""
author : mentix02
timestamp : Sun Feb  3 18:44:33 2019
"""

import json

from . import utils

keys = {}

try:
    with open('/tmp/keys.json', 'r') as key_file:
        keys = json.loads(key_file.read())
except FileNotFoundError:
    print(utils.warning('Credentials for API are missing. Please register ' + \
                        'an account at https://developer.oxforddictionaries.com/'))

    # get input from user 
    # for app_id and app_key
    keys['app_id'] = input(utils.info('Enter your application ID : '))
    keys['app_key'] = input(utils.info('Enter your application key : '))


    # write /tmp/keys.json
    # for future useage
    data = json.dumps(keys)
    key_file = open('/tmp/keys.json', 'w+')
    key_file.write(data)
    key_file.close()
