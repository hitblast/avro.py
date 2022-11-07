# avro.py

A modern Pythonic implementation of the popular Bengali phonetic-typing software **Avro Phonetic.**

[![Unit Tests](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml/badge.svg?branch=main)](https://github.com/hitblast/avro.py/actions/workflows/unit-tests.yml)
[![Linting](https://github.com/hitblast/avro.py/actions/workflows/linting.yml/badge.svg?branch=main)](https://github.com/hitblast/avro.py/actions/workflows/linting.yml)
[![Downloads](https://static.pepy.tech/personalized-badge/avro-py?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avro-py)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avro.py.svg?color=black&label=License)

<br>

## Overview

**avro.py**, whilst being a Python package, provides a text parser that converts Bangla text written in Roman script to its phonetic equivalent of Bangla. It implements the **Avro Phonetic Dictionary Search Library** by [Mehdi Hasan Khan](https://github.com/mugli).

The original project [pyAvroPhonetic](https://github.com/kaustavdm/pyAvroPhonetic) is based on Python 2 and can only work on versions up to **Python 2.7**. It is noteworthy that Python 2 has officially been deprecated by the original maintainers and its usage is being discouraged overall. <br>

## Inspirations

This package is inspired from **Rifat Nabi's jsAvroPhonetic** library and derives from **Kaustav Das Modak's pyAvroPhonetic.**

<br>

## Installation

Installing avro.py in your project is pretty straightforward. Run the command mentioned below (requires **Python 3.8 or higher**):

```bash
# install / upgrade
$ pip install avro.py
```

<br>

## Usage Guide
As of now, you can easily use the package by importing the module and calling the primary `parse` function.

```python
import avro

parsed_text = avro.parse('ami banglay gan gai.')
print(parsed_text)

# আমি বাংলায় গান গাই।
```

Also, you can reverse it Bangla text to English typed Bangla text for readability

```python
import avro

reversed_text = avro.reverse('আমার সোনার বাংলা।')
print(reversed_text)

# amar sonar bangla.
```

Other use cases include [your terminal](https://github.com/hitblast/avro.py-cli), literally!

<br>

## Contributing

:octocat: *Fork -> Do your changes -> Send a Pull Request, it's that easy!*

<br>

---


**Additional Developer Notes**

The coding style for this project embraces readability and consistency over traditional styling methods. To start off, [flake8](https://flake8.pycqa.org/en/latest/) has been used as the primary linting tool. The unit tests are done using the [pytest](https://pypi.python.org/pypi/pytest) framework.

```bash
# Installing the required developer toolchain.
$ python3 -m pip install -r dev-requirements.txt

# Running pytest.
$ python3 -m pytest --verbose

# The results should appear onwards.
# The --verbose / -v flag is used to show all the test results in detail.
```

<br>

### We're looking for bug hunters!

If you come across any kind of bug or wanna request a feature, please let us know by opening an issue [here](https://github.com/hitblast/avro.py/issues). We do need more ideas to keep the project alive and running, don't we? :P

---

<br>

## Acknowledgements

- [Mehdi Hasan Khan](https://github.com/mugli) for originally developing and maintaining [Avro Phonetic](https://github.com/omicronlab/Avro-Keyboard).
- [Rifat Nabi](https://github.com/torifat) for porting it to Javascript.
- [Sarim Khan](https://github.com/sarim) for writing ibus-avro which helped to clarify my concepts further.
- [Kaustav Das Modak](https://github.com/kaustavdm) for porting Rifat Nabi's JavaScript iteration to Python 2.
- Md Enzam Hossain for helping him understand the ins and outs of the Avro dictionary and the way it works.

<br>

## License

```
MIT License

Copyright (c) 2022 HitBlast

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

The original license text can be found [in this document.](https://github.com/hitblast/avro.py/blob/main/LICENSE)
