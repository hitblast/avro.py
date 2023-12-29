# SPDX-License-Identifier: MIT


# Import first-party Python libraries.
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# Import local modules.
from . import config
from .utils import validate

# Constants.
PATTERNS = config.AVRO_DICT['data']['patterns']
NON_RULE_PATTERNS = [p for p in PATTERNS if 'rules' not in p]
RULE_PATTERNS = [p for p in PATTERNS if 'rules' in p]


# The helper function for handling multithreaded workloads.
def _concurrency_helper(func: Callable, params: Tuple[str]) -> List[str]:
    output = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, text): text for text in params}

        for future in as_completed(futures):
            output.append(future.result())

    return output


# The primary parse function for the library.
def parse(*texts: str) -> Union[str, List[str]]:
    '''
    #### Parses input text, matches and replaces using the Avro Dictionary.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to parse.

    Usage:
    ```python
    import avro

    parsed = avro.parse('ami banglay gan gai')
    print(parsed)
    ```
    '''

    # Internal function for multiple parses.
    @lru_cache
    def _parse_backend(text: str) -> str:
        fixed_text = validate.fix_string_case(
            text
        )  # Sanitize text case to meet phonetic comparison standards.
        output = []  # The output list of strings.
        cur_end = 0  # Cursor end point.

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

    # Do the final output.
    output = _concurrency_helper(_parse_backend, texts)
    return output[0] if len(output) == 1 else output


def reverse(*texts: str) -> Union[str, List[str]]:
    '''
    #### Reverses input text to Roman script typed in English.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to reverse.

    Usage:
    ```python
    import avro

    reversed = avro.reverse('আমার সোনার বাংলা')
    print(reversed)
    ```
    '''

    # Internal function for multiple reverses.
    @lru_cache
    def _reverse_backend(text: str) -> str:
        output = []  # The output list of strings.

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
                    if match['reversed']:
                        output.append(match['reversed'])
                    else:
                        output.append(match['found'])

                if not match['matched']:
                    output.append(i)

        return ''.join(output)

    # Split using regex to remove noise.
    compiled_regex = re.compile("(\\s|\\.|,|\\?|\\।|\\-|;|')", re.UNICODE)

    # Extension for the _reverse_backend() function.
    @lru_cache
    def _reverse_backend_ext(text: str) -> str:
        text_segments = []
        exceptions = config.EXCEPTIONS.get(text, None)

        if not exceptions:
            separated_texts = compiled_regex.split(text)

            for separated_text in separated_texts:
                text_segments.append(_reverse_backend(separated_text))

            return ''.join(text_segments)

        else:
            return exceptions

    # Prepare final output.
    output = _concurrency_helper(_reverse_backend_ext, texts)
    return output[0] if len(output) == 1 else output


def match_patterns(
    fixed_text: str, cur: int = 0, rule: bool = False, reversed: bool = False
) -> Dict[str, Any]:
    '''
    Matches given text at cursor position with rule / non rule patterns.

    Returns a dictionary of three (upto four) elements.
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
        result = {"matched": False, "found": None, "replaced": fixed_text[cur]}

        if rule:
            result['rules'] = None

        return result


def exact_find_in_pattern(
    fixed_text: str, reversed: bool, cur: int = 0, patterns: Any = PATTERNS
) -> List[Dict[str, Any]]:
    '''
    Returns pattern items that match given text, cursor position and pattern.
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
        if x.get('find', None)
        and (cur + len(x['find']) <= len(fixed_text))
        and x['find'] == fixed_text[cur : (cur + len(x['find']))]
    ]


@lru_cache
def reverse_with_rules(cursor: int, fixed_text: str, text_reversed: str) -> str:
    '''
    Enhances the word with rules for reverse-parsing.
    '''

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

    return text_reversed if not text_reversed else text_reversed + added_suffix


def process_rules(rules: Dict[str, Any], fixed_text: str, cur: int = 0, cur_end: int = 1) -> Optional[str]:
    '''
    Process rules matched in pattern and returns suitable replacement.

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
    Processes a single match in rules.
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
