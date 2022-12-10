# https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/

from bank_account import account


class Person:
    def __init__(self, name):
        self.name = name

    def spend_money(self, amount):
        account.balance -= amount

    def get_current_balance(self):
        return account.balance


alex = Person(name='Alex')
riley = Person(name='Riley')

alex.spend_money(50)
riley.spend_money(150)

print(alex.get_current_balance())
print(riley.get_current_balance())
