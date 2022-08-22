'''
Created on Aug. 22, 2022

1 - Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
2 - Create a constructor with parameters: accountNumber, name, balance.
3 - Create a Deposit() method which manages the deposit actions.
4 - Create a Withdrawal() method  which manages withdrawals actions.
5 - Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
6- Create a display() method to display account details.

@author: Said
'''

class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self,depAmt):
        self.balance = self.balance + depAmt
    def withdrawl(self, wtdAmt):
        self.balance = self.balance - wtdAmt
    def bankFees(self):
        self.balance = self.balance * .95
    def display(self):
     return("Account Number: " , self.accountNumber, " Name: " , self.name, " Balance: " , self.balance )
jim = BankAccount(1234,"Jim", 500)
jim.bankFees()
print(jim.display())