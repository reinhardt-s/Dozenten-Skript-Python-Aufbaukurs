class Vehicle:
    def __init__(self):
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def drive(self):
        print(f"Dieses Fahrzeug fährt nun: {self.speed}")

    def turn(self, direction):
        print(f"Lenke nach {direction}")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.doors = 5
        # self.speed = "150 km/h"
        print("Auto initialisiert")


bmw = Car()

print(f"Türen: {bmw.doors}")
bmw.drive()
bmw.turn("links")
