class Vehicle:
    """Die Vehicle-Klasse liefert die Grundfunktionalitäten, welche allen Fahrzeugen zur Verfügung stehen."""

    def __init__(self):
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def drive(self):
        """Fährt das Fahrzeug."""
        print(f"Dieses Fahrzeug fährt nun: {self.speed}")

    def turn(self, direction: str):
        """Lenkt das Fahrzeug in die angegebene Richtung."""
        print(f"Lenke nach {direction}")


class Car(Vehicle):
    """Car definiert vollumfänglich die Funktionen eines Autos."""

    def __init__(self):
        super().__init__()
        self.doors = 5
        # self.speed = "150 km/h"
        print("Auto initialisiert")


bmw = Car()

print(f"Türen: {bmw.doors}")
bmw.drive()
bmw.turn("links")
bmw.turn(2) # got int instead
