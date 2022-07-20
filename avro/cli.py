'''

## Command-line entry point for avro.py

---

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

'''


# Import local modules.
from typing import Tuple

# Import third-party modules.
import click
import pyclip
from rich.console import Console
from rich.table import Table

# Import local modules.
import avro


# Initializing Rich.
console = Console()

# Setting up the default group for Click.
@click.group()
def cli():
    pass


# The main command function (parse, in this case).
@cli.command()
@click.option('-t', '--text', required=True, multiple=True, type=str, help='Text you want to parse.')
def parse(text: str | Tuple[str]) -> None:
    '''
    Parses input text into Bangla, matches and replaces using avrodict.
    '''

    # Form a Table() instance for the --view-table flag.
    table = Table()
    table.add_column("Raw", style="cyan", no_wrap=True, justify="center")
    table.add_column("Bengali (copied to clipboard)", style="magenta", justify="center")

    # Define a new function for pre-processing the texts given by the user.
    def subparse_click(text: str):
        parsed_text = avro.parse(text)
        table.add_row(f'{text}\n', f'{parsed_text}')
        
        return parsed_text

    # Processing.
    parsed = []
    for t in tuple(text):
        parsed.append(subparse_click(t))

    # Post-processing and modifying the clipboard.
    pyclip.copy('\n\n'.join(parsed))

    console.line()
    console.print(table, justify="center")
    console.line()