# library to connect to mysql db

from errno import errorcode
import mysql.connector

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
            cnx = mysql.connector.connect(config)
            self.cursor = cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
