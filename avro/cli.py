# SPDX-License-Identifier: MIT


# Imports.
import avro


# The main function for the cli.
def main():
    # Import click but only if it's available.
    try:
        import click
    except ImportError:
        return print('In order to enable CLI, please install avro.py using: pip install avro.py[cli]')

    # Define the command group.
    @click.group(help='(CLI) A modern Pythonic implementation of Avro Phonetic.')
    def cli():
        pass

    # usage: avro parse <text> [--bijoy]
    @cli.command('parse', help='Parse a given text to Bangla / Bengali.')
    @click.argument('text')
    @click.option('--bijoy', is_flag=True, help='Use Bijoy Keyboard format for parsing.')
    def _parse(text: str, bijoy: bool = False):
        click.echo((avro.parse(text) if not bijoy else avro.parse(text, bijoy=True)))

    # usage: avro tobijoy <text>
    @cli.command('tobijoy', help='Convert a given text to Bijoy Keyboard format.')
    @click.argument('text')
    def _tobijoy(text: str):
        click.echo(avro.to_bijoy(text))

    # usage: avro reverse <text>
    @cli.command('reverse', help='Reverse a given text to English.')
    @click.argument('text')
    def _reverse(text: str):
        click.echo(avro.reverse(text))

    # Run the command.
    cli()


# Run the main function.
if __name__ == '__main__':
    main()
