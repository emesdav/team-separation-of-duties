import os
import sys

import click
from datetime import date, timedelta
from internet_forensics.src.internet_forensics.user_manager.user_manager import UserManager
from internet_forensics.src.internet_forensics.validate.validate import Validate
from internet_forensics.src.internet_forensics.user_manager import constants as user_constants
from .dashboard_vc import Dashboard


class UserManagerVC:

    @click.command()
    def login():

        # Action to be decided on
        login_attempts_count = 0
        total_allowed_login_attempts = 3

        # Local method to count login. I just did not want to repeat code here. I hate repeating code
        def login_count_response():
            return True if login_attempts_count < total_allowed_login_attempts else False

        username = ""
        while not Validate(username).if_email() and login_count_response():
            username = click.prompt(user_constants.PROMPT_USERNAME)
            login_attempts_count += 1
            click.echo(user_constants.LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                       "allowed_attempts": total_allowed_login_attempts})
        login_attempts_count = 0
        password = ""
        while not Validate(password).if_string() and login_count_response():
            password = click.prompt(user_constants.PROMPT_PASSWORD)
            login_attempts_count += 1
            click.echo(user_constants.LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                       "allowed_attempts": total_allowed_login_attempts})

        if login_count_response():
            user = UserManager(username, password)
            response_login = user.user_login()

            if response_login > 0:
                # Load Home
                click.echo("TUEEEEEE")
                Dashboard().profile()
            else:
                # Display Error
                click.echo("it is not work oooh")
        else:
            # This restarts the entire application instead of exiting. Is there a better way to do this after an error?
            os.execl(sys.executable, sys.executable, *sys.argv)
            # It will be a great add to display something that says we started all over again

    @click.command()
    def registration():

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

    @click.command()
    def password_reset():

        while not Validate(password).if_string():
            password = click.prompt(user_constants.PROMPT_PASSWORD)

            response = "KEY FROM DB"

            if response != "":
                # Send Email

                # Let`s go back to home
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                # Display Error
                pass
