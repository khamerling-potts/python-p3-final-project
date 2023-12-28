# lib/helpers.py
from models.investigator import Investigator
from models.project import Project
from models.site import Site
from rich.console import Console

console = Console()
print = console.print


def exit_program():
    print("Goodbye!")
    exit()


def all_sites():
    sites = Site.get_all()
    print("All Research Sites:\n", style="u")
    list_sites(sites)
    all_sites_menu()
    choice = input("> ")
    print("\n")
    if choice == "A":
        add_site()
        return True
    elif choice == "B":
        return False
    elif choice.isdigit() and int(choice) in range(1, len(Site.get_all()) + 1):
        while True:
            if not site_details(sites[int(choice) - 1]):
                break
        return True
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice\n", style="bold red")
        return True


def find_site_by_name():
    name = input("Enter site name: ")
    print("\n")
    if site := Site.find_by_name(name):
        while True:
            if not site_details(site):
                break
        return True
    else:
        print(f"No site found with the name '{name}'", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def site_details(site):
    print(
        f"{site.name}: {site.classification} institution located in {site.city} (id: {site.id})\n",
        style="u",
    )
    site_details_menu()
    choice = input("> ")
    print("\n")

    if choice == "I":
        while True:
            if not investigators(site=site):
                break
        return True
    elif choice == "P":
        while True:
            if not site_projects(site):
                break
        return True
    elif choice == "D":
        site.delete()
        print(f"Successfully deleted {site.name}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return False
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def list_sites(sites):
    if sites:
        for i in range(len(sites)):
            print(f"{i+1}. {sites[i].name}")
    else:
        print("None")
    print("\n")


def project_sites_menu():
    print("Type [bold cyan]B[/bold cyan] to go back")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def all_sites_menu():
    print("Type [bold cyan]A[/bold cyan] to add a new Site")
    print("Type [bold cyan]B[/bold cyan] to go back to main menu")
    print("Type the [bold cyan]number of a Site[/bold cyan] to view its details")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def add_site():
    name = input("Enter the Site's name: ")
    city = input("Enter the Site's city: ")
    classification = input(
        "Enter the Site's classification (Government, Academic, or Medical): "
    )
    try:
        site = Site.create(name, city, classification)
        print(f"Successfully created {name}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )

    except Exception as exc:
        print("Error creating Site: ", exc, style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )


def site_details_menu():
    print("Type [bold cyan]I[/bold cyan] to view and edit this Site's Investigators")
    print(
        "Type [bold cyan]P[/bold cyan] to view the Projects associated with this Site"
    )
    print("Type [bold cyan]D[/bold cyan] to delete this Site")
    print("Type [bold cyan]B[/bold cyan] to go back")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def investigators(site=None, project=None):
    if site:
        investigators = site.investigators()
        print(f"{site.name} Investigators:\n", style="u")
    else:
        investigators = project.investigators()
        print(f"'{project.title}' Investigators:\n", style="u")

    list_investigators(investigators)
    investigators_menu()
    choice = input("> ")
    print("\n")
    if choice == "A":
        add_investigator(site, project)
        return True
    elif choice == "B":
        return False
    elif choice.isdigit() and int(choice) in range(1, len(investigators) + 1):
        investigator = investigators[int(choice) - 1]
        while True:
            if not investigator_details(investigator):
                break
        return True
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def investigator_details(investigator):
    print(
        f"{investigator.name}: Works on Project '{Project.find_by_id(investigator.project_id).title}' at {Site.find_by_id(investigator.site_id).name} (id: {investigator.id})\n",
        style="u",
    )
    investigator_details_menu()
    choice = input("> ")
    print("\n")
    if choice == "D":
        investigator.delete()
        print(f"Successfully deleted {investigator.name}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return False
    elif choice == "U":
        update_investigator(investigator)
        return True
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def investigator_details_menu():
    print("Type [bold cyan]D[/bold cyan] to delete this investigator")
    print("Type [bold cyan]U[/bold cyan] to update this investigator")
    print("Type [bold cyan]B[/bold cyan] to go back")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def list_investigators(investigators):
    if investigators:
        for i in range(len(investigators)):
            print(f"{i+1}. {investigators[i].name}")
    else:
        print("None")
    print("\n")


def investigators_menu():
    print("Type [bold cyan]A[/bold cyan] to add a new Investigator here")
    print("Type [bold cyan]B[/bold cyan] to go back")
    print(
        "Type the [bold cyan]the number of an Investigator[/bold cyan] to view its details"
    )
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def find_investigator_by_name():
    name = input("Enter investigator name: ")
    print("\n")
    if investigator := Investigator.find_by_name(name):
        while True:
            if not investigator_details(investigator):
                break
        return True
    else:
        print(f"No investigator found with the name '{name}'", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def add_investigator(site=None, project=None):
    name = input("Enter the Investigator's name: ")
    project_id = (
        project.id if project else input("Enter the Investigator's project id: ")
    )
    site_id = site.id if site else input("Enter the Investigator's site id: ")
    try:
        investigator = Investigator.create(name, site_id, project_id)
        print(
            f"Successfully added {name} to this {'Site' if site else 'Project'}'s Investigator's",
            style="bold green",
        )
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
    except Exception as exc:
        print("Error creating Investigator: ", exc, style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )


def update_investigator(investigator):
    id = investigator.id
    try:
        # consider replacing project id with project name
        investigator.name = input("Enter new name: ")
        investigator.site_id = input("Enter new site id: ")
        investigator.project_id = input("Enter new project id: ")
        investigator.update()
        print(f"Successfully updated {investigator.name}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
    except Exception as exc:
        print("Error updating investigator: ", exc, style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )


def site_projects(site):
    projects = site.projects()
    print(f"{site.name} Projects:\n", style="u")
    list_projects(projects)
    site_projects_menu()
    choice = input("> ")
    print("\n")
    if choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def list_projects(projects):
    if projects:
        for i in range(len(projects)):
            print(f"{i+1}. {projects[i].title}")
    else:
        print("None")
    print("\n")


def site_projects_menu():
    print("Type [bold cyan]B[/bold cyan] to go back")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def all_projects():
    projects = Project.get_all()
    print("All Projects:\n", style="u")
    list_projects(projects)
    all_projects_menu()
    choice = input("> ")
    print("\n")
    if choice == "A":
        add_project()
        return True
    elif choice == "B":
        return False
    elif choice.isdigit() and int(choice) in range(1, len(projects) + 1):
        while True:
            if not project_details(projects[int(choice) - 1]):
                break
        return True
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice\n", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def all_projects_menu():
    print("Type [bold cyan]A[/bold cyan] to add a new Project")
    print("Type [bold cyan]B[/bold cyan] to go back to main menu")
    print("Type [bold cyan]the number of a Project[/bold cyan] to view its details")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def find_project_by_title():
    title = input("Enter project title: ")
    print("\n")
    if project := Project.find_by_title(title):
        while True:
            if not project_details(project):
                break
        return True
    else:
        print(f"No project found with the title '{title}'", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def add_project():
    title = input("Enter the Project's title: ")
    funding = input(
        "Enter the Project's funding amount. Please enter 0 for no funding, or a number greater than 999: "
    )
    try:
        project = Project.create(title, funding)
        print(f"Successfully created {title}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
    except Exception as exc:
        print("Error creating Project: ", exc, style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )


def project_details(project):
    print(
        f"'{project.title}': $[white]{project.funding}[/white] in funding (id: {project.id})",
        style="u",
    )
    print("\n")
    project_details_menu()
    choice = input("> ")
    print("\n")
    if choice == "I":
        while True:
            if not investigators(project=project):
                break
        return True
    elif choice == "S":
        while True:
            if not project_sites(project):
                break
        return True
    elif choice == "D":
        project.delete()
        print(f"Successfully deleted {project.title}", style="bold green")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return False
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True


def project_details_menu():
    print("Type [bold cyan]I[/bold cyan] to view and edit this Project's Investigators")
    print(
        "Type [bold cyan]S[/bold cyan] to view the Sites associated with this Project"
    )
    print("Type [bold cyan]D[/bold cyan] to delete this Project")
    print("Type [bold cyan]B[/bold cyan] to go back")
    print("Type 0 to exit the program")
    print(
        "\n----------------------------------------------------------------\n",
        style="light_sky_blue3",
    )


def project_sites(project):
    sites = project.sites()
    print(f"'{project.title}' Sites:\n", style="u")
    list_sites(sites)
    project_sites_menu()
    choice = input("> ")
    print("\n")
    if choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice", style="bold red")
        print(
            "\n----------------------------------------------------------------\n",
            style="light_sky_blue3",
        )
        return True
