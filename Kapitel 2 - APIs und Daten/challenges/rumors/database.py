import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.db.row_factory = sqlite3.Row
        print("DB connection initialized")

    def read_one_row(self, statement, values=()):
        resource = self.db.execute(statement, values)
        row = resource.fetchone()
        return dict(zip(row.keys(), row))

    def read_all_rows(self, statement, values=()):
        resource = self.db.execute(statement, values)
        rows = resource.fetchall()
        return list(dict(zip(row.keys(), row)) for row in rows)

    def change(self, statement, values=()):
        print(values)
        result = self.db.execute(statement, values)
        self.db.commit()
        return result.lastrowid

    def __del__(self):
        self.db.close()
        print("DB connection destroyed.")
