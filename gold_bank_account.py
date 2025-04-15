from bank_app.accounts.base_bank_account import BaseBankAccount


class GoldBankAccount(BaseBankAccount):
    DEPOSIT_REWARDS_RATE = 0.04
    WITHDRAW_REWARDS_RATE = 0.035
    def __init__(self, owner_name):
        super().__init__(owner_name, account_type="GoldType")

    def return_on_deposit(self, amount):
        bonus = amount * self.DEPOSIT_REWARDS_RATE
        return amount + bonus

    def return_on_withdraw(self, amount):
        bonus = amount * self.WITHDRAW_REWARDS_RATE
        return bonus