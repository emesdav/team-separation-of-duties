import os
import sys
import time
import click
from constants import *
from src.internet_forensics.user.user_manager import UserManager
from src.internet_forensics.cli.dashboard_view_model import dashboard
from src.internet_forensics.log.custom_logger import generate_custom_logger

_log = generate_custom_logger(name="APP")
# When at 0 will display main menu and reset menu options else returns to selected menu at the call of main
_response = 0


@click.command()
def main():
    global _response
    if _response == 0:
        click.echo(TOP_HEADER)
        click.echo(MAIN_MENU_OPTION_LIST)
        click.echo(END_OF_MENU)

    while not isinstance(_response, int) or _response > 4 or _response == 0:
        _response = click.prompt(text=SELECT_MENU_OPTION, type=int)

    if _response == 1:
        login()
    if _response == 2:
        registration()
    if _response == 3:
        click.echo("RESET PASSWORD")
    if _response == 4:
        click.echo("EXIT APPLICATION")
    else:
        click.echo(WRONG_MENU_OPTION_INPUT)  # This will possibly never fire but good to have as precaution


@click.command()
def login():
    global _response

    # Action to be decided on
    login_attempts_count = 0
    total_allowed_login_attempts = 3

    # Local method to count login. I just did not want to repeat code here. I hate repeating code
    def login_count_response() -> bool:
        return True if login_attempts_count < total_allowed_login_attempts else False

    username = None
    while not isinstance(username, str) and login_count_response():
        username = click.prompt(text=PROMPT_USERNAME, type=str)
        login_attempts_count += 1
        click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                    "allowed_attempts": total_allowed_login_attempts})

    login_attempts_count = 0
    password = None
    while not isinstance(password, str) and login_count_response():
        password = click.prompt(text=PROMPT_PASSWORD, type=str)
        login_attempts_count += 1
        click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                    "allowed_attempts": total_allowed_login_attempts})

    if login_count_response():
        user = UserManager(username, password)
        returned_user_id = user.user_login()

        if returned_user_id != 0:
            # Load Home
            dashboard.user_id = returned_user_id
            dashboard.profile()
        else:
            click.echo("username or password is wrong. Please check and try again")
            main()
    else:
        # This restarts the entire application instead of exiting. Is there a better way to do this after an error?
        _response = 0
        main()
        # It will be a great add to display something that says we started all over again


@click.command()
def registration():
    # Instructions
    firstname = lastname = address = email = mobile = privacy = gdpr_marketing = gdpr_necessary = password = None

    while not isinstance(firstname, str) or firstname is None:
        firstname = click.prompt(text=PROMPT_FIRSTNAME, type=str)

    while not isinstance(lastname, str) or lastname is None:
        lastname = click.prompt(text=PROMPT_LASTNAME, type=str)

    while not isinstance(address, str) or address is None:
        address = click.prompt(text=PROMPT_ADDRESS, type=str)

    while not isinstance(mobile, int) or mobile is None:
        mobile = click.prompt(text=PROMPT_MOBILE, type=int)

    while not isinstance(privacy, bool) or privacy is None:
        privacy = click.prompt(text=PROMPT_PRIVACY, type=bool)

    while not isinstance(gdpr_marketing, bool) or gdpr_marketing is None:
        gdpr_marketing = click.prompt(text=PROMPT_GDPR_MARKETING, type=bool)

    while not isinstance(gdpr_necessary, bool) or gdpr_necessary is None:
        gdpr_necessary = click.prompt(text=PROMPT_GDPR_NECESSARY, type=bool)

    while not isinstance(email, str) or email is None:
        email = click.prompt(text=PROMPT_EMAIL, type=str)

    while not isinstance(password, str) or password is None:
        password = click.prompt(text=PROMPT_PASSWORD, type=str)

    user = UserManager(firstname=firstname,
                       lastname=lastname,
                       address=address,
                       email=email,
                       mobile=mobile,
                       password=password,
                       privacy=privacy,
                       gdpr_marketing=gdpr_marketing,
                       gdpr_necessary=gdpr_necessary)
    returned_user_id = user.user_creation()

    if returned_user_id != 0 or returned_user_id is not None:
        # Load Home
        dashboard.privacy()
    else:
        # Error Display
        click.echo("We are having problems accepting your registration. Please ensure all fields are entered with "
                   "expected values")
        registration()
        os.execl(sys.executable, sys.executable, *sys.argv)

    click.echo("DATA_VERIFIED" + firstname + lastname + address + email + password)
    # We can now proceed


@click.command()
def password_reset():
    password = None
    while not isinstance(password, str) or password is None:
        password = click.prompt(text=PROMPT_PASSWORD, type=str)

        response = "KEY FROM DB"

        if response != "":
            # Send Email

            # Let`s go back to home
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            click.echo("")
            pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        click.echo(END_OF_MENU)
        _log.error("An Error Occurred: " + str(e))
        click.echo(END_OF_MENU)
        time.sleep(5)
        main()
