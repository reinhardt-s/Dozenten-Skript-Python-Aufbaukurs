class Singleton:
    """
    A decorator class that implements the Singleton pattern.
    """
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


@Singleton
class GroceryList:
    """
    A class that represents a grocery list.
    """
    def __init__(self):
        self._list = []

    def add_item(self, item):
        """
        Add an item to the grocery list.
        """
        self._list.append(item)

    @property
    def items(self):
        """
        Get the items in the grocery list.
        """
        return self._list


class Person:
    """
    A class that represents a person.
    """
    def __init__(self, name):
        """
        Initialize a new person with the given name.
        """
        self.name = name

    def add_to_grocery_list(self, item):
        """
        Add an item to the grocery list.
        """
        GroceryList().add_item(item)

    def grocery_list(self):
        """
        Get the items in the grocery list.
        """
        return GroceryList().items
