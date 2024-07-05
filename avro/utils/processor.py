# SPDX-License-Identifier: MIT


# Import first-party Python libraries.
import contextlib
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# Import local modules.
from . import config, validate

# Setup pattern variables for matching.
PATTERNS = config.DICT["avro"]["patterns"]
NON_RULE_PATTERNS = [p for p in PATTERNS if "rules" not in p]
RULE_PATTERNS = [p for p in PATTERNS if "rules" in p]


# The following functions provide the functionality for the main "avro" package.
# These include rule / non-rule based pattern matching, remapping, reversing and more.
# Please do not modify these functions if you do not have the intentions to alter the core functionality of the module.


@lru_cache(maxsize=128)
def find_in_remap(text: str, *, reversed: bool = False) -> Tuple[str, bool]:
    """
    Finds and returns the remapped value for a given text.

    Returns a tuple of two elements:
    - (`str`): The remapped text.
    - (`bool`) Whether manual intervention is required.
    """

    previous_text = text

    for key, value in config.AVRO_EXCEPTIONS.items():
        if reversed:
            text = text.replace(key, value) if key.lower() in text.lower() else text
        else:
            text = text.replace(value, key) if (value := value.lower()) in text.lower() else text

    manual_required = any(
        word == previous_word for word, previous_word in zip(text.split(), previous_text.split())
    )

    return (text, manual_required)


def match_patterns(
    fixed_text: str, cur: int = 0, rule: bool = False, reversed: bool = False
) -> Dict[str, Any]:
    """
    Matches given text at cursor position with rule / non rule patterns.

    Returns a dictionary of three (upto four) elements.
    """

    rule_type = NON_RULE_PATTERNS if not rule else RULE_PATTERNS
    pattern = exact_find_in_pattern(fixed_text, reversed, cur, rule_type)

    if pattern:
        p = pattern[0]

        return {
            "matched": True,
            "found": p.get("find"),
            "replaced": p.get("replace"),
            "reversed": reverse_with_rules(cur, fixed_text, p.get("reverse")) if not rule else None,
            "rules": p.get("rules") if rule else None,
        }

    return {
        "matched": False,
        "found": None,
        "replaced": fixed_text[cur],
        "rules": None if rule else None,
    }


def exact_find_in_pattern(
    fixed_text: str, reversed: bool, cur: int = 0, patterns: Any = PATTERNS
) -> List[Dict[str, Any]]:
    """
    Returns pattern items that match given text, cursor position and pattern.
    """

    if reversed:
        return [
            x
            for x in patterns
            if (cur + len(x["replace"]) <= len(fixed_text))
            and x["replace"] == fixed_text[cur : (cur + len(x["replace"]))]
        ]

    return [
        x
        for x in patterns
        if x.get("find", None)
        and (cur + len(x["find"]) <= len(fixed_text))
        and x["find"] == fixed_text[cur : (cur + len(x["find"]))]
    ]


def reverse_with_rules(cursor: int, fixed_text: str, text_reversed: str) -> str:
    """
    Enhances the word with rules for reverse-parsing.
    """

    added_suffix = ""

    if not (
        fixed_text[cursor] in config.AVRO_KAR
        or fixed_text[cursor] in config.AVRO_SHORBORNO
        or fixed_text[cursor] in config.AVRO_IGNORE
        or len(fixed_text) == cursor + 1
    ):
        added_suffix = "o"

    with contextlib.suppress(IndexError):
        if (fixed_text[cursor + 1] in config.AVRO_KAR) or (
            fixed_text[cursor + 2] in config.AVRO_KAR and not cursor == 0
        ):
            added_suffix = ""

    return text_reversed if not text_reversed else text_reversed + added_suffix


def process_rules(rules: Dict[str, Any], fixed_text: str, cur: int = 0, cur_end: int = 1) -> Optional[str]:
    """
    Process rules matched in pattern and returns suitable replacement.

    If any rule's condition is satisfied, output the rules "replace",
    else output None.
    """

    replaced = ""

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


def process_match(match: Any, fixed_text: str, cur: int, cur_end: int) -> bool:
    """
    Processes a single match in rules.
    """

    # Initial/default value for replace.
    replace = True

    # Set check cursor depending on match['type']
    chk = cur - 1 if match["type"] == "prefix" else cur_end

    # Set scope based on whether scope is negative.
    if match["scope"].startswith("!"):
        scope = match["scope"][1:]
        negative = True
    else:
        scope = match["scope"]
        negative = False

    # Let the matching begin!
    if scope == "punctuation":
        if (
            not (
                (chk < 0 and match["type"] == "prefix")
                or (chk >= len(fixed_text) and match["type"] == "suffix")
                or validate.is_punctuation(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == "vowel":
        if (
            not (
                (
                    (chk >= 0 and match["type"] == "prefix")
                    or (chk < len(fixed_text) and match["type"] == "suffix")
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
                    (chk >= 0 and match["type"] == "prefix")
                    or (chk < len(fixed_text) and match["type"] == "suffix")
                )
                and validate.is_consonant(fixed_text[chk])
            )
            != negative
        ):
            replace = False

    elif scope == "exact":
        if match["type"] == "prefix":
            exact_start = cur - len(match["value"])
            exact_end = cur
        else:
            exact_start = cur_end
            exact_end = cur_end + len(match["value"])

        if not validate.is_exact(match["value"], fixed_text, exact_start, exact_end, negative):
            replace = False

    return replace


def rearrange_unicode_text(text: str) -> str:
    """
    Rearranges Unicode (Avro) text to match conversion standards for ASCII.

    Returns the rearranged string.
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

            chars[i - 1], chars[i], chars[i + 1 : i + j + found_pre_kar + 1], chars[i + j + 1 :] = (
                chars[i + j + 1],
                chars[i + 1 : i + j + 1],
                chars[i - 1],
                chars[i],
                chars[i + j + found_pre_kar + 1 :],
            )
            i += j + found_pre_kar
            barrier = i + 1

    return "".join(chars)
