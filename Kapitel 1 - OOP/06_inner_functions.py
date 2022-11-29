def add_fuel(litre: int):
    def a_lot():
        print("Tank ist voll.")

    def a_little():
        print("Tank ist halb voll")

    if litre > 10:
        a_lot()
    elif litre >= 5:
        a_little()
    print("Fahrbereit.")


add_fuel(litre=10)


def translate(lang: str):
    def english():
        return f"{lang}: Hello World"

    def spanish():
        return f"{lang}: Hola Mundo"

    if lang == "spanish":
        return spanish
    if lang == "english":
        return english

    return "Translated"


# print(translate("english"))
# print(translate("spanish"))
# print(translate("german"))
# call = translate("english")
# print(call())
