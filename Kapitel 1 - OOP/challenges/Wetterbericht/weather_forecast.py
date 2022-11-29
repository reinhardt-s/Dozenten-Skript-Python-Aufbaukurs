import matplotlib.pyplot as plt
import requests

STATION_ID = "10441"
r = requests.get(f'https://dwd.api.proxy.bund.dev/v30/stationOverviewExtended?stationIds={STATION_ID}')
print(r.text)
as_dict = r.json()

days = as_dict[STATION_ID]["days"]
start = as_dict[STATION_ID]["forecast1"]["start"]
step = as_dict[STATION_ID]["forecast1"]["timeStep"]
temps = []
temps_max = []
dates = []
for i, day in enumerate(days):
    date = day["dayDate"]
    high_temp = round(day["temperatureMax"] / 10)
    low_temp = round(day["temperatureMin"] / 10)
    sunrise = str((day["sunrise"] - start) / step)
    temps.append(day["temperatureMin"] / 10)
    temps_max.append(day["temperatureMax"] / 10)
    dates.append(date)

    sunset = str((day["sunset"] - start) / step)
    sunrise_hour = str(int(sunrise[:sunrise.index('.')]) - (i * 24))
    sunrise_minute = str(float("0." + sunrise[sunrise.index('.') + 1:]) * 60)
    sunrise_minute = sunrise_minute[:sunrise_minute.index(".")]
    if len(sunrise_hour) == 1:
        sunrise_hour = "0" + sunrise_hour
    if len(sunrise_minute) == 1:
        sunrise_minute = "0" + sunrise_minute

    sunrise = f"{sunrise_hour}:{sunrise_minute}"

    sunset_hour = str(int(sunset[:sunset.index('.')]) - (i * 24))
    sunset_minute = str(float("0." + sunset[sunset.index('.') + 1:]) * 60)
    sunset_minute = sunset_minute[:sunset_minute.index(".")]
    if len(sunset_hour) == 1:
        sunset_hour = "0" + sunset_hour
    if len(sunset_minute) == 1:
        sunset_minute = "0" + sunset_minute

    sunset = f"{sunset_hour}:{sunset_minute}"

    print(f"Vorhersage für: {date}")
    print(f"Temperatur von: {low_temp}°C bis {high_temp}°C")
    print(f"Sonnenaufgang um {sunrise} Uhr - Sonnenuntergang um {sunset} Uhr")
    print("#" * 57)
    print()
plt.plot(dates, temps)
plt.plot(dates, temps_max)
plt.show()