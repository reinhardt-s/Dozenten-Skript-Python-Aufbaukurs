# Schreibe und benutzte für das untenstehende Programm folgende Enumeratoren:
# > YesNo: JA = 'j', NEIN = 'n'
# > Coffee_Choices: KAFFEE = 1, ESPRESSO = 2, AMERICANO = 3, CREMA = 4, COLD_BREW = 5

from enum import Enum

# Maximale Kaffeefüllmenge - kann überschrieben werden
max_in_ml = 1000
# Kaffeesorte, angegeben durch 1,2 oder 3
coffee_type = int(input("Wählen Sie:\n1 - Kaffee\n2 - Espresso\n3 - Americano\n4 - Crema\n5 - Cold Brew\n"))
add_milk = input("Soll Milch hinzugefügt werden? (j/n)\n")
# Tassenfüllstand
filled_to_in_ml = int(input("Wie viel ML Kaffee sind in der Tasse?\n"))


class YesNo(Enum):
    JA = 'j'
    NEIN = 'n'


class CoffeeChoices(Enum):
    KAFFEE = 1
    ESPRESSO = 2
    AMERICANO = 3
    CREMA = 4
    COLD_BREW = 5


add_milk = YesNo(add_milk)
coffee_type = CoffeeChoices(coffee_type)

if add_milk == YesNo.JA:
    add_milk = True
else:
    add_milk = False

# Dein Code kommt unter dieser Zeile

if coffee_type == CoffeeChoices.KAFFEE:
    max_in_ml = 140
elif coffee_type == CoffeeChoices.ESPRESSO:
    max_in_ml = 20
elif coffee_type == CoffeeChoices.AMERICANO:
    max_in_ml = 450
else:
    max_in_ml = 200

if filled_to_in_ml >= max_in_ml:
    if add_milk:
        print("Füge Milch hinzu")
    print("Der Kaffee ist fertig.")
else:
    print("Fülle auf")
