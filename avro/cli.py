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
import pyperclip3
from rich.console import Console
from rich.table import Table

# Import local modules.
import avro

# Initializing Rich
console = Console()
table = Table(show_edge=False, box=None)

# Setting up the default group for Click.
@click.group()
def cli():
    pass


# The main command function (parse, in this case).
@cli.command()
@click.option('-t', '--text', required=True, multiple=True, type=str, help='Text you want to parse.')
@click.option('--copy', help='Copies the result to clipboard.', is_flag=True)
def parse(text: str | Tuple[str], copy: bool):
    '''
    Parses input text into Bangla, matches and replaces using avrodict.
    '''

    def subparse_click(text: str):
        parsed_text = avro.parse(text)
        table.add_column("Raw", style="cyan", no_wrap=True, justify="center")
        table.add_column("Bengali", style="magenta", justify="center")

        table.add_row(f'{text}', f'{parsed_text}')
        console.print("\n")
        console.print(table, justify="center")
        return parsed_text

    parsed = []
    click.echo()
    for t in tuple(text):
        parsed.append(subparse_click(t))
            
    if copy:
        pyperclip3.copy('\n\n'.join(parsed))