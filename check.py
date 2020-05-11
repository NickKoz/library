from db.sql import *
from print import *


def linear_search(data,id):
    "Checks if item is in iterable data. Returns True or False"

    found = False
    for each_row in data:
        if int(each_row[0]) == id:
            found = True
            break
    return found



def check_username(given):
    "Checks if username belongs to another user. Returns True or False"

    users = sql_query("SELECT UsersID FROM Users WHERE Username = BINARY %s",(given,))

    if len(users) > 0 or len(given) == 0:
        return False

    return True



def check_password(given):
    "Checks if given password meets some standards. Returns True or False"

    length = len(given)
    if length < 6 or length > 12:
        system_print("Password's length must be 6 to 12 characters.")
        return False
    counter = 0
    for c in given:
        if ' ' <= c <= '@':
            counter += 1
    if counter == 0:
        system_print("Password must have at least one special character.")
        return False

    return True



def search(table,column,value):
    "Searches in table for record with value in column. Returns ID(s) of record(s)"

    return sql_query("""SELECT {}ID FROM {} WHERE {} 
            LIKE '{}%' OR WHERE {} LIKE '%{}' OR WHERE {} LIKE '%{}%' 
            OR WHERE {} LIKE '{}'
            """.format(table,table,column,value,column,value,column,value,column,value))