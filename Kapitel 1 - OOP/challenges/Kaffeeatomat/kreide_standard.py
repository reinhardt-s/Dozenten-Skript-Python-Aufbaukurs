from prettytable import PrettyTable

from modules.brew_module import BrewModule
from modules.display_module import DisplayModule
from modules.database_module import DatabaseModule
from modules.resource_observer_module import ResourceObserver
from modules.log import log


class AutomaticCoffeeBrewer(ResourceObserver):

    def __init__(self):
        super().__init__()
        self.name = "ACB Default"
        log.debug(f"Initialisiere {self.name}")
        print(hex(id(log.log)))
        self._resources = {
            "water": 1000,
            "beans": 500,
            "milk": 500,
            "coffee_ground": 500,
        }

        self.display = DisplayModule()
        self.database = DatabaseModule()
        self.brew_module = BrewModule(self.display, self.database)
        self.attach(self.brew_module)
        self.attach(self.display)

    def brew(self, beverage):
        recipe = self.database.get_beverage_by_name(name=beverage)
        self.brew_module.brew(beverage, recipe)
        self._resources["water"] -= recipe["water"]
        self._resources["beans"] -= recipe["beans"]
        self._resources["milk"] -= recipe["milk"]
        self._resources["coffee_ground"] -= recipe["coffee_ground"]
        self.notify()

    def get_resources(self):
        return self._resources

    def display_beverage_count(self):
        self.display.show(f"Gebrühte Getränke: {self.brew_module.get_beverage_count()}")

    def display_resources(self):
        resources_table = PrettyTable()
        resources_table.field_names = ["Ressource", "Menge"]
        resources_table.add_rows([[k, v] for k, v in self.get_resources().items()])
        self.display.show(resources_table)
