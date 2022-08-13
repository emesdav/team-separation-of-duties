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
        # Instructions
        username = click.prompt(PROMPT_USERNAME)
        password = click.prompt(PROMPT_PASSWORD)

        # Lets Validate Entries
        click.echo(VERIFYING_DATA)
        if Validate(username).if_email() and Validate(password).if_string():
            click.echo(DATA_VERIFIED)
            # We can now proceed
            # Check DB
            # If record is found and matches return true else false
        else:
            click.echo(LOGIN_VALIDATION_FAILED)

        # Per response, process request
        # We simply calculate 30days from the day of request to delete the data
        deactivation_date = str(date.today() + timedelta(days=30))

        click.echo(deactivation_date)
