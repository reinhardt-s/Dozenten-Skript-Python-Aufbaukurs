from enum import Enum


class Direction(Enum):
    FORWARD = "vorwärts"
    BACKWARD = "zurück"
    LEFT = "links"
    RIGHT = "rechts"


def main():
    """
    Asks the user for a direction and prints the corresponding message.
    """
    user_input = input("In welche Richtung soll ich gehen?\n")
    try:
        user_direction = Direction[user_input.upper()]
        print(f"Laufe nach {user_direction.value}")
    except KeyError:
        print("Damit kann ich nichts anfangen.")


if __name__ == "__main__":
    main()
