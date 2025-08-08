<!-- SPDX-License-Identifier: MIT -->

<div align="center">

# <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" width="35px"/> avro.py

A modern Pythonic implementation of the popular Bengali phonetic-typing software **Avro Phonetic.**

[![Downloads](https://static.pepy.tech/personalized-badge/avro-py?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avro-py)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avro.py.svg?color=black&label=License)

<br>

<img src="https://github.com/hitblast/avro.py/blob/main/assets/banner.png?raw=True" style="width: 500px; height: auto;"><br>

</div>

## ⚡ Overview

**avro.py** provides a fully fledged, batteries-included text parser which can
parse, reverse and even convert English Roman script into its phonetic
equivalent (unicode) of Bengali. At its core, it implements an extensively
modified version of the **Avro Phonetic Dictionary Search Library** by [Mehdi
Hasan Khan](https://github.com/mugli).

## ✨ Inspirations

This package is inspired from Rifat Nabi's jsAvroPhonetic library and derives from Kaustav Das Modak's pyAvroPhonetic.

<br>

## 🔨 Installation

This package requires **Python 3.9 or higher** to be used inside your development environment.

```sh
# Install or upgrade.
pip install -U avro.py
```

<br>

## 🔖 Usage Guide

This small tour guide will describe how you can use avro.py back and forth to
operate (cutlery!) on Bengali text. You can also check the
[examples](https://github.com/hitblast/avro.py/tree/main/examples) directory for
checking [this whole
snippet](https://github.com/hitblast/avro.py/blob/main/examples/basic.py) in
action, as well as other use cases.

1. `parse()`

Let's assume you want to parse a single English string to Bengali, for example `"ami banglay gan gai."`. You can convert it like this:

```python
# Import the package.
import avro

# Our dummy text.
dummy = 'ami banglay gan gai.'

# Parse a single string.
parsed = avro.parse(dummy)
print(parsed)  # Output: আমি বাংলায় গান গাই।
```

1.a `parse_iter()`

If you have multiple strings, use `parse_iter()` to get a list of parsed results:

```python
texts = ['ami banglay gan gai.', 'tumi kothay jao?']
parsed_list = avro.parse_iter(texts)
print(parsed_list)  # Output: ['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?']
```

2. `parse(bijoy=True)`

Alternatively, I can also do it in Bijoy Keyboard format:

```python
bijoy_output = avro.parse(dummy, bijoy=True)
# Output: Avwg evsjvh় Mvb MvB।
```

3. `to_bijoy()`

To convert a single Bengali string (Avro/Unicode) to Bijoy ASCII format:

```python
bijoy_text = avro.to_bijoy(parsed)
print(bijoy_text)  # Output: Avwg evsjvh় Mvb MvB।
```

3.a `to_bijoy_iter()`

To convert multiple strings at once, use `to_bijoy_iter()`:

```python
bijoy_list = avro.to_bijoy_iter(['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?'])
print(bijoy_list)  # Output: ['Avwg evsjvh় Mvb MvB।', 'tvmf wkrwb‡¶ jd?']
```

4. `to_unicode()`

To convert a single Bijoy ASCII string back to Unicode Bengali:

```python
unicode_text = avro.to_unicode(bijoy_text)
print(unicode_text)  # Output: আমি বাংলায় গান গাই।
```

4.a `to_unicode_iter()`

For multiple strings, use `to_unicode_iter()`:

```python
unicode_list = avro.to_unicode_iter(['Avwg evsjvh় Mvb MvB।', 'tvmf wkrwb‡¶ jd?'])
print(unicode_list)  # Output: ['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?']
```

5. `reverse()`

To reverse a single Unicode Bengali string back to Roman script:

```python
reversed_text = avro.reverse(unicode_text)
print(reversed_text)  # Output: ami banglay gan gai.
```

> [!WARNING]
> The reverse functions are by-nature lossy and might not output the correct replacement for some letters in favor of readability sometimes.

5.a `reverse_iter()`

To reverse multiple strings at once, use `reverse_iter()`:

```python
rev_list = avro.reverse_iter(['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?'])
print(rev_list)  # Output: ['ami banglay gan gai.', 'tumi kothay jao?']
```

<br>

## 🔖 Asynchronous Operations

All of the functions above, when suffixed with `_async`, provide their asynchronous counterparts which have a slight performance bump in certain use cases. Please see the [async examples](https://github.com/hitblast/avro.py/blob/main/examples/async.py) to find out more about their usage.

<br>

## 🛠️ Contributing

:octocat: "_Fork -> Do your changes -> Send a Pull Request, it's that easy!_" <br>

This project is based on the [uv](https://github.com/astral-sh/uv) package
manager by Astral. In order to automatically update and set up the environment,
you can run the following command:

```sh
# (Optional) Install recommended Python version: (also sets up the virtual environment)
$ uv python install && uv venv
$ source .venv/bin/activate

# Install the project:
$ uv sync --all-extras --dev

# Build the project:
$ uv build --verbose
```

In order to run the tests, you can use the following command:

```sh
# Run unit tests:
$ uv run pytest .
```

<br>

### 🐛 Bug hunters wanted!

If you come across any kind of bug or wanna request a feature, please let us
know by opening an issue [here](https://github.com/hitblast/avro.py/issues). We
do need more ideas to keep the project alive and running, don't we? :P

---

<br>

## 👑 Acknowledgements

- [Mehdi Hasan Khan](https://github.com/mugli) for originally developing and maintaining [Avro Phonetic](https://github.com/omicronlab/Avro-Keyboard).
- [Rifat Nabi](https://github.com/torifat) for porting it to Javascript.
- [Sarim Khan](https://github.com/sarim) for writing ibus-avro which helped to clarify my concepts further.
- [Kaustav Das Modak](https://github.com/kaustavdm) for porting Rifat Nabi's JavaScript iteration to Python 2.
- Md Enzam Hossain for helping him understand the ins and outs of the Avro dictionary and the way it works.

<br>

## 📋 License

Licensed under the [MIT License](https://github.com/hitblast/avro.py/blob/main/LICENSE).
