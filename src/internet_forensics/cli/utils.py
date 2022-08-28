"""
The purpose of this file is to maintain utility-based functions used by the CLI entry points of the application.
"""

from pathlib import Path
from typing import Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.internet_forensics.database.db import CrimeRecords
from ..constants import DB_FILE_NAME, SQLITE_PATH_PREFIX
from ..cli.constants import INITIAL_NUM_OF_CRIMES


def get_db_session_obj(name_of_db_file: str = DB_FILE_NAME) -> sessionmaker:  # pragma: no cover
    """
    Get the DB's session object.

    Args:
        name_of_db_file: str
                        the name of the DB (.db) file.

    Returns:
            the DB session maker.
    """

    # Get absolute path to .db file based on input file name.
    # This is important to ensure that the 'create_engine' function below allows to find the .db file and connect to
    # it thereafter.
    path_to_db_file = Path(name_of_db_file).resolve()
    str_path_to_db_file = str(path_to_db_file)

    # Create session to connect to the DB
    engine = create_engine(f"{SQLITE_PATH_PREFIX}{str_path_to_db_file}")
    SessionMaker = sessionmaker(bind=engine)
    session_obj = SessionMaker()

    return session_obj


def get_num_repeat_crimes_and_descr(crime_record: CrimeRecords) -> Tuple[str, str]:
    """
    Get the number of times a crime has been repeated and a crime's full description based on a crime record.

    Args:
        crime_record: CrimeRecords
                    an instance of a crime record.

    Returns:
            a tuple with the number of times (string) a crime has been repeated and a crime's full description (string).
    """

    if crime_record.num_of_repeated_crimes == INITIAL_NUM_OF_CRIMES:
        times = 'once'
    elif crime_record.num_of_repeated_crimes == 2:
        times = 'twice'
    else:
        # Given the usage of 'click.IntRange' in the click option/CLI argument 'num_of_repeated_crimes',
        # this case can only occur if the number of repeated crimes were greater than 2.
        times = f"{crime_record.num_of_repeated_crimes}{' times'}"

    response_w_read_crime_record = f"{'The crime of type '}{crime_record.type_of_crime}" \
                                   f"{' has been committed '}{times}" \
                                   f"{' and the suspect is named '}" \
                                   f"{crime_record.name_of_suspect}{' and lives at the following address: '}" \
                                   f"{crime_record.address_of_suspect}"

    return times, response_w_read_crime_record
