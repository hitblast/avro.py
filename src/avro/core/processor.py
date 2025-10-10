# SPDX-License-Identifier: MIT


# Imports.
import contextlib
import re
from functools import lru_cache

from . import validate
from .config import (
    AVRO_EXCEPTIONS,
    AVRO_IGNORE,
    AVRO_KAR,
    AVRO_SHONGKHA,
    AVRO_SHORBORNO,
)
from ..resources import DICT
from ..resources.dictionary import (
    PatternDict,
    PatternRule,
    PatternRuleMatch,
)


# Setup pattern variables for matching.
PATTERNS = DICT["avro"]["patterns"]
NON_RULE_PATTERNS = [p for p in PATTERNS if "rules" not in p]
RULE_PATTERNS = [p for p in PATTERNS if "rules" in p]


# ---

# The following functions provide the functionality for the main "avro" package.
# These include rule / non-rule based pattern matching, remapping, reversing and more.
# Please do not modify these functions if you do not have the intentions to alter the core functionality of the module.

# ---


@lru_cache(maxsize=128)
def find_in_remap(text: str, *, reversed: bool = False) -> tuple[str, bool]:
    """Finds and returns the remapped value for a given text.

    Parameters:
    -----------
    text: str
        The text to be remapped.
    reversed: bool
        Whether to operate in reverse mode.

    Returns:
    -----------
    tuple[str, bool]
        A tuple of two elements:
        1. The remapped text with markers.
        2. Whether manual intervention is required.
    """

    for key, value in AVRO_EXCEPTIONS.items():
        if reversed:
            pattern = re.compile(re.escape(key), re.IGNORECASE)
            text = pattern.sub(lambda m: "<rm>" + value + "</rm>", text)
        else:
            pattern = re.compile(re.escape(value.lower()), re.IGNORECASE)
            text = pattern.sub(lambda m: "<rm>" + key + "</rm>", text)

    segments = re.split(r"(<rm>.*?</rm>)", text)
    manual_required = any(
        segment
        and not (segment.startswith("<rm>") and segment.endswith("</rm>"))
        for segment in segments
    )
    return text, manual_required


def match_patterns(
    fixed_text: str, cur: int = 0, rule: bool = False, reversed: bool = False
) -> dict[str, str | bool | list[PatternRule] | None]:
    """Matches given text at cursor position with rule / non rule patterns.

    Parameters:
    -----------

    fixed_text: str
        The text to be matched.

    cur: int
        The cursor position.

    rule: bool
        Whether to match with rules.

    reversed: bool
        Whether to operate in reverse mode.

    Returns:
    --------

    dict[str, Any]
        A dictionary containing the following keys:
        1. matched: bool
        2. found: str
        3. replaced: str
        4. reversed: str
        5. rules: dict[str, Any]
    """

    rule_type = NON_RULE_PATTERNS if not rule else RULE_PATTERNS
    pattern = exact_find_in_pattern(fixed_text, reversed, cur, rule_type)

    if pattern:
        p = pattern[0]

        return {
            "matched": True,
            "found": p.get("find"),
            "replaced": p.get("replace"),
            "reversed": reverse_with_rules(
                cur, fixed_text, p.get("reverse", None)
            )
            if not rule
            else None,
            "rules": p.get("rules") if rule else None,
        }

    return {
        "matched": False,
        "found": None,
        "replaced": fixed_text[cur],
        "rules": None if rule else None,
    }


def exact_find_in_pattern(
    fixed_text: str,
    reversed: bool,
    cur: int = 0,
    patterns: list[PatternDict] = PATTERNS,
) -> list[PatternDict]:
    """Returns pattern items that match given text, cursor position and pattern.

    Parameters:
    -----------

    fixed_text: str
        The text to be matched.

    reversed: bool
        Whether to operate in reverse mode.

    cur: int = 0
        The cursor position.

    patterns: Any = PATTERNS
        The patterns to be matched.

    Returns:
    --------

    list[dict[str, Any]]
        A list of dictionaries containing the matched patterns.
    """

    if reversed:
        return [
            x
            for x in patterns
            if (
                "replace" in x
                and (cur + len(x["replace"]) <= len(fixed_text))
                and x["replace"] == fixed_text[cur : (cur + len(x["replace"]))]
            )
        ]

    return [
        x
        for x in patterns
        if (
            "find" in x
            and x.get("find") is not None
            and (cur + len(x["find"]) <= len(fixed_text))
            and x["find"] == fixed_text[cur : (cur + len(x["find"]))]
        )
    ]


def reverse_with_rules(
    cursor: int, fixed_text: str, text_reversed: str | None
) -> str | None:
    """Enhances the word with rules for reverse-parsing.

    Parameters:
    -----------

    cursor: int
        The cursor position.

    fixed_text: str
        The fixed text.

    text_reversed: str
        The reversed text.

    Returns:
    --------

    str
        The enhanced word.
    """

    added_suffix = ""

    if not (
        fixed_text[cursor] in AVRO_KAR
        or fixed_text[cursor] in AVRO_SHONGKHA
        or fixed_text[cursor] in AVRO_SHORBORNO
        or fixed_text[cursor] in AVRO_IGNORE
        or len(fixed_text) == cursor + 1
    ):
        added_suffix = "o"

    with contextlib.suppress(IndexError):
        if (fixed_text[cursor + 1] in AVRO_KAR) or (
            fixed_text[cursor + 2] in AVRO_KAR and not cursor == 0
        ):
            added_suffix = ""

    return text_reversed if not text_reversed else text_reversed + added_suffix


def process_rules(
    rules: list[PatternRule], fixed_text: str, cur: int = 0, cur_end: int = 1
) -> str | None:
    """Process rules matched in pattern and returns suitable replacement.

    If any rule's condition is satisfied, output the rules "replace", else output None.

    Parameters:
    -----------

    rules: dict[str, Any]
        The rules to be processed.

    fixed_text: str
        The fixed text.

    cur: int = 0
        The cursor position.

    cur_end: int = 1
        The end cursor position.

    Returns:
    --------

    Optional[str]
        The replaced text if any rule's condition is satisfied, else None.
    """

    replaced = ""
    matched = False

    # Iterate through rules.
    for rule in rules:
        matched = False

        for match in rule["matches"]:
            matched = process_match(match, fixed_text, cur, cur_end)

            if not matched:
                break

        if matched:
            replaced = rule["replace"]
            break

    return replaced if matched else None


def process_match(
    match: PatternRuleMatch, fixed_text: str, cur: int, cur_end: int
) -> bool:
    """Processes a single match in rules.

    Parameters:
    -----------

    match: Any
        The match to be processed.

    fixed_text: str
        The fixed text.

    cur: int
        The cursor position.

    cur_end: int
        The end cursor position.

    Returns:
    --------

    bool
        True if the match is successful, else False.
    """

    # Initial/default value for replace.
    replace = True

    # Defensive access for optional keys in PatternRuleMatch
    match_type = match.get("type")
    match_scope = match.get("scope")
    match_value = match.get("value")

    # If required keys are missing, fail the match
    if match_type is None or match_scope is None:
        return False

    # Set check cursor depending on match['type']
    chk = cur - 1 if match_type == "prefix" else cur_end

    # Set scope based on whether scope is negative.
    if match_scope.startswith("!"):
        scope = match_scope[1:]
        negative = True
    else:
        scope = match_scope
        negative = False

    # Let the matching begin!
    if scope == "punctuation":
        if (
            not (
                (chk < 0 and match_type == "prefix")
                or (chk >= len(fixed_text) and match_type == "suffix")
                or validate.is_punctuation(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == "vowel":
        if (
            not (
                (
                    (chk >= 0 and match_type == "prefix")
                    or (chk < len(fixed_text) and match_type == "suffix")
                )
                and validate.is_vowel(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == "consonant":
        if (
            not (
                (
                    (chk >= 0 and match_type == "prefix")
                    or (chk < len(fixed_text) and match_type == "suffix")
                )
                and validate.is_consonant(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == "exact":
        # Defensive: match_value must be a string
        if not isinstance(match_value, str):
            return False
        if match_type == "prefix":
            exact_start = cur - len(match_value)
            exact_end = cur
        else:
            exact_start = cur_end
            exact_end = cur_end + len(match_value)

        if not validate.is_exact(
            match_value, fixed_text, exact_start, exact_end, negative
        ):
            replace = False

    return replace


def rearrange_unicode_text(text: str) -> str:
    """Rearranges Unicode (Avro) text to match conversion standards for ASCII.

    Parameters:
    -----------

    text: str
        The text to be rearranged.

    Returns:
    --------

    str
        The rearranged text.
    """

    # Convert the string to a list of individual characters.
    chars = list(text)
    length = len(chars)
    barrier = 0

    for i in range(length):
        if validate.is_bangla_prekar(chars[i]):
            j = 1

            while (
                i - j >= 0
                and i - j > barrier
                and validate.is_bangla_banjonborno(chars[i - j])
                and validate.is_bangla_halant(chars[i - j - 1])
            ):
                j += 2

            chars[i - j], chars[i] = chars[i], chars[i - j]
            barrier = i + 1

        if (
            i < length - 1
            and validate.is_bangla_halant(chars[i])
            and chars[i - 1] == "র"
            and not validate.is_bangla_halant(chars[i - 2])
        ):
            j = 1
            found_pre_kar = 0

            while True:
                if validate.is_bangla_banjonborno(chars[i + j]):
                    if validate.is_bangla_halant(chars[i + j + 1]):
                        j += 2
                    elif validate.is_bangla_prekar(chars[i + j + 1]):
                        found_pre_kar = 1
                        break
                else:
                    break

            chars = (
                chars[: i - 1]
                + [chars[i + j + 1]]
                + chars[i + 1 : i + j + 1]
                + [chars[i - 1]]
                + [chars[i]]
                + chars[i + j + found_pre_kar + 1 :]
            )
            i += j + found_pre_kar
            barrier = i + 1

    return "".join(chars)


def rearrange_bijoy_text(text: str) -> str:
    """Rearranges Bijoy Keyboard text to match conversion standards for Unicode.

    Parameters:
    -----------

    text: str
        The text to be rearranged.

    Returns:
    --------

    str
        The rearranged text.
    """

    i = 0
    while i < len(text):
        if (
            i > 0
            and text[i] == "\u09cd"
            and (
                validate.is_bangla_kar(text[i - 1])
                or validate.is_bangla_nukta(text[i - 1])
            )
            and i < len(text) - 1
        ):
            text = (
                text[: i - 1]
                + text[i]
                + text[i + 1]
                + text[i - 1]
                + text[i + 2 :]
            )

        if (
            0 < i < len(text) - 1
            and text[i] == "\u09cd"
            and text[i - 1] == "\u09b0"
            and text[i - 2] != "\u09cd"
            and validate.is_bangla_kar(text[i + 1])
        ):
            text = (
                text[: i - 1]
                + text[i + 1]
                + text[i - 1]
                + text[i]
                + text[i + 2 :]
            )

        if (
            i < len(text) - 1
            and text[i] == "র"
            and validate.is_bangla_halant(text[i + 1])
            and not validate.is_bangla_halant(text[i - 1])
        ):
            j = 1
            while True:
                if i - j < 0:
                    break
                if validate.is_bangla_banjonborno(
                    text[i - j]
                ) and validate.is_bangla_halant(text[i - j - 1]):
                    j += 2
                elif j == 1 and validate.is_bangla_kar(text[i - j]):
                    j += 1
                else:
                    break
            text = (
                text[: i - j]
                + text[i]
                + text[i + 1]
                + text[i - j : i]
                + text[i + 2 :]
            )
            i += 1
            continue

        if (
            i < len(text) - 1
            and validate.is_bangla_prekar(text[i])
            and text[i + 1] != " "
        ):
            j = 1
            part = ""
            while validate.is_bangla_banjonborno(text[i + j]):
                if validate.is_bangla_halant((part := text[i + j + 1])):
                    j += 2
                else:
                    break
            temp = text[:i] + text[i + 1 : i + j + 1]
            if text[i] == "ে" and part == "া":
                temp += "ো"
                add = 1
            elif text[i] == "ে" and part == "ৗ":
                temp += "ৌ"
                add = 1
            else:
                temp += text[i]
                add = 0
            temp += text[i + j + add + 1 :]
            text = temp
            i += j

        if (
            i < len(text) - 1
            and text[i] == "ঁ"
            and validate.is_bangla_postkar(text[i + 1])
        ):
            temp = text[:i] + text[i + 1] + text[i] + text[i + 2 :]
            text = temp

        i += 1

    return text
