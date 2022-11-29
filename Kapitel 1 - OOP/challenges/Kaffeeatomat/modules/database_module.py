import logging
import sqlite3
from datetime import datetime
from .log import log


class DatabaseModule:

    def __init__(self):
        log.debug("Database module initialized")
        self.con = sqlite3.connect("acb.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def get_brew_count(self):
        res = self.cur.execute("SELECT COUNT(*) FROM statistics")
        count = res.fetchall()
        return count

    def add_entry(self, beverage):
        self.cur.execute(f'INSERT INTO statistics VALUES ("{datetime.now()}", "{beverage}")')
        self.con.commit()

    def get_beverage_by_name(self, name):
        res = self.cur.execute(f'SELECT water, beans, milk, coffee_ground FROM beverages where beverage_name = "{name}"')
        beverage = res.fetchone()
        return dict(zip(beverage.keys(), beverage))

    def __del__(self):
        self.con.close()
        self.logger.debug("Database module destroyed")
