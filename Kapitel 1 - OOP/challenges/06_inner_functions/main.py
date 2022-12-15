# Deklariere die Funktion get_best_charge_method(current_charge). Sie soll zwei Funktionen enthalten:
# > fast_charge(charge: int): Sie gibt einen um 4 erhöhten Ladungswert zurück
# > eco_charge(charge: int): Sie gibt einen um 1 erhöhten Ladungswert zurück
# Wenn hour zwischen 6 und 22 Uhr liegt oder ein Ladungsstand von mehr als 89% erreicht wurde,
# gibt get_best_charge_method eco_charge aus, um den Akku zu schonen. Andernfalls gibt es fast_charge aus
#
# Implementiere in der while-Schleife den Funktionsaufruf und erhöhe die Ladung (phone_charge)

hour = 22
phone_charge = 12

def get_best_charge_method(current_charge):
    def fast_charge(charge: int):
        return charge + 4

    def eco_charge(charge: int):
        return charge + 1

    if (6 < hour < 22) or (current_charge > 89):
        return eco_charge
    else:
        return fast_charge


while phone_charge != 100:
    charge_method = get_best_charge_method(phone_charge)
    phone_charge = charge_method(phone_charge)
    print(f"Ladezustand: {phone_charge}%")
