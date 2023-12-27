# lib/cli.py

from helpers import exit_program, list_sites, add_site, sites_menu, sites
from seed import seed_database


def main():
    seed_database()
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
            while sites():
                sites()
        else:
            print("Invalid choice")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all research sites")


if __name__ == "__main__":
    main()
