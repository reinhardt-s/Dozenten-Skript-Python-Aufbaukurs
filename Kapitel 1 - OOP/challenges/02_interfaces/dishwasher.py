from self_cleaning_interface import SelfCleaningInterface


class Dishwasher(SelfCleaningInterface):

    def __init__(self):
        print("Geschirrspüler ist betriebsbereit")
        self.run_cycles = 0

    def start_cleaning(self):
        print("Drehe Spülblätter im Kreis.")
        print("Brrrrrr.")
        print("Vorgang abgeschlossen.")
        self.run_cycles = 0

    def check_if_dirty(self):
        return self.run_cycles > 10


# class Dishwasher:
#     def __init__(self):
#         print("Geschirrspüler ist Betriebsbereit")
#         self.run_cycles = 0
