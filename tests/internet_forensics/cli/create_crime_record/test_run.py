import unittest

from src.internet_forensics.cli.create_crime_record.run import create_crime_record_run


class TestCreateCrimeRecord(unittest.TestCase):

    def test_create_crime_record(self):
        num_of_repeated_crimes = 1
        type_of_crime = 'Stealing a cat'
        name_of_suspect = 'Mr Doggy Doggos'
        address_of_suspect = 'Warm dog house in the backyard'

        expected_response_from_create = f"Created new record: The crime of type {type_of_crime} has been " \
                                        f"committed once and the suspect is named {name_of_suspect} and " \
                                        f"lives at the following address: {address_of_suspect}"
        result_response_from_create = create_crime_record_run(
            num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect
        )

        self.assertEqual(result_response_from_create, expected_response_from_create)
