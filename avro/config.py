'''

## A modern Pythonic implementation of Avro Phonetic.

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


# Import built-in libraries.
import os

# Import local modules.
from .resources import AVRO_DICT


# Path to current directory.
BASE_PATH = os.path.dirname(__file__)

# Shortcuts to vowels, constants, case-sensitives and numbers.
AVRO_VOWELS = set(AVRO_DICT['data']['vowel'])
AVRO_CONSONANTS = set(AVRO_DICT['data']['consonant'])
AVRO_CASESENSITIVES = set(AVRO_DICT['data']['casesensitive'])
AVRO_NUMBERS = set(AVRO_DICT['data']['number'])

# Shortcuts to Bengali Svaravarna, Kar(s)
AVRO_SHORBORNO = set(AVRO_DICT['data']['shorborno'])
AVRO_KAR = AVRO_DICT['data']['kar']
AVRO_IGNORE = AVRO_DICT['data']['ignore']
EXCEPTIONS = AVRO_DICT['data']['exceptions']
