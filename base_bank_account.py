from abc import ABC, abstractmethod
from re import fullmatch


class BaseBankAccount(ABC):
    _next_id = 1
    def __init__(self, owner_name: str, account_type: str):
        self.owner_name = owner_name
        self.account_type = account_type
        self.balance = 0
        self.account_id = BaseBankAccount._next_id
        BaseBankAccount._next_id += 1

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        patterns = r"^[A-Z][a-zA-Z-' ]+$"
        if not fullmatch(patterns, value):
            raise ValueError("Name not correct!")
        self._owner_name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance under 0")
        self._balance = value
    @abstractmethod
    def return_on_withdraw(self, amount): # gives money back based on the type
        pass

    @abstractmethod
    def return_on_deposit(self, amount): # gives money back based on the type
        pass

    def __str__(self):
        return f"Account ID: {self.account_id}, Account Type: {self.account_type}, Owner: {self.owner_name}, Balance: {self.balance}"