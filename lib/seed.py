#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.investigator import Investigator
from models.site import Site
from models.project import Project


def seed_database():
    Site.drop_table()
    Site.create_table()
    Site.create("James J. Peters VA", "Bronx", "Government"),
    Site.create("Mount Sinai", "New York City", "Medical"),
    Site.create("Harvard", "Cambridge", "Academic"),
    Site.create("UChicago", "Chicago", "Academic"),
    Site.create("Central Texas VA", "Waco", "Government"),


seed_database()
print("Seeded database from seed.py")
