#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb

from models.investigator import Investigator
from models.site import Site
from models.project import Project
from random import choice
from faker import Faker


def reset_database():
    Site.drop_table()
    Site.create_table()
    sites = [
        Site.create("James J. Peters VA", "Bronx", "Government"),
        Site.create("Mount Sinai", "New York City", "Medical"),
        Site.create("Harvard", "Cambridge", "Academic"),
        Site.create("UChicago", "Chicago", "Academic"),
        Site.create("Central Texas VA", "Waco", "Government"),
    ]
    print("did sites")

    Project.drop_table()
    Project.create_table()
    projects = [
        Project.create("Predicting Depression in Long COVID Patients", 100000),
        Project.create("Project Life Force - Randomized Control Trial", 1500000),
        Project.create("Prognostic and Diagnostic PTSD Biomarkers", 500000),
        Project.create("Telehealth CBT for Chronic Pain", 750000),
        Project.create("Interpersonal Emotion Regulation in Young Adults", 2000),
        Project.create("Neuroimaging to Predict Bipolar Disorder", 9300000),
        Project.create("Comorbidity of OCD and Autism - A Longitudinal Study", 40000),
    ]
    print("did projects")

    Investigator.drop_table()
    Investigator.create_table()
    for i in range(30):
        Investigator.create(
            Faker().unique.name(), choice(sites).id, choice(projects).id
        )
    print("did investigators")


reset_database()
print("Seeded database from debug.py")

ipdb.set_trace()
