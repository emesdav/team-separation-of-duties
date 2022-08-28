"""
The purpose of this file is to define the business logic that the CLI entry point executes to update a crime record
in the DB.
"""

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.utils import get_db_session_obj, get_num_repeat_crimes_and_descr
from src.internet_forensics.logging.custom_logger import generate_custom_logger

update_crime_record_logger = generate_custom_logger(name="Update crime record in the DB")

session_obj = get_db_session_obj()


def update_crime_record_run(
        num_of_repeated_crimes: int,
        type_of_crime: str,
        name_of_suspect: str,
        address_of_suspect: str
) -> str:
    """
    Update a crime record in the DB based on the name of the suspect and return it.

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

    crime_record = CrimeRecords(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect)

    times, response_w_updated_crime_record = get_num_repeat_crimes_and_descr(crime_record)

    # Update the crime record into the DB based on the name of the suspect
    try:
        session_obj.query(CrimeRecords).filter(
            CrimeRecords.name_of_suspect == name_of_suspect).\
            update(
            {
                "num_of_repeated_crimes": num_of_repeated_crimes,
                "type_of_crime": type_of_crime,
                "address_of_suspect": address_of_suspect
            }, synchronize_session="fetch")
        session_obj.commit()
    except Exception as e:
        update_crime_record_logger.error(e)

    return response_w_updated_crime_record
