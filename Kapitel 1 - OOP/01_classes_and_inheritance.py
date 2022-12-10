class Vehicle:
    """
    Die Vehicle-Klasse liefert die Grundfunktionalitäten, welche allen Fahrzeugen zur Verfügung stehen.
    """

    # Auch mit weiteren Parametern, inkl default Werten
    def __init__(self, speed="25 km/h"):
        self.speed = speed
        print("Fahrzeug initialisiert")

    def drive(self):
        """
        Fährt das Fahrzeug.
        """
        print(f"Dieses Fahrzeug fährt nun: {self.speed}")

    def turn(self, direction: str):
        """
        Lenkt das Fahrzeug in die angegebene Richtung
        :param direction: Die Richtung in welche das Fahrzeug sich bewegen soll
        """

        print(f"Lenke nach {direction}")

    def __del__(self):
        print("Vehicle-Objekt wird gelöscht")


class Car(Vehicle):
    """
    Car definiert vollumfänglich die Funktionen eines Autos.
    """

    def __init__(self, speed="150f km/h"):
        super().__init__()
        self.doors = 5
        self.speed = speed
        print("Auto initialisiert")


bmw = Car()

print(f"Türen: {bmw.doors}")
bmw.drive()
bmw.turn("links")
bmw.turn(2)  # got int instead
