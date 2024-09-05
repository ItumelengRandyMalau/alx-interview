#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    i = 1 << 7
    X = 1 << 6
    byte_count = 0
    for code in data:
        j = 1 << 7
        if byte_count == 0:
            while j & code:
                byte_count += 1
                j = j >> 1
            if byte_count == 0:
                continue
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (code & i and not (code & X)):
                return False
        byte_count -= 1
    return not byte_count
