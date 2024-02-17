# SPDX-License-Identifier: MIT


# Import first-party Python modules.
import os
import sys
from typing import NoReturn

# Add support layer for accessing the primary package.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# Import local modules.
from avro.utils import validate

# Set up test environments.
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
numbers = '0123456789'
prekars = ['ি', 'ৈ', 'ে']
banjonborno = 'কখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমশষসহযরলয়ংঃঁৎ'


# Test functions for this file.
def test_is_consonant() -> NoReturn:
    """
    Test that consonants are correctly identified.
    """

    for i in consonants + consonants.upper():
        assert validate.is_consonant(i)

    for i in vowels + numbers:
        assert not validate.is_consonant(i)


def test_is_number() -> NoReturn:
    """
    Test that numbers are correctly identified.
    """

    for i in numbers:
        assert validate.is_number(i)

    for i in vowels + consonants:
        assert not validate.is_number(i)


def test_is_vowel() -> NoReturn:
    """
    Test that vowels are correctly identified.
    """

    for i in vowels + vowels.upper():
        assert validate.is_vowel(i)

    for i in consonants + numbers:
        assert not validate.is_vowel(i)


def test_is_punctuation() -> NoReturn:
    """
    Test that punctuations are correctly identified.

    Anything that is neither a number, nor vowel nor consonant is
    identified as a punctuation.
    """

    for i in '`~!@#$%^&*()-_=+\\|[{}]\'",<.>/?':
        assert validate.is_punctuation(i)
        assert not validate.is_vowel(i)
        assert not validate.is_consonant(i)
        assert not validate.is_number(i)


def test_fix_string_case() -> NoReturn:
    """
    Test phonetic-compatible case-transformations of strings.

    This ensures validate.fix_strings function works as
    expected. It should properly change text to lowercase but
    retain case-sensitive characters defined in config as
    uppercase.
    """

    assert validate.fix_string_case('ABOL taBOl') == 'abOl tabOl'
    assert validate.fix_string_case('KhiCuRi') == 'khicuRi'
    assert validate.fix_string_case('KaTh-BuRO') == 'kaTh-buRO'
    assert validate.fix_string_case('raMgoRurer Chana') == 'ramgoRurer chana'


def test_is_exact() -> NoReturn:
    """
    Test exact search response of needle in haystack.
    """

    assert validate.is_exact('abcd', 'abcdefgh', 0, 4, False)
    assert not validate.is_exact('abcd', 'abcdefgh', 0, 4, True)
    assert not validate.is_exact('bcd', 'abcdefgh', 0, 4, False)
    assert validate.is_exact('bcd', 'abcdefgh', 0, 4, True)

    assert not validate.is_exact('a', 'a', 1, 2, False)
    assert validate.is_exact('a', 'a', 1, 2, True)


def test_is_prekar() -> NoReturn:
    """
    Test if given string is a prekar.
    """

    for i in prekars:
        assert validate.is_bangla_prekar(i)

    assert not (
        validate.is_bangla_prekar('া')
        and validate.is_bangla_prekar('ূ')
        and validate.is_bangla_prekar('a')
        and validate.is_bangla_prekar('b')
    )


def test_is_banjonborno() -> NoReturn:
    """
    Test if given string is a banjonborno.
    """

    for i in banjonborno:
        assert validate.is_bangla_banjonborno(i)

    assert not (
        validate.is_bangla_banjonborno('a')
        and validate.is_bangla_banjonborno('ূ')
        and validate.is_bangla_banjonborno('া')
        and validate.is_bangla_banjonborno('b')
    )


def test_is_halant() -> NoReturn:
    """
    Test if given string is a halant.
    """

    assert validate.is_bangla_halant('্')
    assert not (
        validate.is_bangla_halant('a')
        and validate.is_bangla_halant('ূ')
        and validate.is_bangla_halant('া')
        and validate.is_bangla_halant('b')
    )
