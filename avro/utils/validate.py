'''

## Validation functions (avro.utils) for avro.py

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


# Imports
from avro import config


# Functions.
def is_vowel(text: str) -> bool:
    '''
    ### Check if given string is a vowel.
    '''

    return text.lower() in config.AVRO_VOWELS

def is_consonant(text: str) -> bool:
    '''
    ### Check if given string is a consonant.
    '''

    return text.lower() in config.AVRO_CONSONANTS

def is_number(text: str) -> bool:
    '''
    ### Check if given string is a number.
    '''

    return text.lower() in config.AVRO_NUMBERS

def is_punctuation(text: str) -> bool:
    '''
    ### Check if given string is a punctuation.
    '''

    return not (text.lower() in config.AVRO_VOWELS or
                text.lower() in config.AVRO_CONSONANTS)

def is_case_sensitive(text: str) -> bool:
    '''
    ### Check if given string is case sensitive.
    '''

    return text.lower() in config.AVRO_CASESENSITIVES

def is_exact(needle, haystack, start, end, matchnot):
    '''
    ### Check exact occurrence of needle in haystack.
    '''

    return ((start >= 0 and end < len(haystack) and
             haystack[start:end] == needle) ^ matchnot)

def fix_string_case(text: str) -> str:
    '''
    ### Converts case-insensitive characters to lower case.

    Case-sensitive characters as defined in config.AVRO_CASESENSITIVES
    retain their case, but others are converted to their lowercase
    equivalents. The result is a string with phonetic-compatible case
    which will the parser will understand without confusion.
    '''

    fixed = []
    for i in text:
        if is_case_sensitive(i):
            fixed.append(i)
        else:
            fixed.append(i.lower())
    return ''.join(fixed)
