import click
from datetime import date, timedelta
from .user_manager_constants import *
from internet_forensics.validation.validate import Validate


# TODO: NOTE: Adding the self argument triggers an error.this should be fixed
# TODO: For the purpose of loosely coupling the whole system, we may want to introduce dependency injections
class UserManager:
    def __init__():
        print(WELCOME_MESSAGE)

    @click.command()
    def user_login():
        # We will count the number of times login is attempted and take an action

        # Action to be decided on
        login_attempts_count = 0
        total_allowed_login_attempts = 3

        # Local method to count login. I just did not wa to repeat code here. I hate repeating code
        def login_count_response():
            return True if login_attempts_count < total_allowed_login_attempts else False

        # Let's set Login instructions and validations here
        click.echo(VERIFYING_DATA)

        username = password = ""
        while not Validate(username).if_email() and login_count_response():
            username = click.prompt(PROMPT_USERNAME)
            login_attempts_count += 1
            click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                        "allowed_attempts": total_allowed_login_attempts})

        while not Validate(password).if_string() and login_count_response():
            password = click.prompt(PROMPT_PASSWORD)
            login_attempts_count += 1
            click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                        "allowed_attempts": total_allowed_login_attempts})

            # We can now proceed
            # Check DB
            # If record is found and matches return true else false
        if login_count_response():
            click.echo(LOGIN_VALIDATION_FAILED)
        else:
            # Let's move on
            pass

        # Per response, process request
        # We simply calculate 30days from the day of request to delete the data
        deactivation_date = str(date.today() + timedelta(days=30))

        click.echo(deactivation_date)

    @click.command()
    def user_registration():

        # Instructions
        firstname = lastname = address = email = password = ""

        while not Validate(firstname).if_string():
            firstname = click.prompt(PROMPT_PASSWORD)

        while not Validate(lastname).if_string():
            lastname = click.prompt(PROMPT_PASSWORD)

        while not Validate(address).if_string():
            address = click.prompt(PROMPT_PASSWORD)

        while not Validate(email).if_string():
            email = click.prompt(PROMPT_PASSWORD)

        while not Validate(password).if_string():
            password = click.prompt(PROMPT_PASSWORD)

        click.echo(DATA_VERIFIED)
        # We can now proceed
        
        click.echo(LOGIN_VALIDATION_FAILED)

        # Per response, process request
        # We simply calculate 30days from the day of request to delete the data
        deactivation_date = str(date.today() + timedelta(days=30))

        click.echo(deactivation_date)
