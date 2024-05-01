# SPDX-License-Identifier: MIT


# Import local modules.
from avro import config


# Functions.
def count_vowels(text: str) -> int:
    """
    Count number of occurrences of vowels in a given string.
    """

    return sum(1 for i in text if i.lower() in config.AVRO_VOWELS)


def count_consonants(text: str) -> int:
    """
    Count number of occurrences of consonants in a given string.
    """

    return sum(1 for i in text if i.lower() in config.AVRO_CONSONANTS)
