import os
import sys

import click
from datetime import date, timedelta
from internet_forensics.user_manager.user_manager import UserManager
from internet_forensics.main_constants import *
from internet_forensics.validation.validate import Validate
from internet_forensics.user_manager import user_manager_constants as user_constants

fresh_start = True


class UserManagerVC:

    @click.command()
    def main_user_login():
        # Global Variables
        global fresh_start

        # Action to be decided on
        login_attempts_count = 0
        total_allowed_login_attempts = 3

        # Local method to count login. I just did not want to repeat code here. I hate repeating code
        def login_count_response():
            return True if login_attempts_count < total_allowed_login_attempts else False

        username = password = ""
        while not Validate(username).if_email() and login_count_response():
            username = click.prompt(user_constants.PROMPT_USERNAME)
            login_attempts_count += 1
            click.echo(user_constants.LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                       "allowed_attempts": total_allowed_login_attempts})

        while not Validate(password).if_string() and login_count_response():
            password = click.prompt(user_constants.PROMPT_PASSWORD)
            login_attempts_count += 1
            click.echo(user_constants.LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                       "allowed_attempts": total_allowed_login_attempts})

        if login_count_response():
            user = UserManager
            response_login = user.user_login(username, password)

            if response_login != 0:
                # Load Home
                pass
            else:
                # Display Error
                pass
        else:
            # Let's move on
            fresh_start = False
            # This restarts the entire application instead of exiting. Is there a better way to do this after an error?
            os.execl(sys.executable, sys.executable, *sys.argv)
            # It will be a great add to display something that says we started all over again

    @click.command()
    def user_registration():
        # Global Variables
        global fresh_start

        # Instructions
        firstname = lastname = address = email = password = ""

        while not Validate(firstname).if_string():
            firstname = click.prompt(user_constants.PROMPT_PASSWORD)

        while not Validate(lastname).if_string():
            lastname = click.prompt(user_constants.PROMPT_PASSWORD)

        while not Validate(address).if_string():
            address = click.prompt(user_constants.PROMPT_PASSWORD)

        while not Validate(email).if_string():
            email = click.prompt(user_constants.PROMPT_PASSWORD)

        while not Validate(password).if_string():
            password = click.prompt(user_constants.PROMPT_PASSWORD)

        click.echo(user_constants.DATA_VERIFIED)
        # We can now proceed

        click.echo(user_constants.LOGIN_VALIDATION_FAILED)

        # Per response, process request
        # We simply calculate 30days from the day of request to delete the data
        deactivation_date = str(date.today() + timedelta(days=30))

        click.echo(deactivation_date)

