from kreide_standard import AutomaticCoffeeBrewer


class AutomaticCoffeeBrewerK10(AutomaticCoffeeBrewer):
    """
    Die ACB Kreide K10 erbt die Grundfunktionen der generischen ACB.
    Sie hat jedoch für die meisten Ressourcen, ein größeres Fassungsvermögen.
    """
    def __int__(self):
        self.name = "ACB Kreide 10"
        self._resources = {
            "water": 2500,
            "beans": 1000,
            "milk": 1000,
            "coffee_ground_max": 500,
        }
        super.__init__()
