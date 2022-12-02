import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cities.json")
def cities():
    cities_list = [
        "Kassel",
        "Wolfhagen",
        "Berlin",
        "Habichtswald"
    ]
    return json.dumps(cities_list)


if __name__ == "__main__":
    app.run(debug=True)
