# Lege ein Modul 'shared' in diesem Ordner an.
# Erstelle in dem Modul die Datei 'grocery_list'.
# Diese enthält die Liste 'our_list'
#
# Vervollständige anschließend die Klassen Parent und Person, sodass:
# > add_to_grocery_list(item) ein neues item auf die gemeinsame Einkaufsliste setzt.
# > get_grocery_list() einen String mit alles items auf der Einkaufsliste zurück gibt.
# > Der jeweilige Konstruktor ein name-Argument annimmt


from person import Person
from parent import Parent


def main():
    # create instances of Person and Parent classes
    alex = Person('Alex')
    riley = Person('Riley')
    hank = Parent('Hank')

    # add items to grocery list
    alex.add_to_grocery_list("Mehl")
    alex.add_to_grocery_list("Eier")
    hank.add_to_grocery_list("Badesalz")
    riley.add_to_grocery_list("Gurken")
    riley.add_to_grocery_list("Knabberzeugs")
    riley.add_to_grocery_list("Kaffee")

    # print grocery list
    print(riley.grocery_list())


if __name__ == '__main__':
    main()

