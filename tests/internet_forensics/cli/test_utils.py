import unittest

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.utils import get_num_repeat_crimes_and_descr

num_of_repeated_crimes = 1
num_times = 'once'
type_of_crime = 'murder'
name_of_suspect = 'John Carpenter'
address_of_suspect = 'Rue de la rose'

crime_records = CrimeRecords(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect)


class TestUtils(unittest.TestCase):

    def test_get_num_repeat_crimes_and_descr(self):

        expected_response_from_read = f"The crime of type {type_of_crime} has been committed {num_times} and the " \
                                      f"suspect is named {name_of_suspect} and lives at the following " \
                                      f"address: {address_of_suspect}"
        times, result_response_from_read = get_num_repeat_crimes_and_descr(crime_records)

        self.assertIsInstance(times, str)
        self.assertEqual(times, num_times)
        self.assertIsInstance(result_response_from_read, str)
        self.assertEqual(result_response_from_read, expected_response_from_read)
