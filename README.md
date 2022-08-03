# avro.py

A modern Pythonic implementation of the popular Bengali phonetic-typing software **Avro Phonetic.**

[![Code Checks](https://github.com/hitblast/avro.py/actions/workflows/code-checks.yml/badge.svg?branch=main&event=push)](https://github.com/hitblast/avro.py/actions/workflows/code-checks.yml)
[![Downloads](https://static.pepy.tech/personalized-badge/avro-py?period=total&units=international_system&left_color=grey&right_color=black&left_text=Downloads)](https://pepy.tech/project/avro-py)
![Python Version](https://img.shields.io/pypi/pyversions/avro.py.svg?color=black&label=Python)
![License](https://img.shields.io/pypi/l/avro.py.svg?color=black&label=License)

<br>

## Overview

**avro.py**, whilst being a Python package, provides a text parser that converts Bangla text written in Roman script to its phonetic equivalent of Bangla. It implements the **Avro Phonetic Dictionary Search Library** by [Mehdi Hasan Khan](https://github.com/mugli).

This library is based on the syntax of Python 3.10. That being said, the latest tested / supported version of Python with this project is **Python 3.10.5**. However, the original project [pyAvroPhonetic](https://github.com/kaustavdm/pyAvroPhonetic) is based on Python 2 and can only work on versions up to **Python 2.7**. It is noteworthy that Python 2 has officially been deprecated by the original maintainers and its usage is being discouraged overall.

<br>

## Inspirations

This package is inspired from [Rifat Nabi's jsAvroPhonetic](https://github.com/torifat/jsAvroPhonetic) library and derives from [Kaustav Das Modak's pyAvroPhonetic](https://github.com/kaustavdm/pyAvroPhonetic). 

<br>

## Installation

Installing Bangla phonetics via Avro inside your workspace is now easier than ever. Make sure you have installed [Python 3.10](https://www.python.org/downloads/) (or later) in your local machine. If it is already installed, then we can proceed with the following commands:

```bash
# Create a virtual environment named "venv". (1)
python3 -m venv venv 

# Activate the virtual environment. (2)
source venv/bin/activate 

# Install the package. (3)
pip install avro.py
```

- This will create a new virtual environment in your working diretory and install avro.py inside it.

- In order to use the package, the virtual environment has to be activated every time you start working on your personal project.

- If you already have a virtual environment set up / you don't need one, then you can skip the first two steps and proceed with a vanilla configuration using [Pip](https://pypi.python.org/pypi/pip).

<br>

## Usage
As of now, you can easily use the package by importing the module and calling the primary `parse` function.

```python
import avro

parsed_text = avro.parse('ami banglay gan gai.')
print(parsed_text)
```

Alternatively, you can use the built-in command line tool for parsing texts without writing code!
```bash
# Get help regarding the CLI inside your terminal.
python3 -m avro --help 
avro --help # Minified, both of them can work depending on your environment.

# Parse a text.
avro parse --text "ami banglay gan gai."
avro parse -t "eije dekh waTar." # Minified --text option.

# Parse multiple texts.
avro parse -t "amar swopnera" -t "Dana mele ure cole" -t "obarito nIle."
```

<br>

## Contributing

:octocat: *Fork -> Do your changes -> Send a Pull Request, it's that easy!*

<br>

---


**Additional Developer Notes**

The coding style for this project embraces readability and consistency over traditional styling methods. To start off, [flake8](https://flake8.pycqa.org/en/latest/) has been used as the primary linting tool. The unit tests are done using the [pytest](https://pypi.python.org/pypi/pytest) framework. The command line tool, on the other hand, is made using [Click](https://pypi.python.org/pypi/click) and the [Rich](https://github.com/Textualize/rich) framework. Coupled with the CLI, [PyClip](https://pypi.python.org/pypi/pyclip) has been used to implement clipboard functionality into the library.

If you want to set up your coding environment for this project, then you can do so by running the following command in your terminal:

```bash
pip install -r tests/requirements.txt
```

This will install all the required packages to test/develop over avro.py, and to make things simpler, you can run the command mentioned below to test the project:

```bash
python3 -m pytest --verbose

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