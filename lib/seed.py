#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.investigator import Investigator
from models.site import Site
from models.project import Project
from random import choice
from faker import Faker


def seed_database():
    Site.drop_table()
    Site.create_table()
    sites = [
        Site.create("James J. Peters VA", "Bronx", "Government"),
        Site.create("Mount Sinai", "New York City", "Medical"),
        Site.create("Harvard", "Cambridge", "Academic"),
        Site.create("UChicago", "Chicago", "Academic"),
        Site.create("Central Texas VA", "Waco", "Government"),
    ]

    Investigator.drop_table()
    Investigator.create_table()
    # add project id here instead of None
    for i in range(30):
        Investigator.create(Faker().unique.name(), choice(sites).id, None)


seed_database()
print("Seeded database from seed.py")
