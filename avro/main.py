# SPDX-License-Identifier: MIT


# Import first-party Python libraries.
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from itertools import chain
from typing import Callable, Generator, List, Tuple, Union

# Import local modules.
from .utils import processor, validate
from .utils.config import BIJOY_MAP


# The helper function for handling multithreaded workloads.
def _concurrency_helper(func: Callable, params: Tuple[str]) -> List[str]:
    output = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(func, text): text for text in params}

        for future in as_completed(futures):
            output.append(future.result())

    return output


# The primary parse function for the library.
def parse(*texts: str, bijoy: bool = False, remap_words: bool = True) -> Union[str, List[str]]:
    """
    #### Parses input text, matches and replaces using the Avro Dictionary.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to parse.
    - `bijoy: bool = False`: Whether to return in the Bijoy Keyboard format (ASCII).
    - `remap_words: bool = True`: Whether to parse input text with remapped (exception) words.

    Usage:
    ```python
    import avro

    parsed = avro.parse('ami banglay gan gai')
    print(parsed)
    ```
    """

    # Compiled regular expression for UTF-8 validation
    utf8_regex = re.compile(r"\A[\x00-\x7F]*\Z")

    @lru_cache(maxsize=128)
    def _parse_backend(text: str) -> str:
        fixed_text = validate.fix_string_case(text)  # Sanitize input text.
        manual_required = True  # Whether manual intervention is required.
        cur_end = 0  # Cursor end point.

        # Replace predefined exceptions in the input text.
        if remap_words:
            fixed_text, manual_required = processor.find_in_remap(fixed_text)

        def output_generator() -> Generator[str, None, None]:
            nonlocal cur_end

            # Iterate through input text.
            for cur, i in enumerate(fixed_text):
                uni_pass = utf8_regex.match(i) is not None

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

        return "".join(chain.from_iterable(output_generator())) if manual_required else fixed_text

    output = _concurrency_helper(_parse_backend, texts)

    # If the `bijoy` parameter is set to `True`, then convert the output to Bijoy Keyboard format.
    if bijoy:
        return to_bijoy(*output)
    else:
        return output[0] if len(output) == 1 else output


def to_bijoy(*texts: str) -> Union[str, List[str]]:
    """
    #### Converts input text to Bijoy Keyboard format (ASCII).

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

    @lru_cache(maxsize=128)
    def _convert_backend(text: str) -> str:
        text = processor.rearrange_unicode_text(re.sub("ৌ", "ৌ", re.sub("ো", "ো", text)))

        for unic in BIJOY_MAP:
            text = re.sub(unic, BIJOY_MAP[unic], text)

        return text.strip()

    output = _concurrency_helper(_convert_backend, texts)
    return output[0] if len(output) == 1 else output


def reverse(*texts: str, remap_words: bool = True) -> Union[str, List[str]]:
    """
    #### Reverses input text to Roman script typed in English.

    If a valid replacement is found, then it returns the replaced string.
    If no replacement is found, then it instead returns the input text.

    Parameters:
    - `*texts: str | Tuple[str]`: The text(s) to reverse.
    - `remap_words: bool = True`: Whether to reverse input text with remapped (exception) words.

    Usage:
    ```python
    import avro

    reversed = avro.reverse('আমার সোনার বাংলা')
    print(reversed)
    ```
    """

    # Internal function for multiple reverses.
    @lru_cache(maxsize=128)
    def _reverse_backend(text: str) -> str:
        manual_required = True  # Whether manual intervention is required.

        # Replace predefined exceptions in the input text.
        if remap_words:
            text, manual_required = processor.find_in_remap(text, reversed=True)

        # Iterate through input text.
        def output_generator() -> Generator[str, None, None]:
            for cur, i in enumerate(text):
                try:
                    i.encode("utf-8")
                    match = processor.match_patterns(text, cur, rule=False, reversed=True)

                    yield (match["reversed"] or match["found"]) if match["matched"] else i

                except UnicodeDecodeError:
                    yield i

        return "".join(chain.from_iterable(output_generator())) if manual_required else text

    # Split using regex to remove noise.
    compiled_regex = re.compile("(\\s|\\.|,|\\?|\\।|\\-|;|')", re.UNICODE)

    # Extension for the _reverse_backend() function.
    @lru_cache(maxsize=128)
    def _reverse_backend_ext(text: str) -> str:
        separated_texts = compiled_regex.split(text)
        text_segments = [_reverse_backend(separated_text) for separated_text in separated_texts]
        return "".join(text_segments)

    # Prepare final output.
    output = _concurrency_helper(_reverse_backend_ext, texts)
    return output[0] if len(output) == 1 else output
