import click
from datetime import date, timedelta
from user_manager.user_manager import UserManager
from main_constants import *
from internet_forensics.validation.validate import Validate
from internet_forensics.user_manager import user_manager_constants as user_constants

fresh_start = True


@click.command()
def main():
    global fresh_start
    # log start of application
    if fresh_start:
        click.echo(WELCOME_SCREEN_MESSAGE)

    response = click.prompt(MAIN_MENU_OPTION_LIST)

    while not Validate(response).if_integer():
        if response == "1":
            main_user_login()
        else:
            click.echo(WRONG_MENU_OPTION_INPUT)
            fresh_start = False
            main()


@click.command()
def main_user_login():
    global fresh_start
    # Action to be decided on
    login_attempts_count = 0
    total_allowed_login_attempts = 3

    # Local method to count login. I just did not wa to repeat code here. I hate repeating code
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
        user.user_login()
    else:
        # Let's move on
        fresh_start = False
        main()
        # It will be a great add to display something that says we started all over again


@click.command()
def user_registration():
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


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        print("An Error Occurred: " + str(e))  # This error should be logged instead of printing out to the user
