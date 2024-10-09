# SPDX-License-Identifier: MIT


"""
Avro Keyboard for Pythoneers

Licensed under the terms of the MIT License.
"""

# Import first-party Python libraries.
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from itertools import chain
from typing import Callable, Generator, Union

# Import local modules.
from .core import processor, validate
from .core.config import BIJOY_MAP, BIJOY_MAP_REVERSE


# Concurrency helper function for handling multithreaded workloads.
def _concurrency_helper(func: Callable, params: tuple[str, ...]) -> list[str]:
    output = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, text): text for text in params}

        for future in as_completed(futures):
            output.append(future.result())

    return output


# Compiled regular expression for UTF-8 validation.
UTF8_REGEX = re.compile(r"\A[\x00-\x7F]*\Z", re.UNICODE)

# Compiled regular expression for removing noise while reversing.
REVERSE_REGEX = re.compile(r"(\s|\.|,|\?|।|-|;|')", re.UNICODE)


# ---


# Backend Functions.
# The output generator for the parse function.
def _parse_output_generator(fixed_text: str, cur_end: int) -> Generator[str, None, None]:
    for cur, i in enumerate(fixed_text):
        uni_pass = UTF8_REGEX.match(i) is not None
        if not uni_pass:
            cur_end = cur + 1
            yield i
        elif cur >= cur_end and uni_pass:
            match = processor.match_patterns(fixed_text, cur, rule=False)
            matched = match["matched"]
            if matched:
                yield match["replaced"]
                cur_end = cur + len(match["found"])
            else:
                match = processor.match_patterns(fixed_text, cur, rule=True)
                matched = match["matched"]
                if matched:
                    cur_end = cur + len(match["found"])
                    replaced = processor.process_rules(
                        rules=match["rules"], fixed_text=fixed_text, cur=cur, cur_end=cur_end
                    )
                    if replaced:
                        yield replaced
                    else:
                        yield match["replaced"]
            if not matched:
                cur_end = cur + 1
                yield i


# The working backend for the parse() function.
@lru_cache(maxsize=128)
def _parse_backend(text: str, remap_words: bool) -> str:
    fixed_text = validate.fix_string_case(text)  # Sanitize input text.
    manual_required = True  # Whether manual intervention is required.
    cur_end = 0  # Cursor end point.

    # Replace predefined exceptions in the input text.
    if remap_words:
        fixed_text, manual_required = processor.find_in_remap(fixed_text)

    return (
        "".join(chain.from_iterable(_parse_output_generator(fixed_text, cur_end)))
        if manual_required
        else fixed_text
    )


# The working backend for the to_bijoy() function.
@lru_cache(maxsize=128)
def _convert_backend(text: str) -> str:
    text = processor.rearrange_unicode_text(re.sub("ৌ", "ৌ", re.sub("ো", "ো", text)))

    for unic in BIJOY_MAP:
        text = re.sub(unic, BIJOY_MAP[unic], text)

    return text.strip()


# The working backend for the to_unicode() function.
@lru_cache(maxsize=128)
def _convert_backend_unicode(text: str) -> str:
    for ascii_c in BIJOY_MAP_REVERSE:
        text = re.sub(re.escape(ascii_c), BIJOY_MAP_REVERSE[ascii_c], text)

    text = re.sub("অা", "আ", processor.rearrange_bijoy_text(text))
    return text.strip()


# The output generator for the reverse function.
def _reverse_output_generator(text: str) -> Generator[str, None, None]:
    for cur, i in enumerate(text):
        try:
            i.encode("utf-8")
            match = processor.match_patterns(text, cur, rule=False, reversed=True)
            yield (match["reversed"] or match["found"]) if match["matched"] else i
        except UnicodeDecodeError:
            yield i


# The working backend for the reverse() function.
@lru_cache(maxsize=128)
def _reverse_backend(text: str, remap_words: bool) -> str:
    manual_required = True  # Whether manual intervention is required.

    # Replace predefined exceptions in the input text.
    if remap_words:
        text, manual_required = processor.find_in_remap(text, reversed=True)

    return "".join(chain.from_iterable(_reverse_output_generator(text))) if manual_required else text


# Backend extension for the reverse() function.
@lru_cache(maxsize=128)
def _reverse_backend_ext(text: str, remap_words: bool) -> str:
    separated_texts = REVERSE_REGEX.split(text)
    text_segments = [_reverse_backend(separated_text, remap_words) for separated_text in separated_texts]
    return "".join(text_segments)


# ---


# Primary user-end functions.
# The parse() function.
# Used to parse from English Roman script to Bengali in Unicode.
def parse(*texts: str, bijoy: bool = False, remap_words: bool = True) -> Union[str, list[str]]:
    """
    #### Parses input text, matches and replaces using the Avro Dictionary.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to parse.
    - `bijoy: bool = False`: Return result in the Bijoy Keyboard format (ASCII).
    - `remap_words: bool = True`: Whether to parse input text with remapped (exception) words.

    Usage:
    ```python
    import avro

    parsed = avro.parse('ami banglay gan gai')
    print(parsed)
    ```
    """

    output = _concurrency_helper(lambda text: _parse_backend(text, remap_words), texts)

    # If the `bijoy` parameter is set to `True`, then convert the output to Bijoy Keyboard format.
    if bijoy:
        return to_bijoy(*output)
    else:
        return output[0] if len(output) == 1 else output


# The to_bijoy() function.
# Used to parse from Bengali in Unicode to Bijoy Keyboard format.
def to_bijoy(*texts: str) -> Union[str, list[str]]:
    """
    #### Converts input text (Avro, Unicode) to Bijoy Keyboard format (ASCII).

    If a valid conversion is found, then it returns the converted string.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to convert.

    Usage:
    ```python
    import avro

    converted = avro.to_bijoy('আমার সোনার বাংলা')
    print(converted)
    ```
    """

    output = _concurrency_helper(_convert_backend, texts)
    return output[0] if len(output) == 1 else output


# The to_unicode() function.
# Used to parse from Bijoy Keyboard format to Bengali in Unicode.
def to_unicode(*texts: str) -> Union[str, list[str]]:
    """
    #### Converts input text (Bijoy Keyboard, ASCII) to Unicode (Avro Keyboard format).

    If a valid conversion is found, then it returns the converted string.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to convert.

    Usage:
    ```python
    import avro

    converted = avro.to_unicode('Avwg evsjvh় Mvb MvB;')
    print(converted)
    ```
    """

    output = _concurrency_helper(_convert_backend_unicode, texts)
    return output[0] if len(output) == 1 else output


# The reverse() function.
# Used to parse from Bengali in Unicode to English Roman script.
def reverse(*texts: str, from_bijoy: bool = False, remap_words: bool = True) -> Union[str, list[str]]:
    """
    #### Reverses input text to Roman script typed in English.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to reverse.
    - `from_bijoy: bool = False`: Reverse text from Bijoy format (ASCII) directly.
    - `remap_words: bool = True`: Whether to reverse input text with remapped (exception) words.

    Usage:
    ```python
    import avro

    reversed = avro.reverse('আমার সোনার বাংলা')
    print(reversed)
    ```
    """

    # Convert from Bijoy to Unicode if from_bijoy is True
    if from_bijoy:
        texts = to_unicode(*texts)
        if isinstance(texts, str):
            texts = (texts,)

    output = _concurrency_helper(lambda text: _reverse_backend_ext(text, remap_words), texts)
    return output[0] if len(output) == 1 else output
