import requests
from weather_models import WeatherData


url = 'https://dataset.api.hub.zamg.ac.at/v1/station/historical/klima-v1-10min'
params = {
    'parameters': 'TL,RR,RRM',
    'start': '2020-12-24T08:00',
    'end': '2020-12-24T09:00',
    'station_ids': '5904'
}

response = requests.get(url, params=params)
data = response.json()

weather_data = WeatherData.from_json(data)
print(weather_data.features[0].properties.parameters['TL'].data[0])
