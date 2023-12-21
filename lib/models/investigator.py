from models.__init__ import CONN, CURSOR

from models.site import Site
from models.project import Project


class Investigator:
    all = {}

    def __init__(self, name, site_id, project_id, id=None):
        self.id = id
        self.name = name
        self.site_id = site_id
        self.project_id = project_id

    def __repr__(self):
        return f"Investigator {self.id}: {self.name} | Site {self.site_id} | Project {self.project_id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 1:
            self._name = name
        else:
            raise Exception(
                "Investigator's name must be a string at least two characters long."
            )

    @property
    def site_id(self):
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        if isinstance(site_id, int) and Site.find_by_id(site_id):
            self._site_id = site_id
        else:
            raise Exception(
                "An investigator's site_id must be an integer that references a site in the database"
            )

    # @property
    # def project_id(self):
    #     return self._project_id

    # @project_id.setter
    # def project_id(self, project_id):
    #     if isinstance(project_id, int) and Project.find_by_id(project_id):
    #         self._project_id = project_id
    #     else:
    #         raise Exception("An investigator's project_id must be an integer that references a project in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS investigators(
            id INTEGER PRIMARY KEY,
            name TEXT,
            FOREIGN KEY (site_id) REFERENCES sites(id)
        )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS investigators"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, site_id, project_id):
        investigator = Investigator(name, site_id, project_id)
        sql = """
            INSERT INTO TABLE investigators (name, site_id, project_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (name, site_id, project_id))
        CONN.commit()
        investigator.id = CURSOR.lastrowid
        cls.all[investigator.id] = investigator
        return investigator

    def update(self):
        sql = """
            UPDATE investigators
            SET name = ?, site_id = ?, project_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.site_id, self.project_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM investigators
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        if investigator := cls.all[row[0]]:
            investigator.name = row[1]
            investigator.site_id = row[2]
            investigator.project_id = row[3]
        else:
            investigator = cls(row[1], row[2], row[3], row[0])
            cls.all[investigator.id] = investigator
        return investigator

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM investigators"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        all_investigators = cls.get_all()
        filtered = list(filter(lambda instance: instance.id == id, all_investigators))
        return filtered[0] if len(filtered) else None

    @classmethod
    def find_by_name(cls, name):
        all_investigators = cls.get_all()
        filtered = list(
            filter(lambda instance: instance.name == name, all_investigators)
        )
        return filtered[0] if len(filtered) else None
