"""
The purpose of this file is to ensure that every input is validated against the expected data type, also
supporting multi-threading.
"""

from re import fullmatch
from typing import Union

from src.internet_forensics.constants import STATE_FOR_THREAD
from .constants import (
    EMAIL_VALID_PATTERN,
    FIRST_SUB_STRING_VAL_LOG_MSG,
    NAME_OF_DATA_VAL_LOG
)
from ..logging.custom_logger import generate_custom_logger
from ..utilities.multi_threading.multi_thread import threaded


custom_logger = generate_custom_logger(name=NAME_OF_DATA_VAL_LOG)


class Validate:
    """
    This class validates if a value were either an integer, a float, a string, or a valid e-mail address, and
    returns a boolean
    """

    def __init__(self, value: Union[float, int, str]) -> None:
        """
        Args:
            value: Union[float, int, str]
                an input value of either of the above-mentioned data types.
        """
        if value is not None:
            self.value = value
            custom_logger.info(f"{'The value passed is: '}{self.value}")
        else:
            custom_logger.info("No value has been provided. Please add a value correctly.")
            return False

    def __str__(self) -> str:
        return f"<{__class__.__name__} having the input value '{self.value}' to validate>"

    def __repr__(self) -> str:
        return f"{__class__.__name__}: (value: '{self.value}')"

    @threaded
    def if_integer(self) -> int:
        """
        This function validates if a value were an integer and returns a boolean

        Returns:
            boolean
                      for if value was a valid integer or not
        """

        if isinstance(self.value, int):
            custom_logger.info(
              f"{'The following valid integer value has been passed: '}{self.value}"
            )
            if self.value._state == STATE_FOR_THREAD:
                return True
        else:
            custom_logger.info(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'integer: '}{self.value}")
            return False

    @threaded
    def if_string(self) -> str:
        """
        This function validates if a value were a string and returns a boolean

        Returns:
            boolean
                      for if value was a valid string or not
        """

        if isinstance(self.value, str):
            custom_logger.info(
              f"{'The following valid string value has been passed: '}{self.value}"
            )
            if self.value._state == STATE_FOR_THREAD:
                return True
        else:
            custom_logger.info(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'string: '}{self.value}")
            return False

    @threaded
    def if_float(self) -> float:
        """
        This function validates if a value were a float and returns a boolean

        Returns:
            boolean
                      for if value was a valid float or not
        """

        if isinstance(self.value, float):
            custom_logger.info(
              f"{'The following valid float value has been passed: '}{self.value}"
            )
            if self.value._state == STATE_FOR_THREAD:
                return True
        else:
            custom_logger.info(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'float: '}{self.value}")
            return False

    @threaded
    def if_email(self) -> str:
        """
        This function validates if a value were a valid e-mail address based on a RegEx pattern defined in the constant
        EMAIL_VALID_PATTERN and returns it if so.

        Returns:
            boolean
                      for if value was a valid email address or not
        """

        # Enforce to return False as 'fullmatch' returns None.
        is_email_valid = False if fullmatch(EMAIL_VALID_PATTERN, self.value) is None else self.value

        if not is_email_valid:
            custom_logger.info(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'e-mail address: '}{self.value}")
            return False
        else:
            custom_logger.info(
              f"{'The following valid e-mail address has been passed: '}{self.value}"
            )

        if is_email_valid._state == STATE_FOR_THREAD:
            return True
