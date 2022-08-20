"""
The purpose of this file is to define the business logic that the CLI entry point executes to update a crime record
in the DB.
"""

from src.internet_forensics.cli.constants import INITIAL_NUM_OF_CRIMES


# TODO: To change business logic once I know what the schema of the DB is and I have a DB to start querying/consuming.
def update_crime_record(
        num_of_repeated_crimes: int,
        type_of_crime: str,
        name_of_suspect: str,
        address_of_suspect: str
) -> str:
    """
    Update a crime record in the DB and return it.

    Args:
        num_of_repeated_crimes: int
                                the number of repeated crimes.
        type_of_crime: str
                    the type of crime committed.
        name_of_suspect: str
                        the name of the suspect.
        address_of_suspect: str
                        the address of the suspect.

    Returns:
            a string with the details of the updated crime record and the associated suspect (name and address).
    """

    if num_of_repeated_crimes is None and type_of_crime is None and name_of_suspect is None and \
            address_of_suspect is None:
        raise ValueError('None of the details to update were provided. Please enter at least one detail to update and '
                         'retry.')

    time_once = 'once'
    times_twice = 'twice'
    # If a crime were committed more than twice.
    times_three_or_more = f"{num_of_repeated_crimes}{' times'}"

    if num_of_repeated_crimes == INITIAL_NUM_OF_CRIMES:
        times = time_once
    elif num_of_repeated_crimes == 2:
        times = times_twice
    else:
        # Given the usage of 'click.IntRange' in the click option/CLI argument 'num_of_repeated_crimes',
        # this case can only occur if the number of repeated crimes were greater than 2.
        times = times_three_or_more

    response_w_updated_crime_record = f"{'Updated existing record: The crime of type '}{type_of_crime}" \
                                      f"{' has been committed '}{times}{' and the suspect is named '}" \
                                      f"{name_of_suspect}{' and lives at the following address: '}{address_of_suspect}"

    return response_w_updated_crime_record
