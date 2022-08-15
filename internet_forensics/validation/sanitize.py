"""
The purpose of this file is to ensure that every input is validated against the expected data type.
"""

import logging
import re
from re import fullmatch
from typing import Union
from .constants import EMAIL_VALID_PATTERN, FIRST_SUB_STRING_VAL_LOG_MSG


# TODO: Insteqd of raising a value error that tells the user who could be an attacker exactly what is happening,
#  We will instead log the error and only return true or false. feedback can be handled by method or etc


class Sanitize:
    """
    This class validates if a value were either an integer, a float, a string, or a valid e-mail address, and
    returns it via the relevant method if so.
    """

    _log = logging.getLogger(__name__)

    def __init__(self, value: Union[float, int, str]):
        if value is not None:
            self.value = value
            self._log.debug(f"{'The value passed is: '}{self.value}")
        else:
            raise ValueError("No value has been provided. Please add a value correctly.")

    def __str__(self):
        return f"<{__class__.__name__} having the input value '{self.value}' to validate>"

    def __repr__(self):
        return f"{__class__.__name__}: (value: '{self.value}')"

    def input_data(self):
        """

        """
        cleaned_string = re.escape(self.value)
        print(cleaned_string)
        return cleaned_string
