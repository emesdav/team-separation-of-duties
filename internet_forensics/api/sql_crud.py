
import database_connect
from internet_forensics.api.database_connect import db_cnx


class crudOps():

    # function to read whole table, to be used when user asks for all records of a topic
    def readWholeTable(table):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        # reading database data from a specific table, %s is not good practice but will not use user input
        cursor.execute("Select * from (%s)", (table))
        result = cursor.fetchall()
        print(result)

        cursor.close()
        connection.close()

    # method to change the status of a record, only for non personal data

    def delNonPersRecord(table, recordId, status):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        # will include sql injection protection
        cursor.execute("UPDATE %s SET status= %s WHERE recordId= %s",
                       (table, status, recordId))

        cursor.close()
        connection.close()

    def readRecord(table, recordId):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        cursor.execute(
            "SELECT * FROM TABLE= %s WHERE recordId= %s", (table, recordId))

        cursor.close()
        connection.close()

    def readUserData(username):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        cursor.execute(
            "SELECT * FROM users WHERE username= %s", (username))

        cursor.close()
        connection.close()

    def deleteAllPersRecords(username):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        cursor.execute(
            "DELETE * FROM users WHERE username= %s", (username))

        cursor.close()
        connection.close()
