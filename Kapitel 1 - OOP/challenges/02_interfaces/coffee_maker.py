from self_cleaning_interface import SelfCleaningInterface
from random import randint


class CoffeeMaker(SelfCleaningInterface):
    """A class representing a coffee maker that implements the SelfCleaningInterface."""

    def __init__(self):
        """Initialize the CoffeeMaker object."""
        print("Coffee maker is ready for use.")

    def start_cleaning(self):
        """Start the cleaning process."""
        print("Running hot water through all hoses.")
        print("PTPFFFFF.")
        print("Cleaning process complete.")

    def check_if_dirty(self):
        """Check if the coffee maker is dirty."""
        return randint(0, 1)
