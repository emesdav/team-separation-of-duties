import unittest

from src.internet_forensics.encryption.encrypt import Encrypt

ENCODING_METHOD = 'utf-8'

# The dummy 'HASHED_PASSWORD' was created by using the method 'hash_password' being tested below for consistency.
HASHED_PASSWORD = '$2b$12$l0iFR5RTv83oEG4SOk/JNOwMlHSZHWzFa7IhJDWlsH5b6gpO7aHri'
PASSWORD = 'my_strongest_password'

STATE_FOR_THREAD = 'FINISHED'

encrypt_obj = Encrypt()


class TestEncrypt(unittest.TestCase):

    def test_hash_password(self):

        expected_hashed_password = HASHED_PASSWORD.encode(ENCODING_METHOD)

        result_hashed_password = encrypt_obj.hash_password(PASSWORD)

        if result_hashed_password._state == STATE_FOR_THREAD:

            self.assertEqual(expected_hashed_password,
                             result_hashed_password._result)

    # The password matches the hashed password (positive test case).
    def test_check_password_matched(self):

        expected_matched_password = HASHED_PASSWORD.encode(ENCODING_METHOD)
        result_matched_hashed_password = encrypt_obj.hash_password(PASSWORD)

        if result_matched_hashed_password._state == STATE_FOR_THREAD:
            self.assertEqual(expected_matched_password,
                             result_matched_hashed_password._result)

    # The password does not match the hashed password (negative test case).
    def test_check_password_mismatched(self):

        expected_mismatched_password = '$3c$12$l0iFR5RTv83oEG4SOk/JNOwMlHSZHWzFa7IhJDWlsH5b6gpO7aHri'.encode(
            ENCODING_METHOD)
        result_mismatched_hashed_password = encrypt_obj.hash_password(PASSWORD)

        if result_mismatched_hashed_password._state == STATE_FOR_THREAD:
            self.assertEqual(expected_mismatched_password,
                             result_mismatched_hashed_password._result)
