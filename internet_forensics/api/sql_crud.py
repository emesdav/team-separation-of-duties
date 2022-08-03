import database_connect
from internet_forensics.api.database_connect import db_cnx

 
class crud_ops(database_connect):

    # establishing connection to db, can be greatly costumized in db_cnx class

    def read_data(connection):
        connection = db_cnx.db_connect(config="") # configs are passed here
        cursor = connection.cursor
        
        cursor.execute() # reading database data, sql commands will be here when db available

