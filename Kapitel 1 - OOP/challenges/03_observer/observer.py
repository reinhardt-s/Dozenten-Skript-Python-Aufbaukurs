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

        :param modifier: Gibt an, wer notify aufgerufen hat.
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