import time

import click
from datetime import date, timedelta
from src.internet_forensics.constants import (
    TOP_HEADER,
    END_OF_MENU,
    SELECT_MENU_OPTION,
    WRONG_MENU_OPTION_INPUT
)
from .constants import *
from src.internet_forensics.cli import create_crime_record, update_crime_record, delete_crime_record, read_crime_record
from src.internet_forensics.user.user_manager import UserManager
from src.internet_forensics.cli.constants import CRIME_REPORTING_MENU_OPTION_LIST

from src.internet_forensics.log.custom_logger import generate_custom_logger
from src.internet_forensics.app import main

user_id = 0
_dashboard_menu_response = 0
_log = generate_custom_logger(name="DASHBOARD")


@click.command()
def menu():
    global _dashboard_menu_response
    if _dashboard_menu_response == 0:
        click.echo(TOP_HEADER)

    click.echo(DASHBOARD_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)

    _dashboard_menu_response = click.prompt(text=SELECT_MENU_OPTION, type=int)

    while not isinstance(_dashboard_menu_response,
                         int) or _dashboard_menu_response > 4 or _dashboard_menu_response == 0:
        _dashboard_menu_response = click.prompt(text=SELECT_MENU_OPTION, type=int)

    if _dashboard_menu_response == 1:
        profile()
    if _dashboard_menu_response == 2:
        privacy()
    if _dashboard_menu_response == 3:
        file_a_report()
    if _dashboard_menu_response == 4:
        logout()
    else:
        click.echo(WRONG_MENU_OPTION_INPUT)


@click.command()
def profile():
    global user_id
    global _dashboard_menu_response
    _dashboard_menu_response = 1
    click.echo(TOP_HEADER)
    click.echo(DASHBOARD_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)
    user = UserManager(user_id=user_id)
    data = user.personal_data()
    click.echo(DASHBOARD_PROFILE % {"first_name": data.first_name,
                                    "last_name": data.last_name,
                                    "email": data.email,
                                    "physical_address": data.address,
                                    "phone_number": data.mobile})
    click.echo(END_OF_MENU)
    menu()


@click.command()
def privacy():
    global user_id
    global _dashboard_menu_response
    _dashboard_menu_response = 1
    click.echo(TOP_HEADER)
    click.echo(DASHBOARD_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)
    user = UserManager(user_id=user_id)
    data = user.personal_data()
    print(data)
    app_privacy = "YES" if data.privacy else "NO"
    gdpr_necessary = "YES" if data.GDPR_necessary else "NO"
    gdpr_marketing = "YES" if data.GDPR_marketing else "NO"
    click.echo(DASHBOARD_PRIVACY % {"privacy": app_privacy,
                                    "GDPR_necessary": gdpr_necessary,
                                    "GDPR_marketing": gdpr_marketing})
    click.echo(END_OF_MENU)
    menu()


@click.command()
def file_a_report():
    global _dashboard_menu_response
    click.echo(END_OF_MENU)
    click.echo(CRIME_REPORTING_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)

    _crime_menu_response = 0
    while not isinstance(_crime_menu_response,
                         int) or _crime_menu_response > 5 or _crime_menu_response == 0:
        _crime_menu_response = click.prompt(text="Select a crime reporting option", type=int)

    if _dashboard_menu_response == 1:
        create_report = create_crime_record.entry
        create_report.create_crime_record()
    if _dashboard_menu_response == 2:
        read_report = read_crime_record.entry
        read_report.read_crime_record()
    if _dashboard_menu_response == 3:
        update_report = update_crime_record.entry
        update_report.update_crime_record()
    if _dashboard_menu_response == 4:
        delete_report = delete_crime_record.entry
        delete_report.delete_crime_record()
    if _dashboard_menu_response == 5:
        _dashboard_menu_response = 0
        menu()
    else:
        click.echo(WRONG_MENU_OPTION_INPUT)

    menu()


@click.command()
def logout():
    global _dashboard_menu_response
    _dashboard_menu_response = 0
    click.echo(TOP_HEADER)
    click.echo(DASHBOARD_MENU_OPTION_LIST)
    click.echo(END_OF_MENU)
    click.echo("You have been successfully logged out. You will now be redirected to the main page")
    time.sleep(5)
    main()
