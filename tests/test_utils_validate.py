'''

## Test cases for avro.utils.validate

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
from avro.utils import validate


# Set up test environments.
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
numbers = '0123456789'


# Test functions for this file.
def test_is_consonant() -> None:
    '''
    ### Test that consonants are correctly identified.
    '''

    for i in consonants + consonants.upper():
        assert validate.is_consonant(i)

    for i in vowels + numbers:
        assert not validate.is_consonant(i)


def test_is_number() -> None:
    '''
    ### Test that numbers are correctly identified.
    '''

    for i in numbers:
        assert validate.is_number(i)

    for i in vowels + consonants:
        assert not validate.is_number(i)


def test_is_vowel() -> None:
    '''
    ### Test that vowels are correctly identified.
    '''

    for i in vowels + vowels.upper():
        assert validate.is_vowel(i)

    for i in consonants + numbers:
        assert not validate.is_vowel(i)


def test_is_punctuation() -> None:
    '''
    ### Test that punctuations are correctly identified.

    Anything that is neither a number, nor vowel nor consonant is
    identified as a punctuation.
    '''

    for i in '`~!@#$%^&*()-_=+\\|[{}]\'",<.>/?':
        assert validate.is_punctuation(i)
        assert not validate.is_vowel(i)
        assert not validate.is_consonant(i)
        assert not validate.is_number(i)


def test_fix_string_case() -> None:
    '''
    ### Test phonetic-compatible case-transformations of strings.

    This ensures validate.fix_strings function works as
    expected. It should properly change text to lowercase but
    retain case-sensitive characters defined in config as
    uppercase.
    '''

    assert validate.fix_string_case('ABOL taBOl') == 'abOl tabOl'
    assert validate.fix_string_case('KhiCuRi') == 'khicuRi'
    assert validate.fix_string_case('KaTh-BuRO') == 'kaTh-buRO'
    assert validate.fix_string_case('raMgoRurer Chana') == 'ramgoRurer chana'


def test_is_exact() -> None:
    '''
    ### Test exact search response of needle in haystack.
    '''

    assert validate.is_exact('abcd', 'abcdefgh', 0, 4, False)
    assert not validate.is_exact('abcd', 'abcdefgh', 0, 4, True)
    assert not validate.is_exact('bcd', 'abcdefgh', 0, 4, False)
    assert validate.is_exact('bcd', 'abcdefgh', 0, 4, True)

    assert not validate.is_exact('a', 'a', 1, 2, False)
    assert validate.is_exact('a', 'a', 1, 2, True)
