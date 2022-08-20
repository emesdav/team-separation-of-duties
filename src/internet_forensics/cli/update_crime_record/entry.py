"""
The purpose of this file is to define a CLI entry point to update a crime record in the DB.
"""

import click

from src.internet_forensics.cli.constants import INITIAL_NUM_OF_CRIMES

import run


# TODO: To change click options/CLI arguments once I know what the schema of the DB is and I have a DB to start
#  querying/consuming.
@click.command()
@click.option('--num_of_repeated_crimes',
              required=False,
              type=click.IntRange(INITIAL_NUM_OF_CRIMES, float("inf")),
              help='Number of repeated crimes of the same type.')
@click.option('--type_of_crime',
              required=False,
              help='The type of crime committed.')
@click.option('--name_of_suspect',
              required=False,
              help='The name of the suspect.')
@click.option('--address_of_suspect',
              required=False,
              help='The address of the suspect.')
def update_crime_record(
        num_of_repeated_crimes: int,
        type_of_crime: str,
        name_of_suspect: str,
        address_of_suspect: str
) -> None:
    """Entry point to update a crime record in the DB."""

    click.echo(run.update_crime_record(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect))
