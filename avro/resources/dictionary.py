# SPDX-License-Identifier: MIT


# Import first-party Python modules.
from typing import Any

# The Avro Dictionary, implemented in Python.
DICT: dict[str, Any] = {
    # Metadata.
    "meta": {
        "file_name": "dictionary.py",
        "file_description": "Provides Avro Dictionary in native Python.",
        "package": "avro.py",
        "license": "MIT License",
        "source": "https://github.com/hitblast/avro.py/blob/main/avro/resources/dictionary.py",
        "adapted_by": "HitBlast",
        "encoding": "utf-8",
    },
    # Avro Keyboard mappings.
    "avro": {
        "patterns": [
            {"find": "bhl", "replace": "ভ্ল"},
            {"find": "psh", "replace": "পশ"},
            {"find": "bdh", "replace": "ব্ধ", "reverse": "bdh"},
            {"find": "bj", "replace": "ব্জ", "reverse": "bj"},
            {"find": "bd", "replace": "ব্দ", "reverse": "bd"},
            {"find": "bb", "replace": "ব্ব", "reverse": "bb"},
            {"find": "bl", "replace": "ব্ল", "reverse": "bl"},
            {"find": "bh", "replace": "ভ", "reverse": "bh"},
            {"find": "vl", "replace": "ভ্ল", "reverse": "vl"},
            {"find": "b", "replace": "ব", "reverse": "b"},
            {"find": "v", "replace": "ভ", "reverse": "bh"},
            {"find": "cNG", "replace": "চ্ঞ", "reverse": "cng"},
            {"find": "cch", "replace": "চ্ছ", "reverse": "cch"},
            {"find": "cc", "replace": "চ্চ", "reverse": "cc"},
            {"find": "ch", "replace": "ছ"},
            {"find": "c", "replace": "চ", "reverse": "ch"},
            {"find": "dhn", "replace": "ধ্ন", "reverse": "dhn"},
            {"find": "dhm", "replace": "ধ্ম", "reverse": "dhm"},
            {"find": "dgh", "replace": "দ্ঘ", "reverse": "dgh"},
            {"find": "ddh", "replace": "দ্ধ", "reverse": "ddh"},
            {"find": "dbh", "replace": "দ্ভ", "reverse": "dv"},
            {"find": "dv", "replace": "দ্ভ", "reverse": "dv"},
            {"find": "dm", "replace": "দ্ম", "reverse": "dd"},
            {"find": "DD", "replace": "ড্ড", "reverse": "dd"},
            {"find": "Dh", "replace": "ঢ", "reverse": "dh"},
            {"find": "dh", "replace": "ধ", "reverse": "dh"},
            {"find": "dg", "replace": "দ্গ"},
            {"find": "dd", "replace": "দ্দ", "reverse": "dd"},
            {"find": "D", "replace": "ড", "reverse": "d"},
            {"find": "d", "replace": "দ", "reverse": "d"},
            {"find": "...", "replace": "..."},
            {"find": ".`", "replace": ".", "reverse": "."},
            {"find": "..", "replace": "।।"},
            {"find": ".", "replace": "।", "reverse": "."},
            {"find": "ghn", "replace": "ঘ্ন", "reverse": "ghn"},
            {"find": "Ghn", "replace": "ঘ্ন", "reverse": "ghn"},
            {"find": "gdh", "replace": "গ্ধ", "reverse": "gdh"},
            {"find": "Gdh", "replace": "গ্ধ", "reverse": "gdh"},
            {"find": "gN", "replace": "গ্ণ", "reverse": "gn"},
            {"find": "GN", "replace": "গ্ণ", "reverse": "gn"},
            {"find": "gn", "replace": "গ্ন", "reverse": "gn"},
            {"find": "Gn", "replace": "গ্ন", "reverse": "gn"},
            {"find": "gm", "replace": "গ্ম"},
            {"find": "Gm", "replace": "গ্ম", "reverse": "gm"},
            {"find": "gl", "replace": "গ্ল", "reverse": "gl"},
            {"find": "Gl", "replace": "গ্ল", "reverse": "gl"},
            {"find": "gg", "replace": "জ্ঞ", "reverse": "gg"},
            {"find": "GG", "replace": "জ্ঞ", "reverse": "gg"},
            {"find": "Gg", "replace": "জ্ঞ", "reverse": "gg"},
            {"find": "gG", "replace": "জ্ঞ", "reverse": "gg"},
            {"find": "gh", "replace": "ঘ", "reverse": "gh"},
            {"find": "Gh", "replace": "ঘ", "reverse": "gh"},
            {"find": "g", "replace": "গ", "reverse": "g"},
            {"find": "G", "replace": "গ", "reverse": "g"},
            {"find": "hN", "replace": "হ্ণ", "reverse": "nn"},
            {"find": "hn", "replace": "হ্ন", "reverse": "nn"},
            {"find": "hm", "replace": "হ্ম", "reverse": "mm"},
            {"find": "hl", "replace": "হ্ল"},
            {"find": "h", "replace": "হ", "reverse": "h"},
            {"find": "jjh", "replace": "জ্ঝ"},
            {"find": "jNG", "replace": "জ্ঞ", "reverse": "gg"},
            {"find": "jh", "replace": "ঝ", "reverse": "jh"},
            {"find": "jj", "replace": "জ্জ", "reverse": "jj"},
            {"find": "j", "replace": "জ", "reverse": "j"},
            {"find": "J", "replace": "জ", "reverse": "j"},
            {"find": "kkhN", "replace": "ক্ষ্ণ", "reverse": "kkhn"},
            {"find": "kShN", "replace": "ক্ষ্ণ", "reverse": "kkhn"},
            {"find": "kkhm", "replace": "ক্ষ্ম"},
            {"find": "kShm", "replace": "ক্ষ্ম", "reverse": "kkh"},
            {"find": "kxN", "replace": "ক্ষ্ণ", "reverse": "kkh"},
            {"find": "kxm", "replace": "ক্ষ্ম", "reverse": "kkh"},
            {"find": "kkh", "replace": "ক্ষ", "reverse": "kkh"},
            {"find": "kSh", "replace": "ক্ষ", "reverse": "kkh"},
            {"find": "ksh", "replace": "কশ"},
            {"find": "kx", "replace": "ক্ষ", "reverse": "kkh"},
            {"find": "kk", "replace": "ক্ক", "reverse": "kk"},
            {"find": "kT", "replace": "ক্ট", "reverse": "kt"},
            {"find": "kt", "replace": "ক্ত", "reverse": "kt"},
            {"find": "kl", "replace": "ক্ল", "reverse": "kl"},
            {"find": "ks", "replace": "ক্স", "reverse": "ks"},
            {"find": "kh", "replace": "খ", "reverse": "kh"},
            {"find": "k", "replace": "ক", "reverse": "k"},
            {"find": "lbh", "replace": "ল্ভ"},
            {"find": "ldh", "replace": "ল্ধ"},
            {"find": "lkh", "replace": "লখ"},
            {"find": "lgh", "replace": "লঘ"},
            {"find": "lph", "replace": "লফ"},
            {"find": "lk", "replace": "ল্ক", "reverse": "lk"},
            {"find": "lg", "replace": "ল্গ"},
            {"find": "lT", "replace": "ল্ট", "reverse": "lt"},
            {"find": "lD", "replace": "ল্ড", "reverse": "ld"},
            {"find": "lp", "replace": "ল্প", "reverse": "lp"},
            {"find": "lv", "replace": "ল্ভ"},
            {"find": "lm", "replace": "ল্ম", "reverse": "lm"},
            {"find": "ll", "replace": "ল্ল", "reverse": "ll"},
            {"find": "lb", "replace": "ল্ব", "reverse": "lb"},
            {"find": "l", "replace": "ল", "reverse": "l"},
            {"find": "mth", "replace": "ম্থ"},
            {"find": "mph", "replace": "ম্ফ", "reverse": "mf"},
            {"find": "mbh", "replace": "ম্ভ", "reverse": "mv"},
            {"find": "mpl", "replace": "মপ্ল"},
            {"find": "mn", "replace": "ম্ন", "reverse": "mn"},
            {"find": "mp", "replace": "ম্প", "reverse": "mp"},
            {"find": "mv", "replace": "ম্ভ", "reverse": "mv"},
            {"find": "mm", "replace": "ম্ম", "reverse": "mm"},
            {"find": "ml", "replace": "ম্ল", "reverse": "ml"},
            {"find": "mb", "replace": "ম্ব", "reverse": "mb"},
            {"find": "mf", "replace": "ম্ফ", "reverse": "mf"},
            {"find": "m", "replace": "ম", "reverse": "m"},
            {"find": "0", "replace": "০", "reverse": "0"},
            {"find": "1", "replace": "১", "reverse": "1"},
            {"find": "2", "replace": "২", "reverse": "2"},
            {"find": "3", "replace": "৩", "reverse": "3"},
            {"find": "4", "replace": "৪", "reverse": "4"},
            {"find": "5", "replace": "৫", "reverse": "5"},
            {"find": "6", "replace": "৬", "reverse": "6"},
            {"find": "7", "replace": "৭", "reverse": "7"},
            {"find": "8", "replace": "৮", "reverse": "8"},
            {"find": "9", "replace": "৯", "reverse": "9"},
            {"find": "NgkSh", "replace": "ঙ্ক্ষ", "reverse": "ngkh"},
            {"find": "Ngkkh", "replace": "ঙ্ক্ষ", "reverse": "ngkh"},
            {"find": "NGch", "replace": "ঞ্ছ", "reverse": "ngch"},
            {"find": "Nggh", "replace": "ঙ্ঘ"},
            {"find": "Ngkh", "replace": "ঙ্খ", "reverse": "ngkh"},
            {"find": "NGjh", "replace": "ঞ্ঝ"},
            {"find": "ngOU", "replace": "ঙ্গৌ"},
            {"find": "ngOI", "replace": "ঙ্গৈ"},
            {"find": "Ngkx", "replace": "ঙ্ক্ষ", "reverse": "ngkh"},
            {"find": "NGc", "replace": "ঞ্চ", "reverse": "nch"},
            {"find": "nch", "replace": "ঞ্ছ", "reverse": "ngch"},
            {"find": "njh", "replace": "ঞ্ঝ"},
            {"find": "ngh", "replace": "ঙ্ঘ"},
            {"find": "Ngk", "replace": "ঙ্ক", "reverse": "ngk"},
            {"find": "Ngx", "replace": "ঙ্ষ"},
            {"find": "Ngg", "replace": "ঙ্গ", "reverse": "ngg"},
            {"find": "Ngm", "replace": "ঙ্ম"},
            {"find": "NGj", "replace": "ঞ্জ", "reverse": "ngj"},
            {"find": "ndh", "replace": "ন্ধ", "reverse": "ndh"},
            {"find": "nTh", "replace": "ন্ঠ", "reverse": "nth"},
            {"find": "NTh", "replace": "ণ্ঠ", "reverse": "nth"},
            {"find": "nth", "replace": "ন্থ", "reverse": "nth"},
            {"find": "nkh", "replace": "ঙ্খ", "reverse": "ngkh"},
            {"find": "ngo", "replace": "ঙ্গ", "reverse": "ngg"},
            {"find": "nga", "replace": "ঙ্গা"},
            {"find": "ngi", "replace": "ঙ্গি"},
            {"find": "ngI", "replace": "ঙ্গী"},
            {"find": "ngu", "replace": "ঙ্গু"},
            {"find": "ngU", "replace": "ঙ্গূ"},
            {"find": "nge", "replace": "ঙ্গে"},
            {"find": "ngO", "replace": "ঙ্গো"},
            {"find": "NDh", "replace": "ণ্ঢ"},
            {"find": "nsh", "replace": "নশ"},
            {"find": "Ngr", "replace": "ঙর"},
            {"find": "NGr", "replace": "ঞর"},
            {"find": "ngr", "replace": "ংর"},
            {"find": "nj", "replace": "ঞ্জ", "reverse": "ngj"},
            {"find": "Ng", "replace": "ঙ", "reverse": "ng"},
            {"find": "NG", "replace": "ঞ", "reverse": "y"},
            {"find": "nk", "replace": "ঙ্ক", "reverse": "ngk"},
            {"find": "ng", "replace": "ং", "reverse": "ng"},
            {"find": "nn", "replace": "ন্ন", "reverse": "nn"},
            {"find": "NN", "replace": "ণ্ণ"},
            {"find": "Nn", "replace": "ণ্ন"},
            {"find": "nm", "replace": "ন্ম", "reverse": "nm"},
            {"find": "Nm", "replace": "ণ্ম"},
            {"find": "nd", "replace": "ন্দ", "reverse": "nd"},
            {"find": "nT", "replace": "ন্ট", "reverse": "nt"},
            {"find": "NT", "replace": "ণ্ট", "reverse": "nt"},
            {"find": "nD", "replace": "ন্ড", "reverse": "nd"},
            {"find": "ND", "replace": "ণ্ড", "reverse": "nd"},
            {"find": "nt", "replace": "ন্ত", "reverse": "nt"},
            {"find": "ns", "replace": "ন্স"},
            {"find": "nc", "replace": "ঞ্চ", "reverse": "nch"},
            {"find": "n", "replace": "ন", "reverse": "n"},
            {"find": "N", "replace": "ণ", "reverse": "n"},
            {"find": "OI`", "replace": "ৈ", "reverse": "oi"},
            {"find": "OU`", "replace": "ৌ", "reverse": "ou"},
            {"find": "O`", "replace": "ো", "reverse": "o"},
            {
                "find": "OI",
                "replace": "ৈ",
                "rules": [
                    {"matches": [{"type": "prefix", "scope": "!consonant"}], "replace": "ঐ"},
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "ঐ"},
                ],
                "reverse": "oi",
            },
            {
                "find": "OU",
                "replace": "ৌ",
                "rules": [
                    {"matches": [{"type": "prefix", "scope": "!consonant"}], "replace": "ঔ"},
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "ঔ"},
                ],
                "reverse": "ou",
            },
            {
                "find": "O",
                "replace": "ো",
                "rules": [
                    {"matches": [{"type": "prefix", "scope": "!consonant"}], "replace": "ও"},
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "ও"},
                ],
                "reverse": "o",
            },
            {"find": "phl", "replace": "ফ্ল", "reverse": "fl"},
            {"find": "pT", "replace": "প্ট", "reverse": "pt"},
            {"find": "pt", "replace": "প্ত", "reverse": "pt"},
            {"find": "pn", "replace": "প্ন", "reverse": "pn"},
            {"find": "pp", "replace": "প্প", "reverse": "pp"},
            {"find": "pl", "replace": "প্ল", "reverse": "pl"},
            {"find": "ps", "replace": "প্স", "reverse": "ps"},
            {"find": "ph", "replace": "ফ", "reverse": "ph"},
            {"find": "fl", "replace": "ফ্ল", "reverse": "fl"},
            {"find": "f", "replace": "ফ", "reverse": "ph"},
            {"find": "p", "replace": "প", "reverse": "p"},
            {"find": "rri`", "replace": "ৃ", "reverse": "ri"},
            {
                "find": "rri",
                "replace": "ৃ",
                "rules": [
                    {"matches": [{"type": "prefix", "scope": "!consonant"}], "replace": "ঋ"},
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "ঋ"},
                ],
                "reverse": "ri",
            },
            {"find": "rrZ", "replace": "রর‍্য"},
            {"find": "rry", "replace": "রর‍্য"},
            {
                "find": "rZ",
                "replace": "র‍্য",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "consonant"},
                            {"type": "prefix", "scope": "!exact", "value": "r"},
                            {"type": "prefix", "scope": "!exact", "value": "y"},
                            {"type": "prefix", "scope": "!exact", "value": "w"},
                            {"type": "prefix", "scope": "!exact", "value": "x"},
                        ],
                        "replace": "্র্য",
                    }
                ],
            },
            {
                "find": "ry",
                "replace": "র‍্য",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "consonant"},
                            {"type": "prefix", "scope": "!exact", "value": "r"},
                            {"type": "prefix", "scope": "!exact", "value": "y"},
                            {"type": "prefix", "scope": "!exact", "value": "w"},
                            {"type": "prefix", "scope": "!exact", "value": "x"},
                        ],
                        "replace": "্র্য",
                    }
                ],
            },
            {
                "find": "rr",
                "replace": "রর",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!vowel"},
                            {"type": "suffix", "scope": "!exact", "value": "r"},
                            {"type": "suffix", "scope": "!punctuation"},
                        ],
                        "replace": "র্",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "consonant"},
                            {"type": "prefix", "scope": "!exact", "value": "r"},
                        ],
                        "replace": "্রর",
                    },
                ],
            },
            {"find": "Rg", "replace": "ড়্গ"},
            {"find": "Rh", "replace": "ঢ়"},
            {"find": "R", "replace": "ড়", "reverse": "r"},
            {
                "find": "r",
                "replace": "র",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "consonant"},
                            {"type": "prefix", "scope": "!exact", "value": "r"},
                            {"type": "prefix", "scope": "!exact", "value": "y"},
                            {"type": "prefix", "scope": "!exact", "value": "w"},
                            {"type": "prefix", "scope": "!exact", "value": "x"},
                            {"type": "prefix", "scope": "!exact", "value": "Z"},
                        ],
                        "replace": "্র",
                    }
                ],
            },
            {"find": "shch", "replace": "শ্ছ", "reverse": "sch"},
            {"find": "ShTh", "replace": "ষ্ঠ", "reverse": "sth"},
            {"find": "Shph", "replace": "ষ্ফ", "reverse": "sf"},
            {"find": "Sch", "replace": "শ্ছ", "reverse": "sch"},
            {"find": "skl", "replace": "স্ক্ল"},
            {"find": "skh", "replace": "স্খ"},
            {"find": "sth", "replace": "স্থ", "reverse": "sth"},
            {"find": "sph", "replace": "স্ফ", "reverse": "sf"},
            {"find": "shc", "replace": "শ্চ", "reverse": "scch"},
            {"find": "sht", "replace": "শ্ত"},
            {"find": "shn", "replace": "শ্ন", "reverse": "sn"},
            {"find": "shm", "replace": "শ্ম", "reverse": "ss"},
            {"find": "shl", "replace": "শ্ল", "reverse": "sl"},
            {"find": "Shk", "replace": "ষ্ক", "reverse": "sk"},
            {"find": "ShT", "replace": "ষ্ট", "reverse": "st"},
            {"find": "ShN", "replace": "ষ্ণ", "reverse": "sn"},
            {"find": "Shp", "replace": "ষ্প", "reverse": "sp"},
            {"find": "Shf", "replace": "ষ্ফ", "reverse": "sf"},
            {"find": "Shm", "replace": "ষ্ম", "reverse": "sm"},
            {"find": "spl", "replace": "স্প্ল"},
            {"find": "sk", "replace": "স্ক", "reverse": "sk"},
            {"find": "Sc", "replace": "শ্চ", "reverse": "scch"},
            {"find": "sT", "replace": "স্ট", "reverse": "st"},
            {"find": "st", "replace": "স্ত", "reverse": "st"},
            {"find": "sn", "replace": "স্ন", "reverse": "sn"},
            {"find": "sp", "replace": "স্প", "reverse": "sp"},
            {"find": "sf", "replace": "স্ফ", "reverse": "sf"},
            {"find": "sm", "replace": "স্ম", "reverse": "sh"},
            {"find": "sl", "replace": "স্ল", "reverse": "sl"},
            {"find": "sh", "replace": "শ", "reverse": "sh"},
            {"find": "Sc", "replace": "শ্চ", "reverse": "scch"},
            {"find": "St", "replace": "শ্ত"},
            {"find": "Sn", "replace": "শ্ন", "reverse": "sn"},
            {"find": "Sm", "replace": "শ্ম", "reverse": "ss"},
            {"find": "Sl", "replace": "শ্ল", "reverse": "sl"},
            {"find": "Sh", "replace": "ষ", "reverse": "sh"},
            {"find": "s", "replace": "স", "reverse": "s"},
            {"find": "S", "replace": "শ", "reverse": "sh"},
            {"find": "oo`", "replace": "ু", "reverse": "u"},
            {
                "find": "oo",
                "replace": "ু",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "উ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "উ",
                    },
                ],
                "reverse": "u",
            },
            # {
            #     "find": "o`"
            #     "replace": ""
            # },
            {"find": "oZ", "replace": "অ্য"},
            {
                "find": "o",
                "replace": "",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "vowel"},
                            {"type": "prefix", "scope": "!exact", "value": "o"},
                        ],
                        "replace": "ও",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "vowel"},
                            {"type": "prefix", "scope": "exact", "value": "o"},
                        ],
                        "replace": "অ",
                    },
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "অ"},
                ],
            },
            {"find": "tth", "replace": "ত্থ"},
            {"find": "t``", "replace": "ৎ", "reverse": "t"},
            {"find": "TT", "replace": "ট্ট", "reverse": "tt"},
            {"find": "Tm", "replace": "ট্ম"},
            {"find": "Th", "replace": "ঠ", "reverse": "th"},
            {"find": "tn", "replace": "ত্ন"},
            {"find": "tm", "replace": "ত্ম", "reverse": "tt"},
            {"find": "th", "replace": "থ", "reverse": "th"},
            {"find": "tt", "replace": "ত্ত", "reverse": "tt"},
            {"find": "T", "replace": "ট", "reverse": "t"},
            {"find": "t", "replace": "ত", "reverse": "t"},
            {"find": "aZ", "replace": "অ্যা"},
            {"find": "AZ", "replace": "অ্যা"},
            {"find": "a`", "replace": "া", "reverse": "a"},
            {"find": "A`", "replace": "া", "reverse": "a"},
            {"replace": "আ", "reverse": "a"},
            {"replace": "র", "reverse": "r"},
            {
                "find": "a",
                "replace": "া",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "আ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "prefix", "scope": "!exact", "value": "a"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "য়া",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "exact", "value": "a"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "আ",
                    },
                ],
                "reverse": "a",
            },
            {"find": "i`", "replace": "ি", "reverse": "i"},
            {"replace": "ই", "reverse": "i"},
            {
                "find": "i",
                "replace": "ি",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ই",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ই",
                    },
                ],
            },
            {"find": "I`", "replace": "ী", "reverse": "i"},
            {
                "find": "I",
                "replace": "ী",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঈ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঈ",
                    },
                ],
                "reverse": "i",
            },
            {"find": "u`", "replace": "ু", "reverse": "u"},
            {"replace": "উ", "reverse": "u"},
            {
                "find": "u",
                "replace": "ু",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "উ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "উ",
                    },
                ],
                "reverse": "u",
            },
            {"find": "U`", "replace": "ূ", "reverse": "u"},
            {
                "find": "U",
                "replace": "ূ",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঊ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঊ",
                    },
                ],
                "reverse": "u",
            },
            {"find": "ee`", "replace": "ী", "reverse": "i"},
            {
                "find": "ee",
                "replace": "ী",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঈ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "ঈ",
                    },
                ],
                "reverse": "i",
            },
            {"find": "e`", "replace": "ে", "reverse": "e"},
            {"replace": "এ", "reverse": "e"},
            {"replace": "ও", "reverse": "w"},
            {
                "find": "e",
                "replace": "ে",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "এ",
                    },
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "!exact", "value": "`"},
                        ],
                        "replace": "এ",
                    },
                ],
                "reverse": "e",
            },
            {"find": "z", "replace": "য", "reverse": "z"},
            {"find": "Z", "replace": "্য"},
            {
                "find": "y",
                "replace": "্য",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "!consonant"},
                            {"type": "prefix", "scope": "!punctuation"},
                        ],
                        "replace": "য়",
                    },
                    {"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "ইয়"},
                ],
            },
            {"find": "Y", "replace": "য়", "reverse": "y"},
            {"find": "q", "replace": "ক", "reverse": "k"},
            {
                "find": "w",
                "replace": "ও",
                "rules": [
                    {
                        "matches": [
                            {"type": "prefix", "scope": "punctuation"},
                            {"type": "suffix", "scope": "vowel"},
                        ],
                        "replace": "ওয়",
                    },
                    {"matches": [{"type": "prefix", "scope": "consonant"}], "replace": "্ব"},
                ],
                "reverse": "o",
            },
            {
                "find": "x",
                "replace": "ক্স",
                "rules": [{"matches": [{"type": "prefix", "scope": "punctuation"}], "replace": "এক্স"}],
                "reverse": "ks",
            },
            {"find": ":`", "replace": ":"},
            {"find": ":", "replace": "ঃ"},
            {"find": "^`", "replace": "^"},
            {"find": "^", "replace": "ঁ", "reverse": ""},
            {"find": ",,", "replace": "্‌"},
            {"find": ",", "replace": ","},
            {"find": "$", "replace": "৳"},
            # {
            #     "find": "`",
            #     "replace": ""
            # }
        ],
        # Remapped words.
        "exceptions": {
            "বাংলাদেশ": "Bangladesh",
            "ইউএসএ": "USA",
            "ইউরোপ": "Europe",
            "আস্ট্রেলিয়া": "Australia",
            "ফেসবুক": "Facebook",
            "গুগল": "Google",
            "উইকিপিডিয়া": "Wikipedia",
            "হোয়াটসঅ্যাপ": "Whatsapp",
            "টুইটার": "Twitter",
            "লিঙ্কডইন": "Linkedin",
            "ইনস্টাগ্রাম": "Instagram",
            "ইউটিউব": "YouTube",
            "আইএমডিবি": "IMDb",
            "অ্যামাজন": "Amazon",
            "মাইক্রোসফট": "Microsoft",
            "অ্যাপল": "Apple",
            "ইউনিভার্সিটি": "University",
            "কম্পিউটার": "Computer",
            "কোম্পানি": "Company",
            "কর্পোরেশন": "Corporation",
            "করোনাভাইরাস": "Coronavirus",
            "আইবিএম": "IBM",
            "ইমেইল": "Email",
            "এসএমএস": "SMS",
        },
        # Constant values.
        "vowel": "aeiou",
        "consonant": "bcdfghjklmnpqrstvwxyz",
        "casesensitive": "oiudgjnrstyz",
        "number": "0123456789",
        # For reverse parsing.
        "shorborno": "অআইঈউঊএঐওঔ",
        "kar": ["া", "ি", "ী", "ৗ", "ু", "ূ", "ৃ", "ে", "ৈ", "ো", "ৌ"],
        # Ignored symbols.
        "ignore": ["ঁ", "।", "?", ".", "-", ";"],
    },
    # Bijoy Keyboard mappings.
    "bijoy": {
        "mappings": {
            "।": "|",
            "‘": "Ô",
            "’": "Õ",
            "“": "Ò",
            "”": "Ó",
            "্র্য": "ª¨",
            "র‌্য": "i¨",
            "ক্ক": "°",
            "ক্ট": "±",
            "ক্ত": "³",
            "ক্ব": "K¡",
            "স্ক্র": "¯Œ",
            "ক্র": "µ",
            "ক্ল": "K¬",
            "ক্ষ": "¶",
            "ক্স": "·",
            "গু": "¸",
            "গ্ধ": "»",
            "গ্ন": "Mœ",
            "গ্ম": "M¥",
            "গ্ল": "M­",
            "গ্রু": "Mªy",
            "ঙ্ক": "¼",
            "ঙ্ক্ষ": "•¶",
            "ঙ্খ": "•L",
            "ঙ্গ": "½",
            "ঙ্ঘ": "•N",
            "চ্চ": "”P",
            "চ্ছ": "”Q",
            "চ্ছ্ব": "”Q¡",
            "চ্ঞ": "”T",
            "জ্জ্ব": "¾¡",
            "জ্জ": "¾",
            "জ্ঝ": "À",
            "জ্ঞ": "Á",
            "জ্ব": "R¡",
            "ঞ্চ": "Â",
            "ঞ্ছ": "Ã",
            "ঞ্জ": "Ä",
            "ঞ্ঝ": "Å",
            "ট্ট": "Æ",
            "ট্ব": "U¡",
            "ট্ম": "U¥",
            "ড্ড": "Ç",
            "ণ্ট": "È",
            "ণ্ঠ": "É",
            "ন্স": "Ý",
            "ণ্ড": "Ê",
            "ন্তু": "š‘",
            "ণ্ব": "Y^",
            "ত্ত": "Ë",
            "ত্ত্ব": "Ë¡",
            "ত্থ": "Ì",
            "ত্ন": "Zœ",
            "ত্ম": "Z¥",
            "ন্ত্ব": "š—¡",
            "ত্ব": "Z¡",
            "থ্ব": "_¡",
            "দ্গ": "˜M",
            "দ্ঘ": "˜N",
            "দ্দ": "Ï",
            "দ্ধ": "×",
            "দ্ব": "˜¡",
            "দ্ব": "Ø",
            "দ্ভ": "™¢",
            "দ্ম": "Ù",
            "দ্রু": "`ª“",
            "ধ্ব": "aŸ",
            "ধ্ম": "a¥",
            "ন্ট": "›U",
            "ন্ঠ": "Ú",
            "ন্ড": "Û",
            "ন্ত্র": "š¿",
            "ন্ত": "š—",
            "স্ত্র": "¯¿",
            "ত্র": "Î",
            "ন্থ": "š’",
            "ন্দ": "›`",
            "ন্দ্ব": "›Ø",
            "ন্ধ": "Ü",
            "ন্ন": "bœ",
            "ন্ব": "š^",
            "ন্ম": "b¥",
            "প্ট": "Þ",
            "প্ত": "ß",
            "প্ন": "cœ",
            "প্প": "à",
            "প্ল": "c­",
            "প্স": "á",
            "ফ্ল": "d¬",
            "ব্জ": "â",
            "ব্দ": "ã",
            "ব্ধ": "ä",
            "ব্ব": "eŸ",
            "ব্ল": "e­",
            "ভ্র": "å",
            "ম্ন": "gœ",
            "ম্প": "¤ú",
            "ম্ফ": "ç",
            "ম্ব": "¤^",
            "ম্ভ": "¤¢",
            "ম্ভ্র": "¤£",
            "ম্ম": "¤§",
            "ম্ল": "¤­",
            "রু": "i“",
            "রূ": "iƒ",
            "ল্ক": "é",
            "ল্গ": "ê",
            "ল্প": "í",
            "ল্ট": "ë",
            "ল্ড": "ì",
            "ল্ফ": "î",
            "ল্ব": "j¦",
            "ল্ম": "j¥",
            "ল্ল": "jø",
            "শু": "ï",
            "শ্চ": "ð",
            "শ্ন": "kœ",
            "শ্ব": "k¦",
            "শ্ম": "k¥",
            "শ্ল": "kø",
            "ষ্ক": "®‹",
            "ষ্ক্র": "®Œ",
            "ষ্ট": "ó",
            "ষ্ঠ": "ô",
            "ষ্ণ": "ò",
            "ষ্প": "®ú",
            "ষ্ফ": "õ",
            "ষ্ম": "®§",
            "স্ক": "¯‹",
            "স্ট": "÷",
            "স্খ": "ö",
            "স্ত": "¯—",
            "স্তু": "¯‘",
            "স্থ": "¯’",
            "স্ন": "mœ",
            "স্প": "¯ú",
            "স্ফ": "ù",
            "স্ব": "¯^",
            "স্ম": "¯§",
            "স্ল": "¯­",
            "হু": "û",
            "হ্ণ": "nè",
            "হ্ন": "ý",
            "হ্ম": "þ",
            "হ্ল": "n¬",
            "হৃ": "ü",
            "র্": "©",
            "্র": "«",
            "্য": "¨",
            "্": "&",
            "আ": "Av",
            "অ": "A",
            "ই": "B",
            "ঈ": "C",
            "উ": "D",
            "ঊ": "E",
            "ঋ": "F",
            "এ": "G",
            "ঐ": "H",
            "ও": "I",
            "ঔ": "J",
            "ক": "K",
            "খ": "L",
            "গ": "M",
            "ঘ": "N",
            "ঙ": "O",
            "চ": "P",
            "ছ": "Q",
            "জ": "R",
            "ঝ": "S",
            "ঞ": "T",
            "ট": "U",
            "ঠ": "V",
            "ড": "W",
            "ঢ": "X",
            "ণ": "Y",
            "ত": "Z",
            "থ": "_",
            "দ": "`",
            "ধ": "a",
            "ন": "b",
            "প": "c",
            "ফ": "d",
            "ব": "e",
            "ভ": "f",
            "ম": "g",
            "য": "h",
            "র": "i",
            "ল": "j",
            "শ": "k",
            "ষ": "l",
            "স": "m",
            "হ": "n",
            "ড়": "o",
            "ঢ়": "p",
            "য়": "q",
            "ৎ": "r",
            "০": "0",
            "১": "1",
            "২": "2",
            "৩": "3",
            "৪": "4",
            "৫": "5",
            "৬": "6",
            "৭": "7",
            "৮": "8",
            "৯": "9",
            "া": "v",
            "ি": "w",
            "ী": "x",
            "ু": "y",
            "ূ": "~",
            "ৃ": "…",
            "ে": "‡",
            "ৈ": "‰",
            "ৗ": "Š",
            "ং": "s",
            "ঃ": "t",
            "ঁ": "u",
        },
        "prekar": ["ি", "ৈ", "ে"],
        "postkar": ["া", "ো", "ৌ", "ৗ", "ু", "ূ", "ী", "ৃ"],
        "banjonborno": "কখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমশষসহযরলয়ংঃঁৎ",
        "exceptions": {
            "halant": "্",
            "nukta": ["ং", "ঃ", "ঁ"],
        },
    },
}
