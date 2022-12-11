import pandas as pd
import sqlite3

con = sqlite3.connect("weather_data.db")
cur = con.cursor()

data_frame = pd.read_excel('gemeinden.xlsx', sheet_name="Onlineprodukt_Gemeinden", header=None)

communities = data_frame[7].tolist()[7:-12]
print(communities)
long = data_frame[14].tolist()[7:-12]
lat = data_frame[15].tolist()[7:-12]
total = set(zip(communities, long, lat))
final = []
for entry in total:
    if entry[0] is not None and type(entry[1]) is str and type(entry[2]) is str:
        long = float(entry[1].replace(",", "."))
        lat = float(entry[2].replace(",", "."))
        sql = """
            INSERT INTO communities (community, latitude, longitude) VALUES (?, ?, ?)
        """
        print(entry[0])
        cur.execute(sql, (entry[0], long, lat))

con.commit()
