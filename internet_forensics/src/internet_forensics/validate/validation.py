"""
The purpose of this file is to ensure that every input is validated against the expected data type.
"""

import os

from re import fullmatch
from typing import Union

from .constants import (
    EMAIL_VALID_PATTERN,
    FIRST_SUB_STRING_VAL_LOG_MSG,
    FOLDER_NAME_LOG_FILE,
    NAME_OF_DATA_VAL_LOG
)
from ..logging.custom_logger import generate_custom_logger

# Get current working directory's path and then create output folder to save .log file.
current_wd_path = os.path.abspath(os.getcwd())
output_dir_log = os.path.join(current_wd_path, FOLDER_NAME_LOG_FILE)
os.makedirs(output_dir_log, exist_ok=True)

custom_logger = generate_custom_logger(output_folder=output_dir_log, name=NAME_OF_DATA_VAL_LOG)


class Validate:
    """
    This class validates if a value were either an integer, a float, a string, or a valid e-mail address, and
    returns it via the relevant method if so.
    """

    def __init__(self, value: Union[float, int, str]) -> None:
        """
        Args:
            value: Union[float, int, str]
                an input value of either of the above-mentioned data types.
        """
        if value is not None:
            self.value = value
            custom_logger.debug(f"{'The value passed is: '}{self.value}")
        else:
            raise ValueError("No value has been provided. Please add a value correctly.")

    def __str__(self) -> str:
        return f"<{__class__.__name__} having the input value '{self.value}' to validate>"

    def __repr__(self) -> str:
        return f"{__class__.__name__}: (value: '{self.value}')"

    def validate_integer(self) -> int:
        """
        This function validates if a value were an integer and returns it if so.

        Returns:
            self.value: int
                      the integer value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, int):
            custom_logger.info(
              f"{'The following valid integer value has been passed: '}{self.value}"
            )
            return self.value
        else:
            raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'integer: '}{self.value}")

    def validate_string(self) -> str:
        """
        This function validates if a value were a string and returns it if so.

        Returns:
            self.value: str
                      the string value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, str):
            custom_logger.info(
              f"{'The following valid string value has been passed: '}{self.value}"
            )
            return self.value
        else:
            raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'string: '}{self.value}")

    def validate_float(self) -> float:
        """
        This function validates if a value were a float and returns it if so.

        Returns:
            self.value: float
                      the float value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, float):
            custom_logger.info(
              f"{'The following valid float value has been passed: '}{self.value}"
            )
            return self.value
        else:
            raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'float: '}{self.value}")

    def validate_email(self) -> str:
        """
        This function validates if a value were a valid e-mail address based on a RegEx pattern defined in the constant
        EMAIL_VALID_PATTERN and returns it if so.

        Returns:
            self.value: str
                      the string value with a valid e-mail address if validated; otherwise, it logs an error.
        """

        # Enforce to return False as 'fullmatch' returns None.
        is_email_valid = False if fullmatch(EMAIL_VALID_PATTERN, self.value) is None else self.value
        if not is_email_valid:
            raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'e-mail address: '}{self.value}")
        else:
            custom_logger.info(
              f"{'The following valid e-mail address has been passed: '}{self.value}"
            )
        return is_email_valid
