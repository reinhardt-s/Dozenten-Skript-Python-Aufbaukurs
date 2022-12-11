import requests
import re
import html
import sqlite3

con = sqlite3.connect("weather_data.db")
cur = con.cursor()

r = requests.get(
    'https://www.dwd.de/DE/leistungen/klimadatendeutschland/statliste/statlex_html.html?view=nasPublication&nn=16102')
matches = re.findall(
    '<tr><td>(.*?)</td><td align=right>(\\d*)</td><td align=center>(.*?)</td><td align=right>(\\d*)'
    '</td><td align=right>(\\d*\\.\\d*)</td><td align=right>(\\d*\\.\\d*)',
    r.text)

for entry in matches:
    print(
        f"Stationsname: {html.unescape(entry[0])} Stations_ID: {entry[1]} Kennung: {entry[2]} "
        f"Stationskennug: {entry[3]} Längengrad: {entry[4]} Breitengrad: {entry[5]}")
    sql = """
                INSERT INTO weather_stations (name, station_id, identifier, station_identifier, longitude, latitude ) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
    cur.execute(sql, (html.unescape(entry[0]), entry[1], entry[2], entry[3], float(entry[4]), float(entry[5])))

con.commit()
