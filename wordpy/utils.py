"""
author : mentix02
timestamp : Sat Feb  2 16:14:39 2019
"""

from termcolor import colored


def success(text: str) -> str:
    return colored(f'[s] {text}', 'green', attrs=['bold'])


def info(text: str) -> str:
    return colored(f'[i] {text}', 'blue', attrs=['bold'])


def warning(text: str) -> str:
    return colored(f'[w] {text}', 'yellow', attrs=['bold'])


def error(text: str) -> str:
    return colored(f'[e] {text}', 'red', attrs=['bold'])


def p_list(words: list) -> str:
    return ', '.join(words)

