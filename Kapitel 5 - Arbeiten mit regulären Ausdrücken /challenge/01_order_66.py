# Erstelle eine Klasse Order, die die Bestellungen repräsentiert.
#   Erstelle auch die Methode __repr__.
# Zerlege die Bestellungen mit regulären Ausdrücken in ihre Bestandteile.
# Lade die Bestellungen in eine Liste von Order-Objekten.
# Gebe die Bestellungen auf der Konsole aus.

import re
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
        return f"{self.name} ({self.profession}) ordered: {', '.join(map(str, self.items))}"


# Regular expression pattern
pattern = r'(\d+)x ([\w\s]+)'

orders_from_string = [
    'Han Solo, Smuggler, 1x Hyperdrive Generator, 3x Droid Repair Kit, 2x Beskar Steel',
    'Luke Skywalker, Jedi, 1x Lightsaber, 4x Droid Repair Kit, 2x Holocron'
]

orders = []

for order in orders_from_string:
    # Find matches
    matches = re.findall(pattern, order)

    # Extract name and profession
    name, profession = order.split(", ")[0:2]

    # Create purchase
    new_order = Order(name=name, profession=profession, items=[Item(item=match[1], quantity=int(match[0])) for match in matches])
    orders.append(new_order)


for order in orders:
    print(order)