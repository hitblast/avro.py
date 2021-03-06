'''

## Test cases for avro.main

---

MIT License

Copyright (c) 2022 HitBlast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
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
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir)
    )
)

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
        "?????????" : avro.parse("bhl"),
        "?????????" : avro.parse("bdh"),
        "?????????" : avro.parse("DD"),
        "?????????????????? ??????" : avro.parse("stbdh bk") # Stunned stork!
    }

    for key, value in conjunctions.items():
        assert key == value


def test_patterns_numbers() -> None:
    '''
    ### Test patterns - numbers
    '''

    numbers = {
        "???" : avro.parse("0"),
        "???" : avro.parse("1"),
        "???" : avro.parse("2"),
        "???" : avro.parse("3"),
        "???" : avro.parse("4"),
        "???" : avro.parse("5"),
        "???" : avro.parse("6"),
        "???" : avro.parse("7"),
        "???" : avro.parse("8"),
        "???" : avro.parse("9"),
        "?????????" : avro.parse("112")
    }
    
    for key, value in numbers.items():
        assert key == value


def test_patterns_punctuations() -> None:
    '''
    ### Tests patterns - punctuations
    '''

    punctuations = {
        "???" : avro.parse("."),
        "??????" : avro.parse(".."),
        "..." : avro.parse("...")
    }
    
    for key, value in punctuations.items():
        assert key == value


def test_patterns_with_rules_svaravarna() -> None:
    '''
    ### Test patterns - with rules - svaravarna / shoroborno (derived from Bangla)
    '''

    svaravarna = {
        "???" : avro.parse("o"),
        "???" : avro.parse("a"),
        "???" : avro.parse("i"),
        "???" : avro.parse("I"),
        "???" : avro.parse("u"),
        "???" : avro.parse("oo"),
        "???" : avro.parse("U"),
        "???" : avro.parse("e"),
        "???" : avro.parse("OI"),
        "???" : avro.parse("O"),
        "???" : avro.parse("OU"),
    }

    for key, value in svaravarna.items():
        assert key == value


def test_non_ascii() -> None:
    '''
    ### Test parser response for non ascii characters.
    Parser should return any non-ascii characters that is passed to it.
    '''

    non_ascii = {
        '???' : avro.parse('???'),
        '????????????' : avro.parse('????????????'),
        '???????????? ??????' : avro.parse('???aba gO'), # Mixed strings.
        '????????? ?????????????????? ????????? ?????????' : avro.parse('a?????? ?????????????????? ga??? ??????i')
    }

    for key, value in non_ascii.items():
        assert key == value


def test_words_with_punctuations() -> None:
    '''
    ### Test parsing of words with punctuations.
    '''

    words_with_punctuations = {
        '????????????,' : avro.parse('ayre,'),
        '????????????' : avro.parse('bhOla'),
        '???????????????' : avro.parse('kheyal'),
        '????????????' : avro.parse('khOla')
    }

    for key, value in words_with_punctuations.items():
        assert key == value


def test_sentences() -> None:
    '''
    ### Test parsing of sentences.
    '''

    assert '????????? ?????????????????? ????????? ?????????' == avro.parse('ami banglay gan gai')