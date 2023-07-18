# Lade die Wetterdaten der letzten 5 Tage von der API des ZAMG herunter.
# Erstelle ein Diagramm, welches die Temperaturen der letzten 5 Tage anzeigt.
# Speichere das Diagramm als PNG und SVG ab.


import datetime
import matplotlib.pyplot as plt
import requests
from weather_models import WeatherData

# Define the time range for the weather data
to_time = datetime.datetime.now()
from_time = to_time - datetime.timedelta(days=5)

# Format the time range for the API request
to_time_str = to_time.strftime('%Y-%m-%dT%H:%M')
from_time_str = from_time.strftime('%Y-%m-%dT%H:%M')

# Define the API request URL
url = f'https://dataset.api.hub.zamg.ac.at/v1/station/historical/klima-v1-10min?parameters=TL,RR,RRM&start={from_time_str}&end={to_time_str}&station_ids=5904'

# Send the API request and parse the response
response = requests.get(url=url)
weather_data = WeatherData.from_json(response.json())

# Create the bar chart
plt.plot(weather_data.timestamps, weather_data.features[0].properties.parameters['TL'].data)

# Add title and axis labels
plt.title('Wetter der letzten 5 Tage')
plt.xlabel('Datum')
plt.ylabel('Temperaturen in °C')

# Save the chart as PNG and SVG files
plt.savefig('bar.png')
plt.savefig('bar.svg')

# Display the chart
plt.show()