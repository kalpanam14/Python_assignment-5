class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title="Ashish", balance=5000, interestRate=5):
        super().__init__(title, balance)
        self.interestRate = interestRate
