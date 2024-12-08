# SPDX-License-Identifier: MIT


"""This is the official documentation for the avro.py Python package.

Overview:
---------

avro.py provides a fully fledged, batteries-included text parser which can
parse, reverse and even convert English Roman script into its phonetic
equivalent (unicode) of Bengali.

Features:
---------
    1. Simple-to-use syntax with functional approach.
    2. Easily convert/parse/reverse English Roman script to Bengali phonetic and vice versa.
    3. Fully asynchronous and `async`/`await` sugarcoated syntax compliant.
    4. Synchronous alternative functions available for applications requiring minimal overhead.
    5. Batteries included. Just write your text and let it do the rest.

Examples:
---------

Please refer to the following link to view the examples:
https://github.com/hitblast/avro.py/tree/main/examples

"""

# Import local modules.
from .main import *

# Version information.
__version_info__ = (2024, 12, 9)
__version__ = ".".join(map(str, __version_info__))
