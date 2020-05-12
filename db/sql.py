from db.db_connection import *


def sql_command(command, data=None):
    """Executes SQL commands like \"INSERT INTO\" or \"UPDATE\"."""

    cnx = connect_to_database()
    cursor = cnx.cursor(dictionary=True)

    try:
        if data is None:
            cursor.execute(command)
        else:
            cursor.execute(command, data)

    except mysql.connector.ProgrammingError as err:
        print(err)
        quit()
    except mysql.connector.Error as err:
        print("Another error!")
        print(err)
        quit()
    
    cnx.commit()
    
    cursor.close()
    close_connection(cnx)


def sql_query(query, data=None):
    """Executes SQL queries. Returns list of dictionaries."""

    cnx = connect_to_database()
    cursor = cnx.cursor(dictionary=True)

    try:
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query,data)

    except mysql.connector.ProgrammingError as err:
        print(err)
        quit()
    except mysql.connector.Error as err:
        print(err)
        quit()
    

    # Always returns list of tuples.
    result = cursor.fetchall()

    cursor.close()
    close_connection(cnx)

    return result
