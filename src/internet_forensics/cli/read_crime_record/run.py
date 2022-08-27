"""
The purpose of this file is to define the business logic that the CLI entry point executes to read relevant crime
records from the DB.
"""

from typing import List

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.constants import READ_ALL_RECORDS
from src.internet_forensics.cli.utils import get_db_session_obj, get_num_repeat_crimes_and_descr
from src.internet_forensics.logging.custom_logger import generate_custom_logger

update_crime_record_logger = generate_custom_logger(name="Read crime record from the DB")

session_obj = get_db_session_obj()


def read_crime_record_run(
        name_of_suspect: str,
        read_all_records: bool = READ_ALL_RECORDS
) -> List[str]:
    """
    Read either all crime records or one based on specific crime records' details from the DB based.

    Args:
        read_all_records: bool
                        whether reading all records (False by default).
        name_of_suspect: str
                        the name of the suspect.

    Returns:
            a list of details (strings) of the relevant crime records and the associated suspect/s (name/s and
            address/es).
    """

    crime_records = session_obj.query(CrimeRecords).all()
    list_of_crime_records = []
    if read_all_records or name_of_suspect is None:

        for crime_record in crime_records:

            times, response_w_read_crime_record = get_num_repeat_crimes_and_descr(crime_record)

            list_of_crime_records.append(response_w_read_crime_record)
    else:
        for crime_record in crime_records:
            if crime_record.name_of_suspect == name_of_suspect:

                times, response_w_read_crime_record = get_num_repeat_crimes_and_descr(crime_record)

                list_of_crime_records.append(response_w_read_crime_record)

    return list_of_crime_records
