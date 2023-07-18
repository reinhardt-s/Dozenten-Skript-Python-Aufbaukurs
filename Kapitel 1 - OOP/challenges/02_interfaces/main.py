# Schreibe ein Interface SelfCleaningInterface (self_cleaning.py), welches folgende Methoden deklariert:
# > start_cleaning
#   Diese Methode startet den Selbstreinigungsprozess des Endgerätes.
#   Der Vorgang kann von Gerät zu Gerät variieren.
# > check_if_dirty
#   Diese Methode prüft, ob ein Gerät gereinigt werden muss.
#   Gibt True aus, falls das Gerät gereinigt werden muss. Andernfalls False.
#
# Erstelle eine Klasse Dishwasher, welches SelfCleaningInterface implementiert:
# > check_if_dirty gibt True aus, wenn run_cycles > 10 ist
# > start_cleaning - gibt per print() aus, dass gereinigt wird und setzt anschließen run_cycles auf null (0).
# > Initialisiere run_cycles in __init__
#
# Erstelle eine Klasse CoffeeMaker, welches SelfCleaningInterface implementiert:
# > check_if_dirty gibt True per Zufall aus
# > start_cleaning - gibt per print() aus, dass gereinigt wird und setzt anschließen run_cycles auf null (0).
#
# Lege in main.py je einen Dishwasher als auch einen CoffeeMaker an.
# Setze den runcycles_count für den Dishwasher auf 15.
# Prüfe beide Geräte, ob sie gereinigt werden müssen und starte ggf. den Reinigungsprozess.

from dishwasher import Dishwasher
from coffee_maker import CoffeeMaker

# Create instances of Dishwasher and CoffeeMaker
dishwasher = Dishwasher()
coffee_maker = CoffeeMaker()

# Set the run_cycles attribute of the Dishwasher instance to 15
dishwasher.run_cycles = 15

# Create a list of widgets
widgets = [dishwasher, coffee_maker]

# Iterate over the widgets list
for widget in widgets:
    # Check if the widget is dirty
    if widget.check_if_dirty():
        # If the widget is dirty, start the cleaning process
        widget.start_cleaning()
