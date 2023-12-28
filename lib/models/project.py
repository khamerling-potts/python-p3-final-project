from models.__init__ import CURSOR, CONN

# from models.investigator import Investigator
# from models.site import Site


class Project:
    all = {}

    def __init__(self, title, funding, id=None):
        self.id = id
        self.title = title
        self.funding = funding

    def __repr__(self):
        return f"Project {self.id}: {self.title} | ${self.funding} in funding"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not title.isdigit() and len(title) > 2:
            self._title = title
        else:
            raise Exception(
                "Project's title must be a string at least 3 characters long"
            )

    @property
    def funding(self):
        return self._funding

    @funding.setter
    def funding(self, funding):
        # Accounts for user input which comes in as a string, as well as seeded data which comes in as an int
        if isinstance(funding, str) and funding.isdigit():
            funding = int(funding)
        if isinstance(funding, int) and (funding >= 1000 or funding == 0):
            self._funding = funding
        else:
            raise Exception(
                "Project's funding amount must be an integer equal to 0 or greater than 999"
            )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            title TEXT,
            funding INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS projects"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, title, funding):
        project = cls(title, funding)
        sql = """
            INSERT INTO projects (title, funding)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (title, funding))
        CONN.commit()
        project.id = CURSOR.lastrowid
        cls.all[project.id] = project
        return project

    def update(self):
        sql = """
            UPDATE projects
            SET title = ?, funding = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.funding, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM projects WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        if project := cls.all[row[0]]:
            project.title = row[1]
            project.funding = row[2]
        else:
            project = cls(row[1], row[2], row[0])
            cls.all[project.id] = project
        return project

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM projects"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        all_projects = cls.get_all()
        filtered = list(filter(lambda instance: instance.id == id, all_projects))
        return filtered[0] if len(filtered) else None

    @classmethod
    def find_by_title(cls, title):
        all_projects = cls.get_all()
        filtered = list(filter(lambda instance: instance.title == title, all_projects))
        return filtered[0] if len(filtered) else None

    def investigators(self):
        from models.investigator import Investigator

        sql = """SELECT * FROM investigators WHERE project_id = ?"""
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Investigator.instance_from_db(row) for row in rows]

    def sites(self):
        from models.site import Site

        sql = """
            SELECT * FROM sites
            INNER JOIN investigators
            ON sites.id = investigators.site_id
            WHERE investigators.project_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        sites = [Site.instance_from_db(row) for row in rows]
        return list(set(sites))
