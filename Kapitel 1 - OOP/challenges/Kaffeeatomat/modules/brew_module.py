import time
import progressbar
from .log import log


class BrewModule:

    def __init__(self, display, database):
        self.name = "BrewModule"
        self.__display = display
        self.__display.show("Initialisiere Brühmodul")
        self.__database = database
        log.debug("Brew module initialized")
        print(hex(id(log.log)))

    def brew(self, beverage, recipe):
        self.__display.show(f"Brühe {beverage}")
        widgets = [
            progressbar.Bar(),
        ]
        time.sleep(0.1)
        for _ in progressbar.progressbar(range(recipe["water"]), redirect_stdout=True, widgets=widgets):
            time.sleep(0.01)
        self.add_beverage(beverage)

    def update(self, acb):
        print(f"resources changed: {acb.get_resources()}", end="\r")

    def get_beverage_count(self):
        return self.__database.get_brew_count()[0][0]

    def add_beverage(self, beverage):
        self.__database.add_entry(beverage)
