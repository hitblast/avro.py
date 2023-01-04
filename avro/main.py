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


# Import third-party modules.
from typing import Any, List, Dict, Union

# Import local modules.
from . import config
from .utils import validate
import re


# Constants.
PATTERNS: Any = config.AVRO_DICT['data']['patterns']
NON_RULE_PATTERNS: list = [p for p in PATTERNS if 'rules' not in p]
RULE_PATTERNS: list = [p for p in PATTERNS if 'rules' in p]


# The primary parse function for the library.
def parse(*texts: str) -> Union[str, List[str]]:
    '''
    ### Parses input text, matches and replaces using avrodict.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Usage:
    ```python
    import avro

    parsed = avro.parse('ami banglay gan gai')
    print(parsed)
    ```
    '''

    def subparse(text: str) -> str:
        # Sanitize text case to meet phonetic comparison standards.
        fixed_text = validate.fix_string_case(text)

        # Prepare output list.
        output = []

        # Cursor end point.
        cur_end = 0

        # Iterate through input text.
        for cur, i in enumerate(fixed_text):
            try:
                i.encode('utf-8')
            except UnicodeDecodeError:
                uni_pass = False
            else:
                uni_pass = True

            match = {"matched": False}

            if not uni_pass:
                cur_end = cur + 1
                output.append(i)

            elif cur >= cur_end and uni_pass:
                match = match_patterns(fixed_text, cur, rule=False)

                if match['matched']:
                    output.append(match['replaced'])
                    cur_end = cur + len(match['found'])

                else:
                    match = match_patterns(fixed_text, cur, rule=True)

                    if match['matched']:
                        cur_end = cur + len(match['found'])
                        replaced = process_rules(
                            rules=match['rules'], fixed_text=fixed_text, cur=cur, cur_end=cur_end
                        )

                        if replaced is not None:
                            output.append(replaced)

                        else:
                            output.append(match['replaced'])

                if not match['matched']:
                    cur_end = cur + 1
                    output.append(i)

        return ''.join(output)

    output = []
    for text in texts:  # Applies to non-keyword arguments.
        output.append(subparse(text))

    return output[0] if len(output) == 1 else output


def reverse(*texts: str) -> Union[str, List[str]]:
    '''
    ### Reverses input text to Roman script typed in English.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Usage:
    ```python
    import avro

    target = avro.reverse('আমার সোনার বাংলা')
    print(target)
    ```
    `output: amar sonar bangla`
    '''

    def subparse(text: str) -> str:
        # Prepare output list.
        output = []

        # Iterate through input text.
        for cur, i in enumerate(text):
            try:
                i.encode('utf-8')
            except UnicodeDecodeError:
                uni_pass = False
            else:
                uni_pass = True

            match = {"matched": False}

            if not uni_pass:
                output.append(i)

            elif uni_pass:
                match = match_patterns(text, cur, rule=False, reversed=True)

                if match['matched']:
                    if not match['reversed'] is None:
                        output.append(match['reversed'])
                    else:
                        output.append(match['found'])

                if not match['matched']:
                    output.append(i)

        return ''.join(output)

    text_segments = []
    output = []

    # Split using regex to remove noise.
    regex_pattern = "(\\s|\\.|,|\\?|\\।|\\-|;|')"
    compiled_regex = re.compile(regex_pattern, re.UNICODE)

    for text in texts:  # Applies to non-keyword arguments.
        exceptions = config.EXCEPTIONS.get(text, None)

        if exceptions is None:
            separated_texts = compiled_regex.split(text)

            for separated_text in separated_texts:
                text_segments.append(subparse(separated_text))

            output.append(''.join(text_segments))
            text_segments = []

        else:
            output.append(exceptions)

    return output[0] if len(output) == 1 else output


def match_patterns(
    fixed_text: str, cur: int = 0, rule: bool = False, reversed: bool = False
) -> Dict[str, Any]:
    '''
    ### Matches given text at cursor position with rule / non rule patterns.

    Returns a dictionary of three elements:

    - `matched`  - Bool: depending on if match found.
    - `found` - string/None: Value of matched pattern's 'find' key or none.
    - `replaced` - string: Replaced string if match found else input string at cursor.
    '''

    rule_type = NON_RULE_PATTERNS if not rule else RULE_PATTERNS
    pattern = exact_find_in_pattern(fixed_text, reversed, cur, rule_type)

    if len(pattern) > 0:
        if not rule:
            return {
                "matched": True,
                "found": pattern[0].get('find', None),
                "replaced": pattern[0].get('replace', None),
                "reversed": reverse_with_rules(cur, fixed_text, pattern[0].get('reverse', None)),
            }
        else:
            return {
                "matched": True,
                "found": pattern[0]['find'],
                "replaced": pattern[0]['replace'],
                "rules": pattern[0]['rules'],
            }
    else:
        if not rule:
            return {"matched": False, "found": None, "replaced": fixed_text[cur]}
        else:
            return {"matched": False, "found": None, "replaced": fixed_text[cur], "rules": None}


def exact_find_in_pattern(
    fixed_text: str, reversed: bool, cur: int = 0, patterns: Any = PATTERNS
) -> list:
    '''
    ### Returns pattern items that match given text, cursor position and pattern.
    '''
    if reversed:
        return [
            x
            for x in patterns
            if (cur + len(x['replace']) <= len(fixed_text))
            and x['replace'] == fixed_text[cur : (cur + len(x['replace']))]
        ]

    return [
        x
        for x in patterns
        if (not x.get('find', None) is None)
        and (cur + len(x['find']) <= len(fixed_text))
        and x['find'] == fixed_text[cur : (cur + len(x['find']))]
    ]


def reverse_with_rules(cursor: int, fixed_text: str, text_reversed) -> bool:
    '''Enhances The Word With Rules For Reverse Parsing'''
    added_suffix = ''

    if not (
        fixed_text[cursor] in config.AVRO_KAR
        or fixed_text[cursor] in config.AVRO_SHORBORNO
        or fixed_text[cursor] in config.AVRO_IGNORE
        or len(fixed_text) == cursor + 1
    ):
        added_suffix = 'o'

    try:
        if fixed_text[cursor + 1] in config.AVRO_KAR:
            added_suffix = ''
        if fixed_text[cursor + 2] in config.AVRO_KAR and not cursor == 0:
            added_suffix = ''

    except IndexError:
        pass

    return text_reversed if text_reversed is None else (text_reversed + added_suffix)


def process_rules(rules: Any, fixed_text: str, cur: int = 0, cur_end: int = 1) -> Union[Any, None]:
    '''
    ### Process rules matched in pattern and returns suitable replacement.

    If any rule's condition is satisfied, output the rules "replace",
    else output None.
    '''

    replaced = ''

    # Iterate through rules.
    for rule in rules:
        matched = False

        for match in rule['matches']:
            matched = process_match(match, fixed_text, cur, cur_end)

            if not matched:
                break

        if matched:
            replaced = rule['replace']
            break

    return replaced if matched else None


def process_match(match: Any, fixed_text: str, cur: int, cur_end: int) -> bool:
    '''
    ### Processes a single match in rules.
    '''

    # Initial/default value for replace.
    replace = True

    # Set check cursor depending on match['type']
    chk = cur - 1 if match['type'] == 'prefix' else cur_end

    # Set scope based on whether scope is negative.
    if match['scope'].startswith('!'):
        scope = match['scope'][1:]
        negative = True
    else:
        scope = match['scope']
        negative = False

    # Let the matching begin!
    if scope == 'punctuation':
        if (
            not (
                (chk < 0 and match['type'] == 'prefix')
                or (chk >= len(fixed_text) and match['type'] == 'suffix')
                or validate.is_punctuation(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == 'vowel':
        if (
            not (
                (
                    (chk >= 0 and match['type'] == 'prefix')
                    or (chk < len(fixed_text) and match['type'] == 'suffix')
                )
                and validate.is_vowel(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == 'consonant':
        if (
            not (
                (
                    (chk >= 0 and match['type'] == 'prefix')
                    or (chk < len(fixed_text) and match['type'] == 'suffix')
                )
                and validate.is_consonant(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == 'exact':
        if match['type'] == 'prefix':
            exact_start = cur - len(match['value'])
            exact_end = cur
        else:
            exact_start = cur_end
            exact_end = cur_end + len(match['value'])

        if not validate.is_exact(match['value'], fixed_text, exact_start, exact_end, negative):
            replace = False

    return replace
