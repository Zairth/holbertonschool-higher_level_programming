#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)
    first_char = ''

    if _len != 0:
        first_char = sentence[0]

    tuple = (_len, first_char)

    return tuple
