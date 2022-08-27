"""
The purpose of this file is to define the business logic that the CLI entry point executes to delete relevant crime
records from the DB.
"""

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.utils import get_db_session_obj
from src.internet_forensics.logging.custom_logger import generate_custom_logger

delete_crime_record_logger = generate_custom_logger(name="Delete crime record from the DB")

session_obj = get_db_session_obj()


def delete_crime_record_run(
        name_of_suspect: str
) -> str:
    """
    Delete a relevant crime record from the DB based on the name of a previous suspect.

    Args:
        name_of_suspect: str
                        the name of the suspect for which a crime record needs to be deleted.

    Returns:
            a message (string) confirming that a crime record has been deleted for the relevant suspect.
    """

    if name_of_suspect is None:
        raise ValueError('The name of the suspect for which a crime record needs to be deleted was not provided. '
                         'Please retry and enter it to be able to delete the relevant crime record.')

    # Delete the crime record from the DB based on the name of the suspect
    try:
        session_obj.query(CrimeRecords).filter(CrimeRecords.name_of_suspect == name_of_suspect).delete()

    except Exception as e:
        delete_crime_record_logger.error(e)

    response_w_deleted_crime_record = f"{'The crime record of the suspect named '}" \
                                      f"{name_of_suspect}{' has been deleted.'}"

    return response_w_deleted_crime_record
