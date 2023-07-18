class Vehicle:
    """
    The Vehicle class provides the basic functionalities that all vehicles have.
    """

    def __init__(self, speed="25 km/h"):
        self.speed = speed

    def drive(self):
        """
        Drives the vehicle.
        """
        print(f"This vehicle is now driving at: {self.speed}")

    def turn(self, direction: str):
        """
        Turns the vehicle in the specified direction.
        :param direction: The direction in which the vehicle should move.
        """
        print(f"Turning {direction}")

    def __del__(self):
        print("Vehicle object is being deleted")


class Car(Vehicle):
    """
    Car defines all the functions of a car.
    """

    def __init__(self, speed="150 km/h"):
        super().__init__(speed=speed)
        self.doors = 5
        print("Car initialized")


bmw = Car()

print(f"Doors: {bmw.doors}")
bmw.drive()
bmw.turn("left")
