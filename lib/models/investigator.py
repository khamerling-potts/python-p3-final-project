from models.__init__ import CONN, CURSOR

from models.site import Site
from models.project import Project


class Investigator:
    def __init__(self, name, site_id, project_id, id=None):
        self.id = id
        self.name = name
        self.site_id = site_id
        self.project_id = project_id
