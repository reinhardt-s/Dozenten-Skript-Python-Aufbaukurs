# Schreibe für einen Chat die API:
# Alle Nachrichten auslesen
# Eine Nachricht senden
# Die Nachrichten sollen in einer Klasse Message gespeichert werden.
# Nachrichten sollen in einer Datenbank gespeichert werden.
# Das Senden einer Nachricht muss authentifiziert erfolgen.
# Lege hierzu eine Tabelle users an, in der die User mit ihren gehasten Passwörtern gespeichert werden.
import uuid
from typing import List

import bcrypt as bcrypt
import uvicorn
import yaml
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

from database import Database

app = FastAPI()

security = HTTPBasic()


def create_database():
    db = Database()
    db.create_table('users', 'user_id', 'name', 'password')
    db.create_table('messages', 'message_id', 'message', 'user_id')
    return db


db = create_database()


class User(BaseModel):
    user_id: str | None = None
    name: str
    password: str | bytes

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'password': self.password
        }

    def to_yaml(self):
        return yaml.dump(self.to_json())

    @staticmethod
    def from_json(json):
        return User(id=json['user_id'], name=json['name'], password=json['password'])


class Message(BaseModel):
    id: str | None = None
    message: str
    user_id: str

    def to_json(self):
        return {
            'message_id': self.id,
            'message': self.message,
            'user_id': self.user_id
        }

    def to_yaml(self):
        return yaml.dump(self.to_json())

    @staticmethod
    def from_json(json):
        return Message(id=json['message_id'], message=json['message'], user_id=json['user_id'])


def get_users_from_db():
    db = Database()
    users = [User.from_json(db_user) for db_user in db.read_all_rows("SELECT user_id, name, password FROM users")]
    return users


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    users = get_users_from_db()
    user_list = [user for user in users if user.name == credentials.username]
    if len(user_list) == 1:
        hashed_password = user_list[0].password
        if bcrypt.checkpw(credentials.password.encode('utf-8'), hashed_password.encode('utf-8')):
            return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get("/messages")
async def read_messages():
    messages = [Message.from_json(db_message) for db_message in
                db.read_all_rows("SELECT message_id, message, user_id FROM messages")]
    return messages


@app.post("/messages")
async def send_message(message: Message, username: str = Depends(get_current_username)):
    message.id = db.change("INSERT INTO messages (message, user_id) VALUES (?, ?)", (message.message, username))
    return message


@app.post("/users")
async def create_user(user: User):
    if user.user_id is None:
        user.user_id = str(uuid.uuid1())
    user.user_id = db.change("INSERT INTO users (user_id, name, password) VALUES (?, ?, ?)",
                        (user.user_id, user.name, bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())))
    return user


@app.get("/users")
async def read_users():
    return db.read_all_rows("SELECT * FROM users")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
