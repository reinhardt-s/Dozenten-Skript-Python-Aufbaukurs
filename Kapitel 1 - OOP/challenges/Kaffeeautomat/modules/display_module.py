from prettytable import PrettyTable
from .log import log


class DisplayModule:

    def __init__(self):
        self.name = "DisplayModule"
        log.debug("Initialize display module")

    def show(self, message):
        on_screen = PrettyTable()
        on_screen.header = False
        on_screen.add_row([message])
        print(on_screen)

    def update(self, acb):
        for k, v in acb.get_resources().items():
            if v <= 0:
                self.show(f"Resource erschöpft: {k}")
                break
