'''

## The Avro Dictionary (Adapted)

---

MIT License

Copyright (c) 2022 HitBlast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


# Imports.
from typing import Dict


# The dictionary variable.
AVRO_DICT: Dict[str, str] = {
    "meta": {
        "file_name": "avrodict.py",
        "file_description": "Provides Avro Dictionary in native Python dictionary. Adapted from avrodict.json",
        "package": "avro.py",
        "license": "MIT License",
        "source": "https://github.com/kaustavdm/pyAvroPhonetic/blob/master/pyavrophonetic/resources/avrodict.json",
        "adapted_by": "HitBlast",
        "updated": "20230403",
        "encoding": "utf-8"
    },
    "data": {
        "patterns": [
            {
                "find": "bhl",
                "replace": "ভ্ল"
            },
            {
                "find": "psh",
                "replace": "পশ"
            },
            {
                "find": "bdh",
                "replace": "ব্ধ"
            },
            {
                "find": "bj",
                "replace": "ব্জ"
            },
            {
                "find": "bd",
                "replace": "ব্দ"
            },
            {
                "find": "bb",
                "replace": "ব্ব"
            },
            {
                "find": "bl",
                "replace": "ব্ল"
            },
            {
                "find": "bh",
                "replace": "ভ"
            },
            {
                "find": "vl",
                "replace": "ভ্ল"
            },
            {
                "find": "b",
                "replace": "ব"
            },
            {
                "find": "v",
                "replace": "ভ",
                "reverse": "bh"
            },
            {
                "find": "cNG",
                "replace": "চ্ঞ",
                "reverse": "cng"
            },
            {
                "find": "cch",
                "replace": "চ্ছ"
            },
            {
                "find": "cc",
                "replace": "চ্চ"
            },
            {
                "find": "ch",
                "replace": "ছ"
            },
            {
                "find": "c",
                "replace": "চ",
                "reverse": "ch"
            },
            {
                "find": "dhn",
                "replace": "ধ্ন"
            },
            {
                "find": "dhm",
                "replace": "ধ্ম"
            },
            {
                "find": "dgh",
                "replace": "দ্ঘ"
            },
            {
                "find": "ddh",
                "replace": "দ্ধ"
            },
            {
                "find": "dbh",
                "replace": "দ্ভ"
            },
            {
                "find": "dv",
                "replace": "দ্ভ"
            },
            {
                "find": "dm",
                "replace": "দ্ম",
                "reverse": "dd"
            },
            {
                "find": "DD",
                "replace": "ড্ড",
                "reverse": "dd"
            },
            {
                "find": "Dh",
                "replace": "ঢ",
                "reverse": "dh"
            },
            {
                "find": "dh",
                "replace": "ধ"
            },
            {
                "find": "dg",
                "replace": "দ্গ"
            },
            {
                "find": "dd",
                "replace": "দ্দ"
            },
            {
                "find": "D",
                "replace": "ড",
                "reverse": "d"
            },
            {
                "find": "d",
                "replace": "দ"
            },
            {
                "find": "...",
                "replace": "..."
            },
            {
                "find": ".`",
                "replace": ".",
                "reverse": "."
            },
            {
                "find": "..",
                "replace": "।।"
            },
            {
                "find": ".",
                "replace": "।"
            },
            {
                "find": "ghn",
                "replace": "ঘ্ন"
            },
            {
                "find": "Ghn",
                "replace": "ঘ্ন",
                "reverse": "ghn"
            },
            {
                "find": "gdh",
                "replace": "গ্ধ"
            },
            {
                "find": "Gdh",
                "replace": "গ্ধ",
                "reverse": "gdh"
            },
            {
                "find": "gN",
                "replace": "গ্ণ",
                "reverse": "gn"
            },
            {
                "find": "GN",
                "replace": "গ্ণ",
                "reverse": "gn"
            },
            {
                "find": "gn",
                "replace": "গ্ন"
            },
            {
                "find": "Gn",
                "replace": "গ্ন",
                "reverse": "gn"
            },
            {
                "find": "gm",
                "replace": "গ্ম"
            },
            {
                "find": "Gm",
                "replace": "গ্ম",
                "reverse": "gm"
            },
            {
                "find": "gl",
                "replace": "গ্ল"
            },
            {
                "find": "Gl",
                "replace": "গ্ল",
                "reverse": "gl"
            },
            {
                "find": "gg",
                "replace": "জ্ঞ"
            },
            {
                "find": "GG",
                "replace": "জ্ঞ",
                "reverse": "gg"
            },
            {
                "find": "Gg",
                "replace": "জ্ঞ",
                "reverse": "gg"
            },
            {
                "find": "gG",
                "replace": "জ্ঞ",
                "reverse": "gg"
            },
            {
                "find": "gh",
                "replace": "ঘ"
            },
            {
                "find": "Gh",
                "replace": "ঘ",
                "reverse": "gh"
            },
            {
                "find": "g",
                "replace": "গ"
            },
            {
                "find": "G",
                "replace": "গ",
                "reverse": "g"
            },
            {
                "find": "hN",
                "replace": "হ্ণ",
                "reverse": "nn"
            },
            {
                "find": "hn",
                "replace": "হ্ন",
                "reverse": "nn"
            },
            {
                "find": "hm",
                "replace": "হ্ম"
            },
            {
                "find": "hl",
                "replace": "হ্ল"
            },
            {
                "find": "h",
                "replace": "হ"
            },
            {
                "find": "jjh",
                "replace": "জ্ঝ"
            },
            {
                "find": "jNG",
                "replace": "জ্ঞ",
                "reverse": "gg"
            },
            {
                "find": "jh",
                "replace": "ঝ"
            },
            {
                "find": "jj",
                "replace": "জ্জ"
            },
            {
                "find": "j",
                "replace": "জ"
            },
            {
                "find": "J",
                "replace": "জ",
                "reverse": "j"
            },
            {
                "find": "kkhN",
                "replace": "ক্ষ্ণ",
                "reverse": "kkhn"
            },
            {
                "find": "kShN",
                "replace": "ক্ষ্ণ",
                "reverse": "kkhn"
            },
            {
                "find": "kkhm",
                "replace": "ক্ষ্ম"
            },
            {
                "find": "kShm",
                "replace": "ক্ষ্ম",
                "reverse": "kkh"
            },
            {
                "find": "kxN",
                "replace": "ক্ষ্ণ",
                "reverse": "kkh"
            },
            {
                "find": "kxm",
                "replace": "ক্ষ্ম",
                "reverse": "kkh"
            },
            {
                "find": "kkh",
                "replace": "ক্ষ"
            },
            {
                "find": "kSh",
                "replace": "ক্ষ",
                "reverse": "kkh"
            },
            {
                "find": "ksh",
                "replace": "কশ"
            },
            {
                "find": "kx",
                "replace": "ক্ষ",
                "reverse": "kkh"
            },
            {
                "find": "kk",
                "replace": "ক্ক"
            },
            {
                "find": "kT",
                "replace": "ক্ট",
                "reverse": "kt"
            },
            {
                "find": "kt",
                "replace": "ক্ত"
            },
            {
                "find": "kl",
                "replace": "ক্ল"
            },
            {
                "find": "ks",
                "replace": "ক্স"
            },
            {
                "find": "kh",
                "replace": "খ"
            },
            {
                "find": "k",
                "replace": "ক"
            },
            {
                "find": "lbh",
                "replace": "ল্ভ"
            },
            {
                "find": "ldh",
                "replace": "ল্ধ"
            },
            {
                "find": "lkh",
                "replace": "লখ"
            },
            {
                "find": "lgh",
                "replace": "লঘ"
            },
            {
                "find": "lph",
                "replace": "লফ"
            },
            {
                "find": "lk",
                "replace": "ল্ক"
            },
            {
                "find": "lg",
                "replace": "ল্গ"
            },
            {
                "find": "lT",
                "replace": "ল্ট",
                "reverse": "lt"
            },
            {
                "find": "lD",
                "replace": "ল্ড",
                "reverse": "ld"
            },
            {
                "find": "lp",
                "replace": "ল্প"
            },
            {
                "find": "lv",
                "replace": "ল্ভ"
            },
            {
                "find": "lm",
                "replace": "ল্ম"
            },
            {
                "find": "ll",
                "replace": "ল্ল"
            },
            {
                "find": "lb",
                "replace": "ল্ব"
            },
            {
                "find": "l",
                "replace": "ল"
            },
            {
                "find": "mth",
                "replace": "ম্থ"
            },
            {
                "find": "mph",
                "replace": "ম্ফ",
                "reverse": "mf"
            },
            {
                "find": "mbh",
                "replace": "ম্ভ"
            },
            {
                "find": "mpl",
                "replace": "মপ্ল"
            },
            {
                "find": "mn",
                "replace": "ম্ন"
            },
            {
                "find": "mp",
                "replace": "ম্প"
            },
            {
                "find": "mv",
                "replace": "ম্ভ"
            },
            {
                "find": "mm",
                "replace": "ম্ম"
            },
            {
                "find": "ml",
                "replace": "ম্ল"
            },
            {
                "find": "mb",
                "replace": "ম্ব"
            },
            {
                "find": "mf",
                "replace": "ম্ফ"
            },
            {
                "find": "m",
                "replace": "ম"
            },
            {
                "find": "0",
                "replace": "০"
            },
            {
                "find": "1",
                "replace": "১"
            },
            {
                "find": "2",
                "replace": "২"
            },
            {
                "find": "3",
                "replace": "৩"
            },
            {
                "find": "4",
                "replace": "৪"
            },
            {
                "find": "5",
                "replace": "৫"
            },
            {
                "find": "6",
                "replace": "৬"
            },
            {
                "find": "7",
                "replace": "৭"
            },
            {
                "find": "8",
                "replace": "৮"
            },
            {
                "find": "9",
                "replace": "৯"
            },
            {
                "find": "NgkSh",
                "replace": "ঙ্ক্ষ",
                "reverse": "ngkh"
            },
            {
                "find": "Ngkkh",
                "replace": "ঙ্ক্ষ",
                "reverse": "ngkh"
            },
            {
                "find": "NGch",
                "replace": "ঞ্ছ",
                "reverse": "nch"
            },
            {
                "find": "Nggh",
                "replace": "ঙ্ঘ",
                "reverse": "ngh"
            },
            {
                "find": "Ngkh",
                "replace": "ঙ্খ",
                "reverse": "ngkh"
            },
            {
                "find": "NGjh",
                "replace": "ঞ্ঝ"
            },
            {
                "find": "ngOU",
                "replace": "ঙ্গৌ"
            },
            {
                "find": "ngOI",
                "replace": "ঙ্গৈ"
            },
            {
                "find": "Ngkx",
                "replace": "ঙ্ক্ষ",
                "reverse": "ngkh"
            },
            {
                "find": "NGc",
                "replace": "ঞ্চ",
                "reverse": "nch"
            },
            {
                "find": "nch",
                "replace": "ঞ্ছ",
                "reverse": "ngch"
            },
            {
                "find": "njh",
                "replace": "ঞ্ঝ"
            },
            {
                "find": "ngh",
                "replace": "ঙ্ঘ"
            },
            {
                "find": "Ngk",
                "replace": "ঙ্ক",
                "reverse": "ngk"
            },
            {
                "find": "Ngx",
                "replace": "ঙ্ষ",
                "reverse": "nsh"
            },
            {
                "find": "Ngg",
                "replace": "ঙ্গ",
                "reverse": "ngg"
            },
            {
                "find": "Ngm",
                "replace": "ঙ্ম",
                "reverse": "ngm"
            },
            {
                "find": "NGj",
                "replace": "ঞ্জ",
                "reverse": "ngj"
            },
            {
                "find": "ndh",
                "replace": "ন্ধ"
            },
            {
                "find": "nTh",
                "replace": "ন্ঠ",
                "reverse": "nth"
            },
            {
                "find": "NTh",
                "replace": "ণ্ঠ",
                "reverse": "nth"
            },
            {
                "find": "nth",
                "replace": "ন্থ"
            },
            {
                "find": "nkh",
                "replace": "ঙ্খ",
                "reverse": "ngkh"
            },
            {
                "find": "ngo",
                "replace": "ঙ্গ"
            },
            {
                "find": "nga",
                "replace": "ঙ্গা"
            },
            {
                "find": "ngi",
                "replace": "ঙ্গি"
            },
            {
                "find": "ngI",
                "replace": "ঙ্গী",
                "reverse": "ngi"
            },
            {
                "find": "ngu",
                "replace": "ঙ্গু"
            },
            {
                "find": "ngU",
                "replace": "ঙ্গূ",
                "reverse": "ngu"
            },
            {
                "find": "nge",
                "replace": "ঙ্গে"
            },
            {
                "find": "ngO",
                "replace": "ঙ্গো",
                "reverse": "ngo"
            },
            {
                "find": "NDh",
                "replace": "ণ্ঢ",
                "reverse": "ndh"
            },
            {
                "find": "nsh",
                "replace": "নশ"
            },
            {
                "find": "Ngr",
                "replace": "ঙর",
                "reverse": "ngr"
            },
            {
                "find": "NGr",
                "replace": "ঞর"
            },
            {
                "find": "ngr",
                "replace": "ংর"
            },
            {
                "find": "nj",
                "replace": "ঞ্জ"
            },
            {
                "find": "Ng",
                "replace": "ঙ",
                "reverse": "ng"
            },
            {
                "find": "NG",
                "replace": "ঞ",
                "reverse": "y"
            },
            {
                "find": "nk",
                "replace": "ঙ্ক",
                "reverse": "ngk"
            },
            {
                "find": "ng",
                "replace": "ং"
            },
            {
                "find": "nn",
                "replace": "ন্ন"
            },
            {
                "find": "NN",
                "replace": "ণ্ণ",
                "reverse": "nn"
            },
            {
                "find": "Nn",
                "replace": "ণ্ন",
                "reverse": "nn"
            },
            {
                "find": "nm",
                "replace": "ন্ম"
            },
            {
                "find": "Nm",
                "replace": "ণ্ম",
                "reverse": "nm"
            },
            {
                "find": "nd",
                "replace": "ন্দ"
            },
            {
                "find": "nT",
                "replace": "ন্ট",
                "reverse": "nt"
            },
            {
                "find": "NT",
                "replace": "ণ্ট",
                "reverse": "nt"
            },
            {
                "find": "nD",
                "replace": "ন্ড",
                "reverse": "nd"
            },
            {
                "find": "ND",
                "replace": "ণ্ড",
                "reverse": "nd"
            },
            {
                "find": "nt",
                "replace": "ন্ত"
            },
            {
                "find": "ns",
                "replace": "ন্স"
            },
            {
                "find": "nc",
                "replace": "ঞ্চ",
                "reverse": "nch"
            },
            {
                "find": "n",
                "replace": "ন"
            },
            {
                "find": "N",
                "replace": "ণ",
                "reverse": "n"
            },
            {
                "find": "OI`",
                "replace": "ৈ",
                "reverse": "oi"
            },
            {
                "find": "OU`",
                "replace": "ৌ",
                "reverse": "ou"
            },
            {
                "find": "O`",
                "replace": "ো",
                "reverse": "o"
            },
            {
                "find": "OI",
                "replace": "ৈ",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            }
                        ],
                        "replace": "ঐ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "ঐ"
                    }
                ],
                "reverse": "oi"
            },
            {
                "find": "OU",
                "replace": "ৌ",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            }
                        ],
                        "replace": "ঔ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "ঔ"
                    }
                ],
                "reverse": "ou"
            },
            {
                "find": "O",
                "replace": "ো",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            }
                        ],
                        "replace": "ও"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "ও"
                    }
                ],
                "reverse": "o"
            },
            {
                "find": "phl",
                "replace": "ফ্ল",
                "reverse": "fl"
            },
            {
                "find": "pT",
                "replace": "প্ট",
                "reverse": "pt"
            },
            {
                "find": "pt",
                "replace": "প্ত"
            },
            {
                "find": "pn",
                "replace": "প্ন"
            },
            {
                "find": "pp",
                "replace": "প্প"
            },
            {
                "find": "pl",
                "replace": "প্ল"
            },
            {
                "find": "ps",
                "replace": "প্স"
            },
            {
                "find": "ph",
                "replace": "ফ"
            },
            {
                "find": "fl",
                "replace": "ফ্ল"
            },
            {
                "find": "f",
                "replace": "ফ",
                "reverse": "ph"
            },
            {
                "find": "p",
                "replace": "প"
            },
            {
                "find": "rri`",
                "replace": "ৃ",
                "reverse": "ri"
            },
            {
                "find": "rri",
                "replace": "ৃ",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            }
                        ],
                        "replace": "ঋ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "ঋ"
                    }
                ],
                "reverse": "ri"
            },
            {
                "find": "rrZ",
                "replace": "রর‍্য",
                "replace": "rry"
            },
            {
                "find": "rry",
                "replace": "রর‍্য"
            },
            {
                "find": "rZ",
                "replace": "র‍্য",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "r"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "y"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "w"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "x"
                            }
                        ],
                        "replace": "্র্য"
                    }
                ],
                "reverse": "ry"
            },
            {
                "find": "ry",
                "replace": "র‍্য",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "r"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "y"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "w"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "x"
                            }
                        ],
                        "replace": "্র্য"
                    }
                ]
            },
            {
                "find": "rr",
                "replace": "রর",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!vowel"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "r"
                            },
                            {
                                "type": "suffix",
                                "scope": "!punctuation"
                            }
                        ],
                        "replace": "র্"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "r"
                            }
                        ],
                        "replace": "্রর"
                    }
                ]
            },
            {
                "find": "Rg",
                "replace": "ড়্গ",
                "reverse": "rg"
            },
            {
                "find": "Rh",
                "replace": "ঢ়",
                "reverse": "rh"
            },
            {
                "find": "R",
                "replace": "ড়",
                "reverse": "r"
            },
            {
                "find": "r",
                "replace": "র",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "r"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "y"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "w"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "x"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "Z"
                            }
                        ],
                        "replace": "্র"
                    }
                ]
            },
            {
                "find": "shch",
                "replace": "শ্ছ",
                "reverse": "sch"
            },
            {
                "find": "ShTh",
                "replace": "ষ্ঠ",
                "reverse": "sth"
            },
            {
                "find": "Shph",
                "replace": "ষ্ফ",
                "reverse": "sf"
            },
            {
                "find": "Sch",
                "replace": "শ্ছ",
                "reverse": "sch"
            },
            {
                "find": "skl",
                "replace": "স্ক্ল"
            },
            {
                "find": "skh",
                "replace": "স্খ"
            },
            {
                "find": "sth",
                "replace": "স্থ"
            },
            {
                "find": "sph",
                "replace": "স্ফ",
                "reverse": "sf"
            },
            {
                "find": "shc",
                "replace": "শ্চ",
                "reverse": "scch"
            },
            {
                "find": "sht",
                "replace": "শ্ত"
            },
            {
                "find": "shn",
                "replace": "শ্ন"
            },
            {
                "find": "shm",
                "replace": "শ্ম"
            },
            {
                "find": "shl",
                "replace": "শ্ল"
            },
            {
                "find": "Shk",
                "replace": "ষ্ক",
                "reverse": "shk"
            },
            {
                "find": "ShT",
                "replace": "ষ্ট",
                "reverse": "sht"
            },
            {
                "find": "ShN",
                "replace": "ষ্ণ",
                "reverse": "shn"
            },
            {
                "find": "Shp",
                "replace": "ষ্প",
                "reverse": "shp"
            },
            {
                "find": "Shf",
                "replace": "ষ্ফ",
                "reverse": "shf"
            },
            {
                "find": "Shm",
                "replace": "ষ্ম",
                "reverse": "shm"
            },
            {
                "find": "spl",
                "replace": "স্প্ল"
            },
            {
                "find": "sk",
                "replace": "স্ক"
            },
            {
                "find": "Sc",
                "replace": "শ্চ",
                "reverse": "scch"
            },
            {
                "find": "sT",
                "replace": "স্ট",
                "reverse": "st"
            },
            {
                "find": "st",
                "replace": "স্ত"
            },
            {
                "find": "sn",
                "replace": "স্ন"
            },
            {
                "find": "sp",
                "replace": "স্প"
            },
            {
                "find": "sf",
                "replace": "স্ফ",
            },
            {
                "find": "sm",
                "replace": "স্ম",
                "reverse": "shm"
            },
            {
                "find": "sl",
                "replace": "স্ল"
            },
            {
                "find": "sh",
                "replace": "শ"
            },
            {
                "find": "Sc",
                "replace": "শ্চ",
                "reverse": "scch"
            },
            {
                "find": "St",
                "replace": "শ্ত"
            },
            {
                "find": "Sn",
                "replace": "শ্ন",
                "reverse": "shn"
            },
            {
                "find": "Sm",
                "replace": "শ্ম",
                "reverse": "ss"
            },
            {
                "find": "Sl",
                "replace": "শ্ল",
                "reverse": "sl"
            },
            {
                "find": "Sh",
                "replace": "ষ",
                "reverse": "sh"
            },
            {
                "find": "s",
                "replace": "স"
            },
            {
                "find": "S",
                "replace": "শ",
                "reverse": "sh"
            },
            {
                "find": "oo`",
                "replace": "ু",
                "reverse": "u"
            },
            {
                "find": "oo",
                "replace": "ু",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "উ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "উ"
                    }
                ],
                "reverse": "u"
            },
            {
                "find": "oZ",
                "replace": "অ্য"
            },
            {
                "find": "o",
                "replace": "",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "vowel"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "o"
                            }
                        ],
                        "replace": "ও"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "vowel"
                            },
                            {
                                "type": "prefix",
                                "scope": "exact",
                                "value": "o"
                            }
                        ],
                        "replace": "অ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "অ"
                    }
                ]
            },
            {
                "find": "tth",
                "replace": "ত্থ"
            },
            {
                "find": "t``",
                "replace": "ৎ",
                "reverse": "t"
            },
            {
                "find": "TT",
                "replace": "ট্ট",
                "reverse": "tt"
            },
            {
                "find": "Tm",
                "replace": "ট্ম",
                "reverse": "tm"
            },
            {
                "find": "Th",
                "replace": "ঠ",
                "reverse": "th"
            },
            {
                "find": "tn",
                "replace": "ত্ন"
            },
            {
                "find": "tm",
                "replace": "ত্ম",
                "reverse": "tt"
            },
            {
                "find": "th",
                "replace": "থ"
            },
            {
                "find": "tt",
                "replace": "ত্ত"
            },
            {
                "find": "T",
                "replace": "ট",
                "reverse": "t"
            },
            {
                "find": "t",
                "replace": "ত"
            },
            {
                "find": "aZ",
                "replace": "অ্যা"
            },
            {
                "find": "AZ",
                "replace": "অ্যা"
            },
            {
                "find": "a`",
                "replace": "া",
                "reverse": "a"
            },
            {
                "find": "A`",
                "replace": "া",
                "reverse": "a"
            },
            {
                "replace": "আ",
                "reverse": "a"
            },
            {
                "replace": "র",
                "reverse": "r"
            },
            {
                "find": "a",
                "replace": "া",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "আ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!exact",
                                "value": "a"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "য়া"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "exact",
                                "value": "a"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "আ"
                    }
                ]
            },
            {
                "find": "i`",
                "replace": "ি",
                "reverse": "i"
            },
            {
                "replace": "ই",
                "reverse": "i"
            },
            {
                "find": "i",
                "replace": "ি",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ই"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ই"
                    }
                ]
            },
            {
                "find": "I`",
                "replace": "ী",
                "reverse": "i"
            },
            {
                "find": "I",
                "replace": "ী",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঈ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঈ"
                    }
                ],
                "reverse": "i"
            },
            {
                "find": "u`",
                "replace": "ু",
                "reverse": "u"
            },
            {
                "replace": "উ",
                "reverse": "u"
            },
            {
                "find": "u",
                "replace": "ু",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "উ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "উ"
                    }
                ]
            },
            {
                "find": "U`",
                "replace": "ূ",
                "reverse": "u"
            },
            {
                "find": "U",
                "replace": "ূ",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঊ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঊ"
                    }
                ],
                "reverse": "u"
            },
            {
                "find": "ee`",
                "replace": "ী",
                "reverse": "i"
            },
            {
                "find": "ee",
                "replace": "ী",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঈ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "ঈ"
                    }
                ],
                "reverse": "i"
            },
            {
                "find": "e`",
                "replace": "ে",
                "reverse": "e"
            },
            {
                "replace": "এ",
                "reverse": "e"
            },
            {
                "replace": "ও",
                "reverse": "w"
            },
            {
                "find": "e",
                "replace": "ে",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "এ"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "!exact",
                                "value": "`"
                            }
                        ],
                        "replace": "এ"
                    }
                ]
            },
            {
                "find": "z",
                "replace": "য"
            },
            {
                "find": "Z",
                "replace": "্য",
                "reverse": "z"
            },
            {
                "find": "y",
                "replace": "্য",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "!consonant"
                            },
                            {
                                "type": "prefix",
                                "scope": "!punctuation"
                            }
                        ],
                        "replace": "য়"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "ইয়"
                    }
                ]
            },
            {
                "find": "Y",
                "replace": "য়",
                "reverse": "y"
            },
            {
                "find": "q",
                "replace": "ক",
                "reverse": "k"
            },
            {
                "find": "w",
                "replace": "ও",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            },
                            {
                                "type": "suffix",
                                "scope": "vowel"
                            }
                        ],
                        "replace": "ওয়"
                    },
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "consonant"
                            }
                        ],
                        "replace": "্ব"
                    }
                ],
                "reverse": "o"
            },
            {
                "find": "x",
                "replace": "ক্স",
                "rules": [
                    {
                        "matches": [
                            {
                                "type": "prefix",
                                "scope": "punctuation"
                            }
                        ],
                        "replace": "এক্স"
                    }
                ],
                "reverse": "ks"
            },
            {
                "find": ":`",
                "replace": ":"
            },
            {
                "find": ":",
                "replace": "ঃ"
            },
            {
                "find": "^`",
                "replace": "^"
            },
            {
                "find": "^",
                "replace": "ঁ",
                "reverse": ""
            },
            {
                "find": ",,",
                "replace": "্‌"
            },
            {
                "find": ",",
                "replace": ","
            },
            {
                "find": "$",
                "replace": "৳"
            },
        ],

        # Remapped words
        "exceptions": {
            "ফেসবুক": "Facebook",
            "গুগল": "Google",
            "উইকিপিডিয়া": "Wikipedia"
        },

        # Constant values
        "vowel": "aeiou",
        "consonant": "bcdfghjklmnpqrstvwxyz",
        "casesensitive": "oiudgjnrstyz",
        "number": "0123456789",

        # For reverse parsing
        "shorborno": "অআইঈউঊঊএঐওঔ",
        "kar": {
            'া',
            'ি',
            'ী',
            'ু',
            'ূ',
            'ৃ',
            'ে',
            'ৈ',
            'ো',
            'ৌ'
        },

        # Ignored symbols
        "ignore": {
            "ঁ",
            "।",
            "?",
            ".",
            "-",
            ";"
        }
    }
}
