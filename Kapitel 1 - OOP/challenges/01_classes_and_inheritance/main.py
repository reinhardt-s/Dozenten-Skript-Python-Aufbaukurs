# TEIL I: Klassen
# Schreibe eine Klasse "Trainee", welche folgende Methoden hat:
# > __init__
#    > Lege mit Hilfe von self die die Attribute course: str, name: str, skill_level: int an
# > who_am_i
#    > Gebe einen String aus, welcher name, course und skill_level beinhaltet
# > add_skill_points(quantity: int)
#    > Füge dem skill_level quantity skill-Punkte hinzu
# > __del__
#    > Gebe mit einem print-Aufruf aus, dass das Objekt zerstört wurde.
#
# Erstelle anschließend in main.py zwei Instanzen von Trainee Namens alice und bob mit den Werten:
# alice: name="Alice", course="Python Aufbaukurs", skill_level=75
# bob: name="Bob", course="Data Science und Machine Learning mit Python"
# Rufe jeweils who_am_i auf
# Rufe jeweils add_skill_points(12) auf
# Rufe erneut who_am_i auf
#
# TEIL II: Vererbung
# Schreibe eine Klasse Trainer, die von Trainee erbt.
# Auch Trainer initialisiert die Parameter name, course und skill_points.
# Reiche dies an den Konstruktor von Trainee weiter.
# Erstelle eine Methode in Trainer namens teach:
# > teach fügt zuerst dem Trainer 3 Skillpunkte hinzu.
#   >>> Falls der Trainer den Kurs in Java hält, wird mit print() "Ich möchte das nicht." ausgegeben.
#       Andernfalls wird "Willkommen zu 'Kursname'" ausgegeben

from trainee import Trainee
from trainer import Trainer


def test_trainees():
    alice = Trainee(name="Alice", course="Python Aufbaukurs", skill_points=12)
    bob = Trainee(name="Bob", course="Data Science und Machine Learning mit Python")
    print(alice.who_am_i())
    print(bob.who_am_i())
    alice.add_skill_points(12)
    bob.add_skill_points(12)
    print(alice.who_am_i())
    print(bob.who_am_i())


def test_trainer():
    alex = Trainer(name="Alex", course="Java", skill_points=44)
    print(alex.who_am_i())
    alex.teach()
    print(alex.who_am_i())


test_trainees()
test_trainer()
