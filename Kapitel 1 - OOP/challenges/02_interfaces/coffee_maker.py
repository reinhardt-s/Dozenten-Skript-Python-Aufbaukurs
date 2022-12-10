from self_cleaning_interface import SelfCleaningInterface
from random import randint


class CoffeeMaker(SelfCleaningInterface):
    """
    Beste und einzige Kaffemaschine in unserem Angebot.
    """

    def __init__(self):
        print("Kaffeemaschine ist betriebsbereit")

    def start_cleaning(self):
        print("Drücke heißes Wasser durch alle Schläuche.")
        print("PTPFFFFF.")
        print("Vorgang abgeschlossen.")

    def check_if_dirty(self):
        return randint(0, 1)

# class CoffeeMaker(SelfCleaningInterface):
#
#     def __init__(self):
#         print("Kaffeemaschine ist betriebsbereit")
