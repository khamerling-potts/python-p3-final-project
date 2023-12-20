from models.__init__ import CURSOR, CONN

# from models.investigator import Investigator
# from models.site import Site


class Project:
    def __init__(self, title, funding, id=None):
        self.id = id
        self.title = title
        self.funding = funding
