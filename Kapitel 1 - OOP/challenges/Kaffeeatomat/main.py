import sys

from kreide_k10 import AutomaticCoffeeBrewerK10

k10 = AutomaticCoffeeBrewerK10()
k10.brew(beverage="Americano")
k10.display_resources()
k10.brew(beverage="Teewasser")
k10.display_resources()
k10.brew(beverage="Latte Macchiato")
k10.display_resources()
k10.brew(beverage="Espresso")
k10.display_resources()
k10.display_beverage_count()
