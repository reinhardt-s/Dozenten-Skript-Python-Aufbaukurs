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
user_list = {user['name']: user['password'] for user in users_rows}

@auth.verify_password
def verify_password(username, password):
    return user_list.get(username) and check_password_hash(user_list.get(username), password)

# read one
@app.route('/<attendee_id>', methods=['GET'])
def get(attendee_id):
    return attendees.get(attendee_id, 404)

# read all
@app.route('/', methods=['GET'])
def get_all():
    return {'attendees': attendees}

# create
@app.route('/', methods=['POST'])
def post():
    attendee_id = uuid.uuid1().hex
    attendees[attendee_id] = request.json
    return {'attendee_id': attendee_id}

# update
@app.route('/<attendee_id>', methods=['PUT'])
def put(attendee_id):
    attendees[attendee_id] = request.json
    return {'attendee_id': attendee_id}

# delete
@app.route('/<attendee_id>', methods=['DELETE'])
@auth.login_required
def delete(attendee_id):
    result = attendees.pop(attendee_id, 404)
    return {'attendee_id': attendee_id}

if __name__ == '__main__':
    app.run(debug=True)
