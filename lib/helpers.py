# lib/helpers.py
from models.investigator import Investigator
from models.project import Project
from models.site import Site


def exit_program():
    print("Goodbye!")
    exit()


def list_sites():
    sites = Site.get_all()
    for i in range(len(sites)):
        print(f"{i+1}. {sites[i].name}")


def sites_menu():
    print("Type A to add a new Site")
    print("Type B to go back to main menu")
    print("Type the number of a Site to view its details")
    print("Type 0 to exit the program")


def add_site():
    name = input("Enter the Site's name: ")
    city = input("Enter the Site's city: ")
    classification = input(
        "Enter the Site's classification (Government, Academic, or Medical): "
    )
    try:
        site = Site.create(name, city, classification)
        list_sites()
    except Exception as exc:
        print("Error creating Site: ", exc)
        list_sites()


def site_details_menu():
    print("Type I to view the site's Investigators")
    print("Type P to see the site's Projects")
    print("Type B to go back")
    print("Type 0 to exit the program")


def site_details(index):
    site = Site.get_all()[index]
    print(f"{site.name}: {site.classification} institution located in {site.city}")
    site_details_menu()
    choice = input("> ")
    if choice == "I":
        while True:
            if not investigators(site):
                break
        return True
    elif choice == "B":
        return False


def sites():
    list_sites()
    sites_menu()
    choice = input("> ")
    if choice == "A":
        add_site()
        return True
    elif choice == "B":
        return False
    elif int(choice) in range(1, len(Site.get_all()) + 1):
        while True:
            if not site_details(int(choice) - 1):
                break
        return True
    elif choice == "0":
        exit_program()
    else:
        print("Invalid choice")


def investigators(site):
    if not site == "all":
        investigators = site.investigators()
        list_investigators(investigators)
        investigators_menu()
        choice = input("> ")
        if choice == "A":
            add_investigator(site.id)
            return True
        if choice == "B":
            return False


def list_investigators(investigators):
    for i in range(len(investigators)):
        print(f"{i+1}. {investigators[i].name}")


def investigators_menu():
    print("Type A to add a new Investigator to this Site")
    print("Type B to go back")
    print("Type the number of an Investigator to view its details")
    print("Type 0 to exit the program")


def add_investigator(site_id):
    name = input("Enter the Investigator's name: ")
    project_id = int(input("Enter the Investigator's project id: "))
    try:
        investigator = Investigator.create(name, site_id, project_id)
        print(f"Successfully added {name} to this Site's Investigator's")
    except Exception as exc:
        print("Error creating Investigator: ", exc)
