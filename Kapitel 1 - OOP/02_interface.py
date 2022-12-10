from abc import ABC, abstractmethod


class AccelerationInterface(ABC):
    """Dieses Interface bietet die nötigen Methoden, um ein Objekt zu beschleunigen."""

    @abstractmethod
    def accelerate(self) -> str:
        """Beschreibe wie das Fahrzeug beschleunigt."""
        pass

    @abstractmethod
    def get_max_speed(self) -> int:
        """
        Gibt die maximale Geschwindigkeit in km/h wieder
        """
        pass


class Vehicle:
    """
    Die Vehicle-Klasse liefert die Grundfunktionalitäten, welche allen Fahrzeugen zur Verfügung stehen.
    """

    def __init__(self, speed):
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def turn(self, direction: str) -> None:
        """
        Lenkt das Fahrzeug in die angegebene Richtung.
        """
        print(f"Lenke nach {direction}")


# Erbung von Klasse Vehicle und Interface AccelerationInterface
class Car(Vehicle, AccelerationInterface):
    """
    Car definiert vollumfänglich die Funktionen eines Autos.
    """

    def __init__(self):
        super().__init__()
        self.doors = 5
        # self.speed = "150 km/h"
        print("Auto initialisiert")

    # Implementierung des Interfaces
    def accelerate(self) -> str:
        return "Trete auf Gaspedal"

    def get_max_speed(self) -> int:
        return 120


class Turtle(AccelerationInterface):
    """
    Eine Schildkröte.
    """

    def get_max_speed(self) -> int:
        return 35

    def accelerate(self) -> str:
        return "Watschel!"


class Bicycle(Vehicle, AccelerationInterface):
    """Ein manuelles Motorrad."""


def __init__(self):
    super().__init__()
    self.doors = 0
    # self.speed = "20 km/h"
    print("Fahrrad initialisiert")


def accelerate(self) -> str:
    return "Trete in die Pedale"


class Quad(Vehicle, AccelerationInterface):
    """
    Ein Auto ohne Türen.
    """


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
print(quad.accelerate())  # warum None?

toby = Turtle()
print(toby.get_max_speed())
print(toby.accelerate())
