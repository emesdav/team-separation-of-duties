import os
import sys

import click
from datetime import date, timedelta
from internet_forensics.src.internet_forensics.constants import (
    TOP_HEADER,
    DASHBOARD_MENU_OPTION_LIST,
    END_OF_MENU,
    BOTTOM_HEADER
)


class Dashboard:

    @click.command()
    def __init__():
        click.echo(TOP_HEADER)
        click.echo(DASHBOARD_MENU_OPTION_LIST)
        click.echo(END_OF_MENU)

    @click.command()
    def profile():
        click.echo("PROFILE")

    @click.command()
    def privacy_settings():
        click.echo("PRIVACY SETTINGS")

    @click.command()
    def news():
        click.echo("NEWS")

    @click.command()
    def logout():
        click.echo("LOGOUT")
        pass

