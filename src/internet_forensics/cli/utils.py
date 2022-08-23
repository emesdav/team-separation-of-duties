"""
The purpose of this file is to maintain utility-based functions used by the CLI entry points of the application.
"""

from pathlib import Path

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .constants import CRIME_RECORDS_TABLE_NAME, DB_FILE_NAME, SQLITE_PATH_PREFIX

# The declarative base helps to manage the tables
base = declarative_base()


class CrimeRecords(base):

    __tablename__ = CRIME_RECORDS_TABLE_NAME

    name_of_suspect = Column(String, primary_key=True)
    num_of_repeated_crimes = Column(Integer)
    type_of_crime = Column(String)
    address_of_suspect = Column(String)

    def __init__(
            self, num_of_repeated_crimes: int, type_of_crime: str, name_of_suspect: str, address_of_suspect: str
    ) -> None:
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
        """

        self.num_of_repeated_crimes = num_of_repeated_crimes
        self.type_of_crime = type_of_crime
        self.name_of_suspect = name_of_suspect
        self.address_of_suspect = address_of_suspect


def get_db_session_obj(name_of_db_file: str = DB_FILE_NAME) -> sessionmaker:
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
