# lib/helpers.py
from models.investigator import Investigator
from models.project import Project
from models.site import Site


def exit_program():
    print("Goodbye!")
    exit()


def list_sites():
    sites = Site.get_all()
    print("Research Sites:")
    for i in range(len(sites)):
        print(f"{i+1}. {sites[i].name}")
    print("\n")


def sites_menu():
    print("Type A to add a new Site")
    print("Type B to go back to main menu")
    print("Type the number of a Site to view its details")
    print("Type 0 to exit the program")
    print("---------------------------")


def add_site():
    name = input("Enter the Site's name: ")
    city = input("Enter the Site's city: ")
    classification = input(
        "Enter the Site's classification (Government, Academic, or Medical): "
    )
    try:
        site = Site.create(name, city, classification)
    except Exception as exc:
        print("Error creating Site: ", exc)
    print("\n")


def site_details_menu():
    print("Type I to view the site's Investigators")
    print("Type P to see the site's Projects")
    print("Type B to go back")
    print("Type 0 to exit the program")
    print("---------------------------")


def site_details(index):
    site = Site.get_all()[index]
    print(f"{site.name}: {site.classification} institution located in {site.city}")
    print("\n")
    site_details_menu()
    choice = input("> ")
    print("\n")
    if choice == "I":
        while True:
            if not investigators(site):
                break
        return True
    elif choice == "P":
        while True:
            if not projects(site):
                break
        return True
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice")
        return True


def sites():
    list_sites()
    sites_menu()
    choice = input("> ")
    if choice == "A":
        add_site()
        return True
    elif choice == "B":
        return False
    elif choice.isdigit() and int(choice) in range(1, len(Site.get_all()) + 1):
        while True:
            # change this to site parameter and not id parameter
            if not site_details(int(choice) - 1):
                break
        return True
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice")
        print("\n")
        return True


def investigators(site):
    if not site == "all":
        investigators = site.investigators()
        print(f"{site.name} Investigators:")
        list_investigators(investigators)
        investigators_menu()
        choice = input("> ")
        if choice == "A":
            add_investigator(site.id)
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
            print("Invalid choice")
            return True


def investigator_details(investigator):
    print(
        f"{investigator.name}: Works on Project '{Project.find_by_id(investigator.project_id).title}' at {Site.find_by_id(investigator.site_id).name}"
    )
    print("\n")
    investigator_details_menu()
    choice = input("> ")
    print("\n")
    if choice == "D":
        investigator.delete()
        return False
    elif choice == "U":
        update_investigator(investigator)
        return True
    elif choice == "B":
        return False
    elif choice == "0":
        exit_program()
    else:
        print("Invalid Choice")
        return True


def list_investigators(investigators):
    for i in range(len(investigators)):
        print(f"{i+1}. {investigators[i].name}")
    print("\n")


def investigators_menu():
    print("Type A to add a new Investigator to this Site")
    print("Type B to go back")
    print("Type the number of an Investigator to view its details")
    print("Type 0 to exit the program")
    print("---------------------------")


def add_investigator(site_id):
    name = input("Enter the Investigator's name: ")
    project_id = input("Enter the Investigator's project id: ")
    try:
        investigator = Investigator.create(name, site_id, int(project_id))
        print(f"Successfully added {name} to this Site's Investigator's")
        print("\n")
    except Exception as exc:
        if type(exc).__name__ == "ValueError":
            print(
                "Error creating Investigator: the project id you supplied is not a number"
            )
        else:
            print("Error creating Investigator: ", exc)
            print("\n")


def investigator_details_menu():
    print("Type D to delete this investigator")
    print("Type U to update this investigator")
    print("Type B to go back")
    print("Type 0 to exit the program")
    print("---------------------------")


def update_investigator(investigator):
    id = investigator.id
    try:
        # consider replacing project id with project name
        investigator.name = input("Enter new name: ")
        investigator.site_id = int(input("Enter new site id: "))
        investigator.project_id = int(input("Enter new project id: "))
        print("\n")
        investigator.update()
    except Exception as exc:
        print("Error updating investigator: ", exc)
        print("\n")


def projects(site):
    if not site == "all":
        projects = site.projects()
        print(f"{site.name} Projects:")
        list_projects(projects)
        projects_menu()
        choice = input("> ")
        if choice == "B":
            return False
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")
            return True


def list_projects(projects):
    for i in range(len(projects)):
        print(f"{i+1}. {projects[i].title} (id: {projects[i].id})")
    print("\n")


def projects_menu():
    print("Type B to go back")
    print("Type 0 to exit the program")
    print("---------------------------")
