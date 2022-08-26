import os
import sys

import click
from session import Session
from constants import *


@click.command()
def main():
    click.clear()

    click.echo(message=TOP_HEADER)
    click.echo(MAIN_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)

    response = 100
    while not isinstance(response, int) or response > 4:
        response = click.prompt(text=SELECT_MENU_OPTION, type=int)

    if response == 1:
        login()
    if response == 2:
        click.echo("NEW ACCOUNT")
    if response == 3:
        click.echo("RESET PASSWORD")
    if response == 4:
        click.echo("EXIT APPLICATION")
    else:
        click.echo(WRONG_MENU_OPTION_INPUT) # This will possibly never fire but good to have as precaution


@click.command()
def login():

    # Action to be decided on
    login_attempts_count = 0
    total_allowed_login_attempts = 3

    # Local method to count login. I just did not want to repeat code here. I hate repeating code
    def login_count_response():
        return True if login_attempts_count < total_allowed_login_attempts else False

    username = ""
    while not isinstance(username, str) and login_count_response():
        username = click.prompt(text=PROMPT_USERNAME, type=str)
        login_attempts_count += 1
        click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                   "allowed_attempts": total_allowed_login_attempts})
    login_attempts_count = 0
    password = ""
    while not isinstance(password, str) and login_count_response():
        password = click.prompt(text=PROMPT_PASSWORD, type=str)
        login_attempts_count += 1
        click.echo(LOGIN_ATTEMPT_COUNT_REMAINING % {"attempts_count": login_attempts_count,
                                                                   "allowed_attempts": total_allowed_login_attempts})

    if login_count_response():
        #user = UserManager(username, password)
        returned_user_id = 0 #user.user_login()

        if returned_user_id > 0:
            # Load Home
            if Session(returned_user_id).start() != 0:
                #Dashboard().privacy()
                pass
            else:
                Session(0).stop()
        else:
            # Display Error
            click.echo("it is not work oooh")
    else:
        # This restarts the entire application instead of exiting. Is there a better way to do this after an error?
        os.execl(sys.executable, sys.executable, *sys.argv)
        # It will be a great add to display something that says we started all over again

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # log exception error
        print("An Error Occurred: " + str(e))
