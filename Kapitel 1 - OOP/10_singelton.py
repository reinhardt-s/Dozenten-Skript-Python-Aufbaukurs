# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/

from bank_account import account


class Person:
    """
    A class representing a person with a name and a bank account.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes a Person object with a name and a bank account.
        """
        self.name = name

    def spend_money(self, amount: float) -> None:
        """
        Decreases the balance of the bank account by the given amount.
        """
        account.balance -= amount

    def get_current_balance(self) -> float:
        """
        Returns the current balance of the bank account.
        """
        return account.balance


alex = Person(name='Alex')
riley = Person(name='Riley')

alex.spend_money(50)
riley.spend_money(150)

print(alex.get_current_balance())
print(riley.get_current_balance())
