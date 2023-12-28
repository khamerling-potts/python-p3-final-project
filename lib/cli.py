# lib/cli.py

from helpers import (
    exit_program,
    all_sites,
    all_projects,
    find_site_by_name,
    find_project_by_title,
)
from seed import seed_database
from colorama import Fore, Back, Style

# from rich import print
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
        else:
            print("Invalid choice")


def main_menu():
    print("Main Menu\n", style="bold bright_cyan")
    print("Please select an option:\n")
    print("[bold bright_white]0.[/bold bright_white] Exit the program")
    print("[bold bright_white]1.[/bold bright_white] List all research Sites")
    print("[bold bright_white]2.[/bold bright_white] List all research Projects")
    print("[bold bright_white]3.[/bold bright_white] Find Site by name")
    print("[bold bright_white]4.[/bold bright_white] Find Project by title")
    print("\n_______________________________________\n", style="light_sky_blue3")


if __name__ == "__main__":
    main()
