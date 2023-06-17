# Erstelle eine Datenbank mit folgenden Tabellen:
# warehouse:
# id (integer, primary key)
# product (text)
# amount (integer)
# price (real)
# reorder_level (integer)
#
# sales:
# id (integer, primary key)
# product (id aus warehouse)
# amount (integer)
# price (real)
# customer (integer aus customer)
# date (text)
#
# customer:
# id (integer, primary key)
# name (text)
# address (text)
# city (text)
# country (text)
#
# Benutze folgende Insert-Befehle, um Daten in die Tabellen einzufügen:
# warehouse:
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Schraube 3x30 metrisch', 312, 0.17, 50)
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Stahlplatte 5000x2000x5', 15, 2494, 7)
# INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Drallrohr', 40, 4994, 10)
#
# customer:
# INSERT INTO customer (name, address, city, country) VALUES ('Müller GmbH', 'Hauptstraße 1', 'Berlin', 'Deutschland')
# INSERT INTO customer (name, address, city, country) VALUES ('Schmidt KG', 'Hauptstraße 2', 'Wien', 'Österreich
# INSERT INTO customer (name, address, city, country) VALUES ('Meyer AG', 'Hauptstraße 3', 'Zürich', 'Schweiz')
#
# sales:
# INSERT INTO sales (product, amount, price, customer, date) VALUES (1, 100, 0.17, 1, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (2, 1, 2494, 2, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (3, 1, 4994, 3, '2023-01-01')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (1, 100, 0.17, 1, '2023-01-02')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (2, 1, 2494, 2, '2023-01-02')
# INSERT INTO sales (product, amount, price, customer, date) VALUES (3, 1, 4994, 3, '2023-01-02')
#
# Gebe auf der Konsole alle Produkte aus die an die Schmid KG verkauft wurden.


# Herstellen der Verbindung zur Datenbank
import sqlite3




def create_table(table, columns, cursor):
    # Erstellen einer Tabelle mit dem Namen warehouse
    if cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone() is not None:
        # Tabelle löschen, falls sie bereits existiert
        cursor.execute(f"DROP TABLE {table}", )
    cursor.execute(f"CREATE TABLE {table} ({columns})")
    connection.commit()


# Verbindung zur Datenbank herstellen
connection = sqlite3.connect("erm.db")
connection.row_factory = sqlite3.Row

# Erstellen eines Cursors
# Ein Cursor ist ein Objekt, das die Kommunikation mit der Datenbank verwaltet.
# Mit dem Cursor können Sie SQL-Anweisungen ausführen.

cursor = connection.cursor()

create_table("warehouse", "id INTEGER PRIMARY KEY, product TEXT, amount INTEGER, price REAL, reorder_level INTEGER"
             , cursor)
create_table("sales", "id INTEGER PRIMARY KEY, product INTEGER, amount INTEGER, price REAL, customer INTEGER, date TEXT"
             , cursor)
create_table("customer", "id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, country TEXT"
             , cursor)

# Daten in die Tabelle warehouse einfügen
tuple_list_of_warehouse = [
    ('Schraube 3x30 metrisch', 312, 0.17, 50),
    ('Stahlplatte 5000x2000x5', 15, 2494, 7),
    ('Drallrohr', 40, 4994, 10)
]
cursor.executemany(
    "INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ( ?, ?, ?, ?)", tuple_list_of_warehouse)
tuple_list_of_customer = [
    ('Müller GmbH', 'Hauptstraße 1', 'Berlin', 'Deutschland'),
    ('Schmidt KG', 'Hauptstraße 2', 'Wien', 'Österreich'),
    ('Meyer AG', 'Hauptstraße 3', 'Zürich', 'Schweiz')
]
cursor.executemany(
    "INSERT INTO customer (name, address, city, country) VALUES ( ?, ?, ?, ?)", tuple_list_of_customer)


tuple_list_of_sales = [
    (1, 100, 0.17, 1, '2023-01-01'),
    (3, 1, 2494, 2, '2023-01-01'),
    (3, 1, 4994, 3, '2023-01-01'),
    (1, 100, 0.17, 1, '2023-01-02'),
    (1, 1200, 0.32, 2, '2023-01-02'),
    (3, 1, 4994, 3, '2023-01-02')
]
cursor.executemany(
    "INSERT INTO sales (product, amount, price, customer, date) VALUES (?, ?, ?, ?, ?)", tuple_list_of_sales)
connection.commit()

# Bsp um left join erweitern
cursor.execute(
    "SELECT sales.amount, sales.price, sales.product, "
    "customer.name as customer_name, "
    "warehouse.product as product_name FROM warehouse JOIN sales ON warehouse.id = sales.product "
    "JOIN customer ON sales.customer = customer.id")
rows = cursor.fetchall()

list_of_sold_products = [dict(zip(row.keys(), row)) for row in rows]

total_price = 0
for product in list_of_sold_products:
    total_price += product["price"] * product["amount"]


for product in list_of_sold_products:
    print(product)
print(f"Total price: {total_price}")
