# SPDX-License-Identifier: MIT


# Imports.
from typing import Optional

import avro

# Try to import the required modules.
try:
    import click
    import pyclip
except ImportError:
    print('In order to enable CLI, please install avro.py using: pip install avro.py[cli]')
    exit()


# Create a new group for putting the CLI commands.
@click.group(help=avro.__description__)
@click.version_option(
    package_name='avro.py',
    message='Package: %(prog)s, version %(version)s\nCore: version {0}'.format(avro.__version__),
)
def cli() -> None:
    pass


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
            return click.echo('No text provided.')
        else:
            if not (text := pyclip.paste(text=True).strip()):
                return click.echo('No text found in the clipboard.')

    if reverse:
        text = avro.reverse(text)
    else:
        text = avro.parse(text) if not bijoy else avro.parse(text, bijoy=True)

    if copy_on_success:
        pyclip.copy(text)

    click.echo(text)


# usage: avro parse <text> [--bijoy] [--from-clip] [--copy]
@cli.command('parse', help='Parse a given text to Bangla / Bengali.')
@click.argument('text', required=False)
@click.option('--bijoy', is_flag=True, help='Use Bijoy Keyboard format for parsing.')
@click.option('--from-clip', is_flag=True, help='Parse text from clipboard.')
@click.option('--copy', is_flag=True, help='Copy the parsed text to clipboard.')
def _parse(text: str = '', bijoy: bool = False, from_clip: bool = False, copy: bool = False) -> None:
    _cli_action(
        text,
        bijoy=bijoy,
        from_clipboard=from_clip,
        copy_on_success=copy,
    )


# usage: avro reverse <text> [--from-clip] [--copy]
@cli.command('reverse', help='Reverse a given text to English.')
@click.argument('text')
@click.option('--from-clip', is_flag=True, help='Reverse text from clipboard.')
@click.option('--copy', is_flag=True, help='Copy the reversed text to clipboard.')
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
