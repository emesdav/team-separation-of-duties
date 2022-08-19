import unittest

from src.internet_forensics.validate.validation import Validate

VALID_FLOAT = 5.
VALID_INTEGER = 5
VALID_STRING = 'Koala'
INVALID_FLOAT = VALID_STRING
INVALID_INTEGER = VALID_STRING
INVALID_STRING = VALID_INTEGER
VALID_EMAIL = 'dr_sheldon@cooper.com'
INVALID_EMAIL = 'dr_sheldon-not_nobel_prize_winner.com'

FIRST_SUB_STRING_VAL_LOG_MSG = "The following value is not a valid "

STATE_FOR_THREAD = 'FINISHED'


class TestValidation(unittest.TestCase):

    def test___str__(self):
        expected_str = f"<{Validate.__name__} having the input value '{VALID_FLOAT}' to validate>"
        self.assertEqual(expected_str, Validate(VALID_FLOAT).__str__())

    def test___repr__(self):
        expected_repr = f"{Validate.__name__}: (value: '{VALID_FLOAT}')"
        self.assertEqual(expected_repr, Validate(VALID_FLOAT).__repr__())

    def test_validate_float_value_valid(self):

        expected_float_valid = VALID_FLOAT
        result_float_valid = Validate(VALID_FLOAT).validate_float()

        if result_float_valid._state == STATE_FOR_THREAD:
            self.assertEqual(expected_float_valid, result_float_valid._result)

    def test_validate_float_value_invalid(self):
        if Validate(INVALID_FLOAT).validate_float()._state == STATE_FOR_THREAD:
            self.assertEqual(
                f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'float: '}{INVALID_FLOAT}",
                str(Validate(INVALID_FLOAT).validate_float()._exception)
            )

    def test_validate_integer_value_valid(self):

        expected_integer_valid = VALID_INTEGER
        result_integer_valid = Validate(VALID_INTEGER).validate_integer()

        if result_integer_valid._state == STATE_FOR_THREAD:
            self.assertEqual(expected_integer_valid, result_integer_valid._result)

    def test_validate_integer_value_invalid(self):
        if Validate(INVALID_INTEGER).validate_integer()._state == STATE_FOR_THREAD:
            self.assertEqual(
                f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'integer: '}{INVALID_INTEGER}",
                str(Validate(INVALID_INTEGER).validate_integer()._exception)
            )

    def test_validate_string_value_valid(self):

        expected_string_valid = VALID_STRING
        result_string_valid = Validate(VALID_STRING).validate_string()

        if result_string_valid._state == STATE_FOR_THREAD:
            self.assertEqual(expected_string_valid, result_string_valid._result)

    def test_validate_string_value_invalid(self):
        if Validate(INVALID_STRING).validate_string()._state == STATE_FOR_THREAD:
            self.assertEqual(
                f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'string: '}{INVALID_STRING}",
                str(Validate(INVALID_STRING).validate_string()._exception)
            )

    def test_validate_email_value_valid(self):

        expected_email_valid = VALID_EMAIL
        result_email_valid = Validate(VALID_EMAIL).validate_email()

        if result_email_valid._state == STATE_FOR_THREAD:
            self.assertEqual(expected_email_valid, result_email_valid._result)

    def test_validate_email_value_invalid(self):
        if Validate(INVALID_EMAIL).validate_email()._state == STATE_FOR_THREAD:
            self.assertEqual(
                f"{FIRST_SUB_STRING_VAL_LOG_MSG}{'e-mail address: '}{INVALID_EMAIL}",
                str(Validate(INVALID_EMAIL).validate_email()._exception)
            )
