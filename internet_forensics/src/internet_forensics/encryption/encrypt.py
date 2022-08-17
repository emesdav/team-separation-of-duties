import os
import bcrypt

from internet_forensics.src.internet_forensics.encryption.constants import FOLDER_NAME_LOG_FILE, NAME_OF_DATA_VAL_LOG
from ..logging.custom_logger import generate_custom_logger

"""
This file's purpose is to provide encryption features to all the system 
using Bcrypt library that follows cryptography security standards
"""

current_wd_path = os.path.abspath(os.getcwd())
output_dir_log = os.path.join(current_wd_path, FOLDER_NAME_LOG_FILE)
os.makedirs(output_dir_log, exist_ok=True)

custom_logger = generate_custom_logger(
    output_folder=output_dir_log, name=NAME_OF_DATA_VAL_LOG)


class encrypt():

    """
    This method hashes a password passed in string type converting it to byte string
    """
    def hash_pssw(password):

        # generating a bytestring
        pssw = password.encode('utf-8')

        # generating hashed password with random salt
        hashed = bcrypt.hashpw(pssw, bcrypt.gensalt())

        return hashed

    """
    This method checks if the unhashed password(string type) matches the hashed password coming from DB, no conversions needed
    returns true if password matches, returns false if password doesn't match
    """
    def check_pssw(password, hashed_password):

        # check if the hashed password matches the non-hashed one
        if bcrypt.checkpw(password, hashed_password):
            custom_logger.debug("It Matches!")
            return True
        else:
            custom_logger.debug("It Does not Match :(")
            return False
