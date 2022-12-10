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
# class TooMuchChocolateException(Exception):
#     """Diese Ausnahme wird erzeugt, wenn CandyEater zu viel Schokolade gegessen hat"""
#
#     def __init__(self, bars_eaten):
#         self.bars_eaten = bars_eaten
#         self.message = f"Zu viel Schokolade gegessen! Kann nicht mehr als {bars_eaten} Schokoladen essen!"
#         super().__init__(self.message)
#
#
# class NotEnoughWaterException(Exception):
#     """Diese Ausnahme wird erzeugt, wenn CandyEater vor dem Essen von Schokolade, nicht genug getrunken hat."""
#
#     def __init__(self, min_water):
#         self.min_water = min_water
#         self.message = f"Zu wenig Wasser getrunken! CandyEater muss zum Essen mindesten {min_water} Wasser haben!"
#         super().__init__(self.message)
#
#
# class CandyEater:
#     def __init__(self):
#         self.MAX_CHOCOLATE = 5
#         self.MIN_WATER = 2
#         self.chocolate_bars_eaten = 0
#         self.water_sipped = 4
#
#     def eat_chocolate_bar(self):
#         if self.chocolate_bars_eaten >= self.MAX_CHOCOLATE:
#             raise TooMuchChocolateException(self.MAX_CHOCOLATE)
#         elif self.water_sipped < self.MIN_WATER:
#             raise NotEnoughWaterException(self.MIN_WATER)
#         else:
#             self.chocolate_bars_eaten += 1
#             self.water_sipped -= 1
#             return "Esse Schokolade."
#
#
# bob = CandyEater()
# for _ in range(6):
#     bob.eat_chocolate_bar()
#
# for i in range(7):
#     try:
#         print(f"{i} {bob.eat_chocolate_bar()}")
#     except TooMuchChocolateException as chocolate:
#         print(f"{i} Verdaue Schokolade, da ich den Maximalwert von: {chocolate.bars_eaten}.")
#     except NotEnoughWaterException as water:
#         print(f"{i} Ich trinke erstmal Wasser bevor ich noch mehr Schokolade esse.")
#         bob.water_sipped = 5
#     # else:
#     #     print(f"{i} Ich werde nur dann ausgeführt, wenn keinen Exception aufgerufen wurde.")
#     # finally:
#     #     print(f"{i} Ich werde immer aufgerufen, egal ob eine exception aufgerufen wurde.")
