from typing import List


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class GroceryList:
    def __init__(self):
        self._our_list: List[str] = []

    def add_item(self, item: str):
        self._our_list.append(item)

    @property
    def our_list(self) -> List[str]:
        return self._our_list


class Parent:
    def __init__(self, name: str):
        self.name = name
        self.grocery_list = GroceryList()

    def add_to_grocery_list(self, item: str):
        self.grocery_list.add_item(item)

    def get_grocery_list(self) -> List[str]:
        return self.grocery_list.our_list
