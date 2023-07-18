from typing import List


class Observer:
    """
    The Observer class is inherited by the class that should inform other classes about a state change.
    """

    def __init__(self):
        self._observers: List = []

    def notify(self, modifier=None):
        """
        Notifies all subscribers about a state change.
        """
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """
        Adds subscribers.

        :param observer: The object to be added
        """
        if observer not in self._observers:
            print(f"New subscriber: {observer.name}")
            self._observers.append(observer)

    def detach(self, observer):
        """
        Removes subscribers.

        :param observer: The object to be removed.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            print(f"Observer {observer} could not be removed.")


class BreakModule:
    """
    A module that all vehicles should have. It brakes.
    """

    def __init__(self):
        self.name = "Brake Module"

    def update(self, caller):
        """
        Implementation of the update functionality. It is called when an observed state changes.

        :param caller: Calling object.
        """
        print(f"{self.name}: {caller} reports collision!")
        print(f"Perform full brake")


class LightModule:
    """
    This module covers all common lighting scenarios of a vehicle.
    """

    def __init__(self):
        self.name = "Light Module"

    def update(self, caller):
        """
        Implementation of the update functionality. It is called when an observed state changes.

        :param caller: Calling object.
        """
        print(f"{self.name}: {caller} reports collision!")
        print(f"Turn on hazard lights")


###########################################################################

class AccelerationInterface:
    def accelerate(self) -> str:
        """
        Describes how the vehicle accelerates.

        :return: Returns a string describing how the vehicle accelerates.
        """
        pass


class Vehicle(Observer):
    """
    The Vehicle class provides the basic functionalities that are available to all vehicles.
    """

    def __init__(self):
        super().__init__()
        self.speed = "25 km/h"
        print("Vehicle initialized")

    def turn(self, direction: str):
        """
        Steers the vehicle in the specified direction.

        :param direction: Specifies the direction to steer.
        """
        print(f"Steering towards {direction}")


class Car(Vehicle, AccelerationInterface):
    """Car fully defines the functions of a car."""

    def __init__(self):
        super().__init__()
        self.doors = 5
        # Create car modules
        self.light_module = LightModule()
        self.break_module = BreakModule()
        # Add the modules as observers
        self.attach(self.break_module)
        self.attach(self.light_module)

        print("Car initialized")

    def accelerate(self) -> str:
        return "Step on gas pedal"


bmw = Car()

# A tree jumps onto the road. The car reacts.
bmw.notify()
