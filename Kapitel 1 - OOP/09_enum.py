from enum import Enum


class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4


user_input = int(input("In welche Richtung soll ich gehen?\n"))
user_direction = Direction(user_input)

if user_direction == Direction.RIGHT:
    print("Laufe nach rechts")
elif user_direction == Direction.LEFT:
    print("Laufe nach link")
elif user_direction == Direction.FORWARD:
    print("Laufe vorwärts")
elif user_direction == Direction.BACKWARD:
    print("Laufe zurück")
else:
    print("Damit kann ich nichts anfangen.")
