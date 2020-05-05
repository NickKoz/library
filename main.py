from login_register import *


os.system("clear")
system_print("Welcome to the online Library!")
while True:

    print_menu("MAIN MENU:\n1.Login\n2.Register\n3.Quit")
    while True:
        choice = int(input("Please give your option: "))
        if choice != 1 and choice != 2 and choice != 3:
            print("\tWrong input!Please choose 1,2 or 3.")
        else:
            break

    # Login
    if choice == 1:
        login()
    # Register
    elif choice == 2:
        register()
    # Quit
    else:
        break

os.system("clear")
print_menu("Bye.")