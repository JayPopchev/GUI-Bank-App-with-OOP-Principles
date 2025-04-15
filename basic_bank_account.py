from bank_app.accounts.base_bank_account import BaseBankAccount


class BasicBankAccount(BaseBankAccount):
    DEPOSIT_REWARDS_RATE = 0.005
    WITHDRAW_REWARDS_RATE = 0.003
    def __init__(self, owner_name):
        super().__init__(owner_name, account_type="BasicType")

    def return_on_deposit(self, amount):
        bonus = amount * self.DEPOSIT_REWARDS_RATE
        return amount + bonus

    def return_on_withdraw(self, amount):
        bonus = amount * self.WITHDRAW_REWARDS_RATE
        return bonus