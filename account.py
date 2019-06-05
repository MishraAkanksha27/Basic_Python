class Accountant():
    def __init__(self, balance=0):
        self.balance=balance;
        
    def deposit(self, amount):
        if type(amount) not in [int, float]:
            raise TypeError("Amount should be integer or float!!, Enter a valid number")
        if amount <= 0 :
            raise ValueError("Amount to deposit cannot be negative. Enter a value greater than zero!!")
        else:
            self.balance += amount
    
    def withdraw(self, amount):
        if type(amount) not in [int, float]:
            raise TypeError("Amount should be integer or float!!, Enter a valid number")
        if amount <= 0 :
            raise ValueError("Enter a valid value greater than zero!!")
        if amount > self.balance:
            raise ValueError("This will make account balance negative!! Operation cannot be performed")
        else:
            self.balance = self.balance-amount
