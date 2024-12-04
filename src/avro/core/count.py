# SPDX-License-Identifier: MIT


# Imports.
from avro.core import config


# Functions.
def count_vowels(text: str) -> int:
    """Count number of occurrences of vowels in a given string.

    Parameters:
    -----------

    text: str
        The text to count vowels from.

    Returns:
    --------

    int
        The number of vowels in the given text.
    """

    return sum(1 for i in text if i.lower() in config.AVRO_VOWELS)


def count_consonants(text: str) -> int:
    """Count number of occurrences of consonants in a given string.

    Parameters:
    -----------

    text: str
        The text to count consonants from.

    Returns:
    --------

    int
        The number of consonants in the given text.
    """

    return sum(1 for i in text if i.lower() in config.AVRO_CONSONANTS)
