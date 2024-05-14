# SPDX-License-Identifier: MIT


# Imports.
from typing import Optional

import avro

# Try to import the required modules.
try:
    import click
    import pyclip
    from rich.console import Console

except ImportError:
    print("In order to enable CLI, please install avro.py using: pip install avro.py[cli]")
    exit()


# Create a new group for putting the CLI commands.
@click.group(help="A modern Pythonic implementation of Avro Phonetic.")
@click.version_option(
    package_name="avro.py",
    message="Package: %(prog)s, version %(version)s\n",
)
def cli() -> None:
    pass


# Initialize Console object for rich-based output.
console = Console()


# Helper functions for CLI commands.
def _print_err(text: str) -> None:
    console.print(text, style="red")
    return click.echo(err=True)


# Helper function for CLI actions.
def _cli_action(
    text: str,
    *,
    bijoy: bool = False,
    from_clipboard: bool = False,
    copy_on_success: bool = False,
    reverse: bool = False,
) -> Optional[str]:
    if not text:
        if not from_clipboard:
            return _print_err("No text provided.")
        else:
            if not (text := pyclip.paste(text=True).strip()):
                return _print_err("No text found in the clipboard.")

    if reverse:
        output = avro.reverse(text)
    else:
        output = avro.parse(text) if not bijoy else avro.parse(text, bijoy=True)

    if output == text:
        return _print_err("No changes in output.")

    console.print(f"\n[bold green]Output[/bold green]\n {output}\n")

    if copy_on_success:
        pyclip.copy(text)
        console.print("[bold yellow](copied to clipboard)[/bold yellow]\n")


# usage: avro parse <text> [--bijoy] [--from-clip] [--copy]
@cli.command("parse", help="Parse a given text to Bangla / Bengali.")
@click.argument("text", required=False)
@click.option("--bijoy", is_flag=True, help="Use Bijoy Keyboard format for parsing.")
@click.option("--from-clip", is_flag=True, help="Parse text from clipboard.")
@click.option("--copy", is_flag=True, help="Copy the parsed text to clipboard.")
def _parse(text: str = "", bijoy: bool = False, from_clip: bool = False, copy: bool = False) -> None:
    _cli_action(
        text,
        bijoy=bijoy,
        from_clipboard=from_clip,
        copy_on_success=copy,
    )


# usage: avro reverse <text> [--from-clip] [--copy]
@cli.command("reverse", help="Reverse a given text to English.")
@click.argument("text")
@click.option("--from-clip", is_flag=True, help="Reverse text from clipboard.")
@click.option("--copy", is_flag=True, help="Copy the reversed text to clipboard.")
def _reverse(text: str, from_clip: bool = False, copy: bool = False) -> None:
    _cli_action(
        text,
        from_clipboard=from_clip,
        copy_on_success=copy,
        reverse=True,
    )


# Run the main function.
def main() -> None:
    cli()
