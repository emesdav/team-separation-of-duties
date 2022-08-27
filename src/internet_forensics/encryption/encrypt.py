"""
This file's purpose is to provide encryption features to the system
using the 'bcrypt' library that adheres to cryptography security standards.
"""

import os

import bcrypt

from src.internet_forensics.encryption.constants import (ENCODING_METHOD,
                                                         FOLDER_NAME_LOG_FILE,
                                                         NAME_OF_DATA_VAL_LOG)

from ..logging.custom_logger import generate_custom_logger
from ..utilities.multi_threading.multi_thread import threaded

current_wd_path = os.path.abspath(os.getcwd())
output_dir_log = os.path.join(current_wd_path, FOLDER_NAME_LOG_FILE)
os.makedirs(output_dir_log, exist_ok=True)

custom_logger = generate_custom_logger(
    output_folder=output_dir_log, name=NAME_OF_DATA_VAL_LOG)


class Encrypt:

    @threaded
    def hash_password(self, password: str) -> bytes:
        """
        Hash a password and convert it to byte string. Then, encrypt it with random-generated salts and return
        the encrypted password.

        Args:
            password: str
                    the password entered by a user.

        Returns: bytes
                the hashed password in the DB.
        """

        # Generate a bytestring
        password = password.encode(ENCODING_METHOD)

        # Generate hashed password with random salt
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        return hashed_password

    @threaded
    def check_password(self, password: str, hashed_password: bytes) -> bool:
        """
        Check if the un-hashed password matches the hashed password coming from the DB.

        Args:
            password: str
                    the password entered by a user.
            hashed_password: str
                    the hashed password in the DB.

        Returns: bool
            True if the password matches the hashed password, False otherwise.
        """

        if bcrypt.checkpw(password.encode(ENCODING_METHOD), hashed_password):
            custom_logger.debug(f"The password '{password}' matches the hashed password '{hashed_password}'.")
            return True
        else:
            custom_logger.debug(f"The password '{password}' does not match the hashed password '{hashed_password}'.")
            return False
