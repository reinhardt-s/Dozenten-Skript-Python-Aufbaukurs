import os
import sqlite3

from werkzeug.security import generate_password_hash

DB_FILE = "./database.db"

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

with sqlite3.connect(DB_FILE) as con:
    cur = con.cursor()

    cur.execute("CREATE TABLE rumors(rumor_id text primary key, rumor text, propagated int, loved int, user text)")
    cur.execute("CREATE TABLE users(name, password)")

    cur.execute(f'INSERT INTO rumors VALUES ("1d38e455759a11eda3e394de807959fa", "Weihnachten soll dieses Jahr auf '
                f'Sylvester fallen", 12, 51, "Riley Weinberg")')
    cur.execute(f'INSERT INTO rumors VALUES ("1d38e4557sd4g54f4db594de807959fa", "PC-College wird auch kommendes Jahr '
                f'den Bildungs-Award gewinnen.", 43, 144, "Alex Fine")')

    password = generate_password_hash("12354")
    cur.execute(f'INSERT INTO users VALUES ("craft", "{password}")')

    con.commit()

    res = cur.execute("SELECT * FROM rumors")
    print(res.fetchall())

    res = cur.execute("SELECT * FROM users")
    print(res.fetchall())
