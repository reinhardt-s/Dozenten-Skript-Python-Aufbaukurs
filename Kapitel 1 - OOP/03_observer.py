
from abc import ABC


class Observer:
    """
    Die Observerklasse wird jener Klasse vererbt, welche andere Klassen über die Änderung eines Zustandes
    informieren soll.
    """

    def __init__(self):
        self._observer = []

    def notify(self, modifier=None):
        """
        Wird aufgerufen, um alle Subscriber über eine Zustandsänderung zu informieren.
        """
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """
        Hiermit werden die Subscriber hinzugefügt.

        :param observer: Das hinzuzufügende Objekt
        """
        if observer not in self._observer:
            print(f"Neuer Subscriber: {observer.name}")
            self._observer.append(observer)

    def detach(self, observer):
        """
        Wird benutzt, um Subscriber wieder zu entfernen.

        :param observer: Das wieder zu entfernede Objekt.
        """
        try:
            self._observer.remove(observer)
        except ValueError:
            # Falls es nicht möglich ist, den Subscriber zu entfernen, informieren wir den Aufrufer mit einer
            # Exception darüber.
            print(f"Observer konnte nicht {observer} konnte nicht entfernt werden.")


class BreakModule:
    """
    Ein Modul, welches alle Fahrzeuge haben sollten. Es bremst.
    """

    def __init__(self):
        self.name = "Bremsmodul"

    def update(self, caller):
        """
        Implementierung der update Funktionalität. Sie wird aufgerufen, so ein beobachteter Zustand sich ändert.

        :param caller: Aufrufendes Objekt.
        """
        print(f"{self.name}: {caller} meldet Aufprall!")
        print(f"Führe Vollbremsung durch")


class LightModule:
    """
    Dieses Modul deckt alles üblichen Lichtszenarien eines Fahrzeugs ab.
    """

    def __init__(self):
        self.name = "Lichtmodul"

    def update(self, caller):
        """
        Implementierung der update Funktionalität. Sie wird aufgerufen, so ein beobachteter Zustand sich ändert.

        :param caller: Aufrufendes Objekt.
        """
        print(f"{self.name}: {caller} meldet Aufprall!")
        print(f"Schalte Warnblicklicht an")


###########################################################################

class AccelerationInterface(ABC):
    def accelerate(self) -> str:
        """
        Beschreibe wie das Fahrzeug beschleunigt

        :return: Gibt als String aus, wie das Fahrzeug beschleunigt.
        """
        pass


# Die Fahrzeugklasse erbt die Observerklasse
class Vehicle(Observer):
    """
    Die Vehicle-Klasse liefert die Grundfunktionalitäten, welche allen Fahrzeugen zur Verfügung stehen.
    """

    def __init__(self):
        super().__init__()
        self.speed = "25 km/h"
        print("Fahrzeug initialisiert")

    def turn(self, direction: str):
        """
        Lenkt das Fahrzeug in die angegebene Richtung.

        :param direction: Gibt die Richtung an, in die gelenkt werden soll.
        """
        print(f"Lenke nach {direction}")


class Car(Vehicle, AccelerationInterface):
    """Car definiert vollumfänglich die Funktionen eines Autos."""

    def __init__(self):
        super().__init__()
        self.doors = 5
        # Erstelle Auto-Module
        self.light_module = LightModule()
        self.break_module = BreakModule()
        # Füge die Module als Observer hinzu
        self.attach(self.break_module)
        self.attach(self.light_module)

        print("Auto initialisiert")

    def accelerate(self) -> str:
        return "Trete auf Gaspedal"


bmw = Car()

# Baum springt auf die Straße. Das Auto reagiert.
bmw.notify()
