# SPDX-License-Identifier: MIT


# Import local modules.
from .resources import DICT

# Shortcuts to vowels, constants, case-sensitives and numbers.
AVRO_VOWELS = set(DICT['avro']['vowel'])
AVRO_CONSONANTS = set(DICT['avro']['consonant'])
AVRO_CASESENSITIVES = set(DICT['avro']['casesensitive'])
AVRO_NUMBERS = set(DICT['avro']['number'])

# Shortcuts to Bengali Svaravarna, Kar(s)
AVRO_SHORBORNO = set(DICT['avro']['shorborno'])
AVRO_KAR = DICT['avro']['kar']
AVRO_IGNORE = DICT['avro']['ignore']
AVRO_EXCEPTIONS = DICT['avro']['exceptions']

# Shortcuts for conversion (e.g. for Bijoy Keyboard support).
BIJOY_MAP = DICT['bijoy']['mappings']
