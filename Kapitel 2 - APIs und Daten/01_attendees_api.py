import uuid

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from database_01 import Database

app = Flask(__name__)
auth = HTTPBasicAuth()


# start up config
attendees = {
    "1d38e455759a11eda3e394de807959fa": {'name': 'James Dean', 'skill_level': 'expert'}
}

users = {
    "john": generate_password_hash("deer"),
    "susan": generate_password_hash("sanders")
}

# db based config
user_db = Database()
users_rows = user_db.read_all_rows('SELECT name, password from users')

user_list = dict()

for user in users_rows:
    user_list[user['name']] = user['password']


@auth.verify_password
def verify_password(username, password):
    if username in user_list and check_password_hash(user_list.get(username), password):
        return username


# read one
@app.route('/<attendee_id>', methods=['GET'])
def get(attendee_id):

    # startup config
    return attendees[attendee_id]

    # db config
    # threaded
    # db = Database()
    # return db.read_one_row(f'SELECT * from attendees where attendee_id = ?', (attendee_id,))


# read all
@app.route('/', methods=['GET'])
def get_all():
    # startup config
    attendees_list = attendees

    # db config
    # threaded
    # db = Database()
    # attendees_list = db.read_all_rows(f'SELECT * from attendees')
    return {'attendees': attendees_list}


# create
@app.route('/', methods=['POST'])
def post():
    attendee_id = uuid.uuid1().hex

    # start up config
    attendees[attendee_id] = request.json

    # db config
    # attendee = request.json
    # db = Database()
    # db.change('INSERT INTO attendees VALUES (?, ?, ?)', (attendee_id, attendee['name'], attendee['skill_level']))

    return {'attendee_id': attendee_id}


# update
@app.route('/<attendee_id>', methods=['PUT'])
def put(attendee_id):
    # startup config
    attendees[attendee_id] = request.json

    # db config
    # attendee = request.json
    # db = Database()
    # db.change("UPDATE attendees SET name = ?, skill_level = ?  WHERE attendee_id = ?",
    #           (attendee['name'], attendee['skill_level'], attendee_id))
    return {'attendee_id': attendee_id}


# delete
@app.route('/<attendee_id>', methods=['DELETE'])
@auth.login_required
def delete(attendee_id):
    # startup config
    result = attendees.pop(attendee_id, 404)
    # db config
    # db = Database()
    # db.change("DELETE FROM attendees WHERE attendee_id = ?",
    #           (attendee_id,))
    return {'attendee_id': attendee_id}


if __name__ == '__main__':
    app.run(debug=True)
