# SPDX-License-Identifier: MIT


# Import first-party Python modules.
import os
import sys
from typing import NoReturn

# Add support layer for accessing the primary package.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# Import local modules.
import avro
from avro.core import config


# Test functions for this file.
def test_patterns_without_rules_from_config() -> NoReturn:
    """
    Tests all patterns from config that don't have rules.
    """

    for pattern in config.DICT["avro"]["patterns"]:
        if "rules" not in pattern and pattern.get("find", None):
            assert pattern["replace"] == avro.parse(pattern["find"])


def test_patterns_without_rules_not_from_config() -> NoReturn:
    """
    Tests all patterns not from config that don't have rules.

    This test is done in addition to
    test_patterns_without_rules_from_config() to ensure that text
    passed manually to avro.parse are properly parsed when they
    don't exact match a pattern that has no rules specified.
    """

    conjunctions = {
        "ভ্ল": "bhl",
        "ব্ধ": "bdh",
        "ড্ড": "DD",
        "স্তব্ধ বক": "stbdh bk",  # Stunned stork!
    }

    for key, value in conjunctions.items():
        assert key == avro.parse(value)


def test_patterns_numbers() -> NoReturn:
    """
    Test patterns - numbers
    """

    numbers = {
        "০": "0",
        "১": "1",
        "২": "2",
        "৩": "3",
        "৪": "4",
        "৫": "5",
        "৬": "6",
        "৭": "7",
        "৮": "8",
        "৯": "9",
        "১১২": "112",
    }

    for key, value in numbers.items():
        assert key == avro.parse(value)


def test_patterns_punctuations() -> NoReturn:
    """
    Tests patterns - punctuations
    """

    punctuations = {
        "।": ".",
        "।।": "..",
        "...": "...",
    }

    for key, value in punctuations.items():
        assert key == avro.parse(value)
        assert value == avro.reverse(key)


def test_patterns_with_rules_svaravarna() -> NoReturn:
    """
    Test patterns - with rules - svaravarna / shoroborno (derived from Bengali)
    """

    svaravarna = {
        "অ": "o",
        "আ": "a",
        "ই": "i",
        "ঈ": "I",
        "উ": "u",
        "ঊ": "oo",
        "ঊ": "U",
        "এ": "e",
        "ঐ": "OI",
        "ও": "O",
        "ঔ": "OU",
    }

    for key, value in svaravarna.items():
        assert key == avro.parse(value)


def test_non_ascii() -> NoReturn:
    """
    Test processor response for non-ASCII characters.
    Parse function should return any non-ASCII characters that is passed to it.
    """

    # Mixed strings.
    non_ascii = {
        "ব": "ব",
        "অভ্র": "অভ্র",
        "বআবা গো": "বaba gO",
        "আমি বাংলায় গান গাই": "aমি বাংলায় gaন গাi",
    }

    for key, value in non_ascii.items():
        assert key == avro.parse(value)


def test_ascii() -> NoReturn:
    """
    Test processor response for ASCII characters.
    Reverse function should return any ASCII characters that is passed to it.
    """

    assert "Avwg evsjvi gan MvB|" == avro.reverse("Avwg evsjvi গান MvB|")
    assert "Avwg amar Avwg‡K wPiw`b GB banglay Lyu‡R cvB!" == avro.reverse(
        "Avwg আমার Avwg‡K wPiw`b GB বাংলায় Lyu‡R cvB!"
    )


def test_words_with_punctuations() -> NoReturn:
    """
    Test parsing and reversing of words with punctuations.
    """

    test_words = {
        "আয়রে,": "ayre,",
        "ভোলা;": "bhOla;",
        "/খেয়াল": "/kheyal",
        "খোলা|": "khOla|",
    }

    for key, value in test_words.items():
        assert key == avro.parse(value)
        assert value.lower() == avro.reverse(key)


def test_exceptions() -> NoReturn:
    """
    Test parsing and reversing of exceptions.
    """

    assert "আমি উইকিপিডিয়া আর ফেসবুক চালাই।" == avro.parse("ami Wikipedia ar Facebook calai.")
    assert "ami Wikipedia ar Facebook chalai." == avro.reverse("আমি উইকিপিডিয়া আর ফেসবুক চালাই।")


def test_conversion_bijoy_func() -> NoReturn:
    """
    Test conversion to Bijoy directly.
    """

    # Regular Conversion.
    assert "Avwg evsjvq Mvb MvB;" == avro.to_bijoy("আমি বাংলায় গান গাই;")
    assert [
        "Avwg evsjvi Mvb MvB|",
        "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
    ] == avro.to_bijoy("আমি বাংলার গান গাই।", "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!")

    # Fail-safe Conversion.
    assert "Hello, World!" == avro.to_bijoy("Hello, World!")


def test_conversion_unicode_func() -> NoReturn:
    """
    Test conversion to Unicode directly.
    """

    # Regular Conversion.
    assert "আমি বাংলায় গান গাই;" == avro.to_unicode("Avwg evsjvh় Mvb MvB;")
    assert [
        "আমি বাংলার গান গাই।",
        "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!",
    ] == avro.to_unicode("Avwg evsjvi Mvb MvB|", "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!")


def test_parse_sentences() -> NoReturn:
    """
    Test parsing of sentences (Unicode).
    """

    # Default parsing.
    assert "আমি বাংলায় গান গাই;" == avro.parse("ami banglay gan gai;")
    assert [
        "আমি বাংলার গান গাই।",
        "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই।",
    ] == avro.parse("ami banglar gan gai.", "ami amar amike cirodin ei banglay khu^je pai.")

    # Bijoy parsing.
    assert "Avwg evsjvq Mvb MvB;" == avro.parse("ami banglay gan gai;", bijoy=True)
    assert [
        "Avwg evsjvi Mvb MvB|",
        "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
    ] == avro.parse("ami banglar gan gai.", "ami amar amike cirodin ei banglay khu^je pai!", bijoy=True)


def test_reverse_error() -> NoReturn:
    """
    Tests
    """


def test_reverse_sentences() -> NoReturn:
    """
    Test reversing of sentences (Unicode).
    """

    # Default reversing.
    assert "ami banglay gan gai." == avro.reverse("আমি বাংলায় গান গাই।")
    assert [
        "rohim, tomake korim dakche. ekhon ki rowna debe?",
        "rowna dile amake bole zew.",
    ] == avro.reverse("রহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?", "রওনা দিলে আমাকে বলে যেও।")

    # Bijoy reversing.
    assert "ami banglar gan gai." == avro.reverse("Avwg evsjvi Mvb MvB|", from_bijoy=True)
