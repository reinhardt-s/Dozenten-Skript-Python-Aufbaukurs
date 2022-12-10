import os
import sqlite3

DB_FILE = "./support_tickets.db"

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# Stelle Verbindung zur Datenbank her
with sqlite3.connect(DB_FILE) as con:
    # Gebe sqlite3.Row anstelle von tuple zurück
    con.row_factory = sqlite3.Row
    # Erzeuge einen Cursor, der auf der Datenbank operieren kann
    cursor = con.cursor()
    # Führe SQL-Befehl aus
    cursor.execute("CREATE TABLE tickets(issue, resolved)")
    cursor.execute("INSERT INTO tickets VALUES ('Outlook startet nicht mehr.', FALSE)")
    cursor.execute("INSERT INTO tickets VALUES ('PC macht komische Geräusche. Klingt wie KBRRRR-whap-whap', TRUE)")
    cursor.execute("INSERT INTO tickets VALUES ('Der Monitor ist schwarz', FALSE)")
    # Setze SQL-Befehle ab
    con.commit()
    result = cursor.execute("SELECT * FROM tickets WHERE resolved = FALSE")
    rows = result.fetchall()
    for row in rows:
        # print(row)

        # https://docs.python.org/3/library/sqlite3.html?highlight=sqlite3%20row#sqlite3.Row
        # https://docs.python.org/3/library/functions.html?highlight=zip#zip
        # print(row['issue'])
        row = dict(zip(row.keys(), row))
        print(row)

        print(type(row))
