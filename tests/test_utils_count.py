# SPDX-License-Identifier: MIT


# Import first-party Python modules.
import os
import sys
from typing import NoReturn

# Add support layer for accessing the primary package.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# Import local modules.
from avro.utils import count


# Test functions for this file.
def test_count_vowels() -> NoReturn:
    """
    Test vowel count in a given string.
    """

    strings = {
        'haTTima Tim Tim': 5,
        'tara maThe paRe Dim': 7,
        'tader mathay duTO sing': 7,
        'tara haTTima Tim Tim': 7,
    }

    for string, integer in strings.items():
        assert count.count_vowels(string) == integer


def test_count_consonants() -> NoReturn:
    """
    Test consonant count in a given string.
    """

    strings = {
        'ei dekh pensil': 7,
        'nOTbuk e hate': 6,
        'ei dekh bhora sob': 8,
        'kil`bil lekha te': 8,
    }

    for string, integer in strings.items():
        assert count.count_consonants(string) == integer
