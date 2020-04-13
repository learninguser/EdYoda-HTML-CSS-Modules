class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount >= 50000:
            return  'Please provide your pan card details.'
        else:
            self.balance += amount
        return self.balance

    # question ninth Solution:
    def withdraw(self, amount):
        if amount >= 50000:
            return  'Please provide your pan card details.'
        if amount > self.balance:
            return "You don't have sufficient balance."
        else:
            self.balance -= amount
        return self.balance

class MinimumBalance(BankAccount):
    def withdraw(self, amount):
        if amount >= 50000:
            return  'Please provide your pan card details.'
        if ((self.balance - amount) < 5000):
            return 'Sorry, minimum balance must be maintained.'
        else:
            self.balance -= amount
        return self.balance
user1 = MinimumBalance()
balance = user1.deposit(10000)
balance = user1.withdraw(6000)
print(balance)
