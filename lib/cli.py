# lib/cli.py

from helpers import (
    exit_program,
    all_sites,
    all_projects,
)
from seed import seed_database
from colorama import Fore, Back, Style


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
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Main Menu\n" + Style.RESET_ALL)
    print("Please select an option:")
    print("\n")
    print("0. Exit the program")
    print("1. List all research Sites")
    print("2. List all research Projects")
    print("\n_______________________________________")


if __name__ == "__main__":
    main()
