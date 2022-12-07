from dataclasses import dataclass

import requests

from data.database import Database

SEARCH_RANGE = .5
DWD_API_URL = 'https://dwd.api.proxy.bund.dev/v30/stationOverviewExtended?stationIds='


def get_communities():
    db = Database()
    return {'communities': db.read_all_rows("SELECT community FROM communities")}


def get_geo_coordinates(community):
    db = Database()
    return db.read_one_row(
        "SELECT longitude, latitude, (longitude + latitude) as distance FROM communities WHERE community = ?",
        (community,))


def get_best_weather_station_for_gps(long, lat, distance):
    min_long = long - SEARCH_RANGE
    max_long = long + SEARCH_RANGE
    min_lat = lat - SEARCH_RANGE
    max_lat = lat + SEARCH_RANGE
    db = Database()
    stations = db.read_all_rows(
        "SELECT *, (longitude + latitude) as distance FROM weather_stations WHERE longitude >= ? AND longitude <= ? "
        "AND latitude >= ? AND latitude <= ? AND identifier = 'MN'", (min_long, max_long, min_lat, max_lat))

    # rate station by distance to community center
    best_station = None
    best_distance = 999
    for station in stations:
        if abs(station['distance'] - distance) < best_distance:
            best_distance = abs(station['distance'] - distance)
            best_station = station
        print(station)

    print(f"Nächste Station ist: {best_station}")
    return best_station


def resolve_time(time, start, step, day_count):
    resolved = str((time - start) / step)
    resolved_hour = str(int(resolved[:resolved.index('.')]) - (day_count * 24))
    resolved_minute = str(float("0." + resolved[resolved.index('.') + 1:]) * 60)
    resolved_minute = resolved_minute[:resolved_minute.index(".")]
    if len(resolved_hour) == 1:
        resolved_hour = "0" + resolved_hour
    if len(resolved_minute) == 1:
        resolved_minute = "0" + resolved_minute

    return f"{resolved_hour}:{resolved_minute}"


def request_forecast_from_dwd(station_id):
    response = requests.get(f'{DWD_API_URL}{station_id}')
    # create dictionary from response data
    as_dict = response.json()

    # days that have a forecast
    days = as_dict[station_id]["days"]
    # first time station measured data
    start = as_dict[station_id]["forecast1"]["start"]
    # time increments
    step = as_dict[station_id]["forecast1"]["timeStep"]

    output = []
    for day_count, day in enumerate(days):
        # temperature is given without comma
        # in order to get the exact time we need to do some math
        forecast = {'date': day["dayDate"],
                    'highest_temperature': round(day["temperatureMax"] / 10),
                    'lowest_temperature': round(day["temperatureMin"] / 10),
                    'sunrise': resolve_time(day["sunrise"], start, step, day_count),
                    'sunset': resolve_time(day["sunset"], start, step, day_count)}

        print(forecast)
        output.append(forecast)
    return output
