from flask import Flask, render_template

import forecast as fc

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cities.json")
def cities():
    return fc.get_communities()


@app.route("/forecast/<community>")
def forecast(community):
    city_params = get_gps_by_community(community)
    station = fc.get_best_weather_station_for_gps(city_params["longitude"], city_params["latitude"],
                                                  city_params["distance"])
    return {'data': fc.request_forecast_from_dwd(station["station_identifier"])}


@app.route("/community/<community>")
def get_gps_by_community(community):
    return fc.get_geo_coordinates(community)


if __name__ == "__main__":
    app.run(debug=True)
