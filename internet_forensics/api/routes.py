from flask import Flask, session, redirect, url_for

"""
The purpose of this file is to contain all the necessary routes to connect the application interface to the DB
"""

app = Flask(__name__)

"""
Landing route that tells if the user is already logged in
will use username string to check if present in session memory
"""


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    if 'username' not in session:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    # will complete as soon as we have a structure of DB
    username = str(input())
