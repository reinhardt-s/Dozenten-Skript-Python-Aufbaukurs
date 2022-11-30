import time
from .decorators import notified
from .resource_observer import ResourceObserver


class BrewModule(ResourceObserver):
    """Das BrewModule kann einem Kreide-ACB hinzugefügt werden, sodass dieser Kaffee kochen kann."""

    def __init__(self, display, database):
        self.name = "BrewModule"
        self.__display = display
        self.__display.show("Initialisiere Brühmodul")
        self.__database = database
        # Die Durchflußgeschwindigkeit von Wasser im Brühvorgang
        self.__FLOW_RATE = 0.01

    def brew(self, beverage, recipe):
        """Brüht den Kaffee. Die Brühzeit richtet sich ausschließlich nach der Menge des eingesetzten Wassers."""

        # Zeige auf dem Display an, welches Getränk zubereitet wird
        self.__display.show(f"Brühe {beverage}")

        # Zeige auf dem Display an, wie weit das Getränk ist
        for ml in range(recipe["water"]):
            time.sleep(0.01)
            self.__display.show_progress(ml, recipe['water'])
        self.__display.show(f"Ihr {beverage} ist fertig!")
        # Vermerke in der Datenbank, dass dieses Getränk gebrüht wurde.
        self.add_beverage(beverage)

    @notified
    def update(self, caller):
        print(f"resources changed: {caller.get_resources()}")

    def get_beverage_count(self):
        """Fragt das Datenbankmodul an, wie viele Getränke bereits zubereitet wurden."""
        return self.__database.get_brew_count()[0][0]

    def add_beverage(self, beverage: str):
        """
        Vermerkt in der Datenbank, dass ein neues Getränk zubereitet wurde.

        :param beverage: Name des zu vermerkenden Getränks.
        """
        self.__database.add_entry(beverage)
