import database_connect
from internet_forensics.api.database_connect import db_cnx


class crudOps(database_connect):

    # function to read whole table, to be used when user asks for all records of a topic
    def readWholeTable(table):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        # reading database data from a specific table, %s is not good practice but will not use user input
        cursor.execute("Select * from (%s)", (table))
        result = cursor.fetchall()
        print(result)

    # method to change the status of a record, only for non personal data
    def delNonPersRecord(table, recordId, status):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        cursor.execute("UPDATE %s SET status= %s WHERE recordId= %s",
                       (table, status, recordId))
