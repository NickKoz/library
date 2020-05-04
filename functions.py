from db_connection import *
import os
import time


def give_book_to(target_id):

    available_books = sql_query("""SELECT BookID,Title,Author,Year FROM Books
                WHERE UserID IS NULL""",None)

    if print_books(available_books):

        while True:
            book_id = int(input("\n\tSelect book accordingly to their ID(Press 0 to exit): "))
            if book_id == 0:
                return

            if linear_search(available_books,book_id):
                break
            else:
                system_print("Wrong input!Try again.")

        sql_command("""UPDATE Books SET UserID=%s 
            WHERE BookID=%s""",(target_id, book_id))

        system_print("Book is given!")



def take_book_from(target_id):

    books_of_user = sql_query("""SELECT BookID,Title,Author,Year FROM Books
                    WHERE UserID=%s""",(target_id,))

    if print_books(books_of_user):

        while True:
            book_id = int(input("\n\nSelect book accordingly to their ID(Press 0 to exit): "))
            if book_id == 0:
                return

            if linear_search(books_of_user,book_id):
                break
            else:
                system_print("Wrong input!Try again.")


        sql_command("""UPDATE Books SET UserID=NULL 
            WHERE BookID=%s""",(book_id, ))

        system_print("Book with ID: {} is removed!".format(book_id))



def print_books(books):

    if len(books) == 0:
        system_print("There are no books!")
        return False
    else:
        system_print("Books are:")
        print("------------------------------------------------------\n")
        for each_book in books:
            print("\t",end="")
            for item in each_book:
                print(item, end=" ")
        print("\n------------------------------------------------------\n")
        print("\n")
        return True



def print_users():
    users = sql_query("""SELECT UserID,Username,RoleID FROM Users
                WHERE RoleID<>3""",None)
    
    if len(users) == 0:
        system_print("There are no users!")
        return users

    system_print("Users are:")
    print("------------------------------------------------------\n")
    for each in users:
        print("\t\tID: {} | {} | Role: ".format(each[0],each[1]),end="")
        if int(each[2]) == 1:
            print("Visitor\n")
        elif int(each[2]) == 2:
            print("Editor\n")
    print("------------------------------------------------------")
    print("\n\n")
    return users



def print_menu(given):
    print("\n\t\t*****************************************")
    print("\t\t\t\t", end="")
    temp = list(given)
    for i in range(len(temp)):
        if temp[i] == "\n":
            temp.insert(i+1,"\t\t\t\t")

    print("".join(temp))

    print("\t\t*****************************************\n\n")



def system_print(given):
    print("\n\n\t\t## {} ##\n\n".format(given))



def linear_search(data,id):
    found = False
    for each_row in data:
        if int(each_row[0]) == id:
            found = True
            break
    return found



def show_personal_data(user_id):
    
    person_id = sql_query("""SELECT PersonID FROM Users 
                    WHERE UserID=%s""",(user_id,))

    row = sql_query("""SELECT LastName,FirstName,City,Address,PostalCode,PhoneNumber,Email
            FROM Persons WHERE PersonID=%s""",(person_id[0][0],))

    data = row[0]

    print("Last Name: {}".format(data[0]))
    print("First Name: {}".format(data[1]))
    print("City: {}".format(data[2]))
    print("Address: {}".format(data[3]))
    print("Postal Code: {}".format(data[4]))
    print("Phone Number: {}".format(data[5]))
    print("Email: {}".format(data[6]))



def check_username(given):

    users = sql_query("SELECT UserID FROM Users WHERE Username = BINARY %s",(given,))

    if len(users) > 0:
        return False

    return True



def check_password(given):
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



def disconnect():
    print_menu("Disconnecting...")
    time.sleep(0.5)
    os.system("clear")



def sql_command(command,data):

    cnx = connect_to_database()
    cursor = cnx.cursor(buffered=True)

    try:
        if data is None:
            cursor.execute(command)
        else:
            cursor.execute(command,data)

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




def sql_query(query,data):

    cnx = connect_to_database()
    cursor = cnx.cursor(buffered=True)

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
