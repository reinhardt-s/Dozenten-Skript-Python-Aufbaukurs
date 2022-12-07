from datetime import datetime
import sqlite3

from werkzeug.security import generate_password_hash

with sqlite3.connect("./attendees.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE attendees")
    cur.execute("DROP TABLE users")

    cur.execute("CREATE TABLE attendees(attendee_id text primary key, name, skill_level)")
    cur.execute("CREATE TABLE users(name, password)")

    cur.execute(f'INSERT INTO attendees VALUES ("14", "Edalyn Clawthorne", 100)')
    cur.execute(f'INSERT INTO attendees VALUES ("if1433", "Gus Porter", 60)')
    password = generate_password_hash("12354")
    cur.execute(f'INSERT INTO users VALUES ("craft", "{password}")')

    con.commit()

    res = cur.execute("SELECT * FROM attendees")
    print(res.fetchall())

    res = cur.execute("SELECT * FROM users")
    print(res.fetchall())
