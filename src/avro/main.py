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
from typing import Callable, Generator, Union

from .core import processor, validate
from .core.config import BIJOY_MAP, BIJOY_MAP_REVERSE

# Compiled regex patterns. These are primarily used in parse() and reverse()
# function calls to validate input text and search for invalid UTF-8 characters.
UTF8_REGEX = re.compile(r"\A[\x00-\x7F]*\Z", re.UNICODE)
REVERSE_REGEX = re.compile(r"(\s|\.|,|\?|।|-|;|')", re.UNICODE)


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

    for unic in BIJOY_MAP:
        text = re.sub(unic, BIJOY_MAP[unic], text)

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

    for ascii_c in BIJOY_MAP_REVERSE:
        text = re.sub(re.escape(ascii_c), BIJOY_MAP_REVERSE[ascii_c], text)

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
    *texts: str, bijoy: bool = False, remap_words: bool = True
) -> Union[str, list[str]]:
    """Asynchronous version of parse() function.

    Parses input text, matches and replaces using the Avro Dictionary.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    *texts: str
        The text(s) to parse.
    bijoy: bool = False
        Whether to return result in the Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to parse input text with remapped (exception) words.

    Returns:
    --------
    str | list[str]
        The parsed text(s).
    """

    output = await _async_concurrency_helper(
        lambda text: _parse_backend(text, remap_words), texts
    )

    # If the `bijoy` parameter is set to `True`, then convert the output to Bijoy Keyboard format.
    if bijoy:
        return await to_bijoy_async(*output)
    else:
        return output[0] if len(output) == 1 else output


def parse(
    *texts: str, bijoy: bool = False, remap_words: bool = True
) -> Union[str, list[str]]:
    """Parses input text, matches and replaces using the Avro Dictionary.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    *texts: str
        The text(s) to parse.
    bijoy: bool = False
        Whether to return result in the Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to parse input text with remapped (exception) words.

    Returns:
    --------
    str | list[str]
        The parsed text(s).
    """

    output = _sync_concurrency_helper(
        lambda text: _parse_backend(text, remap_words), texts
    )

    if bijoy:
        return to_bijoy(*output)
    else:
        return output[0] if len(output) == 1 else output


async def to_bijoy_async(*texts: str) -> Union[str, list[str]]:
    """Asynchronous version of to_bijoy() function.

    Converts input text (Avro, Unicode) to Bijoy Keyboard format (ASCII).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    *texts: str
        The text(s) to convert.

    Returns:
    --------
    str | list[str]
        The converted text(s).
    """

    output = await _async_concurrency_helper(_convert_backend, texts)
    return output[0] if len(output) == 1 else output


def to_bijoy(*texts: str) -> Union[str, list[str]]:
    """Converts input text (Avro, Unicode) to Bijoy Keyboard format (ASCII).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    *texts: str
        The text(s) to convert.

    Returns:
    --------
    str | list[str]
        The converted text(s).
    """

    output = _sync_concurrency_helper(_convert_backend, texts)
    return output[0] if len(output) == 1 else output


async def to_unicode_async(*texts: str) -> Union[str, list[str]]:
    """Asynchronous version of to_unicode() function.

    Converts input text (Bijoy Keyboard, ASCII) to Unicode (Avro Keyboard format).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    *texts: str
        The text(s) to convert.

    Returns:
    --------
    str | list[str]
        The converted text(s).
    """

    output = await _async_concurrency_helper(_convert_backend_unicode, texts)
    return output[0] if len(output) == 1 else output


def to_unicode(*texts: str) -> Union[str, list[str]]:
    """Converts input text (Bijoy Keyboard, ASCII) to Unicode (Avro Keyboard format).
    If a valid conversion is found, then it returns the converted string.

    Parameters:
    -----------
    *texts: str
        The text(s) to convert.

    Returns:
    --------
    str | list[str]
        The converted text(s).
    """

    output = _sync_concurrency_helper(_convert_backend_unicode, texts)
    return output[0] if len(output) == 1 else output


async def reverse_async(
    *texts: str, from_bijoy: bool = False, remap_words: bool = True
) -> Union[str, list[str]]:
    """Asynchronous version of reverse() function.

    Reverses input text to Roman script typed in English.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    *texts: str
        The text(s) to reverse.
    from_bijoy: bool = False
        Whether to reverse input text from Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str | list[str]
        The reversed text(s).
    """

    # Convert from Bijoy to Unicode if from_bijoy is True
    if from_bijoy:
        converted_texts = await to_unicode_async(*texts)
        if isinstance(converted_texts, str):
            texts = (converted_texts,)

    output = await _async_concurrency_helper(
        lambda text: _reverse_backend_ext(text, remap_words), texts
    )

    return output[0] if len(output) == 1 else output


def reverse(
    *texts: str, from_bijoy: bool = False, remap_words: bool = True
) -> Union[str, list[str]]:
    """Reverses input text to Roman script typed in English.
    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    -----------
    *texts: str
        The text(s) to reverse.
    from_bijoy: bool = False
        Whether to reverse input text from Bijoy Keyboard format (ASCII).
    remap_words: bool = True
        Whether to reverse input text with remapped (exception) words.

    Returns:
    --------
    str | list[str]
        The reversed text(s).
    """

    # Convert from Bijoy to Unicode if from_bijoy is True
    if from_bijoy:
        converted_texts = to_unicode(*texts)
        if isinstance(converted_texts, str):
            texts = (converted_texts,)

    output = _sync_concurrency_helper(
        lambda text: _reverse_backend_ext(text, remap_words), texts
    )
    return output[0] if len(output) == 1 else output
