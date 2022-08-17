import click
from datetime import date, timedelta

class DataManagement:
    def __init__(self):
        print("here ooooh")

    @click.command()
    @catch
    def deactivate(self):

        message = "You have requested to deactivate your data from our systems. This request cannot be undone. Do you " \
                  "wish to proceed "

        # We simply calculate 30days from the day of request to delete the data
        deactivation_date = date.today() + timedelta(days=30)

        # send a prompt
        response = click.prompt(message)

        # Per response, process request

        # We send the deactivation Date in an update to the database

        # TODO: A cron job that will run daily to automatically deactivate the accounts on time
        # cron job should not be in this file. (Obviously)

        click.echo(response + " at " + deactivation_date)

    def request(self):
        pass
