from abc import ABC, abstractmethod


class AccelerationInterface(ABC):
    """This interface provides the necessary methods to accelerate an object."""

    @abstractmethod
    def accelerate(self) -> str:
        """Describes how the vehicle accelerates."""
        pass

    @abstractmethod
    def get_max_speed(self) -> int:
        """
        Returns the maximum speed in km/h.
        """
        pass


class Vehicle:
    """
    The Vehicle class provides the basic functionalities that are available to all vehicles.
    """

    def __init__(self, speed):
        self.speed = speed
        print("Vehicle initialized")

    def turn(self, direction: str) -> None:
        """
        Steers the vehicle in the specified direction.
        """
        print(f"Steering towards {direction}")


class Car(Vehicle, AccelerationInterface):
    """
    Car fully defines the functions of a car.
    """

    def __init__(self):
        super().__init__(speed='150 km/h')
        self.doors = 5
        print("Car initialized")

    # Implementation of the interface
    def accelerate(self) -> str:
        return "Press accelerator pedal"

    def get_max_speed(self) -> int:
        return 120


class Turtle(AccelerationInterface):
    """
    A turtle.
    """

    def get_max_speed(self) -> int:
        return 35

    def accelerate(self) -> str:
        return "Waddle!"


class Bicycle(Vehicle, AccelerationInterface):
    """A manual motorcycle."""

    def __init__(self):
        super().__init__(speed='20 km/h')
        self.doors = 0
        print("Bicycle initialized")

    def accelerate(self) -> str:
        return "Pedal"

    def get_max_speed(self) -> int:
        return 150


class Quad(Vehicle, AccelerationInterface):
    """
    A car without doors.
    """

    def __init__(self):
        super().__init__(speed='70 km/h')
        self.doors = 0
        print("Quad initialized")

    def accelerate(self) -> str:
        return 'Accelerate'

    def get_max_speed(self) -> int:
        return 75


if __name__ == '__main__':
    bmw = Car()
    willier = Bicycle()
    quad = Quad()

    print(f"Doors: {bmw.doors}")
    bmw.accelerate()
    bmw.turn("left")
    print(bmw.accelerate())

    print(willier.accelerate())
    print(quad.accelerate())

    toby = Turtle()
    print(toby.get_max_speed())
    print(toby.accelerate())
