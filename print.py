from db.sql import *
import check_search


def print_books(books=None):
    """Prints iterable's fields. Returns True/False for Not empty/Empty."""

    if books is None:
        books = sql_query("SELECT BooksID,Title,Author,Year FROM Books")

    if len(books) == 0:
        system_print("There are no books!")
        return False
    else:
        system_print("Books are:")
        print("------------------------------------------------------\n")
        for each_book in books:
            print("\t", end="")
            for item in each_book:
                print(item, end=" ")
            print("\n")
        print("------------------------------------------------------\n")
        print("\n")
        return True



def print_users(users=None):
    """Prints ID,Username and Role of all users except admin's.Returns list of them."""

    if users is None:
        users = sql_query("""SELECT UsersID,Username,RolesID FROM Users
                    WHERE RolesID<>3""")
        
    if len(users) == 0:
        system_print("There are no users!")
        return users
    else:
        system_print("Users are:")
        print("------------------------------------------------------\n")
        for each in users:
            print("\t\tID: {} | {} | Role: ".format(each[0], each[1]), end="")
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



def search_menu(table, column, value):
    """Searches in table in column for value."""

    ids = check_search.search(table, column, value)

    if table == "Users":
        print_users()
    elif table == "Books":
        print_books()

    return ids


def show_personal_data(user_id):
    """Prints user's data from table \"Persons\"."""
    
    person_id = sql_query("""SELECT PersonsID FROM Users 
                    WHERE UsersID=%s""", (user_id,))

    row = sql_query("""SELECT LastName,FirstName,City,Address,PostalCode,PhoneNumber,Email
            FROM Persons WHERE PersonsID=%s""",(person_id[0][0],))

    data = row[0]

    print("Last name: {}".format(data[0]))
    print("First name: {}".format(data[1]))
    print("City: {}".format(data[2]))
    print("Address: {}".format(data[3]))
    print("Postal code: {}".format(data[4]))
    print("Phone number: {}".format(data[5]))
    print("Email: {}".format(data[6]))