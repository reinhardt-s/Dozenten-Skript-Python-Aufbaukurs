# file = open("none_existent_file.txt", mode="r")
# print(file.read())
# file.close()
#
# try:
#     file = open("none_existent_file.txt", mode="r")
#     print(file.read())
#     file.close()
# except:
#     print("Datei konnte nicht geladen werden")
#
# try:
#     file = open("none_existent_file.txt", mode="r")
#     print(file.read())
#     file.close()
# except FileNotFoundError as fnf:
#     print(f"Datei {fnf.filename} konnte nicht geladen werden")
#
#

class TooMuchChocolateException(Exception):
    """Raised when CandyEater has eaten too much chocolate"""

    def __init__(self, bars_eaten):
        self.bars_eaten = bars_eaten
        self.message = f"Too much chocolate! Cannot eat more than {bars_eaten} chocolate bars!"
        super().__init__(self.message)


class NotEnoughWaterException(Exception):
    """Raised when CandyEater has not drunk enough water before eating chocolate"""

    def __init__(self, min_water):
        self.min_water = min_water
        self.message = f"Not enough water! CandyEater needs at least {min_water} water to eat chocolate!"
        super().__init__(self.message)


class CandyEater:
    MAX_CHOCOLATE = 5
    MIN_WATER = 2

    def __init__(self):
        self.chocolate_bars_eaten = 0
        self.water_sipped = 4

    def eat_chocolate_bar(self):
        if self.chocolate_bars_eaten >= self.MAX_CHOCOLATE:
            raise TooMuchChocolateException(self.MAX_CHOCOLATE)
        elif self.water_sipped < self.MIN_WATER:
            raise NotEnoughWaterException(self.MIN_WATER)
        else:
            self.chocolate_bars_eaten += 1
            self.water_sipped -= 1
            return "Eating chocolate."

bob = CandyEater()
for i in range(7):
    try:
        print(f"{i} {bob.eat_chocolate_bar()}")
    except TooMuchChocolateException as chocolate:
        print(f"{i} Digesting chocolate, as I have reached the maximum limit of: {chocolate.bars_eaten}.")
    except NotEnoughWaterException as water:
        print(f"{i} Drinking water before eating more chocolate.")
        bob.water_sipped = 5

    # else:
    #     print(f"{i} Ich werde nur dann ausgeführt, wenn keinen Exception aufgerufen wurde.")
    # finally:
    #     print(f"{i} Ich werde immer aufgerufen, egal ob eine exception aufgerufen wurde.")
