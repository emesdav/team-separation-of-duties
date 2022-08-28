"""
The purpose of this file is to define a CLI entry point to update a crime record in the DB.
"""

import click

from src.internet_forensics.cli.constants import INITIAL_NUM_OF_CRIMES

from .run import update_crime_record_run


@click.command()
@click.option('--num_of_repeated_crimes',
              required=True,
              prompt='Enter the number of repeated crime committed',
              type=click.IntRange(INITIAL_NUM_OF_CRIMES, float("inf")),
              help='Number of repeated crimes of the same type.')
@click.option('--type_of_crime',
              required=True,
              prompt='Enter the type of crime committed',
              help='The type of crime committed.')
@click.option('--name_of_suspect',
              required=True,
              prompt='Enter the name of the suspect',
              help='The name of the suspect.')
@click.option('--address_of_suspect',
              required=True,
              prompt='Enter the address of the suspect',
              help='The address of the suspect.')
def update_crime_record(
        num_of_repeated_crimes: int,
        type_of_crime: str,
        name_of_suspect: str,
        address_of_suspect: str
) -> None:
    """Entry point to update a crime record in the DB."""

    click.echo(
        f"{'Updated crime record: '}{update_crime_record_run(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect)}"
    )


if __name__ == '__main__':
    update_crime_record()
