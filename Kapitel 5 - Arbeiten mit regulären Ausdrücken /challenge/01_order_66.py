# Erstelle eine Klasse Order, die die Bestellungen repräsentiert.
#   Erstelle auch die Methode __repr__.
# Zerlege die Bestellungen mit regulären Ausdrücken in ihre Bestandteile.
# Lade die Bestellungen in eine Liste von Order-Objekten.
# Gebe die Bestellungen auf der Konsole aus.

import re
from pydantic import BaseModel

orders_from_string = [
    'Han Solo, Smuggler, 1x Hyperdrive Generator, 3x Droid Repair Kit, 2x Beskar Steel',
    'Luke Skywalker, Jedi, 1x Lightsaber, 4x Droid Repair Kit, 2x Holocron'
]

from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    item: str
    quantity: int

    def __repr__(self):
        return f"{self.quantity}x {self.item}"


class Order(BaseModel):
    name: str
    profession: str
    items: List[Item]

    def __repr__(self):
        return f"{self.name} ({self.profession}) ordered: {', '.join([str(item) for item in self.items])}"


# Regular expression pattern
pattern = r'(\d+)x ([\w\s]+)'

orders = []

for order in orders_from_string:
    # Find matches
    matches = re.findall(pattern, order)

    # Extract name and profession
    splitted = re.split(r', ', order)
    name = splitted[0]
    profession = splitted[1]

    # Create purchase
    new_order = Order(name=name, profession=profession, items=[])

    for match in matches:
        new_order.items.append(Item(item=match[1], quantity=int(match[0])))
    orders.append(new_order)


for order in orders:
    print(order)