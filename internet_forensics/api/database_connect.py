import pyodbc
import logging

""" 
This is a default blank script to connect to our database that will be filled 
with db informations and security measures when will be developed, it will be called after
user authentication with the necessary credentials
"""

"""
To connect to DB we'll need the configuration data drom the DB creation which will be provided when the DB is ready
here is an example:
connection_string = (
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=mydb;'
    'UID=root;'
    'PWD=mypassword;'
    'charset=utf8mb4;'
)
"""


class db_cnx():
    # establishing connection to database
    # parameters will be held in a config file as per python guidelines
    def db_connect(self, config):
        try:
            cnx = pyodbc.connect(config)
            self.cursor = cnx.cursor()
        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            logging.debug(sqlstate)
        else:
            cnx.close()
