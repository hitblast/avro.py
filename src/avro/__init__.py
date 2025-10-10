# SPDX-License-Identifier: MIT


"""A modern Pythonic implementation of the popular Bangla typing software Avro Phonetic.

Project Links:
    https://github.com/hitblast/avro.py

"""

# Import only the public API functions to avoid import cycles.
from .main import (
    parse,
    parse_async,
    parse_iter,
    parse_async_iter,
    to_bijoy,
    to_bijoy_async,
    to_bijoy_iter,
    to_bijoy_async_iter,
    to_unicode,
    to_unicode_async,
    to_unicode_iter,
    to_unicode_async_iter,
    reverse,
    reverse_async,
    reverse_iter,
    reverse_async_iter,
)

__all__ = [
    "parse",
    "parse_async",
    "parse_iter",
    "parse_async_iter",
    "to_bijoy",
    "to_bijoy_async",
    "to_bijoy_iter",
    "to_bijoy_async_iter",
    "to_unicode",
    "to_unicode_async",
    "to_unicode_iter",
    "to_unicode_async_iter",
    "reverse",
    "reverse_async",
    "reverse_iter",
    "reverse_async_iter",
]
