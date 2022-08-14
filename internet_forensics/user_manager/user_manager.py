import click
from datetime import date, timedelta
from .user_manager_constants import *
from internet_forensics.validation.validate import Validate
from internet_forensics.validation.sanitize import Sanitize


# TODO: NOTE: Adding the self argument triggers an error.this should be fixed
# TODO: For the purpose of loosely coupling the whole system, we may want to introduce dependency injections
class UserManager:
    def __init__(self, username, password="", firstname="", lastname="", address="", email=""):
        self.username = Sanitize(username).input_data()
        self.password = Sanitize(password).input_data()
        self.firstname = Sanitize(lastname).input_data()
        self.lastname = Sanitize(lastname).input_data()
        self.address = Sanitize(address).input_data()
        self.email = Sanitize(email).input_data()
        self.user_id = ""

    def user_login(self):
        # Harsh Password

        # Query DB for username and password

        return self.user_id

    def user_password_reset(self):
        # Instructions

        # Query DB for username and if found, select email and send password reset code to email

        # Insert new password request into password request table with a 2hour time expiry

        # If all processes completed, return true else return false

        return self.user_id # ignore this line. Intentional

    def user_creation(self):
        # Instructions

        # Insert Data into DB

        # return userID

        return self.user_id



