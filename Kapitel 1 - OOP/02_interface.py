class AccelerationInterface:
    def accelerate(self) -> str:
        """Beschreibe wie das Fahrzeug beschleunigt"""
        pass


class Vehicle():
    def __init__(self):
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def turn(self, direction):
        print(f"Lenke nach {direction}")


class Car(Vehicle, AccelerationInterface):

    def __init__(self):
        super().__init__()
        self.doors = 5
        # self.speed = "150 km/h"
        print("Auto initialisiert")

    def accelerate(self) -> str:
        return "Trete auf Gaspedal"


class Bicycle(Vehicle, AccelerationInterface):

    def __init__(self):
        super().__init__()
        self.doors = 0
        # self.speed = "20 km/h"
        print("Fahrrad initialisiert")

    def accelerate(self) -> str:
        return "Trete in die Pedale"


class Quad(Vehicle, AccelerationInterface):

    def __init__(self):
        super().__init__()
        self.doors = 0
        self.speed = "70 km/h"
        print("Quad initialisiert")


bmw = Car()
willier = Bicycle()
quad = Quad()

print(f"Türen: {bmw.doors}")
bmw.accelerate()
bmw.turn("links")
print(bmw.accelerate())

print(willier.accelerate())
print(quad.accelerate())
