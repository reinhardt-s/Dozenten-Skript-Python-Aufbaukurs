# Erstelle eine Observerklasse und implementiere diese in der zu erstellenden Klasse FireAlertSystem (Brandmeldeanlage)
# Erstelle in FireAlertSystem die Methode fire_detected() welche alle Observer benachrichtigt.
# Implementiere in den Klassen ExtinguishingSystem und EmergencyCall, die update() Methode:
# > ExtinguishingSystem: sobald die Brandmeldeanlage auslöst, sollen die Wasserzufuhr-Ventile geöffnet werden
#   und der aktuelle Restwasserstand ausgegeben werden.
# > EmergencyCall setzt einen Text-Notruf bei der Leitstelle ab.
from observer import Observer


class ExtinguishingSystem:
    """
    This class represents the extinguishing system which is an observer of the FireAlertSystem.
    """
    def __init__(self):
        self.name = "Dam Break 22"
        self.water_supply = 2500
        self.valves_open_state = False

    def show_water_supply(self):
        """
        Prints the current remaining water supply.
        """
        print(f'Remaining water supply: {self.water_supply} liters')

    def set_valves_open(self, state: bool):
        """
        Opens or closes the valves to the extinguishing water.
        :param state: True = open, False = closed
        """
        self.valves_open_state = state
        state = 'open' if state else 'closed'
        print(f'The valves are now {state}.')

    def update(self, caller):
        """
        This method is called by the FireAlertSystem when a fire is detected.
        It opens the valves and shows the remaining water supply.
        """
        print(f'{self.name}: {caller.name} reports fire!')
        self.set_valves_open(True)
        self.show_water_supply()


class EmergencyCall:
    """
    This class represents the emergency call system which is an observer of the FireAlertSystem.
    """
    def __init__(self):
        self.name = "E-Call 1433"

    def make_call(self):
        """
        Makes an emergency call.
        """
        print(f'Making emergency call.')
        print(f'...')
        print(f'Emergency call made.')

    def update(self, caller):
        """
        This method is called by the FireAlertSystem when a fire is detected.
        It makes an emergency call.
        """
        print(f'{self.name}: {caller.name} reports fire!')
        self.make_call()


class FireAlertSystem(Observer):
    """
    This class represents the FireAlertSystem which is the subject of the observers.
    """
    def __init__(self):
        self.name = "BAM!"
        super().__init__()
        self.attach(ExtinguishingSystem())
        self.attach(EmergencyCall())

    def fire_detected(self):
        """
        This method is called when a fire is detected.
        It notifies all the observers.
        """
        self.notify()


fas = FireAlertSystem()
fas.fire_detected()
