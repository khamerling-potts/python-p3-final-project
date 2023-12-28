# lib/cli.py

from helpers import (
    exit_program,
    list_sites,
    add_site,
    all_sites_menu,
    all_sites,
    all_projects,
)
from seed import seed_database


def main():
    seed_database()
    while True:
        main_menu()
        choice = input("> ")
        print("\n")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while True:
                if not all_sites():
                    break
        elif choice == "2":
            while True:
                if not all_projects():
                    break
        else:
            print("Invalid choice")


def main_menu():
    print("Main Menu:")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all research Sites")
    print("2. List all research Projects")
    print("---------------------------")


if __name__ == "__main__":
    main()
