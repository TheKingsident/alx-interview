#!/usr/bin/python3
""" 0. UTF-8 Validation
"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """ method that determines if a given data set represents a
        valid UTF-8 encoding
    """
    bytes_left = 0

    for item in data:
        mask = 0b10000000

        if bytes_left == 0:
            if item & 0b10000000 == 0:
                continue
            elif item & 0b11100000 == 0b11000000:
                bytes_left = 1
            elif item & 0b11110000 == 0b11100000:
                bytes_left = 2
            elif item & 0b11111000 == 0b11110000:
                bytes_left = 3
            else:
                return False
        else:
            if item & mask == 0b10000000:
                bytes_left -= 1
            else:
                return False

    return bytes_left == 0
