"""
The purpose of this file is to define a CLI entry point to read relevant crime records from the DB.
"""

import click

from .run import read_crime_record_run


@click.command()
@click.option('--name_of_suspect',
              required=True,
              prompt='Enter the name of the suspect',
              help='The name of the suspect.')
@click.option(
    '--read_all_records', '-v', is_flag=True, help="Read all records only if this command line argument were provided"
)
def read_crime_record(
        name_of_suspect: str,
        read_all_records: bool
) -> None:
    """Entry point to read a crime record from the DB."""

    click.echo(
        f"{'Read crime record: '}{read_crime_record_run(name_of_suspect, read_all_records)}"
    )


if __name__ == '__main__':
    read_crime_record()
