import click
from flask import Flask
import database_connect
from internet_forensics.api.database_connect import db_cnx

 
class crud_ops(database_connect):

    # establishing connection to db, can be greatly costumized in db_cnx class
    connection = db_cnx.db_connect(config="") # configs are passed here

    def read_data(connection):
        cursor = connection.cursor
        
        cursor.execute() # reading database data

