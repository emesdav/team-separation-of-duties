import unittest

from src.internet_forensics.database.db import CrimeRecords
from src.internet_forensics.cli.read_crime_record.run import read_crime_record_run

num_of_repeated_crimes = 'once'
type_of_crime = 'murder'
name_of_suspect = 'John Carpenter'
address_of_suspect = 'Rue de la rose'

crime_records = [CrimeRecords(num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect)]


class TestReadCrimeRecord(unittest.TestCase):

    def test_read_crime_record_run(self):

        expected_response_from_read = [f"The crime of type {type_of_crime} has been "
                                       f"committed {num_of_repeated_crimes} and the suspect is named "
                                       f"{name_of_suspect} and lives at the following address: {address_of_suspect}"]
        result_response_from_read = read_crime_record_run(name_of_suspect)

        self.assertIsInstance(result_response_from_read, list)
        self.assertIsInstance(result_response_from_read[0], str)
        self.assertEqual(len(result_response_from_read), 1)
        self.assertEqual(result_response_from_read, expected_response_from_read)
