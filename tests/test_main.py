'''

## Test cases for avro.main

---

MIT License

Copyright (c) 2022-present HitBlast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


# Import third-party modules.
import os
import sys

# Add support layer for accessing the primary package.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

# Import local modules.
import avro
from avro.config import AVRO_DICT


# Test functions for this file.
def test_patterns_without_rules_from_config() -> None:
    '''
    ### Tests all patterns from config that don't have rules.
    '''

    for pattern in AVRO_DICT['data']['patterns']:
        if 'rules' not in pattern:
            if pattern.get('find', None) is not None:
                assert pattern['replace'] == avro.parse(pattern['find'])


def test_patterns_without_rules_not_from_config() -> None:
    '''
    ### Tests all patterns not from config that don't have rules.

    This test is done in addition to
    test_patterns_without_rules_from_config() to ensure that text
    passed manually to avro.parse are properly parsed when they
    don't exact match a pattern that has no rules specified.
    '''

    conjunctions = {
        "ভ্ল": avro.parse("bhl"),
        "ব্ধ": avro.parse("bdh"),
        "ড্ড": avro.parse("DD"),
        "স্তব্ধ বক": avro.parse("stbdh bk"),  # Stunned stork!
    }

    for key, value in conjunctions.items():
        assert key == value


def test_patterns_numbers() -> None:
    '''
    ### Test patterns - numbers
    '''

    numbers = {
        "০": avro.parse("0"),
        "১": avro.parse("1"),
        "২": avro.parse("2"),
        "৩": avro.parse("3"),
        "৪": avro.parse("4"),
        "৫": avro.parse("5"),
        "৬": avro.parse("6"),
        "৭": avro.parse("7"),
        "৮": avro.parse("8"),
        "৯": avro.parse("9"),
        "১১২": avro.parse("112"),
    }

    for key, value in numbers.items():
        assert key == value


def test_patterns_punctuations() -> None:
    '''
    ### Tests patterns - punctuations
    '''

    punctuations = {"।": avro.parse("."), "।।": avro.parse(".."), "...": avro.parse("...")}

    for key, value in punctuations.items():
        assert key == value


def test_patterns_with_rules_svaravarna() -> None:
    '''
    ### Test patterns - with rules - svaravarna / shoroborno (derived from Bengali)
    '''

    svaravarna = {
        "অ": avro.parse("o"),
        "আ": avro.parse("a"),
        "ই": avro.parse("i"),
        "ঈ": avro.parse("I"),
        "উ": avro.parse("u"),
        "ঊ": avro.parse("oo"),
        "ঊ": avro.parse("U"),
        "এ": avro.parse("e"),
        "ঐ": avro.parse("OI"),
        "ও": avro.parse("O"),
        "ঔ": avro.parse("OU"),
    }

    for key, value in svaravarna.items():
        assert key == value


def test_non_ascii() -> None:
    '''
    ### Test parser response for non ascii characters.
    Parser should return any non-ascii characters that is passed to it.
    '''

    non_ascii = {
        'ব': avro.parse('ব'),
        'অভ্র': avro.parse('অভ্র'),
        'বআবা গো': avro.parse('বaba gO'),  # Mixed strings.
        'আমি বাংলায় গান গাই': avro.parse('aমি বাংলায় gaন গাi'),
    }

    for key, value in non_ascii.items():
        assert key == value


def test_words_with_punctuations() -> None:
    '''
    ### Test parsing of words with punctuations.
    '''

    words_with_punctuations = {
        'আয়রে,': avro.parse('ayre,'),
        'ভোলা': avro.parse('bhOla'),
        'খেয়াল': avro.parse('kheyal'),
        'খোলা': avro.parse('khOla'),
    }

    for key, value in words_with_punctuations.items():
        assert key == value


def tests_sentences_with_default() -> None:
    '''
    ### Test parsing of sentences (Unicode).
    '''

    assert 'আমি বাংলায় গান গাই' == avro.parse('ami banglay gan gai')


def test_sentences_with_ascii_flag() -> None:
    '''
    ### Test parsing of sentences (ASCII).
    '''

    assert str(
        b'\\u0986\\u09ae\\u09bf \\u09ac\\u09be\\u0982\\u09b2\\u09be\\u09df'
        + b' \\u0997\\u09be\\u09a8 \\u0997\\u09be\\u0987'
    ) == avro.parse('ami banglay gan gai', in_ascii=True)


def test_reverse_func() -> None:
    '''
    ### Test reverse-parsing with sentences.
    '''

    assert 'ami banglay gan gai' == avro.reverse('আমি বাংলায় গান গাই')
    assert 'rahim, tomake korim dakche. ekhon ki rowna debe?' == avro.reverse(
        'রাহিম, তোমাকে করিম ডাকছে। এখন কি রওনা দেবে?'
    )
