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
