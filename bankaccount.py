class BankAccount:
    def __init__(self,owner,balance_attribute=0.0):
        self.owner=owner
        self.balance_attribute=balance_attribute
    def balance(self):
        return self.balance_attribute
    def deposit(self, amount):
        self.balance_attribute= self.balance_attribute+ amount
        return self.balance_attribute
    def withdraw(self, amount):
        self.balance_attribute= self.balance_attribute-amount
        return self.balance_attribute


acct1= BankAccount("Darcy")
print(acct1.balance())
print(acct1.deposit(10))
print(acct1.withdraw(7))
print(acct1.balance())
