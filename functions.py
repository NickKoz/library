from db.db_connection import *
import os
import time
import getpass


def give_book_to(target_id):
    "Gives target a book."

    available_books = sql_query("""SELECT BookID,Title,Author,Year FROM Books
                WHERE UserID IS NULL""")

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
    "Takes from target a book."

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
    "Prints iterable's fields. Returns True/False for Not empty/Empty."

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
            print("\n")
        print("------------------------------------------------------\n")
        print("\n")
        return True



def print_users():
    "Prints ID,Username and Role of all users except admin's.Returns list of them."

    users = sql_query("""SELECT UserID,Username,RoleID FROM Users
                WHERE RoleID<>3""")
    
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
    "Prints given as menu so the user can choose from."

    print("\n\t\t*****************************************")
    print("\t\t\t\t", end="")
    temp = list(given)
    for i in range(len(temp)):
        if temp[i] == "\n":
            temp.insert(i+1,"\t\t\t\t")

    print("".join(temp))

    print("\t\t*****************************************\n\n")



def system_print(given):
    "Prints library's system's messages to console."

    print("\n\n\t\t## {} ##\n\n".format(given))



def linear_search(data,id):
    "Checks if item is in iterable data. Returns True or False"

    found = False
    for each_row in data:
        if int(each_row[0]) == id:
            found = True
            break
    return found



def show_personal_data(user_id):
    "Prints user's data from table \"Persons\"."
    
    person_id = sql_query("""SELECT PersonID FROM Users 
                    WHERE UserID=%s""",(user_id,))

    row = sql_query("""SELECT LastName,FirstName,City,Address,PostalCode,PhoneNumber,Email
            FROM Persons WHERE PersonID=%s""",(person_id[0][0],))

    data = row[0]

    print("Last name: {}".format(data[0]))
    print("First name: {}".format(data[1]))
    print("City: {}".format(data[2]))
    print("Address: {}".format(data[3]))
    print("Postal code: {}".format(data[4]))
    print("Phone number: {}".format(data[5]))
    print("Email: {}".format(data[6]))



def check_username(given):
    "Checks if username belongs to another user. Returns True or False"

    users = sql_query("SELECT UserID FROM Users WHERE Username = BINARY %s",(given,))

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



def change_data(id):
    "Changes user's data."

    os.system("clear")
    while True:
        system_print("Please select what field you want to change.")
        menu = "1.Username\n2.Password\n3.Last name\n4.First name\n5.City\n6.Address\n"
        menu = menu + "7.Postal code\n8.Phone number\n9.Email\n10.Exit\n"
        print_menu(menu)

        while True:
            choice = int(input("Please give your option: "))
            if choice in range(1,11):
                break
            else:
                system_print("Wrong input!Try again.")

        os.system("clear")

        # Username
        if choice == 1:
            while True:
                username = input("Please give new username: ")
                if check_username(username):
                    
                    break
                else:
                    system_print("Invalid username!")
            
            sql_command("UPDATE Users SET Username=%s",(username,))

            system_print("Username changed!")

            continue

        # Password
        elif choice == 2:
            while True:
                while True:
                    # Getpass function does password invisible
                    password = getpass.getpass("New password: ")
                    if check_password(password):
                        break

                confirm_password = getpass.getpass("Confirm Password: ")
                if password == confirm_password:
                    break
                else:
                    system_print("Passwords don't match!Try again.")

            sql_command("UPDATE Users SET Password=%s",(password,))

            system_print("Password changed!")

            continue

        # Last name
        elif choice == 3:
            mess_input = "Last name: "
            column = "LastName"
            smess = "Last name changed!"
        
        # First name
        elif choice == 4:
            mess_input = "First name: "
            column = "FirstName"
            smess = "First name changed!"
        
        # City
        elif choice == 5:
            mess_input = "City: "
            column = "City"
            smess = "City changed!"
        
        # Address
        elif choice == 6:
            mess_input = "Address: "
            column = "Address"
            smess = "Address changed!"

        # Postal code
        elif choice == 7:
            mess_input = "Postal code: "
            column = "PostalCode"
            smess = "Postal code changed!"

        # Phone number
        elif choice == 8:
            while True:
                data = input("Phone number: ")
                if len(data) == 10:
                    break
                else:
                    system_print("Wrong phone number!")
            
            sql_command("UPDATE Persons SET PhoneNumber=%s",(data,))

            system_print("Phone number changed!")

            continue
        
        # Email
        elif choice == 9:
            mess_input = "Email: "
            column = "Email"
            smess = "Email changed!"

        # Exit
        else:
            os.system("clear")
            break

        data = input("\n"+ mess_input)

        sql_command("UPDATE Persons SET %s = %s" % (column,"%s"),(data,))

        system_print(smess)



def disconnect():
    "Used when user is disconnecting from system."

    print_menu("Disconnecting...")
    time.sleep(0.5)
    os.system("clear")



def sql_command(command,data=None):
    "Executes SQL commands like \"INSERT INTO\" or \"UPDATE\"."

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



def sql_query(query,data=None):
    "Executes SQL queries. Returns list of tuples."

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
