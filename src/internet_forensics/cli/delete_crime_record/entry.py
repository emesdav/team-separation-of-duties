"""
The purpose of this file is to define a CLI entry point to delete relevant crime records from the DB.
"""

import click

from .run import delete_crime_record_run


@click.command()
@click.option('--name_of_suspect',
              required=True,
              prompt='Enter the name of the suspect',
              help='The name of the suspect.')
def delete_crime_record(
        name_of_suspect: str
) -> None:
    """Entry point to delete a crime record from the DB."""

    click.echo(delete_crime_record_run(name_of_suspect))


if __name__ == '__main__':
    delete_crime_record()
