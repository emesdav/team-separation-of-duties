"""
The purpose of this file is to ensure that every input is validated against the expected data type.
"""

import logging
from re import fullmatch
from typing import Union
from .validate_constants import EMAIL_VALID_PATTERN, FIRST_SUB_STRING_VAL_LOG_MSG


# TODO: Insteqd of raising a value error that tells the user who could be an attacker exactly what is happening,
#  We will instead log the error and only return true or false. feedback can be handled by method or etc


class Validate:
    """
    This class validates if a value were either an integer, a float, a string, or a valid e-mail address, and
    returns it via the relevant method if so.
    """

    _log = logging.getLogger(__name__)

    def __init__(self, value: Union[float, int, str]):
        """
        Args:
            value: Union[float, int, str]
                an input value of either of the above-mentioned data types.
        """
        if value is not None:
            self.value = value
            self._log.debug(f"{'The value passed is: '}{self.value}")
        else:
            raise ValueError("No value has been provided. Please add a value correctly.")

    def __str__(self):
        return f"<{__class__.__name__} having the input value '{self.value}' to validate>"

    def __repr__(self):
        return f"{__class__.__name__}: (value: '{self.value}')"

    def if_integer(self):
        """
        This function validates if a value were an integer and returns it if so.

        Returns:
            self.value: int
                      the integer value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, int):
            self._log.info(
                f"{'The following valid integer value has been passed: '}{self.value}"
            )
            return True
        else:
            # raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'integer: '}{self.value}")
            return False

    def if_string(self):
        """
        This function validates if a value were a string and returns it if so.

        Returns:
            self.value: str
                      the string value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, str):
            self._log.info(
                f"{'The following valid string value has been passed: '}{self.value}"
            )
            return True
        else:
            # raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'string: '}{self.value}")
            return False

    def if_float(self):
        """
        This function validates if a value were a float and returns it if so.

        Returns:
            self.value: float
                      the float value if validated; otherwise, it logs an error.
        """

        if isinstance(self.value, float):
            self._log.info(
                f"{'The following valid float value has been passed: '}{self.value}"
            )
            return True
        else:
            # raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'float: '}{self.value}")
            return False

    def if_email(self):
        """
        This function validates if a value were a valid e-mail address based on a RegEx pattern defined in the constant
        EMAIL_VALID_PATTERN and returns it if so.

        Returns:
            self.value: str
                      the string value with a valid e-mail address if validated; otherwise, it logs an error.
        """

        # Enforce to return False as 'fullmatch' returns None.
        is_email_valid = False if fullmatch(EMAIL_VALID_PATTERN, self.value) is None else True
        if not is_email_valid:
            # raise ValueError(f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'e-mail address: '}{self.value}")
            return False
        else:
            self._log.info(
                f"{'The following valid e-mail address has been passed: '}{self.value}"
            )
        return is_email_valid
