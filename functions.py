import os
import time
import getpass
from db.sql import *
from print import *
from check_search import *


def give_book_to(target_id):
    """Gives target a book."""

    available_books = sql_query("""SELECT BooksID,Title,Author,Year FROM Books
                WHERE UsersID IS NULL""")

    if print_books(available_books):

        while True:
            book_id = int(input("\n\tSelect book accordingly to their ID(Press 0 to exit): "))
            if book_id == 0:
                return

            if linear_search(available_books,book_id):
                break
            else:
                system_print("Wrong input!Try again.")

        sql_command("""UPDATE Books SET UsersID=%s 
            WHERE BooksID=%s""",(target_id, book_id))

        system_print("Book is given!")



def take_book_from(target_id):
    "Takes from target a book."

    books_of_user = sql_query("""SELECT BooksID,Title,Author,Year FROM Books
                    WHERE UsersID=%s""", (target_id,))

    if print_books(books_of_user):

        while True:
            book_id = int(input("\n\nSelect book accordingly to their ID(Press 0 to exit): "))
            if book_id == 0:
                return

            if linear_search(books_of_user,book_id):
                break
            else:
                system_print("Wrong input!Try again.")


        sql_command("""UPDATE Books SET UsersID=NULL 
            WHERE BooksID=%s""",(book_id, ))

        system_print("Book with ID: {} is removed!".format(book_id))



def change_data(id):
    """Changes user's data."""
    
    person_id = sql_query("SELECT PersonsID FROM Users WHERE UsersID=%s",(id,))

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
            
            sql_command("UPDATE Users SET Username=%s WHERE UsersID=%s",(username,id))

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

            sql_command("UPDATE Users SET Password=%s WHERE UsersID=%s",(password,id))

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

            sql_command("""UPDATE Persons p SET p.PhoneNumber=%s 
            WHERE PersonsID=%s""",(data,person_id[0][0]))

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

        sql_command("""UPDATE Persons SET {} = %s WHERE
        PersonsID=%s""".format(column),(data,person_id[0][0]))

        system_print(smess)



def disconnect():
    "Used when user is disconnecting from system."

    print_menu("Disconnecting...")
    time.sleep(0.5)
    os.system("clear")
