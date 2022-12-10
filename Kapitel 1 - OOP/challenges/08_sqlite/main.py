# Frage die Nutzer*in via Kommandozeile, für welche Stadt sie die Geo-Koordinaten sehen möchten
#
# Laden sie vorher alle Städte bzw. Gemeinden-Namen aus der Tabelle communities in die Liste communities.
#
# Durchsuchen sie die Liste communities nach allen Einträgen,
# welche die Nutzer-Eingabe beinhalten: 'lin' findet unter anderem 'Berlin' und auch 'Lingenfeld'
#
# Präsentiere der Nutzer*in die Treffer und frage, welcher gemeint ist: 0: Berlin 1: Lingenfeld ...
#
# Frage abschließend von der Datenbank den Eintrag für community = gewählter Treffer ab und
# präsentiere in einem print-Statement, die Längen- und Breitengrade des Treffers
import sqlite3

DB_FILE = "./weather_data.db"


def request_db(statement, values=()):
    with sqlite3.connect(DB_FILE) as con:
        # Gebe sqlite3.Row anstelle von tuple zurück
        con.row_factory = sqlite3.Row
        # Erzeuge einen Cursor, der auf der Datenbank operieren kann
        cursor = con.cursor()
        result = cursor.execute(statement, values)
        return result.fetchall()


communities = [row['community'] for row in request_db("SELECT community FROM communities")]
user_input = input("Bitte Stadt oder Gemeindenamen eingeben.\n")

candidates = []
for community in communities:
    if user_input.lower() in community.lower():
        candidates.append(community)

for pos, candidate in enumerate(candidates):
    print(f'{pos}:\t{candidate}')

user_input = input("Welches dieser Ergebnisse meinen Sie?\n")
chosen_community = candidates[int(user_input)]
data = request_db('SELECT longitude, latitude FROM communities WHERE community = ?', (chosen_community,))
row = data[0]
print(f'Die Stadt bzw. Gemeinde {chosen_community} liegt bei '
      f'Längengrad {row["longitude"]} und Breitengrad {row["latitude"]}.')
