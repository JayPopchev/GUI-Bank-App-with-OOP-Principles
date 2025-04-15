from bank_app.accounts.basic_bank_account import BasicBankAccount
from bank_app.accounts.gold_bank_account import GoldBankAccount
from bank_app.accounts.premium_bank_account import PremiumBankAccount


class BankManager:
    def __init__(self):
        self.bank_accounts = {"BasicAccount": [],
                              "PremiumAccount": [],
                              "GoldAccount": []}

    def create_bank_account(self, name, account_type):
        valid_type = {"BasicAccount": BasicBankAccount,
                      "PremiumAccount": PremiumBankAccount,
                      "GoldAccount": GoldBankAccount}.get(account_type)

        if not valid_type:
            raise ValueError("Wrong type!")

        new_user = valid_type(name)
        self.bank_accounts[account_type].append(new_user)

    def get_accounts_by_type(self, name, account_type):
        person = next((u for u in self.bank_accounts[account_type] if u.owner_name == name), None)


        if person is None:
            raise ValueError("No account found")

        return person




