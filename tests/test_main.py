# SPDX-License-Identifier: MIT OR Apache-2.0


# Import first-party Python modules.
import os
import sys

# Add support layer for accessing the primary package.
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# Import local modules.
import pytest

import avro
from avro.resources import DICT


# Test functions for this file.
@pytest.mark.asyncio
async def test_patterns_without_rules_from_config() -> None:
    """
    Tests all patterns from config that don't have rules.
    """

    # Use config.DICT instead of config.get_dict() to avoid attribute error.
    patterns = DICT["avro"]["patterns"]

    # Ensure patterns is a list of dicts.
    assert isinstance(patterns, list)
    for pattern in patterns:
        assert isinstance(pattern, dict)
        find = pattern.get("find")
        replace = pattern.get("replace")

        if (
            "rules" not in pattern
            and isinstance(find, str)
            and isinstance(replace, str)
        ):
            assert replace == await avro.parse_async(find) == avro.parse(find)


@pytest.mark.asyncio
async def test_patterns_without_rules_not_from_config() -> None:
    """
    Tests all patterns not from config that don't have rules.

    This test is done in addition to
    test_patterns_without_rules_from_config() to ensure that text
    passed manually to avro.parse_async are properly parsed when they
    don't exact match a pattern that has no rules specified.
    """

    conjunctions = {
        "ভ্ল": "bhl",
        "ব্ধ": "bdh",
        "ড্ড": "DD",
        "স্তব্ধ বক": "stbdh bk",  # Stunned stork!
    }

    for key, value in conjunctions.items():
        assert key == await avro.parse_async(value) == avro.parse(value)


@pytest.mark.asyncio
async def test_patterns_numbers() -> None:
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
        assert key == await avro.parse_async(value) == avro.parse(value)
        assert value == await avro.reverse_async(key) == avro.reverse(key)


@pytest.mark.asyncio
async def test_patterns_punctuations() -> None:
    """
    Tests patterns - punctuations
    """

    punctuations = {
        "।": ".",
        "।।": "..",
        "...": "...",
    }

    for key, value in punctuations.items():
        assert key == await avro.parse_async(value) == avro.parse(value)
        assert value == await avro.reverse_async(key) == avro.reverse(key)


@pytest.mark.asyncio
async def test_patterns_with_rules_svaravarna() -> None:
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
        "ঊ": "U",  # noqa: F601
        "এ": "e",
        "ঐ": "OI",
        "ও": "O",
        "ঔ": "OU",
    }

    for key, value in svaravarna.items():
        assert key == await avro.parse_async(value) == avro.parse(value)


@pytest.mark.asyncio
async def test_non_ascii() -> None:
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
        assert key == await avro.parse_async(value) == avro.parse(value)


@pytest.mark.asyncio
async def test_ascii() -> None:
    """
    Test processor response for ASCII characters.
    Reverse function should return any ASCII characters that is passed to it.
    """

    assert (
        "Avwg evsjvi gan MvB|"
        == await avro.reverse_async("Avwg evsjvi গান MvB|")
        == avro.reverse("Avwg evsjvi গান MvB|")
    )
    assert (
        "Avwg amar Avwg‡K wPiw`b GB banglay Lyu‡R cvB!"
        == await avro.reverse_async(
            "Avwg আমার Avwg‡K wPiw`b GB বাংলায় Lyu‡R cvB!"
        )
        == avro.reverse("Avwg আমার Avwg‡K wPiw`b GB বাংলায় Lyu‡R cvB!")
    )


@pytest.mark.asyncio
async def test_words_with_punctuations() -> None:
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
        assert key == await avro.parse_async(value) == avro.parse(value)
        assert (
            value.lower() == await avro.reverse_async(key) == avro.reverse(key)
        )


@pytest.mark.asyncio
async def test_exceptions() -> None:
    """
    Test parsing and reversing of exceptions.
    """

    assert (
        "আমি উইকিপিডিয়া আর ফেসবুক চালাই।"
        == await avro.parse_async("ami Wikipedia ar Facebook calai.")
        == avro.parse("ami Wikipedia ar Facebook calai.")
    )
    assert (
        "ami Wikipedia ar Facebook chalai."
        == await avro.reverse_async("আমি উইকিপিডিয়া আর ফেসবুক চালাই।")
        == avro.reverse("আমি উইকিপিডিয়া আর ফেসবুক চালাই।")
    )


@pytest.mark.asyncio
async def test_conversion_bijoy_func() -> None:
    """
    Test conversion to Bijoy directly.
    """

    # Regular Conversion.
    assert (
        "Avwg evsjvq Mvb MvB;"
        == await avro.to_bijoy_async("আমি বাংলায় গান গাই;")
        == avro.to_bijoy("আমি বাংলায় গান গাই;")
    )
    assert (
        [
            "Avwg evsjvi Mvb MvB|",
            "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
        ]
        == await avro.to_bijoy_async_iter(
            ["আমি বাংলার গান গাই।", "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!"]
        )
        == avro.to_bijoy_iter(
            ["আমি বাংলার গান গাই।", "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!"]
        )
    )

    # Fail-safe Conversion.
    assert (
        "Hello, World!"
        == await avro.to_bijoy_async("Hello, World!")
        == avro.to_bijoy("Hello, World!")
    )


@pytest.mark.asyncio
async def test_conversion_unicode_func() -> None:
    """
    Test conversion to Unicode directly.
    """

    # Regular Conversion.
    assert (
        "আমি বাংলায় গান গাই;"
        == await avro.to_unicode_async("Avwg evsjvh় Mvb MvB;")
        == avro.to_unicode("Avwg evsjvh় Mvb MvB;")
    )
    assert (
        [
            "আমি বাংলার গান গাই।",
            "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!",
        ]
        == await avro.to_unicode_async_iter(
            [
                "Avwg evsjvi Mvb MvB|",
                "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
            ]
        )
        == avro.to_unicode_iter(
            [
                "Avwg evsjvi Mvb MvB|",
                "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
            ]
        )
    )


@pytest.mark.asyncio
async def test_parse_sentences() -> None:
    """
    Test parsing of sentences (Unicode).
    """

    # Default parsing.
    assert (
        "আমি বাংলায় গান গাই;"
        == await avro.parse_async("ami banglay gan gai;")
        == avro.parse("ami banglay gan gai;")
    )
    assert (
        [
            "আমি বাংলার গান গাই।",
            "আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই।",
        ]
        == await avro.parse_async_iter(
            [
                "ami banglar gan gai.",
                "ami amar amike cirodin ei banglay khu^je pai.",
            ]
        )
        == avro.parse_iter(
            [
                "ami banglar gan gai.",
                "ami amar amike cirodin ei banglay khu^je pai.",
            ]
        )
    )

    # Bijoy parsing.
    assert (
        "Avwg evsjvq Mvb MvB;"
        == await avro.parse_async("ami banglay gan gai;", bijoy=True)
        == avro.parse("ami banglay gan gai;", bijoy=True)
    )
    assert (
        [
            "Avwg evsjvi Mvb MvB|",
            "Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!",
        ]
        == await avro.parse_async_iter(
            [
                "ami banglar gan gai.",
                "ami amar amike cirodin ei banglay khu^je pai!",
            ],
            bijoy=True,
        )
        == avro.parse_iter(
            [
                "ami banglar gan gai.",
                "ami amar amike cirodin ei banglay khu^je pai!",
            ],
            bijoy=True,
        )
    )


@pytest.mark.asyncio
async def test_reverse_sentences() -> None:
    """
    Test reversing of sentences (Unicode).
    """

    # Default reversing.
    assert (
        "ami banglay gan gai."
        == await avro.reverse_async("আমি বাংলায় গান গাই।")
        == avro.reverse("আমি বাংলায় গান গাই।")
    )
    assert (
        [
            "rohim, tomake korim dakche. ekhon ki rowna debe?",
            "rowna dile amake bole zew.",
        ]
        == await avro.reverse_async_iter(
            [
                "রহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?",
                "রওনা দিলে আমাকে বলে যেও।",
            ]
        )
        == avro.reverse_iter(
            [
                "রহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?",
                "রওনা দিলে আমাকে বলে যেও।",
            ]
        )
    )

    # Bijoy reversing.
    assert (
        "ami banglar gan gai."
        == await avro.reverse_async("Avwg evsjvi Mvb MvB|", from_bijoy=True)
        == avro.reverse("Avwg evsjvi Mvb MvB|", from_bijoy=True)
    )
