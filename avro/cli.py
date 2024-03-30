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
    @click.group()
    def cli():
        pass

    # usage: avro parse <text>
    @cli.command('parse', help='Parse a given text to Bangla.')
    @click.argument('text')
    def _parse(text: str):
        click.echo(avro.parse(text))

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
