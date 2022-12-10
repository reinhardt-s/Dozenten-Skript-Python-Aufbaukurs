from abc import ABC, abstractmethod


class SelfCleaningInterface(ABC):
    """
    Dieses Interface wird in all unseren Produkten verwendet.
    Hiermit soll sichergestellt werden, dass ein normierter Reinigungsvorgang ausgeführt werden kann.
    """

    @abstractmethod
    def start_cleaning(self):
        """
        Diese Methode startet den Selbstreinigungsprozess des Endgerätes.
        Der Vorgang kann von Gerät zu Gerät variieren.
        """
        pass

    @abstractmethod
    def check_if_dirty(self):
        """
        Diese Methode prüft, ob ein Gerät gereinigt werden muss

        :return: Gibt True aus, falls das Gerät gereinigt werden muss. Andernfalls False.
        """
