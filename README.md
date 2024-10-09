<!-- SPDX-License-Identifier: MIT -->

<div align="center">

# <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="40px"/> avro.py

A modern Pythonic implementation of the popular Bengali phonetic-typing software **Avro Phonetic.**

[![Downloads](https://static.pepy.tech/personalized-badge/avro-py?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avro-py)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avro.py.svg?color=black&label=License)

<br>

<img src="https://github.com/hitblast/avro.py/blob/main/assets/banner.png?raw=True" style="width: 500px; height: auto;"><br>

[![Unit Tests](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml)
[![Nightly Builds](https://github.com/hitblast/avro.py/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/hitblast/avro.py/actions/workflows/nightly.yml)
[![Linting](https://github.com/hitblast/avro.py/actions/workflows/linting.yml/badge.svg)](https://github.com/hitblast/avro.py/actions/workflows/linting.yml)
[![Formatting](https://github.com/hitblast/avro.py/actions/workflows/formatting.yml/badge.svg)](https://github.com/hitblast/avro.py/actions/workflows/formatting.yml)

<br>

</div>

## ⚡ Overview

**avro.py** provides a fully fledged, batteries-included text parser which can parse, reverse and even convert English Roman script into its phonetic equivalent (unicode) of Bengali. At its core, it implements an extensively modified version of the **Avro Phonetic Dictionary Search Library** by [Mehdi Hasan Khan](https://github.com/mugli).

> Update: As of October 2024, Python 3.8 has reached its EOL, so for keeping this project updated, the minimum required version will be Python 3.9 from now onwards. It is strongly suggested that you migrate your project for better compatibility. <br>

## ✨ Inspirations

This package is inspired from Rifat Nabi's jsAvroPhonetic library and derives from Kaustav Das Modak's pyAvroPhonetic.

<br>

## 🔨 Installation

This package requires **Python 3.9 or higher** to be used inside your development environment.

```sh
# Install / upgrade.
$ pip install avro.py
```

#### 📦 ...or you can try the CLI!

[**avnie**](https://github.com/hitblast/avnie) is a newly developed CLI tool that uses avro.py under the hood. You can install it using:

```sh
# Install / upgrade avnie.
$ pip install avnie
```

<br>

## 🔖 Usage Guide

This small tour guide will describe how you can use avro.py back and forth to operate (cutlery!) on Bengali text. You can also check the [examples](https://github.com/hitblast/avro.py/tree/main/examples) directory for checking [this whole snippet](https://github.com/hitblast/avro.py/blob/main/examples/simple.py) in action, as well as other use cases.

#### 1. `parse()`

Let's assume I want to parse some English text to Bengali, which is "ami banglay gan gai.", so in this case to convert it to Bengali, we can use this snippet:

```python
# Import the package.
import avro

# Our dummy text.
dummy = 'ami banglay gan gai.'

# Parsing the text.
avro_output = avro.parse(dummy)
print(output)  # Output: আমি বাংলায় গান গাই।
```

#### 2. `parse(bijoy=True)`

Alternatively, I can also do it in Bijoy Keyboard format:

```python
# Parsing in Bijoy.
bijoy_output = avro.parse(dummy, bijoy=True)  # Output: Avwg evsjvh় Mvb MvB।
```

#### 3. `to_bijoy()`

Or, we can take the previous `avro_output` and convert it to Bijoy if we want to, like this:

```python
# Converting to Bijoy.
bijoy_text = avro.to_bijoy(avro_output)  # Output: Avwg evsjvh় Mvb MvB।
```

#### 4. `to_unicode()`

Conversely, we can convert the Bijoy text we got just now and convert it back to Unicode Bengali:

```python
# Converting back!
unicode_text = avro.to_unicode(bijoy_text)  # Output: আমি বাংলায় গান গাই।
```

#### 4. `reverse()`

Finally, we can just reverse back to the original text we passed as input in the first place:

```python
# Reversing back!
reversed_text = avro.reverse(uncode_text)  # Output: ami banglay gan gai.
```

<br>

## 🛠️ Contributing

:octocat: _Fork -> Do your changes -> Send a Pull Request, it's that easy!_ <br>

---

**Additional Developer Notes**

In short, avro.py doesn't depend on any third-party libraries. However, if you'd like to contribute to the project, you'll need a handful of such useful tools.

**Poetry** has been used to manage the project's dependencies and virtual environment. You can install it by following [the instructions here](https://python-poetry.org/docs/). The dependencies have been configured using the `pyproject.toml` file and doesn't require manual installation. Simply set up your developer environment using the following commands: <br>

```sh
# Set up virtual environment and activate it.
$ python3 -m venv venv && source venv/bin/activate

# Setup project using Poetry.
$ make install  # same as `poetry install --sync --no-interaction`

# Perform updates on lockfile.
$ poetry update
```

Later, you can run the tests provided with the project using the following command. This option has already been configured in the "Testing" panel if you're using Visual Studio Code as your primary IDE.

```sh
# Run unit tests.
$ make test  # same as `poetry run pytest .`

# Build sdist and wheel packages for distributing the project.
$ make build  # same as `poetry build --verbose --no-interaction`
```

<br>

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
