from errno import errorcode
import pyodbc

""" 
This is a default blank script to connect to our database that will be filled 
with db informations and security measures when will be developed, it will be called after
user authentication with the necessary credentials
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
            print(sqlstate)
        else:
            cnx.close()
