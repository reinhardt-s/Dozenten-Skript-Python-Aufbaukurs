from shared import grocery_list


class Person:
    def __init__(self, name):
        self.name = name

    def add_to_grocery_list(self, item):
        grocery_list.our_list.append(item)

    def get_grocery_list(self):
        return grocery_list.our_list
