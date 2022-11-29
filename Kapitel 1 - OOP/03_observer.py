class Observer:

    def __init__(self):
        self._observer = []

    def notify(self, modifier=None):
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observer:
            print(f"New subscriber detected: {observer.name}")
            self._observer.append(observer)

    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            print(f"Observer konnte nicht {observer} konnte nicht entfernt werden.")


class BreakModule:
    name = "Bremsmodul"
    def update(self, caller):
        print(f"{caller} meldet Aufprall!")
        print(f"Führe Vollbremsung durch")


class LightModule:
    name = "Lichtmodul"
    def update(self, caller):
        print(f"{caller} meldet Aufprall!")
        print(f"Schalte Warnblicklicht an")



###########################################################################

class AccelerationInterface:
    def accelerate(self) -> str:
        """Beschreibe wie das Fahrzeug beschleunigt"""
        pass


class Vehicle(Observer):
    def __init__(self):
        super().__init__()
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def turn(self, direction):
        print(f"Lenke nach {direction}")


class Car(Vehicle, AccelerationInterface):

    def __init__(self):
        super().__init__()
        self.doors = 5

        self.light_module = LightModule()
        self.break_module = BreakModule()
        self.attach(self.break_module)
        self.attach(self.light_module)

        print("Auto initialisiert")

    def accelerate(self) -> str:
        return "Trete auf Gaspedal"


bmw = Car()

# Baum springt auf die Straße
bmw.notify()