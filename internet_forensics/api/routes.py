import click
from flask import Flask

"""
This code is just a placeholder to fill the api routes file, will be removed
"""

app = Flask(__name__)

@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')