# library to connect to mysql db

import mysql.connector
from mysql.connector import Error

""" 
This is a default blank script to connect to our database that will be filled 
with db informations and security measures when will be developed, it will be called after
user authentication with the necessary credentials
"""

# establishing connection to database
try:
    connection = mysql.connector.connect(host='',
                                         database='',
                                         user='',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        # initializing cursor to perform CRUD operations
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

# error handling
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
