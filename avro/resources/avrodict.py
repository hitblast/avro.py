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


# The dictionary variable.
AVRO_DICT: dict = {
    "meta": {
        "file_name": "avrodict.py",
        "file_description": "Provides Avro Dictionary in JSON. Adapted from avrodict.json",
        "package": "avro.py",
        "license": "MIT License",
        "source": "https://github.com/kaustavdm/pyAvroPhonetic/blob/master/pyavrophonetic/resources/avrodict.json",
        "adapted_by": "HitBlast",
        "updated": "20221001",
        "encoding": "utf-8"
    },
    "data": {
        "patterns": [
            {
                "find": "bhl",
                "replace": "ভ্ল",
                "reversed": "vl"
            },
            {
                "find": "psh",
                "replace": "পশ"
            },
            {
                "find": "bdh",
                "replace": "ব্ধ",
                "reversed": "bdh"
            },
            {
                "find": "bj",
                "replace": "ব্জ",
                "reversed": "bj"
            },
            {
                "find": "bd",
                "replace": "ব্দ",
                "reversed": "bd"
            },
            {
                "find": "bb",
                "replace": "ব্ব",
                "reversed": "bb"
            },
            {
                "find": "bl",
                "replace": "ব্ল",
                "reversed": "bl"
            },
            {
                "find": "bh",
                "replace": "ভ",
                "reversed": "bh"
            },
            {
                "find": "vl",
                "replace": "ভ্ল",
                "reversed": "vl"
            },
            {
                "find": "b",
                "replace": "ব",
                "reversed": "b"
            },
            {
                "find": "v",
                "replace": "ভ",
                "reversed": "bh"
            },
            {
                "find": "cNG",
                "replace": "চ্ঞ",
                "reversed": "cng"
            },
            {
                "find": "cch",
                "replace": "চ্ছ",
                "reversed": "cch"
            },
            {
                "find": "cc",
                "replace": "চ্চ",
                "reversed": "cc"
            },
            {
                "find": "ch",
                "replace": "ছ",
                "reversed": "s"
            },
            {
                "find": "c",
                "replace": "চ",
                "reversed": "ch"
            },
            {
                "find": "dhn",
                "replace": "ধ্ন",
                "reversed": "dhn"
            },
            {
                "find": "dhm",
                "replace": "ধ্ম",
                "reversed": "dhm"
            },
            {
                "find": "dgh",
                "replace": "দ্ঘ",
                "reversed": "dgh"
            },
            {
                "find": "ddh",
                "replace": "দ্ধ",
                "reversed": "ddh"
            },
            {
                "find": "dbh",
                "replace": "দ্ভ",
                "reversed": "dv"
            },
            {
                "find": "dv",
                "replace": "দ্ভ",
                "reversed": "dv"
            },
            {
                "find": "dm",
                "replace": "দ্ম",
                "reversed": "dd"
            },
            {
                "find": "DD",
                "replace": "ড্ড",
                "reversed": "dd"
            },
            {
                "find": "Dh",
                "replace": "ঢ",
                "reversed": "dh"
            },
            {
                "find": "dh",
                "replace": "ধ",
                "reversed": "dh"
            },
            {
                "find": "dg",
                "replace": "দ্গ"
            },
            {
                "find": "dd",
                "replace": "দ্দ",
                "reversed": "dd"
            },
            {
                "find": "D",
                "replace": "ড",
                "reversed": "d"
            },
            {
                "find": "d",
                "replace": "দ",
                "reversed": "d"
            },
            {
                "find": "...",
                "replace": "..."
            },
            {
                "find": ".`",
                "replace": "."
            },
            {
                "find": "..",
                "replace": "।।"
            },
            {
                "find": ".",
                "replace": "।",
                "reversed": "."
            },
            {
                "find": "ghn",
                "replace": "ঘ্ন",
                "reversed": "ghn"
            },
            {
                "find": "Ghn",
                "replace": "ঘ্ন",
                "reversed": "ghn"
            },
            {
                "find": "gdh",
                "replace": "গ্ধ",
                "reversed": "gdh"
            },
            {
                "find": "Gdh",
                "replace": "গ্ধ",
                "reversed": "gdh"
            },
            {
                "find": "gN",
                "replace": "গ্ণ",
                "reversed": "gn"
            },
            {
                "find": "GN",
                "replace": "গ্ণ",
                "reversed": "gn"
            },
            {
                "find": "gn",
                "replace": "গ্ন",
                "reversed": "gn"
            },
            {
                "find": "Gn",
                "replace": "গ্ন",
                "reversed": "gn"
            },
            {
                "find": "gm",
                "replace": "গ্ম"
            },
            {
                "find": "Gm",
                "replace": "গ্ম",
                "reversed": "gm"
            },
            {
                "find": "gl",
                "replace": "গ্ল",
                "reversed": "gl"
            },
            {
                "find": "Gl",
                "replace": "গ্ল",
                "reversed": "gl"
            },
            {
                "find": "gg",
                "replace": "জ্ঞ",
                "reversed": "gg"
            },
            {
                "find": "GG",
                "replace": "জ্ঞ",
                "reversed": "gg"
            },
            {
                "find": "Gg",
                "replace": "জ্ঞ",
                "reversed": "gg"
            },
            {
                "find": "gG",
                "replace": "জ্ঞ",
                "reversed": "gg"
            },
            {
                "find": "gh",
                "replace": "ঘ",
                "reversed": "gh"
            },
            {
                "find": "Gh",
                "replace": "ঘ",
                "reversed": "gh"
            },
            {
                "find": "g",
                "replace": "গ",
                "reversed": "g"
            },
            {
                "find": "G",
                "replace": "গ",
                "reversed": "g"
            },
            {
                "find": "hN",
                "replace": "হ্ণ",
                "reversed": "nn"
            },
            {
                "find": "hn",
                "replace": "হ্ন",
                "reversed": "nn"
            },
            {
                "find": "hm",
                "replace": "হ্ম",
                "reversed": "mm"
            },
            {
                "find": "hl",
                "replace": "হ্ল"
            },
            {
                "find": "h",
                "replace": "হ",
                "reversed": "h"
            },
            {
                "find": "jjh",
                "replace": "জ্ঝ"
            },
            {
                "find": "jNG",
                "replace": "জ্ঞ",
                "reversed": "gg"
            },
            {
                "find": "jh",
                "replace": "ঝ",
                "reversed": "jh"
            },
            {
                "find": "jj",
                "replace": "জ্জ",
                "reversed": "jj"
            },
            {
                "find": "j",
                "replace": "জ",
                "reversed": "j"
            },
            {
                "find": "J",
                "replace": "জ",
                "reversed": "j"
            },
            {
                "find": "kkhN",
                "replace": "ক্ষ্ণ",
                "reversed": "kkhn"
            },
            {
                "find": "kShN",
                "replace": "ক্ষ্ণ",
                "reversed": "kkhn"
            },
            {
                "find": "kkhm",
                "replace": "ক্ষ্ম"
            },
            {
                "find": "kShm",
                "replace": "ক্ষ্ম",
                "reversed": "kkh"
            },
            {
                "find": "kxN",
                "replace": "ক্ষ্ণ",
                "reversed": "kkh"
            },
            {
                "find": "kxm",
                "replace": "ক্ষ্ম",
                "reversed": "kkh"
            },
            {
                "find": "kkh",
                "replace": "ক্ষ",
                "reversed": "kkh"
            },
            {
                "find": "kSh",
                "replace": "ক্ষ",
                "reversed": "kkh"
            },
            {
                "find": "ksh",
                "replace": "কশ"
            },
            {
                "find": "kx",
                "replace": "ক্ষ",
                "reversed": "kkh"
            },
            {
                "find": "kk",
                "replace": "ক্ক",
                "reversed": "kk"
            },
            {
                "find": "kT",
                "replace": "ক্ট",
                "reversed": "kt"
            },
            {
                "find": "kt",
                "replace": "ক্ত",
                "reversed": "kt"
            },
            {
                "find": "kl",
                "replace": "ক্ল",
                "reversed": "kl"
            },
            {
                "find": "ks",
                "replace": "ক্স",
                "reversed": "ks"
            },
            {
                "find": "kh",
                "replace": "খ",
                "reversed": "kh"
            },
            {
                "find": "k",
                "replace": "ক",
                "reversed": "k"
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
                "replace": "ল্ক",
                "reversed": "lk"
            },
            {
                "find": "lg",
                "replace": "ল্গ"
            },
            {
                "find": "lT",
                "replace": "ল্ট",
                "reversed": "lt"
            },
            {
                "find": "lD",
                "replace": "ল্ড",
                "reversed": "ld"
            },
            {
                "find": "lp",
                "replace": "ল্প",
                "reversed": "lp"
            },
            {
                "find": "lv",
                "replace": "ল্ভ"
            },
            {
                "find": "lm",
                "replace": "ল্ম",
                "reversed": "lm"
            },
            {
                "find": "ll",
                "replace": "ল্ল",
                "reversed": "ll"
            },
            {
                "find": "lb",
                "replace": "ল্ব",
                "reversed": "lb"
            },
            {
                "find": "l",
                "replace": "ল",
                "reversed": "l"
            },
            {
                "find": "mth",
                "replace": "ম্থ"
            },
            {
                "find": "mph",
                "replace": "ম্ফ",
                "reversed": "mf"
            },
            {
                "find": "mbh",
                "replace": "ম্ভ",
                "reversed": "mv"
            },
            {
                "find": "mpl",
                "replace": "মপ্ল"
            },
            {
                "find": "mn",
                "replace": "ম্ন",
                "reversed": "mn"
            },
            {
                "find": "mp",
                "replace": "ম্প",
                "reversed": "mp"
            },
            {
                "find": "mv",
                "replace": "ম্ভ",
                "reversed": "mv"
            },
            {
                "find": "mm",
                "replace": "ম্ম",
                "reversed": "mm"
            },
            {
                "find": "ml",
                "replace": "ম্ল",
                "reversed": "ml"
            },
            {
                "find": "mb",
                "replace": "ম্ব",
                "reversed": "mb"
            },
            {
                "find": "mf",
                "replace": "ম্ফ",
                "reversed": "mf"
            },
            {
                "find": "m",
                "replace": "ম",
                "reversed": "m"
            },
            {
                "find": "0",
                "replace": "০",
                "reversed": "0"
            },
            {
                "find": "1",
                "replace": "১",
                "reversed": "1"
            },
            {
                "find": "2",
                "replace": "২",
                "reversed": "2"
            },
            {
                "find": "3",
                "replace": "৩",
                "reversed": "3"
            },
            {
                "find": "4",
                "replace": "৪",
                "reversed": "4"
            },
            {
                "find": "5",
                "replace": "৫",
                "reversed": "5"
            },
            {
                "find": "6",
                "replace": "৬",
                "reversed": "6"
            },
            {
                "find": "7",
                "replace": "৭",
                "reversed": "7"
            },
            {
                "find": "8",
                "replace": "৮",
                "reversed": "8"
            },
            {
                "find": "9",
                "replace": "৯",
                "reversed": "9"
            },
            {
                "find": "NgkSh",
                "replace": "ঙ্ক্ষ",
                "reversed": "ngkh"
            },
            {
                "find": "Ngkkh",
                "replace": "ঙ্ক্ষ",
                "reversed": "ngkh"
            },
            {
                "find": "NGch",
                "replace": "ঞ্ছ",
                "reversed": "ngch"
            },
            {
                "find": "Nggh",
                "replace": "ঙ্ঘ"
            },
            {
                "find": "Ngkh",
                "replace": "ঙ্খ",
                "reversed": "ngkh"
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
                "reversed": "ngkh"
            },
            {
                "find": "NGc",
                "replace": "ঞ্চ",
                "reversed": "nch"
            },
            {
                "find": "nch",
                "replace": "ঞ্ছ",
                "reversed": "ngch"
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
                "reversed": "ngk"
            },
            {
                "find": "Ngx",
                "replace": "ঙ্ষ"
            },
            {
                "find": "Ngg",
                "replace": "ঙ্গ",
                "reversed": "ngg"
            },
            {
                "find": "Ngm",
                "replace": "ঙ্ম"
            },
            {
                "find": "NGj",
                "replace": "ঞ্জ",
                "reversed": "ngj"
            },
            {
                "find": "ndh",
                "replace": "ন্ধ",
                "reversed": "ndh"
            },
            {
                "find": "nTh",
                "replace": "ন্ঠ",
                "reversed": "nth"
            },
            {
                "find": "NTh",
                "replace": "ণ্ঠ",
                "reversed": "nth"
            },
            {
                "find": "nth",
                "replace": "ন্থ",
                "reversed": "nth"
            },
            {
                "find": "nkh",
                "replace": "ঙ্খ",
                "reversed": "ngkh"
            },
            {
                "find": "ngo",
                "replace": "ঙ্গ",
                "reversed": "ngg"
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
                "replace": "ঙ্গী"
            },
            {
                "find": "ngu",
                "replace": "ঙ্গু"
            },
            {
                "find": "ngU",
                "replace": "ঙ্গূ"
            },
            {
                "find": "nge",
                "replace": "ঙ্গে"
            },
            {
                "find": "ngO",
                "replace": "ঙ্গো"
            },
            {
                "find": "NDh",
                "replace": "ণ্ঢ"
            },
            {
                "find": "nsh",
                "replace": "নশ"
            },
            {
                "find": "Ngr",
                "replace": "ঙর"
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
                "replace": "ঞ্জ",
                "reversed": "ngj"
            },
            {
                "find": "Ng",
                "replace": "ঙ",
                "reversed": "ng"
            },
            {
                "find": "NG",
                "replace": "ঞ",
                "reversed": "y"
            },
            {
                "find": "nk",
                "replace": "ঙ্ক",
                "reversed": "ngk"
            },
            {
                "find": "ng",
                "replace": "ং",
                "reversed": "ng"
            },
            {
                "find": "nn",
                "replace": "ন্ন",
                "reversed": "nn"
            },
            {
                "find": "NN",
                "replace": "ণ্ণ"
            },
            {
                "find": "Nn",
                "replace": "ণ্ন"
            },
            {
                "find": "nm",
                "replace": "ন্ম",
                "reversed": "nm"
            },
            {
                "find": "Nm",
                "replace": "ণ্ম"
            },
            {
                "find": "nd",
                "replace": "ন্দ",
                "reversed": "nd"
            },
            {
                "find": "nT",
                "replace": "ন্ট",
                "reversed": "nt"
            },
            {
                "find": "NT",
                "replace": "ণ্ট",
                "reversed": "nt"
            },
            {
                "find": "nD",
                "replace": "ন্ড",
                "reversed": "nd"
            },
            {
                "find": "ND",
                "replace": "ণ্ড",
                "reversed": "nd"
            },
            {
                "find": "nt",
                "replace": "ন্ত",
                "reversed": "nt"
            },
            {
                "find": "ns",
                "replace": "ন্স"
            },
            {
                "find": "nc",
                "replace": "ঞ্চ",
                "reversed": "nch"
            },
            {
                "find": "n",
                "replace": "ন",
                "reversed": "n"
            },
            {
                "find": "N",
                "replace": "ণ",
                "reversed": "n"
            },
            {
                "find": "OI`",
                "replace": "ৈ",
                "reversed": "oi"
            },
            {
                "find": "OU`",
                "replace": "ৌ",
                "reversed": "ou"
            },
            {
                "find": "O`",
                "replace": "ো",
                "reversed": "o"
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
                "reversed": "oi"
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
                "reversed": "ou"
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
                "reversed": "o"
            },
            {
                "find": "phl",
                "replace": "ফ্ল",
                "reversed": "fl"
            },
            {
                "find": "pT",
                "replace": "প্ট",
                "reversed": "pt"
            },
            {
                "find": "pt",
                "replace": "প্ত",
                "reversed": "pt"
            },
            {
                "find": "pn",
                "replace": "প্ন",
                "reversed": "pn"
            },
            {
                "find": "pp",
                "replace": "প্প",
                "reversed": "pp"
            },
            {
                "find": "pl",
                "replace": "প্ল",
                "reversed": "pl"
            },
            {
                "find": "ps",
                "replace": "প্স",
                "reversed": "ps"
            },
            {
                "find": "ph",
                "replace": "ফ",
                "reversed": "ph"
            },
            {
                "find": "fl",
                "replace": "ফ্ল",
                "reversed": "fl"
            },
            {
                "find": "f",
                "replace": "ফ",
                "reversed": "ph"
            },
            {
                "find": "p",
                "replace": "প",
                "reversed": "p"
            },
            {
                "find": "rri`",
                "replace": "ৃ",
                "reversed": "ri"
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
                "reversed": "ri"
            },
            {
                "find": "rrZ",
                "replace": "রর‍্য"
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
                ]
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
                "replace": "ড়্গ"
            },
            {
                "find": "Rh",
                "replace": "ঢ়"
            },
            {
                "find": "R",
                "replace": "ড়",
                "reversed": "r"
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
                ],
                "reversed": "r"
            },
            {
                "find": "shch",
                "replace": "শ্ছ",
                "reversed": "sch"
            },
            {
                "find": "ShTh",
                "replace": "ষ্ঠ",
                "reversed": "sth"
            },
            {
                "find": "Shph",
                "replace": "ষ্ফ",
                "reversed": "sf"
            },
            {
                "find": "Sch",
                "replace": "শ্ছ",
                "reversed": "sch"
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
                "replace": "স্থ",
                "reversed": "sth"
            },
            {
                "find": "sph",
                "replace": "স্ফ",
                "reversed": "sf"
            },
            {
                "find": "shc",
                "replace": "শ্চ",
                "reversed": "scch"
            },
            {
                "find": "sht",
                "replace": "শ্ত"
            },
            {
                "find": "shn",
                "replace": "শ্ন",
                "reversed": "sn"
            },
            {
                "find": "shm",
                "replace": "শ্ম",
                "reversed": "ss"
            },
            {
                "find": "shl",
                "replace": "শ্ল",
                "reversed": "sl"
            },
            {
                "find": "Shk",
                "replace": "ষ্ক",
                "reversed": "sk"
            },
            {
                "find": "ShT",
                "replace": "ষ্ট",
                "reversed": "st"
            },
            {
                "find": "ShN",
                "replace": "ষ্ণ",
                "reversed": "sn"
            },
            {
                "find": "Shp",
                "replace": "ষ্প",
                "reversed": "sp"
            },
            {
                "find": "Shf",
                "replace": "ষ্ফ",
                "reversed": "sf"
            },
            {
                "find": "Shm",
                "replace": "ষ্ম",
                "reversed": "sm"
            },
            {
                "find": "spl",
                "replace": "স্প্ল"
            },
            {
                "find": "sk",
                "replace": "স্ক",
                "reversed": "sk"
            },
            {
                "find": "Sc",
                "replace": "শ্চ",
                "reversed": "scch"
            },
            {
                "find": "sT",
                "replace": "স্ট",
                "reversed": "st"
            },
            {
                "find": "st",
                "replace": "স্ত",
                "reversed": "st"
            },
            {
                "find": "sn",
                "replace": "স্ন",
                "reversed": "sn"
            },
            {
                "find": "sp",
                "replace": "স্প",
                "reversed": "sp"
            },
            {
                "find": "sf",
                "replace": "স্ফ",
                "reversed": "sf"
            },
            {
                "find": "sm",
                "replace": "স্ম",
                "reversed": "sh"
            },
            {
                "find": "sl",
                "replace": "স্ল",
                "reversed": "sl"
            },
            {
                "find": "sh",
                "replace": "শ",
                "reversed": "sh"
            },
            {
                "find": "Sc",
                "replace": "শ্চ",
                "reversed": "scch"
            },
            {
                "find": "St",
                "replace": "শ্ত"
            },
            {
                "find": "Sn",
                "replace": "শ্ন",
                "reversed": "sn"
            },
            {
                "find": "Sm",
                "replace": "শ্ম",
                "reversed": "ss"
            },
            {
                "find": "Sl",
                "replace": "শ্ল",
                "reversed": "sl"
            },
            {
                "find": "Sh",
                "replace": "ষ",
                "reversed": "sh"
            },
            {
                "find": "s",
                "replace": "স",
                "reversed": "s"
            },
            {
                "find": "S",
                "replace": "শ",
                "reversed": "sh"
            },
            {
                "find": "oo`",
                "replace": "ু",
                "reversed": "u"
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
                "reversed": "u"
            },
            {
                "find": "o`",
                "replace": ""
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
                "reversed": "t"
            },
            {
                "find": "TT",
                "replace": "ট্ট",
                "reversed": "tt"
            },
            {
                "find": "Tm",
                "replace": "ট্ম"
            },
            {
                "find": "Th",
                "replace": "ঠ",
                "reversed": "th"
            },
            {
                "find": "tn",
                "replace": "ত্ন"
            },
            {
                "find": "tm",
                "replace": "ত্ম",
                "reversed": "tt"
            },
            {
                "find": "th",
                "replace": "থ",
                "reversed": "th"
            },
            {
                "find": "tt",
                "replace": "ত্ত",
                "reversed": "tt"
            },
            {
                "find": "T",
                "replace": "ট",
                "reversed": "t"
            },
            {
                "find": "t",
                "replace": "ত",
                "reversed": "t"
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
                "reversed": "a"
            },
            {
                "find": "A`",
                "replace": "া",
                "reversed": "a"
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
                ],
                "reversed": "a"
            },
            {
                "find": "i`",
                "replace": "ি",
                "reversed": "i"
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
                ],
                "reversed": "i"
            },
            {
                "find": "I`",
                "replace": "ী",
                "reversed": "i"
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
                "reversed": "i"
            },
            {
                "find": "u`",
                "replace": "ু",
                "reversed": "u"
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
                ],
                "reversed": "u"
            },
            {
                "find": "U`",
                "replace": "ূ",
                "reversed": "u"
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
                "reversed": "u"
            },
            {
                "find": "ee`",
                "replace": "ী",
                "reversed": "i"
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
                "reversed": "i"
            },
            {
                "find": "e`",
                "replace": "ে",
                "reversed": "e"
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
                ],
                "reversed": "e"
            },
            {
                "find": "z",
                "replace": "য",
                "reversed": "z"
            },
            {
                "find": "Z",
                "replace": "্য"
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
                "reversed": "y"
            },
            {
                "find": "q",
                "replace": "ক",
                "reversed": "k"
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
                "reversed": "o"
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
                "reversed": "ks"
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
                "reversed": ""
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
            {
                "find": "`",
                "replace": ""
            }
        ],
        "vowel": "aeiou",
        "consonant": "bcdfghjklmnpqrstvwxyz",
        "casesensitive": "oiudgjnrstyz",
        "number": "0123456789"
    }
}