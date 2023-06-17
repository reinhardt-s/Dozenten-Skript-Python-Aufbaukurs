# Lade die Wetterdaten der letzten 5 Tage von der API des ZAMG herunter.
# Erstelle ein Diagramm, welches die Temperaturen der letzten 5 Tage anzeigt.
# Speichere das Diagramm als PNG und SVG ab.


import datetime
import matplotlib.pyplot as plt
import requests
from weather_models import WeatherData

to_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
from_time = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime('%Y-%m-%dT%H:%M')
url = 'https://dataset.api.hub.zamg.ac.at/v1/station/historical/klima-v1-10min' \
      '?parameters=TL,RR,RRM&start={from_time}&end={to_time}&station_ids=5904'\
      .format(from_time=from_time, to_time=to_time)

print(url)
r = requests.get(url=url)

weather_data = WeatherData.from_json(r.json())

# Erstellen des Balkendiagramms
plt.plot(weather_data.timestamps, weather_data.features[0].properties.parameters['TL'].data)

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Wetter der letzten 5 Tage')
plt.xlabel('Datum')
plt.ylabel('Temperaturen in °C')

# Diagramm anzeigen
plt.savefig('bar.png')
plt.savefig('bar.svg')
plt.show()