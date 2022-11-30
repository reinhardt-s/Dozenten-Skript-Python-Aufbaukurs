import sys

from prettytable import PrettyTable
from .log import log
from .resource_observer import ResourceObserver


class DisplayModule(ResourceObserver):
    """
    Dieses Modul steuert, was auf dem Display des ACB angezeigt wird.
    """

    def __init__(self):
        self.name = "DisplayModule"
        log.debug("Initialize display module")

    def show(self, message: any):
        """
        Gibt eine Nachricht auf dem Display aus.

        :param message: Die anzuzeigende Nachricht.
        """
        on_screen = PrettyTable()
        on_screen.header = False
        on_screen.add_row([message])
        print(on_screen)

    def show_progress(self, current_value: int, max_value: int):
        """
        Zeigt einen Fortschrittsbalken auf dem Display an.

        :param current_value: Der aktuelle Fortschrittswert
        :param max_value: Der maximal erreichbare Wert.
        """

        fraction = current_value / max_value
        progress = int(fraction * 20) * '🟩'
        padding = int(19 - len(progress)) * '⬜'

        ending = '\n' if current_value == max_value else '\r'

        message = f'{ending * 2}{progress}{padding} {int(fraction * 100)}%'

        sys.stdout.write(message)
        sys.stdout.flush()

    def update(self, caller):
        for k, v in caller.get_resources().items():
            if v <= 0:
                self.show(f"Resource erschöpft: {k}")
                break
