# SPDX-License-Identifier: MIT


# Imports.
import avro


# The main function for the cli.
def main():
    # Import click but only if it's available.
    try:
        import click
        import pyclip
    except ImportError:
        return print('In order to enable CLI, please install avro.py using: pip install avro.py[cli]')

    # Define the command group.
    @click.group(help=avro.__description__)
    @click.version_option(
        package_name='avro.py',
        message='Package: %(prog)s, version %(version)s\nCore: version {0}'.format(avro.__version__),
    )
    def cli():
        pass

    # usage: avro parse <text> [--bijoy]
    @cli.command('parse', help='Parse a given text to Bangla / Bengali.')
    @click.argument('text')
    @click.option('--bijoy', is_flag=True, help='Use Bijoy Keyboard format for parsing.')
    @click.option('--from-clipboard', is_flag=True, help='Parse text from clipboard.')
    def _parse(text: str, bijoy: bool = False, from_clipboard: bool = False):
        if text.strip() == '' and from_clipboard:
            text = pyclip.paste(text=True)

            if not text:
                return click.echo('No text found in the clipboard.')

        click.echo((avro.parse(text) if not bijoy else avro.parse(text, bijoy=True)))

    # usage: avro reverse <text>
    @cli.command('reverse', help='Reverse a given text to English.')
    @click.argument('text')
    @click.option('--from-clipboard', is_flag=True, help='Reverse text from clipboard.')
    def _reverse(text: str, from_clipboard: bool = False):
        if text.strip() == '' and from_clipboard:
            text = pyclip.paste(text=True)

            if not text:
                return click.echo('No text found in the clipboard.')

        click.echo(avro.reverse(text))

    # Run the command.
    cli()


# Run the main function.
if __name__ == '__main__':
    main()
