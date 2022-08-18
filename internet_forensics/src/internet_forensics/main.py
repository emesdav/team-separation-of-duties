import validate
import click
import view_control
from constants import *


@click.command()
def main():

    # inits
    user_manager_vc = view_control.user_manager_vc.UserManagerVC
    validate_this = validate.validate.Validate

    response = click.prompt(MAIN_MENU_OPTION_LIST)

    while not validate_this(response).if_integer():
        if response == "1":
            user_manager_vc.main_user_login()
        if response == "2":
            user_manager_vc.main_user_registration()
        if response == "3":
            user_manager_vc.main_user_password_reset()
        if response == "4":
            exit()
        else:
            click.echo(WRONG_MENU_OPTION_INPUT)
            main()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        print("An Error Occurred: " + str(e))  # This error should be logged instead of printing out to the user
