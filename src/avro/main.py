# SPDX-License-Identifier: MIT


"""The core module for the avro.py package.

avro.py
Licensed under the terms of the MIT License.
"""

# Imports.
import asyncio
import re
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from itertools import chain
from typing import Callable, Generator, Iterable

from .core import processor, validate
from .core.config import BIJOY_MAP, BIJOY_MAP_REVERSE

# Compiled regex patterns. These are primarily used in parse() and reverse()
# function calls to validate input text and search for invalid UTF-8 characters.
UTF8_REGEX = re.compile(r"\A[\x00-\x7F]*\Z", re.UNICODE)
REVERSE_REGEX = re.compile(r"(\s|\.|,|\?|।|-|;|')", re.UNICODE)

# Pre-compiled regex patterns for bijoy conversion optimization
_BIJOY_REGEX_PATTERN = None
_BIJOY_REVERSE_REGEX_PATTERN = None


def _get_bijoy_regex_pattern():
    """Get or create the compiled regex pattern for bijoy conversion."""
    global _BIJOY_REGEX_PATTERN
    if _BIJOY_REGEX_PATTERN is None:
        # Sort by length (descending) to match longer patterns first
        sorted_patterns = sorted(BIJOY_MAP.keys(), key=len, reverse=True)
        # Escape each pattern and join with |
        pattern = "|".join(re.escape(p) for p in sorted_patterns)
        _BIJOY_REGEX_PATTERN = re.compile(pattern)
    return _BIJOY_REGEX_PATTERN


def _get_bijoy_reverse_regex_pattern():
    """Get or create the compiled regex pattern for reverse bijoy conversion."""
    global _BIJOY_REVERSE_REGEX_PATTERN
    if _BIJOY_REVERSE_REGEX_PATTERN is None:
        # Sort by length (descending) to match longer patterns first
        sorted_patterns = sorted(
            BIJOY_MAP_REVERSE.keys(), key=len, reverse=True
        )
        # Escape each pattern and join with |
        pattern = "|".join(re.escape(p) for p in sorted_patterns)
        _BIJOY_REVERSE_REGEX_PATTERN = re.compile(pattern)
    return _BIJOY_REVERSE_REGEX_PATTERN


# This is a backend function and MUST NOT BE EXPORTED!
async def _async_concurrency_helper(
    func: Callable, params: tuple[str, ...]
) -> list[str]:
    """Concurrency helper for the core functions of avro.py.

    Parameters:
    -----------

    func: Callable
        The function to run concurrently.

    params: tuple[str, ...]
        The parameters to pass to the function.

    Returns:
    --------

    list[str]
        The results of the function run concurrently.

    """

    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(None, func, text) for text in params]
    results = await asyncio.gather(*tasks)
    return results


# This is a backend function and MUST NOT BE EXPORTED!
def _sync_concurrency_helper(
    func: Callable, params: tuple[str, ...]
) -> list[str]:
    """Synchronous concurrency helper for the core functions of avro.py using multithreading.

    Parameters:
    -----------
    func: Callable
        The function to run concurrently.

    params: tuple[str, ...]
        The parameters to pass to the function.

    Returns:
    --------
    list[str]
        The results of the function run concurrently.
    """

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(func, params))
    return results


# Helper function to manage remapped markers in text.
def _process_remapped(
    text: str, manual_required: bool, process_func: Callable[[str], str]
) -> str:
    """Helper to process text segments with remapped markers.

    If all segments have been replaced, it removes the markers.
    Otherwise, it splits the text by marker and processes non-marked segments using process_func.

    Parameters:
    -----------
    text : str
        The text containing possible remapped segments.
    manual_required : bool
        Indicator if further manual processing is needed.
    process_func : Callable[[str], str]
        A function to process segments without markers.

    Returns:
    --------
    str
        The processed text.
    """

    if not manual_required:
        return text.replace("<rm>", "").replace("</rm>", "")

    segments = re.split(r"(<rm>.*?</rm>)", text)
    processed_segments = []

    for segment in segments:
        if segment.startswith("<rm>") and segment.endswith("</rm>"):
            processed_segments.append(segment[4:-5])
        elif segment:
            processed_segments.append(process_func(segment))

    return "".join(processed_segments)


# This is a backend function and MUST NOT BE EXPORTED!
def _parse_output_generator(
    fixed_text: str, cur_end: int
) -> Generator[str, None, None]:
    """Output generator for the parse() function.

    Parameters:
    -----------
    fixed_text: str
        The fixed text to parse.
    cur_end: int
        The cursor end point.

    Yields:
    -------
    str
        The parsed output.
    """

    for cur, i in enumerate(fixed_text):
        # Optimized UTF-8 check - most ASCII chars are in range 0-127
        uni_pass = ord(i) < 128
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
                        rules=match["rules"],
                        fixed_text=fixed_text,
                        cur=cur,
                        cur_end=cur_end,
                    )
                    if replaced:
                        yield replaced
                    else:
                        yield match["replaced"]
            if not matched:
                cur_end = cur + 1
                yield i


# This is a backend function and MUST NOT BE EXPORTED!
@lru_cache(maxsize=128)
def _parse_backend(text: str, remap_words: bool) -> str:
    """The working backend for the parse() function.

    Parameters:
    -----------
    text: str
        The text to parse.
    remap_words: bool
        Whether to parse input text with remapped (exception) words.

    Returns:
    --------
    str
        The parsed text.
    """

    fixed_text = validate.fix_string_case(text)

    if remap_words:
        fixed_text, manual_required = processor.find_in_remap(fixed_text)
        return _process_remapped(
            fixed_text,
            manual_required,
            lambda segment: "".join(
                chain.from_iterable(_parse_output_generator(segment, 0))
            ),
        )
    else:
        return "".join(
            chain.from_iterable(_parse_output_generator(fixed_text, 0))
        )


# This is a backend function and MUST NOT BE EXPORTED!
@lru_cache(maxsize=128)
def _convert_backend(text: str) -> str:
    """The working backend for the to_bijoy() function.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    text = processor.rearrange_unicode_text(
        re.sub("ৌ", "ৌ", re.sub("ো", "ো", text))
    )

    # Use compiled regex with replacement function for better performance
    def replace_func(match):
        return BIJOY_MAP[match.group(0)]

    pattern = _get_bijoy_regex_pattern()
    text = pattern.sub(replace_func, text)

    return text.strip()


# This is a backend function and MUST NOT BE EXPORTED!
@lru_cache(maxsize=128)
def _convert_backend_unicode(text: str) -> str:
    """The working backend for the to_unicode() function.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    # Use compiled regex with replacement function for better performance
    def replace_func(match):
        return BIJOY_MAP_REVERSE[match.group(0)]

    pattern = _get_bijoy_reverse_regex_pattern()
    text = pattern.sub(replace_func, text)

    text = re.sub("অা", "আ", processor.rearrange_bijoy_text(text))

    return text.strip()


# This is a backend function and MUST NOT BE EXPORTED!
def _reverse_output_generator(text: str) -> Generator[str, None, None]:
    """Generates the reversed output for the reverse() function.

    Parameters:
    -----------
    text: str
        The text to reverse.

    Yields:
    -------
    str
        The reversed output.
    """

    for cur, i in enumerate(text):
        try:
            i.encode("utf-8")
            match = processor.match_patterns(
                text, cur, rule=False, reversed=True
            )

            yield (
                (match["reversed"] or match["found"])
                if match["matched"]
                else i
            )
        except UnicodeDecodeError:
            yield i


# This is a backend function and MUST NOT BE EXPORTED!
@lru_cache(maxsize=128)
def _reverse_backend(text: str, remap_words: bool) -> str:
    """The working backend for the reverse() function.

    Parameters:
    -----------
    text: str
        The text to reverse.
    remap_words: bool
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str
        The reversed text.
    """

    if remap_words:
        text, manual_required = processor.find_in_remap(text, reversed=True)
        return _process_remapped(
            text,
            manual_required,
            lambda segment: "".join(
                chain.from_iterable(_reverse_output_generator(segment))
            ),
        )
    else:
        return "".join(chain.from_iterable(_reverse_output_generator(text)))


# This is a backend function and MUST NOT BE EXPORTED!
@lru_cache(maxsize=128)
def _reverse_backend_ext(text: str, remap_words: bool) -> str:
    """Backend extension for the reverse() function.

    Parameters:
    -----------
    text: str
        The text to reverse.
    remap_words: bool
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str
        The reversed text.
    """

    separated_texts = REVERSE_REGEX.split(text)
    text_segments = [
        _reverse_backend(separated_text, remap_words)
        for separated_text in separated_texts
    ]
    return "".join(text_segments)


# ---

# Primary user-end functions.
# ---


async def parse_async(
    text: str, bijoy: bool = False, remap_words: bool = True
) -> str:
    """Asynchronous version of parse() function.

    Parses input text, matches and replaces using the Avro Dictionary.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    text: str
        The text to parse.
    bijoy: bool = False
        Whether to return result in the Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to parse input text with remapped (exception) words.

    Returns:
    --------
    str
        The parsed text.
    """

    result = await _async_concurrency_helper(
        lambda t: _parse_backend(t, remap_words), (text,)
    )
    parsed = result[0]
    if bijoy:
        return await to_bijoy_async(parsed)
    return parsed


async def parse_async_iter(
    texts: Iterable[str], bijoy: bool = False, remap_words: bool = True
) -> list[str]:
    """Asynchronous version of parse for multiple texts."""
    params = tuple(texts)
    output = await _async_concurrency_helper(
        lambda text: _parse_backend(text, remap_words), params
    )
    if bijoy:
        return await to_bijoy_async_iter(output)
    return output


def parse(text: str, bijoy: bool = False, remap_words: bool = True) -> str:
    """Parses input text, matches and replaces using the Avro Dictionary.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    text: str
        The text to parse.
    bijoy: bool = False
        Whether to return result in the Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to parse input text with remapped (exception) words.

    Returns:
    --------
    str
        The parsed text.
    """

    parsed = _parse_backend(text, remap_words)
    if bijoy:
        return to_bijoy(parsed)
    return parsed


def parse_iter(
    texts: Iterable[str], bijoy: bool = False, remap_words: bool = True
) -> list[str]:
    """Parses multiple texts and returns list of parsed strings."""
    params = tuple(texts)
    output = _sync_concurrency_helper(
        lambda text: _parse_backend(text, remap_words), params
    )
    if bijoy:
        return to_bijoy_iter(output)
    return output


async def to_bijoy_async(text: str) -> str:
    """Asynchronous version of to_bijoy() function.

    Converts input text (Avro, Unicode) to Bijoy Keyboard format (ASCII).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    result = await _async_concurrency_helper(_convert_backend, (text,))
    return result[0]


def reverse_iter(
    texts: Iterable[str], from_bijoy: bool = False, remap_words: bool = True
) -> list[str]:
    """Reverses multiple texts to Roman script and returns list of strings."""
    params = tuple(texts)
    if from_bijoy:
        converted = to_unicode_iter(params)
        params = tuple(converted)
    return _sync_concurrency_helper(
        lambda text: _reverse_backend_ext(text, remap_words), params
    )


async def reverse_async_iter(
    texts: Iterable[str], from_bijoy: bool = False, remap_words: bool = True
) -> list[str]:
    """Asynchronous version of reverse for multiple texts."""
    params = tuple(texts)
    if from_bijoy:
        converted = await to_unicode_async_iter(params)
        params = tuple(converted)
    return await _async_concurrency_helper(
        lambda text: _reverse_backend_ext(text, remap_words), params
    )


def to_unicode_iter(texts: Iterable[str]) -> list[str]:
    """Converts multiple texts from Bijoy ASCII to Unicode and returns list of strings."""
    params = tuple(texts)
    return _sync_concurrency_helper(_convert_backend_unicode, params)


async def to_unicode_async_iter(texts: Iterable[str]) -> list[str]:
    """Asynchronous version of to_unicode for multiple texts."""
    params = tuple(texts)
    return await _async_concurrency_helper(_convert_backend_unicode, params)


def to_bijoy_iter(texts: Iterable[str]) -> list[str]:
    """Converts multiple texts to Bijoy ASCII and returns list of strings."""
    params = tuple(texts)
    return _sync_concurrency_helper(_convert_backend, params)


async def to_bijoy_async_iter(texts: Iterable[str]) -> list[str]:
    """Asynchronous version of to_bijoy for multiple texts."""
    params = tuple(texts)
    return await _async_concurrency_helper(_convert_backend, params)


def to_bijoy(text: str) -> str:
    """Converts input text (Avro, Unicode) to Bijoy Keyboard format (ASCII).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    return _convert_backend(text)


async def to_unicode_async(text: str) -> str:
    """Asynchronous version of to_unicode() function.

    Converts input text (Bijoy Keyboard, ASCII) to Unicode (Avro Keyboard format).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    result = await _async_concurrency_helper(_convert_backend_unicode, (text,))
    return result[0]


def to_unicode(text: str) -> str:
    """Converts input text (Bijoy Keyboard, ASCII) to Unicode (Avro Keyboard format).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    text: str
        The text to convert.

    Returns:
    --------
    str
        The converted text.
    """

    return _convert_backend_unicode(text)


async def reverse_async(
    text: str, from_bijoy: bool = False, remap_words: bool = True
) -> str:
    """Asynchronous version of reverse() function.

    Reverses input text to Roman script typed in English.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    text: str
        The text to reverse.
    from_bijoy: bool = False
        Whether to reverse input text from Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str
        The reversed text.
    """

    # Convert from Bijoy to Unicode if from_bijoy is True
    if from_bijoy:
        text = await to_unicode_async(text)
    result = await _async_concurrency_helper(
        lambda t: _reverse_backend_ext(t, remap_words), (text,)
    )
    return result[0]


def reverse(
    text: str, from_bijoy: bool = False, remap_words: bool = True
) -> str:
    """Reverses input text to Roman script typed in English.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    text: str
        The text to reverse.
    from_bijoy: bool = False
        Whether to reverse input text from Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str
        The reversed text.
    """

    # Convert from Bijoy to Unicode if from_bijoy is True
    if from_bijoy:
        text = to_unicode(text)
    return _reverse_backend_ext(text, remap_words)
