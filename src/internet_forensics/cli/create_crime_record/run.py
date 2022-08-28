"""
The purpose of this file is to define the business logic that the CLI entry point executes to create a crime record
in the DB.
"""

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.constants import INITIAL_NUM_OF_CRIMES
from src.internet_forensics.cli.utils import get_db_session_obj
from src.internet_forensics.logging.custom_logger import generate_custom_logger

custom_logger = generate_custom_logger(name="Create crime record in the DB")

session_obj = get_db_session_obj()


def create_crime_record_run(
        num_of_repeated_crimes: int,
        type_of_crime: str,
        name_of_suspect: str,
        address_of_suspect: str
) -> str:
    """
    Create a crime record in the DB and return it.

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
            a string with the details of the crime record created and the associated suspect (name and address).
    """

    if num_of_repeated_crimes == INITIAL_NUM_OF_CRIMES:
        times = 'once'
    else:
        raise ValueError(f"The number of repeated crimes you entered ('{num_of_repeated_crimes}' is incorrect, as it "
                         f"should be {INITIAL_NUM_OF_CRIMES} initially. Please retry and enter {INITIAL_NUM_OF_CRIMES} "
                         f"to start creating a new crime record in the database.)")

    response_w_created_crime_record = f"{'Created new record: The crime of type '}{type_of_crime}" \
                                      f"{' has been committed '}{times}{' and the suspect is named '}" \
                                      f"{name_of_suspect}{' and lives at the following address: '}{address_of_suspect}"

    crime_record_to_add = CrimeRecords(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect)

    # Insert the crime record into the DB
    try:
        session_obj.add(crime_record_to_add)
        session_obj.commit()
    except Exception as e:
        custom_logger.error(e)

    return response_w_created_crime_record
