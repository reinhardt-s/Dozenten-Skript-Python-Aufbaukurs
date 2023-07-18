import sqlite3
from werkzeug.security import generate_password_hash

attendees = [
    ("14", "Edalyn Clawthorne", 100),
    ("if1433", "Gus Porter", 60)
]

users = [
    ("craft", "12354")
]

with sqlite3.connect("./attendees.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS attendees")
    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("CREATE TABLE attendees(attendee_id TEXT PRIMARY KEY, name TEXT, skill_level INTEGER)")
    cur.execute("CREATE TABLE users(name TEXT, password TEXT)")

    cur.executemany('INSERT INTO attendees VALUES (?, ?, ?)', attendees)
    hashed_password = generate_password_hash(users[0][1])
    cur.execute('INSERT INTO users VALUES (?, ?)', (users[0][0], hashed_password))

    con.commit()

    res = cur.execute("SELECT * FROM attendees")
    print(res.fetchall())

    res = cur.execute("SELECT * FROM users")
    print(res.fetchall())
