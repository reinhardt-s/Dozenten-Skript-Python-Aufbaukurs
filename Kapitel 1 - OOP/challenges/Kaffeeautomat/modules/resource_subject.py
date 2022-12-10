from .log import log


class ResourceSubject:
    """Wird einer Klasse vererbt, welche von Observer beobachtet werden soll."""

    def __init__(self):
        self._observer = []
        log.debug("Subject initialisiert")

    def notify(self, modifier=None):
        """Informiert bei aufruf alle registrierten Observer"""
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """Registriert einen neuen Observer."""
        if observer not in self._observer:
            log.info(f"New subscriber detected: {observer.name}")
            self._observer.append(observer)

    def detach(self, observer):
        """Entfernt einen Observer"""
        try:
            self._observer.remove(observer)
        except ValueError:
            log.info(f"Observer konnte nicht {observer} konnte nicht entfernt werden.")
