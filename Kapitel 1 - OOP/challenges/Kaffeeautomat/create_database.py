from datetime import datetime
import sqlite3

with sqlite3.connect("./acb.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE statistics")
    cur.execute("DROP TABLE beverages")

    cur.execute("CREATE TABLE statistics(timestamp, beverage)")
    cur.execute("CREATE TABLE beverages(beverage_name, water, beans, milk, coffee_ground)")

    cur.execute(f'INSERT INTO statistics VALUES ("{datetime.now()}", "Latte Macchiato")')
    cur.execute(f'INSERT INTO beverages VALUES ("Americano", 200, 15, 0, 20)')
    cur.execute(f'INSERT INTO beverages VALUES ("Latte Macchiato", 80, 10, 200, 14)')
    cur.execute(f'INSERT INTO beverages VALUES ("Espresso", 25, 200, 0, 210)')
    cur.execute(f'INSERT INTO beverages VALUES ("Teewasser", 800, 0, 0, 0)')

    con.commit()

    res = cur.execute("SELECT * FROM statistics")
    print(res.fetchall())

    res = cur.execute("SELECT * FROM beverages")
    print(res.fetchall())
