from kreide_standard import AutomaticCoffeeBrewer


class AutomaticCoffeeBrewerK10(AutomaticCoffeeBrewer):

    def __int__(self):
        self.name = "ACB Kreide 10"
        self._resources = {
            "water": 2500,
            "beans": 1000,
            "milk": 1000,
            "coffee_ground_max": 500,
        }
        super.__init__()
