"""
author : mentix02
timestamp : Sun Feb  3 18:17:27 2019
"""

class WordNotFoundException(Exception):
    """
    raised when a word
    the user enters isn't
    found in the Oxford API
    """
    pass


class InvalidCredentialsException(Exception):
    """
    raised when app_id 
    and other credentials
    are wrong and API returns
    with a status code of 403
    """
    pass