# lib/cli.py

from helpers import (
    exit_program,
    all_sites,
    all_projects,
    find_site_by_name,
    find_project_by_title,
    investigators,
    find_investigator_by_name,
)
from seed import seed_database
from rich.console import Console
from art import text2art

console = Console()
rprint = console.print


def main():
    seed_database()

    # ASCII Heading
    rprint(
        f"[light_slate_grey]{text2art('RDM', font='isometric3')[0:-2]}[/light_slate_grey]",
        "[light_slate_grey]research database manager.[/light_slate_grey]\n\n\n",
    )

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
            find_site_by_name()
        elif choice == "3":
            while True:
                if not all_projects():
                    break
        elif choice == "4":
            find_project_by_title()
        elif choice == "5":
            while True:
                if not investigators():
                    break
        elif choice == "6":
            find_investigator_by_name()
        else:
            rprint("Invalid choice\n", style="bold red")


def main_menu():
    rprint("Main Menu\n", style="bold bright_cyan")
    rprint("Please select an option:\n")
    rprint("1. List all research Sites")
    rprint("2. Find Site by name")
    rprint("3. List all research Projects")
    rprint("4. Find Project by title")
    rprint("5. List all Investigators")
    rprint("6. Find Investigator by name")
    rprint("0. Exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


if __name__ == "__main__":
    main()
