# SPDX-License-Identifier: MIT


# Import first-party Python modules.
import os
import sys
from typing import NoReturn

# Add support layer for accessing the primary package.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# Import local modules.
import avro
from avro.config import DICT


# Test functions for this file.
def test_patterns_without_rules_from_config() -> NoReturn:
    """
    Tests all patterns from config that don't have rules.
    """

    for pattern in DICT['avro']['patterns']:
        if 'rules' not in pattern and pattern.get('find', None):
            assert pattern['replace'] == avro.parse(pattern['find'])


def test_patterns_without_rules_not_from_config() -> NoReturn:
    """
    Tests all patterns not from config that don't have rules.

    This test is done in addition to
    test_patterns_without_rules_from_config() to ensure that text
    passed manually to avro.parse are properly parsed when they
    don't exact match a pattern that has no rules specified.
    """

    conjunctions = {
        'ভ্ল': avro.parse('bhl'),
        'ব্ধ': avro.parse('bdh'),
        'ড্ড': avro.parse('DD'),
        'স্তব্ধ বক': avro.parse('stbdh bk'),  # Stunned stork!
    }

    for key, value in conjunctions.items():
        assert key == value


def test_patterns_numbers() -> NoReturn:
    """
    Test patterns - numbers
    """

    numbers = {
        '০': avro.parse('0'),
        '১': avro.parse('1'),
        '২': avro.parse('2'),
        '৩': avro.parse('3'),
        '৪': avro.parse('4'),
        '৫': avro.parse('5'),
        '৬': avro.parse('6'),
        '৭': avro.parse('7'),
        '৮': avro.parse('8'),
        '৯': avro.parse('9'),
        '১১২': avro.parse('112'),
    }

    for key, value in numbers.items():
        assert key == value


def test_patterns_punctuations() -> NoReturn:
    """
    Tests patterns - punctuations
    """

    punctuations = {'।': avro.parse('.'), '।।': avro.parse('..'), '...': avro.parse('...')}

    for key, value in punctuations.items():
        assert key == value


def test_patterns_with_rules_svaravarna() -> NoReturn:
    """
    Test patterns - with rules - svaravarna / shoroborno (derived from Bengali)
    """

    svaravarna = {
        'অ': avro.parse('o'),
        'আ': avro.parse('a'),
        'ই': avro.parse('i'),
        'ঈ': avro.parse('I'),
        'উ': avro.parse('u'),
        'ঊ': avro.parse('oo'),
        'ঊ': avro.parse('U'),
        'এ': avro.parse('e'),
        'ঐ': avro.parse('OI'),
        'ও': avro.parse('O'),
        'ঔ': avro.parse('OU'),
    }

    for key, value in svaravarna.items():
        assert key == value


def test_non_ascii() -> NoReturn:
    """
    Test parser response for non ascii characters.
    Parser should return any non-ascii characters that is passed to it.
    """

    non_ascii = {
        'ব': avro.parse('ব'),
        'অভ্র': avro.parse('অভ্র'),
        'বআবা গো': avro.parse('বaba gO'),  # Mixed strings.
        'আমি বাংলায় গান গাই': avro.parse('aমি বাংলায় gaন গাi'),
    }

    for key, value in non_ascii.items():
        assert key == value


def test_words_with_punctuations() -> NoReturn:
    """
    Test parsing of words with punctuations.
    """

    words_with_punctuations = {
        'আয়রে,': avro.parse('ayre,'),
        'ভোলা;': avro.parse('bhOla;'),
        '/খেয়াল': avro.parse('/kheyal'),
        'খোলা|': avro.parse('khOla|'),
    }

    for key, value in words_with_punctuations.items():
        assert key == value


def test_conversion_bijoy_func() -> NoReturn:
    """
    Test conversion to Bijoy directly.
    """

    assert 'Avwg evsjvq Mvb MvB;' == avro.to_bijoy('আমি বাংলায় গান গাই;')
    assert [
        'Avwg evsjvi Mvb MvB|',
        'Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!',
    ] == avro.to_bijoy('আমি বাংলার গান গাই।', 'আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই!')


def test_full_sentences() -> NoReturn:
    """
    Test parsing of sentences (Unicode).
    """

    # Default settings.
    assert 'আমি বাংলায় গান গাই;' == avro.parse('ami banglay gan gai;')
    assert [
        'আমি বাংলার গান গাই।',
        'আমি আমার আমিকে চিরদিন এই বাংলায় খুঁজে পাই।',
    ] == avro.parse('ami banglar gan gai.', 'ami amar amike cirodin ei banglay khu^je pai.')

    # Bijoy settings.
    assert 'Avwg evsjvq Mvb MvB;' == avro.parse('ami banglay gan gai;', bijoy=True)
    assert [
        'Avwg evsjvi Mvb MvB|',
        'Avwg Avgvi Avwg‡K wPiw`b GB evsjvq Lyu‡R cvB!',
    ] == avro.parse('ami banglar gan gai.', 'ami amar amike cirodin ei banglay khu^je pai!', bijoy=True)


def test_reverse_func() -> NoReturn:
    """
    Test reverse-parsing with sentences.
    """

    assert 'ami banglay gan gai.' == avro.reverse('আমি বাংলায় গান গাই।')
    assert [
        'rohim, tomake korim dakche. ekhon ki rowna debe?',
        'rowna dile amake bole zew.',
    ] == avro.reverse('রহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?', 'রওনা দিলে আমাকে বলে যেও।')
