'''

## Test cases for avro.utils.count

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
from avro.utils import count


# Test functions for this file.
def test_count_vowels() -> None:
    '''
    ### Test vowel count in a given string.
    '''

    strings = {
        'haTTima Tim Tim': 5,
        'tara maThe paRe Dim': 7,
        'tader mathay duTO sing': 7,
        'tara haTTima Tim Tim': 7,
    }

    for string, integer in strings.items():
        assert count.count_vowels(string) == integer


def test_count_consonants() -> None:
    '''
    ### Test consonant count in a given string.
    '''

    strings = {
        'ei dekh pensil': 7,
        'nOTbuk e hate': 6,
        'ei dekh bhora sob': 8,
        'kil`bil lekha te': 8,
    }

    for string, integer in strings.items():
        assert count.count_consonants(string) == integer
