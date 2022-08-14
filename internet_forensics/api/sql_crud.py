from internet_forensics.api.database_connect import db_cnx
import logging

"""
CRUD opeations to be performed on database data, these will be imported in api routes file
and will be called with specific routes
"""


class CRUDOps():

    # function to read whole table, to be used when user asks for all records of a topic
    def read_whole_table(table):
        connection = db_cnx.db_connect(config="")  # configs are passed here
        cursor = connection.cursor

        # reading database data from a specific table, %s is not good practice but will not use user input
        cursor.execute("Select * from (%s)", (table))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        logging.debug(result)

        return result

    # method to change the status of a record, only for non personal data

    def del_non_pers_record(table, recordId, status):
        # TODO: configs are passed here
        connection = db_cnx.db_connect(config="")
        cursor = connection.cursor

        # will include sql injection protection
        cursor.execute("UPDATE %s SET status= %s WHERE recordId= %s",
                       (table, status, recordId))

        cursor.close()
        connection.close()

    def read_records(table, recordId):
        # TODO: configs are passed here
        connection = db_cnx.db_connect(config="")
        cursor = connection.cursor

        cursor.execute(
            "SELECT * FROM TABLE= %s WHERE recordId= %s", (table, recordId))

        cursor.close()
        connection.close()

    def read_user_data(username):
        # TODO: configs are passed here
        connection = db_cnx.db_connect(config="")
        cursor = connection.cursor

        cursor.execute(
            "SELECT * FROM users WHERE username= %s", (username))

        cursor.close()
        connection.close()

    def delete_all_pers_records(username):
        # TODO: configs are passed here
        connection = db_cnx.db_connect(config="")
        cursor = connection.cursor

        cursor.execute(
            "DELETE * FROM users WHERE username= %s", (username))

        cursor.close()
        connection.close()

    def update_pers_record(property, value, username):
        # TODO: configs are passed here
        connection = db_cnx.db_connect(config="")
        cursor = connection.cursor

        # will include sql injection protection
        cursor.execute("UPDATE users SET %s= %s WHERE username= %s",
                       (property, value, username))

        cursor.close()
        connection.close()
