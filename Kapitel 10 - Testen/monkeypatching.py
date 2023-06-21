import os

def get_database_url():
    return os.environ['DATABASE_URL']


def test_get_database_url(monkeypatch):
    # Setzen Sie die Umgebungsvariable DATABASE_URL auf einen vordefinierten Wert
    monkeypatch.setenv('DATABASE_URL', 'test_database_url')

    assert get_database_url() == 'test_database_url'


class Database:
    def connect(self):
        return "could not connect to server"

def monkey_connect(self):
    return "connection established"

def test_method(monkeypatch):
    # Ersetzen Sie die Methode "method" in MyClass durch die Funktion "new_method"
    monkeypatch.setattr(Database, 'connect', monkey_connect)

    my_class = Database()
    assert my_class.connect() == "connection established"