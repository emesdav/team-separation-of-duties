import unittest

from src.internet_forensics.cli.update_crime_record.run import update_crime_record


class TestUpdateCrimeRecord(unittest.TestCase):

    def test_update_crime_record(self):
        num_of_repeated_crimes = 1
        type_of_crime = 'Stealing a dog'
        name_of_suspect = 'Ms Cat Kitten'
        address_of_suspect = 'Warm cat bed in the house'

        expected_response_from_update = f"Updated existing record: The crime of type {type_of_crime} has been " \
                                        f"committed once and the suspect is named {name_of_suspect} and " \
                                        f"lives at the following address: {address_of_suspect}"
        result_response_from_update = update_crime_record(
            num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect
        )

        self.assertEqual(result_response_from_update, expected_response_from_update)
