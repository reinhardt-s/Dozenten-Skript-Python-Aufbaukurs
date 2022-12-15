import uuid

from flask import Flask, request, render_template, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from database import Database

app = Flask(__name__)
auth = HTTPBasicAuth()

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


@app.route("/", methods=['GET', 'POST'])
def index():
    db = Database()

    if request.method == 'POST':
        rumor_id = uuid.uuid1().hex
        db.change('INSERT INTO rumors VALUES (?, ?, ?, ?, ?)',
                  (rumor_id, request.form['new_rumor'], 0, 0, request.form['username']))

    rumors = db.read_all_rows(f'SELECT * from rumors order by rowid desc')
    return render_template("index.html", rumors=rumors)


# read one
@app.route('/one/<rumor_id>', methods=['GET'])
def get(rumor_id):
    db = Database()
    return db.read_one_row(f'SELECT * from rumors where rumor_id = ?', (rumor_id,))


# read all
@app.route('/all', methods=['GET'])
def get_all():
    db = Database()
    rumors_list = db.read_all_rows(f'SELECT * from rumors')
    return {'rumors': rumors_list}


# update
@app.route('/<rumor_id>', methods=['PUT'])
def put(rumor_id):
    rumor = request.json
    db = Database()
    db.change("UPDATE rumors SET name = ?, skill_level = ?  WHERE rumor_id = ?",
              (rumor['name'], rumor['skill_level'], rumor_id))
    return {'rumor_id': rumor_id}


@app.route('/spread/<rumor_id>', methods=['PUT'])
def put_spread(rumor_id):
    db = Database()
    rumor = db.read_one_row(f'SELECT * from rumors where rumor_id = ?', (rumor_id,))
    db.change("UPDATE rumors SET propagated = ? WHERE rumor_id = ?",
              (rumor['propagated'] + 1, rumor_id))
    return {'propagated': rumor['propagated'] + 1}


@app.route('/love/<rumor_id>', methods=['PUT'])
def put_love(rumor_id):
    db = Database()
    rumor = db.read_one_row(f'SELECT * from rumors where rumor_id = ?', (rumor_id,))
    db.change("UPDATE rumors SET loved = ? WHERE rumor_id = ?",
              (rumor['loved'] + 1, rumor_id))
    return {'loved': rumor['loved'] + 1}


# delete
@app.route('/<rumor_id>', methods=['DELETE'])
@auth.login_required
def delete(rumor_id):
    db = Database()
    db.change("DELETE FROM rumors WHERE rumor_id = ?",
              (rumor_id,))
    return {'rumor_id': rumor_id}


if __name__ == '__main__':
    app.run(debug=True)
