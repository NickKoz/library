import mysql.connector
from mysql.connector import errorcode

def connect_to_database():
    "Connecting to MySQL database using mysql connector."

    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="library_user",
            passwd="1234",
            database="Library"
        )
    except mysql.connector.Error as CnxError:
        if CnxError.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif CnxError.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print(CnxError)
        print("Database connection failed!")
        quit()
    else:
        return cnx


def close_connection(cnx):
    cnx.close()
