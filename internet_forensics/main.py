import click
from datetime import date, timedelta
from user_manager.user_manager import UserManager
from main_constants import *
from internet_forensics.validation.validate import Validate

@click.command()
def main():
    # log start of application
    click.echo(WELCOME_SCREEN_MESSAGE)
    response = click.prompt(MAIN_MENU_OPTION_LIST)

    if Validate(response).if_integer:
        if response == 1:
            main_user_login()
        else:
            click.echo(WRONG_MENU_OPTION_INPUT)
            click.echo(APPLICATION_EXIT_MESSAGE) #TODO: Application should not exit but provide an option to try again


def main_user_login():
    user = UserManager
    user.user_login()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        print("An Error Occurred: " + str(e))  # This error should be logged instead of printing out to the user
