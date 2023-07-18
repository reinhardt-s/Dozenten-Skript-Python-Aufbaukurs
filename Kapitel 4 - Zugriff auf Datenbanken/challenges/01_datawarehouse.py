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
    """
    Create a table with the given name and columns using the given cursor.
    If the table already exists, it will be dropped and recreated.
    """
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} ({columns})")

def insert_data(table, data, cursor):
    """
    Insert data into the given table using the given cursor.
    """
    cursor.executemany(f"INSERT INTO {table} VALUES ({','.join(['?']*len(data[0]))})", data)

# Establish a connection to the database
connection = sqlite3.connect("erm.db")
connection.row_factory = sqlite3.Row

# Create a cursor to execute SQL statements
cursor = connection.cursor()

# Create the tables
create_table("warehouse", "id INTEGER PRIMARY KEY, product TEXT, amount INTEGER, price REAL, reorder_level INTEGER", cursor)
create_table("sales", "id INTEGER PRIMARY KEY, product INTEGER, amount INTEGER, price REAL, customer INTEGER, date TEXT", cursor)
create_table("customer", "id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, country TEXT", cursor)

# Insert data into the tables
insert_data("warehouse", [
    ('Schraube 3x30 metrisch', 312, 0.17, 50),
    ('Stahlplatte 5000x2000x5', 15, 2494, 7),
    ('Drallrohr', 40, 4994, 10)
], cursor)

insert_data("customer", [
    ('Müller GmbH', 'Hauptstraße 1', 'Berlin', 'Deutschland'),
    ('Schmidt KG', 'Hauptstraße 2', 'Wien', 'Österreich'),
    ('Meyer AG', 'Hauptstraße 3', 'Zürich', 'Schweiz')
], cursor)

insert_data("sales", [
    (1, 100, 0.17, 1, '2023-01-01'),
    (3, 1, 2494, 2, '2023-01-01'),
    (3, 1, 4994, 3, '2023-01-01'),
    (1, 100, 0.17, 1, '2023-01-02'),
    (1, 1200, 0.32, 2, '2023-01-02'),
    (3, 1, 4994, 3, '2023-01-02')
], cursor)

# Retrieve all products sold to Schmidt KG
cursor.execute("""
    SELECT sales.amount, sales.price, warehouse.product as product_name
    FROM sales
    JOIN warehouse ON sales.product = warehouse.id
    JOIN customer ON sales.customer = customer.id
    WHERE customer.name = 'Schmidt KG'
""")
rows = cursor.fetchall()

# Print the results
total_price = 0
for row in rows:
    amount, price, product_name = row
    total_price += price * amount
    print(f"{amount} x {product_name} @ {price} €")

print(f"Total price: {total_price} €")

# Commit the changes to the database and close the connection
connection.commit()
connection.close()
