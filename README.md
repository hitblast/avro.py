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

### ✨ Inspirations

This package is inspired from Rifat Nabi's jsAvroPhonetic library and derives from Kaustav Das Modak's pyAvroPhonetic.

<br>

## 🔨 Installation

This package requires **Python 3.10 or higher** to be used inside your development environment.

```sh
# Install or upgrade.
$ pip install -U avro.py

# Or, add with the uv package manager.
$ uv add avro.py
```

<br>

## Usage Guide

You can also check the [examples](https://github.com/hitblast/avro.py/tree/main/examples) directory for
checking [this whole snippet](https://github.com/hitblast/avro.py/blob/main/examples/basic.py) in
action, as well as other use cases.

### Parsing to Bengali

For a single block of text, use `avro.parse()`:

```python
# Import the package.
import avro

# Our dummy text.
dummy = 'ami banglay gan gai.'

# Parse a single string.
parsed = avro.parse(dummy)
print(parsed)  # আমি বাংলায় গান গাই।
```

If you have multiple strings, use `avro.parse_iter()` to get a list of parsed results:

```python
texts = ['ami banglay gan gai.', 'tumi kOthay zao?']
parsed_list = avro.parse_iter(texts)
print(parsed_list)  # ['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?']
```

Alternatively, set the `bijoy` flag to `True` for receiving the output in the [Bijoy Keyboard]() format.

```python
bijoy_output = avro.parse(dummy, bijoy=True)
# Output: Avwg evsjvh় Mvb MvB।
```

### Conversions

To convert a single Bengali string (Avro/Unicode) to the Bijoy Keyboard format:

```python
bijoy_text = avro.to_bijoy("আমি বাংলায় গান গাই।")
print(bijoy_text)  # Avwg evsjvh় Mvb MvB।
```

To convert multiple strings at once, use `avro.to_bijoy_iter()`:

```python
bijoy_list = avro.to_bijoy_iter(['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?'])
print(bijoy_list)  # ['Avwg evsjvh় Mvb MvB।', 'tvmf wkrwb‡¶ jd?']
```

On the contrary, to convert a single Bijoy string back to Unicode Bengali:

```python
unicode_text = avro.to_unicode("Avwg evsjvh় Mvb MvB।")
print(unicode_text)  # আমি বাংলায় গান গাই।
```

For multiple strings, use `avro.to_unicode_iter()`:

```python
unicode_list = avro.to_unicode_iter(['Avwg evsjvh় Mvb MvB।', 'tvmf wkrwb‡¶ jd?'])
print(unicode_list)  # ['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?']
```

### Reversing Back

To reverse a single Unicode Bengali string back to English Roman script:

```python
reversed_text = avro.reverse("আমি বাংলায় গান গাই।")
print(reversed_text)  # ami banglay gan gai.
```

> [!WARNING]
> The reverse functions are by-nature lossy and might not output the correct replacement for some letters in favor of readability sometimes.

To reverse multiple strings at once, use `avro.reverse_iter()`:

```python
rev_list = avro.reverse_iter(['আমি বাংলায় গান গাই।', 'তুমি কোথায় যাও?'])
print(rev_list)  # ['ami banglay gan gai.', 'tumi kothay zaw?']
```

<br>

## Remapped Exceptions

avro.py also contains a built-in collection of words which are pre-baked to be passed into your text without *any* processing. These words can be accessed through both the `parse` and `reverse` functions, so that you do not have to care for phonetics:

> [!NOTE]
> Remapping is a work-in-progress feature. Some words may still be missing.

```python
avro.parse("ami Microsoft e kaj kori")
# আমি মাইক্রোসফট এ কাজ করি
```

## Asynchronous Operations

All of the functions above, when suffixed with `_async`, provide their asynchronous counterparts which have a slight performance bump in certain use cases. Please see the [async examples](https://github.com/hitblast/avro.py/blob/main/examples/async.py) to find out more about their usage.

<br>

## 🛠️ Contributing

:octocat: **Fork -> Do your changes -> Send a Pull Request, it's that easy!** <br>

This project is based on the [uv](https://github.com/astral-sh/uv) package
manager by Astral. In order to automatically update and set up the environment,
you can run the following command:

```sh
# (Optional) Install recommended Python version and
# setup virtual environment for development.
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

## ❤️ Acknowledgements

avro.py would not be possible without the awesome minds behind the original Avro Keyboard software:

- [Mehdi Hasan Khan](https://github.com/mugli)
- [Rifat Nabi](https://github.com/torifat)
- [Sarim Khan](https://github.com/sarim)
- [Kaustav Das Modak](https://github.com/kaustavdm)

And, some awesome people:

- [Arni Bhowmick]()
- [Saleh Sadiq Tanim](https://github.com/TanimSk)
- [Isfer Hossain](https://github.com/furtidev)
- [Md. Abdullah Al Riyad](https://github.com/Itsmemonzu)
- [baseplate-admin](https://github.com/baseplate-admin)

<br>

## License

This project has been licensed under the [MIT License](https://github.com/hitblast/avro.py/blob/main/LICENSE).
