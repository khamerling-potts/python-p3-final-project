# lib/cli.py

from helpers import exit_program, list_sites, add_site


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("\n")
            print("------------------------")
            list_sites()
            print("\n")
            while True:
                sites_menu()
        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all research sites")


def sites_menu():
    print("Type A to add a new Site")
    print("Type B to go back to main menu")
    print("Type the number of a Site to view its details")
    print("Type 0 to exit the program")
    choice = input("> ")
    if choice == "A":
        add_site()
    elif choice == "0":
        exit_program()


if __name__ == "__main__":
    main()
