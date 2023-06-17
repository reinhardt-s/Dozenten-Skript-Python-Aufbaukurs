# Herstellen der Verbindung zur Datenbank
import sqlite3

# Verbindung zur Datenbank herstellen
connection = sqlite3.connect("erm.db")

# Erstellen eines Cursors
# Ein Cursor ist ein Objekt, das die Kommunikation mit der Datenbank verwaltet.
# Mit dem Cursor können Sie SQL-Anweisungen ausführen.

cursor = connection.cursor()

# Erstellen einer Tabelle
# Valide Datentypen für sqlite3: NULL, INTEGER, REAL, TEXT, BLOB
# Nullwerte werden mit NULL belegt
# INTEGER: Ganzzahlen
# REAL: Gleitkommazahlen
# TEXT: Text
# BLOB: Binärdaten

# Erstellen einer Tabelle mit dem Namen warehouse
if cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='warehouse'").fetchone() is not None:
    # Tabelle löschen, falls sie bereits existiert
    cursor.execute("DROP TABLE warehouse")
cursor.execute(
    "CREATE TABLE warehouse (id INTEGER PRIMARY KEY, product TEXT, amount INTEGER, price REAL, reorder_level INTEGER)")

# Erstellen einer Tabelle mit dem Namen sales
if cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'").fetchone() is not None:
    # Tabelle löschen, falls sie bereits existiert
    cursor.execute("DROP TABLE sales")
cursor.execute(
    "CREATE TABLE sales (id INTEGER PRIMARY KEY, product INTEGER, amount INTEGER, "
    "price REAL, customer INTEGER, date TEXT)")

# Info:
# In SQLite, dem in Python eingebauten Datenbankmodul,
# wird die AUTOINCREMENT-Funktion auf die Spalte ID angewendet,
# sobald Sie sie als PRIMARY KEY deklarieren. SQLite verfolgt die höchste ROWID,
# die jemals in einer Tabelle verwendet wurde, und die nächste ID wird immer eins höher sein.

# Erstellen von Beispiel-Datensätzen für ein Maschinenbauunternehmen
cursor.execute(
    "INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Schraube 3x30 metrisch', 100, 0.05, 50)")
cursor.execute(
    "INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Stahlplatte 5000x2000x5', 15, 2494, 7)")
cursor.execute(
    "INSERT INTO warehouse (product, amount, price, reorder_level) VALUES ('Drallrohr', 40, 4994, 10)")

cursor.execute(
    "INSERT INTO sales (product, amount, price, customer, date) VALUES (1, 10, 0.05, 1, '2023-01-01')")
cursor.execute(
    "INSERT INTO sales (product, amount, price, customer, date) VALUES (2, 1, 2494, 2, '2023-01-01')")
cursor.execute(
    "INSERT INTO sales (product, amount, price, customer, date) VALUES (3, 1, 4994, 3, '2023-01-01')")

# Änderungen bestätigen
# Änderungen werden erst mit dem Commit-Befehl in die Datenbank geschrieben.
connection.commit()

# Lesezugriff auf die Datenbank
# Mit dem SELECT-Befehl können Sie Daten aus der Datenbank abrufen.
# Der Stern (*) bedeutet, dass alle Spalten ausgewählt werden sollen.
cursor.execute("SELECT * FROM warehouse")

# Ausgabe der Daten
# fetchone() gibt nur einen Datensatz zurück.
# fetchmany() gibt eine bestimmte Anzahl von Datensätzen zurück.
# fetchall() gibt alle Datensätze zurück.
print(cursor.fetchall())


class Inventory:
    def __init__(self, product, amount, price, reorder_level):
        self.product = product
        self.amount = amount
        self.price = price
        self.reorder_level = reorder_level

    def __repr__(self):
        return f"Product: {self.product}\nAmount: {self.amount}\nPrice: {self.price}\nReorder Level: {self.reorder_level}"


# Umwandlung der Daten in ein Objekt der Klasse Inventory
for row in cursor.execute("SELECT * FROM warehouse"):
    item = Inventory(row[1], row[2], row[3], row[4])
    print(item)

# ohne id Spalte, mit List Comprehension
items = [Inventory(row[0], row[1], row[2], row[3]) for row in
         cursor.execute("SELECT product, amount, price, reorder_level FROM warehouse")]
print(items)

# Select mit (Inner)-Join
# Mit dem JOIN-Befehl können Sie Daten aus mehreren Tabellen abrufen.
# Der ON-Befehl gibt an, welche Spalten aus den Tabellen übereinstimmen müssen.
# Der AS-Befehl gibt an, wie die Spalten in der Ausgabe benannt werden sollen.
cursor.execute(
    "SELECT sales.id, sales.date, sales.amount, sales.price, warehouse.product, warehouse.amount, warehouse.price, "
    "warehouse.reorder_level FROM sales JOIN warehouse ON sales.product = warehouse.id")

print(cursor.fetchall())

# Umwandlung in Dictionary
items = [dict(product=row[0], amount=row[1], price=row[2], reorder_level=row[3]) for row in cursor.execute(
    "SELECT product, amount, price, reorder_level FROM warehouse")]
print(items)

# Änderung der Daten
# Mit dem UPDATE-Befehl können Sie Daten in der Datenbank ändern.
# Der WHERE-Befehl gibt an, welche Zeile geändert werden soll.
cursor.execute("UPDATE warehouse SET amount = 200 WHERE id = 1")
connection.commit()

cursor.execute("SELECT * FROM warehouse WHERE id = 1")
print(cursor.fetchone())

# Insert or Update
# Mit dem INSERT OR REPLACE-Befehl können Sie Daten in der Datenbank ändern.
# Der WHERE-Befehl gibt an, welche Zeile geändert werden soll.
cursor.execute(
    "INSERT OR REPLACE INTO warehouse (id, product, amount, price, reorder_level) VALUES (1, 'Schraube 3x30 "
    "metrisch', 312, 0.17, 50)")
connection.commit()

cursor.execute("SELECT * FROM warehouse WHERE id = 1")
print(cursor.fetchone())

# Löschen von Daten
# Mit dem DELETE-Befehl können Sie Daten aus der Datenbank löschen.
# Der WHERE-Befehl gibt an, welche Zeile gelöscht werden soll.
cursor.execute("DELETE FROM warehouse WHERE id = 1")
connection.commit()

cursor.execute("SELECT * FROM warehouse WHERE id = 1")
print(cursor.fetchone())

# Verbindung schließen
connection.close()
