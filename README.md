<!-- SPDX-License-Identifier: MIT -->

<div align="center">

# <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="40px"/> avro.py

A modern Pythonic implementation of the popular Bengali phonetic-typing software **Avro Phonetic.**

[![Downloads](https://static.pepy.tech/personalized-badge/avro-py?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avro-py)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avro.py.svg?color=black&label=License)

<br>

<img src="https://github.com/hitblast/avro.py/blob/main/assets/banner.png" style="width: 500px; height: auto;"><br>

[![Unit Tests](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml)
[![Linting](https://github.com/hitblast/avro.py/actions/workflows/linting.yml/badge.svg)](https://github.com/hitblast/avro.py/actions/workflows/linting.yml)
[![Formatting](https://github.com/hitblast/avro.py/actions/workflows/formatting.yml/badge.svg)](https://github.com/hitblast/avro.py/actions/workflows/formatting.yml)

<br>

</div>

## ⚡ Overview

**avro.py** provides a fully fledged, batteries-included text parser which can parse, reverse and even convert English Roman script into its phonetic equivalent (unicode) of Bengali. At its core, it implements an extensively modified version of the **Avro Phonetic Dictionary Search Library** by [Mehdi Hasan Khan](https://github.com/mugli).

> The original project ([pyAvroPhonetic](https://github.com/kaustavdm/pyAvroPhonetic)) can only be used on versions up to **Python 2.7** and doesn't contain proper support for Python's third major version AKA Python 3. It is noteworthy that Python 2 has officially been deprecated by the original maintainers and its usage is being discouraged overall. <br>

## ✨ Inspirations

This package is inspired from Rifat Nabi's jsAvroPhonetic library and derives from Kaustav Das Modak's pyAvroPhonetic. 

<br>

## 🔨 Installation

This package requires **Python 3.8 or higher** to be used inside your development environment.

```sh
# Install / upgrade.
$ pip install avro.py
```

<br>

## 🔖 Usage Guide

### 1. `parse()`
This is the most basic use case for avro.py, which includes parsing English Roman script to unicode Bengali:

```python
# Imports.
import avro

# Parsing some text.
output = avro.parse('ami banglay gan gai.')
print(output)
```

### 2. `parse(bijoy=True)`
Alternatively, we can generate the same output, but in compliance with the Bijoy Keyboard format:

```python
# Parsing some text in Bijoy!
output = avro.parse('tumi emon keno?', bijoy=True)
```

### 3. `to_bijoy()`
We can also use avro.py to convert existing unicode Bengali to its Bijoy Keyboard equivalent:

```python
# Converting some text.
bijoy_text = avro.to_bijoy('আমি বাংলায় গান গাই।')
```

### 4. `reverse()`
Finally, you can reverse unicode Bengali to English as well (newly added).

```python
# Reversing back!
reversed_text = avro.reverse('আমার সোনার বাংলা।')
```

---

## 🔖 Command Line Usage

Alternatively, instead of using avro.py from within your Python project, you can also use it as a simple,
tiny command-line interface for easy parsing and reversing of text.

```sh
# Installing the package.
$ pip install avro.py[cli]
```

Here are some examples for you to get started with:

```sh
# Main help section.
$ avro --help  # or, use: avro <command> --help

# Parsing some text.
$ avro parse "tumi onek bhalO!"
$ avro parse --bijoy "amio kharap na, taina?"  # (bijoy keyboard format)

# Reversing.
$ avro reverse "তাই তো!"

# Using additional flags to ease workflow.
$ avro parse --from-clip  # (fetching input from clipboard)
$ avro parse "asolei!" --copy  # (copying output to clipboard)
$ avro parse --from-clip --copy  # (clipboard input -> output)
```

<br>

## 🛠️ Contributing

:octocat: *Fork -> Do your changes -> Send a Pull Request, it's that easy!* <br>

---

**Additional Developer Notes**

In short, avro.py doesn't depend on any third-party libraries. However, if you'd like to contribute to the project, you'll need a handful of such useful tools. <br>

- [ruff](https://github.com/astral-sh/ruff) - linter
- [pytest](https://pypi.python.org/pypi/pytest) - testing framework

```sh
# Installing the required developer toolchain.
$ python3 -m pip install -r requirements.txt

# (Optional) Setting up the package itself for testing purposes.
$ python3 setup.py develop

# Running the predetermined tests inside the project.
$ python3 -m pytest --verbose
```

### 🐛 We're looking for bug hunters, by the way!

If you come across any kind of bug or wanna request a feature, please let us know by opening an issue [here](https://github.com/hitblast/avro.py/issues). We do need more ideas to keep the project alive and running, don't we? :P

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
