# lib/helpers.py
from models.investigator import Investigator
from models.project import Project
from models.site import Site
from rich.console import Console

console = Console()
rprint = console.print


def exit_program():
    rprint("Thank you for using RDM\n", style="bold light_slate_grey")
    exit()


def all_sites():
    sites = Site.get_all()
    rprint("All Research Sites:\n", style="u")
    list_sites(sites)
    all_sites_menu()
    choice = input("> ")
    rprint("\n")
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
        rprint("Invalid choice\n", style="bold red")
        return True


def all_sites_menu():
    rprint("Type [bold cyan]A[/bold cyan] to add a new Site")
    rprint("Type [bold cyan]B[/bold cyan] to go back to main menu")
    rprint("Type the [bold cyan]number of a Site[/bold cyan] to view its details")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def site_details(site):
    rprint(
        f"{site.name}: {site.classification} institution located in {site.city} (id: {site.id})\n",
        style="u",
    )
    site_details_menu()
    choice = input("> ")
    rprint("\n")

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
        rprint(f"Successfully deleted {site.name}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return False
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def site_details_menu():
    rprint("Type [bold cyan]I[/bold cyan] to view and edit this Site's Investigators")
    rprint(
        "Type [bold cyan]P[/bold cyan] to view the Projects associated with this Site"
    )
    rprint("Type [bold cyan]D[/bold cyan] to delete this Site")
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def list_sites(sites):
    if sites:
        for i in range(len(sites)):
            rprint(f"{i+1}. {sites[i].name}")
    else:
        rprint("None")
    rprint("\n")


def add_site():
    name = input("Enter the Site's name: ")
    city = input("Enter the Site's city: ")
    classification = input(
        "Enter the Site's classification (Government, Academic, or Medical): "
    )
    try:
        site = Site.create(name, city, classification)
        rprint(f"Successfully created {name}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )

    except Exception as exc:
        rprint("Error creating Site: ", exc, style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )


def find_site_by_name():
    name = input("Enter site name: ")
    rprint("\n")
    if site := Site.find_by_name(name):
        while True:
            if not site_details(site):
                break
        return True
    else:
        rprint(f"No site found with the name '{name}'", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def project_sites_menu():
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def investigators(site=None, project=None):
    if not site and not project:
        investigators = Investigator.get_all()
        rprint("All Investigators:", style="u")
    elif site:
        investigators = site.investigators()
        rprint(f"{site.name} Investigators:\n", style="u")
    else:
        investigators = project.investigators()
        rprint(f"'{project.title}' Investigators:\n", style="u")

    list_investigators(investigators)
    investigators_menu()
    choice = input("> ")
    rprint("\n")
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
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def investigators_menu():
    rprint("Type [bold cyan]A[/bold cyan] to add a new Investigator here")
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint(
        "Type the [bold cyan]the number of an Investigator[/bold cyan] to view its details"
    )
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def investigator_details(investigator):
    rprint(
        f"{investigator.name}: Works on Project '{Project.find_by_id(investigator.project_id).title}' at {Site.find_by_id(investigator.site_id).name} (id: {investigator.id})\n",
        style="u",
    )
    investigator_details_menu()
    choice = input("> ")
    rprint("\n")
    if choice == "D":
        investigator.delete()
        rprint(f"Successfully deleted {investigator.name}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
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
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def investigator_details_menu():
    rprint("Type [bold cyan]D[/bold cyan] to delete this investigator")
    rprint("Type [bold cyan]U[/bold cyan] to update this investigator")
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def list_investigators(investigators):
    if investigators:
        for i in range(len(investigators)):
            rprint(f"{i+1}. {investigators[i].name}")
    else:
        rprint("None")
    rprint("\n")


def add_investigator(site=None, project=None):
    name = input("Enter the Investigator's name: ")
    project_id = (
        project.id if project else input("Enter the Investigator's project id: ")
    )
    site_id = site.id if site else input("Enter the Investigator's site id: ")
    try:
        investigator = Investigator.create(name, site_id, project_id)
        if not site and not project:
            rprint(
                f"Successfully added {name} to the Investigators",
                style="bold green",
            )
        else:
            rprint(
                f"Successfully added {name} to this {'Site' if site else 'Project'}'s Investigator's",
                style="bold green",
            )
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
    except Exception as exc:
        rprint("Error creating Investigator: ", exc, style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )


def update_investigator(investigator):
    try:
        # consider replacing project id with project name
        investigator.name = input("Enter new name: ")
        investigator.site_id = input("Enter new site id: ")
        investigator.project_id = input("Enter new project id: ")
        investigator.update()
        rprint(f"Successfully updated {investigator.name}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
    except Exception as exc:
        rprint("Error updating investigator: ", exc, style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )


def find_investigator_by_name():
    name = input("Enter investigator name: ")
    rprint("\n")
    if investigator := Investigator.find_by_name(name):
        while True:
            if not investigator_details(investigator):
                break
        return True
    else:
        rprint(f"No investigator found with the name '{name}'", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def site_projects(site):
    projects = site.projects()
    rprint(f"{site.name} Projects:\n", style="u")
    list_projects(projects)
    site_projects_menu()
    choice = input("> ")
    rprint("\n")
    if choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def list_projects(projects):
    if projects:
        for i in range(len(projects)):
            rprint(f"{i+1}. {projects[i].title}")
    else:
        rprint("None")
    rprint("\n")


def site_projects_menu():
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def all_projects():
    projects = Project.get_all()
    rprint("All Projects:\n", style="u")
    list_projects(projects)
    all_projects_menu()
    choice = input("> ")
    rprint("\n")
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
        rprint("Invalid Choice\n", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def all_projects_menu():
    rprint("Type [bold cyan]A[/bold cyan] to add a new Project")
    rprint("Type [bold cyan]B[/bold cyan] to go back to main menu")
    rprint("Type [bold cyan]the number of a Project[/bold cyan] to view its details")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def find_project_by_title():
    title = input("Enter project title: ")
    rprint("\n")
    if project := Project.find_by_title(title):
        while True:
            if not project_details(project):
                break
        return True
    else:
        rprint(f"No project found with the title '{title}'", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def add_project():
    title = input("Enter the Project's title: ")
    funding = input(
        "Enter the Project's funding amount. Please enter 0 for no funding, or a number greater than 999: "
    )
    try:
        project = Project.create(title, funding)
        rprint(f"Successfully created {title}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
    except Exception as exc:
        rprint("Error creating Project: ", exc, style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )


def project_details(project):
    rprint(
        f"'{project.title}': $[white]{project.funding}[/white] in funding (id: {project.id})",
        style="u",
    )
    rprint("\n")
    project_details_menu()
    choice = input("> ")
    rprint("\n")
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
        rprint(f"Successfully deleted {project.title}", style="bold green")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return False
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True


def project_details_menu():
    rprint(
        "Type [bold cyan]I[/bold cyan] to view and edit this Project's Investigators"
    )
    rprint(
        "Type [bold cyan]S[/bold cyan] to view the Sites associated with this Project"
    )
    rprint("Type [bold cyan]D[/bold cyan] to delete this Project")
    rprint("Type [bold cyan]B[/bold cyan] to go back")
    rprint("Type 0 to exit the program")
    rprint(
        "\n----------------------------------------------------------------\n",
        style="light_slate_grey",
    )


def project_sites(project):
    sites = project.sites()
    rprint(f"'{project.title}' Sites:\n", style="u")
    list_sites(sites)
    project_sites_menu()
    choice = input("> ")
    rprint("\n")
    if choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        rprint("Invalid Choice", style="bold red")
        rprint(
            "\n----------------------------------------------------------------\n",
            style="light_slate_grey",
        )
        return True
