# SPDX-License-Identifier: MIT


# Import local modules.
from .resources import AVRO_DICT

# Shortcuts to vowels, constants, case-sensitives and numbers.
AVRO_VOWELS = set(AVRO_DICT['data']['vowel'])
AVRO_CONSONANTS = set(AVRO_DICT['data']['consonant'])
AVRO_CASESENSITIVES = set(AVRO_DICT['data']['casesensitive'])
AVRO_NUMBERS = set(AVRO_DICT['data']['number'])

# Shortcuts to Bengali Svaravarna, Kar(s)
AVRO_SHORBORNO = set(AVRO_DICT['data']['shorborno'])
AVRO_KAR = AVRO_DICT['data']['kar']
AVRO_IGNORE = AVRO_DICT['data']['ignore']
EXCEPTIONS = AVRO_DICT['data']['exceptions']
