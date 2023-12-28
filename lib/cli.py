# lib/cli.py

from helpers import (
    exit_program,
    all_sites,
    all_projects,
    find_site_by_name,
    find_project_by_title,
    find_investigator_by_name,
)
from seed import seed_database
from rich.console import Console

console = Console()
print = console.print


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
        elif choice == "3":
            find_site_by_name()
        elif choice == "4":
            find_project_by_title()
        elif choice == "5":
            find_investigator_by_name()
        else:
            print("Invalid choice\n", style="bold red")


def main_menu():
    print("Main Menu\n", style="bold bright_cyan")
    print("Please select an option:\n")
    print("1. List all research Sites")
    print("2. List all research Projects")
    print("3. Find Site by name")
    print("4. Find Project by title")
    print("5. Find Investigator by name")
    print("0. Exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


if __name__ == "__main__":
    main()
