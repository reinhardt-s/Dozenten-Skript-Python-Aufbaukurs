# Schreibe und benutzte für das untenstehende Programm folgende Enumeratoren:
# > YesNo: JA = 'j', NEIN = 'n'
# > Coffee_Choices: KAFFEE = 1, ESPRESSO = 2, AMERICANO = 3, CREMA = 4, COLD_BREW = 5

from enum import Enum

class YesNo(Enum):
    JA = 'j'
    NEIN = 'n'

class CoffeeChoices(Enum):
    KAFFEE = 140
    ESPRESSO = 20
    AMERICANO = 450
    CREMA = 200
    COLD_BREW = 1000

def add_milk_to_coffee():
    return YesNo(input("Soll Milch hinzugefügt werden? (j/n)\n")) == YesNo.JA

def get_coffee_type():
    return CoffeeChoices(int(input("Wählen Sie:\n1 - Kaffee\n2 - Espresso\n3 - Americano\n4 - Crema\n5 - Cold Brew\n")))

def get_filled_to_in_ml():
    return int(input("Wie viel ML Kaffee sind in der Tasse?\n"))

def make_coffee():
    coffee_type = get_coffee_type()
    filled_to_in_ml = get_filled_to_in_ml()
    max_in_ml = coffee_type.value
    if filled_to_in_ml >= max_in_ml:
        if add_milk_to_coffee():
            print("Füge Milch hinzu")
        print("Der Kaffee ist fertig.")
    else:
        print("Fülle auf")

make_coffee()
