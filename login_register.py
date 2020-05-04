from functions import *
import getpass



def login():

    os.system("clear")
    print_menu("Login:")

    while True:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        ids = sql_query("""SELECT UserID FROM Users 
            WHERE Username = BINARY %s AND Password = BINARY %s""",(username,password))

        if len(ids) == 0:
           system_print("Wrong name,password or both!Try again.")
        else:
            system_print("Successfully logged in!")
            user_id = ids[0][0]
            break
            

    data = sql_query("""SELECT RoleID FROM Users 
            WHERE UserID=%s""",(user_id,))

    role = data[0][0]

    if role == 1:
        visitor_login(user_id)
    elif role == 2:
        editor_login(user_id)
    else:
        admin_login(user_id)


# Types of login accordingly to role.

def visitor_login(visitor_id):
    os.system("clear")
    print_menu("VISITOR")
    show_personal_data(visitor_id)
    while 1:
        while 1:
            print_menu("1.Show books\n2.Disconnect")
            choice = int(input("Your choice: "))
            if choice == 1 or choice == 2:
                break
            else:
                system_print("Wrong input!Try again.")
        if choice == 1:

            books = sql_query("""SELECT Title,Author,Year FROM Books 
            WHERE UserID=%s""",(visitor_id,))
            
            print_books(books)

        else:
            disconnect()
            break


def editor_login(editor_id):

    os.system("clear")
    print_menu("EDITOR")
    show_personal_data(editor_id)

    while True:
        while True:
            print_menu("1.Give book\n2.Take book\n3.Disconnect")
            choice = int(input("Your choice: "))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                system_print("Wrong input!Try again.")

        if choice == 3:
            disconnect()
            break


        print("\n\tPlease enter ID of target person ", end="")
        print("in order to add/remove a book to/from their personal library.\n")

        print_users()

        while True:
            id = int(input("User's ID: "))

            userIDs = sql_query("SELECT UserID FROM Users WHERE UserID=%s",(id,))

            if len(userIDs) == 0:
                system_print("User with ID: {} doesn't exist!Try again.".format(id))
            else:
                break

        if choice == 1:
            give_book_to(id)
        elif choice == 2:
            take_book_from(id)


def admin_login(admin_id):
    
    os.system("clear")
    print_menu("ADMIN")
    show_personal_data(admin_id)

    while True:
        while True:
            
            print_menu("""1.Show users\n2.Delete user\n3.Generate book\n4.Delete book\n5.Change role\n6.Disconnect""")
            choice = int(input("Your choice: "))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
                break
            else:
                system_print("Wrong input!")

        # Show users.
        if choice == 1:
            os.system("clear")
            print_users()
        
        # Delete user.
        elif choice == 2:
            os.system("clear")

            while True:
                users = print_users()

                if len(users) == 0:
                    break

                while True:
                    answer = int(input("""Please select a user to be deleted by giving its ID:(Press 0 for exit.) """))
                    
                    if answer == 0:
                        break
                    if linear_search(users,answer):
                        break
                    else:
                        system_print("Wrong input!Try again.")

                if answer == 0:
                    break

                person_id = sql_query("""SELECT PersonID FROM Users
                        WHERE UserID=%s""",(answer,))

                # Firstly, we take all books that target may have.
                sql_command("UPDATE Books SET UserID=NULL WHERE UserID=%s",(answer,))

                # We delete user.
                sql_command("DELETE FROM Users WHERE UserID=%s",(answer,))
                
                # We delete their data.
                sql_command("DELETE FROM Persons WHERE PersonID=%s",(person_id[0][0],))

                system_print("User with ID: {} is deleted!".format(answer))

        # Generate book.
        elif choice == 3:
            os.system("clear")
            system_print("Please enter title, author, year of book:")
            while True:
                title = input("Title: ")
                author = input("Author: ")
                year = input("Year: ")
                while True:
                    answer = input("\tAre you sure for your choice?(Y/n) ")
                    if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
                        break
                    else:
                        system_print("Wrong input!")

                if answer == "Y" or answer == "y":
                    break


            sql_command("INSERT INTO Books (Title,Author,Year) VALUES(%s,%s,%s)",(title, author, year))
            
            system_print("Book inserted!")

        # Delete a book
        elif choice == 4:
            os.system("clear")

            while True:

                books = sql_query("SELECT BookID,Title,Author,Year FROM Books",None)

                print_books(books)

                while True:
                    answer = int(input("""Please select a book to be deleted by giving its ID:(Press 0 for exit.) """))
                    if answer == 0:
                        break

                    if linear_search(books,answer):
                        system_print("Wrong input!Try again.")
                    else:
                        break

                if answer == 0:
                    break
                
                sql_command("DELETE FROM Books WHERE BookID=%s",(answer,))

                system_print("Book is deleted!")

        # Change role of user.
        elif choice == 5:
            os.system("clear")
            print("\n\tPlease enter ID of target person ", end="")
            print("in order to change his role.\n")

            users = print_users()

            print("")

            while True:
                target_id = int(input("ID: "))
                
                if linear_search(users,target_id):
                    break
                else:
                    system_print("Wrong input!Try again.")

            while True:
                while True:
                    print("What kind of role do you want to give them?\n")
                    print_menu("1.Visitor\n2.Editor\n3.Exit")
                    role = int(input("\nPlease give your option: "))
                    if role == 1 or role == 2 or role == 3:
                        break
                    else:
                        system_print("Wrong input!Try again.")

                if role == 3:
                    break

                data = sql_query("""SELECT RoleID FROM Users 
                                        WHERE UserID=%s""", (target_id,))

                role_of_target = data[0][0]

                if role == role_of_target:
                    system_print("They already have this role!")
                else:
                    sql_command("""UPDATE Users SET RoleID=%s 
                        WHERE UserID=%s""",(role, target_id,))
                    
                    system_print("Role changed!")
                    break

        # Disconnect
        elif choice == 6:
            disconnect()
            break


# Register function
def register():

    os.system("clear")
    print_menu("Register")

    system_print("Please give username,password and your personal data:")

    while True:
        username = input("Username: ")
        if check_username(username):
            break
        else:
            system_print("Username already exists!")

    while True:
        while True:
            # Getpass function does password invisible
            password = getpass.getpass("Password: ")
            if check_password(password):
                break

        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            system_print("Passwords don't match!Try again.")


    last_name = input("Last name: ")
    first_name = input("First name: ")
    city = input("City: ")
    address = input("Address: ")
    postal = input("Postal code: ")
    while True:
        phone = input("Phone Number: ")
        if len(phone) == 10:
            break
        else:
            system_print("Wrong phone number!")

    email = input("Email: ")

    # Inserting into persons.
    sql_command("""INSERT INTO Persons (LastName,FirstName,City,PostalCode,
                Address,PhoneNumber,Email)
                VALUES(%s,%s,%s,%s,%s,%s,%s)""",(last_name, first_name, city, postal, address, phone, email))


    person_id = sql_query("""SELECT PersonID FROM Persons 
            WHERE LastName=%s AND Address=%s""",(last_name,address))


    role_id = sql_query("SELECT RoleID FROM Roles WHERE Title='Visitor';",None)

    # Inserting into users.
    sql_command("""INSERT INTO Users (Username,Password,RoleID,PersonID)
            VALUES (%s,%s,%s,%s)""",(username, password, role_id[0][0], person_id[0][0]))
    
    system_print("User is created successfully!")


    # --------------------------------------------------------------------#

    while True:
        choice = input("Do you want to login?Press Yes or No (Y/n): ")
        if choice == "Y" or choice == "y" or choice == "N" or choice == "n":
            break
        else:
            system_print("Wrong input!Try again")

    if choice == "Y" or choice == "y":
        login()
