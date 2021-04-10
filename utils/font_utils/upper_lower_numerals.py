#!/usr/bin/env python3

import string

class UpperLowerNumerals:

    @staticmethod
    def get_ascii_codes():
        _upper_lower = string.ascii_letters
        _numerals = '0123456789'
        _uln = _upper_lower+_numerals
        return [ord(x) for x in _uln]
