from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Attendees(Resource):
    def get(self):
        return {'name': 'Robert'}


api.add_resource(Attendees, '/')

if __name__ == '__main__':
    app.run(debug=True)
