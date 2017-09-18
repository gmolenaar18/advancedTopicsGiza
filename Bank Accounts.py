

class BankAccount():

  accounts = 1

  def __init__(self, name):
    self.balance = 0
    self.owner = name
    self.number = BankAccount.accounts
    BankAccount.accounts += 1

  def dep(self, amount):
    self.balance += amount
    print amount,"Moneys Deposited"
    print self.balance,"is your new balance"

  def wit(self, amount):
    self.balance -= amount
    print amount,"Moneys Withdrawn"
    print self.balance,"is your new balance"

  def check(self):
    print self.balance,"is your current balance"

GizaAccount=BankAccount("Giza")
print GizaAccount.owner
GizaAccount.check()
