import unittest

from src.internet_forensics.cli.delete_crime_record.run import delete_crime_record_run

name_of_suspect = 'John Carpenter'


class TestDeleteCrimeRecord(unittest.TestCase):

    def test_read_crime_record_run(self):

        expected_response_from_delete = f"{'The crime record of the suspect named '}" \
                                      f"{name_of_suspect}{' has been deleted.'}"
        result_response_from_delete = delete_crime_record_run(name_of_suspect)

        self.assertIsInstance(result_response_from_delete, str)
        self.assertEqual(result_response_from_delete, expected_response_from_delete)
