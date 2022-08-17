import click
from datetime import date, timedelta
from user_manager.user_manager import UserManager
from main_constants import *
from internet_forensics.validation.validate import Validate
from internet_forensics.user_manager import user_manager_constants as user_constants
from internet_forensics.View_control.user_manager_vc import UserManagerVC

fresh_start = True


@click.command()
def main():
    # Global Variables
    global fresh_start

    # inits
    user_manager_vc = UserManagerVC

    # log start of application
    if fresh_start:
        click.echo(WELCOME_SCREEN_MESSAGE)

    response = click.prompt(MAIN_MENU_OPTION_LIST)

    while not Validate(response).if_integer():
        if response == "1":
            user_manager_vc.main_user_login()
        if response == "2":
            user_manager_vc.user_registration()
        else:
            click.echo(WRONG_MENU_OPTION_INPUT)
            fresh_start = False
            main()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        print("An Error Occurred: " + str(e))  # This error should be logged instead of printing out to the user
