class ResourceObserver:

    def __init__(self):
        self._observer = []
        print("RO init completed")

    def notify(self, modifier=None):
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observer:
            print(f"New subscriber detected: {observer.name}")
            self._observer.append(observer)

    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            print(f"Observer konnte nicht {observer} konnte nicht entfernt werden.")
