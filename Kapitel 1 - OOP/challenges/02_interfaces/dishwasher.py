from self_cleaning_interface import SelfCleaningInterface


class Dishwasher(SelfCleaningInterface):
    """
    A class representing a dishwasher that implements the SelfCleaningInterface.

    Attributes:
    - run_cycles (int): The number of cleaning cycles the dishwasher has run.

    Methods:
    - __init__(): Initializes a new instance of the Dishwasher class.
    - start_cleaning(): Starts the cleaning process of the dishwasher.
    - check_if_dirty(): Checks if the dishwasher is dirty based on the number of cleaning cycles it has run.
    """

    def __init__(self):
        """
        Initializes a new instance of the Dishwasher class.
        """
        print("Geschirrspüler ist betriebsbereit")
        self.run_cycles = 0

    def start_cleaning(self):
        """
        Starts the cleaning process of the dishwasher.
        """
        print("Drehe Spülblätter im Kreis.")
        print("Brrrrrr.")
        print("Vorgang abgeschlossen.")
        self.run_cycles = 0

    def check_if_dirty(self):
        """
        Checks if the dishwasher is dirty based on the number of cleaning cycles it has run.

        Returns:
        - bool: True if the dishwasher is dirty, False otherwise.
        """
        return self.run_cycles > 10
