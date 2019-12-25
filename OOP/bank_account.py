class BankAccount:
  def __init__(self, int_rate=0.01, balance=0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    if amount >= 0:
      self.balance += amount
    else:
      raise Exception('amount cannot be negative')
    return self

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print('Insufficient funds: Charging a $5 fee')
      self.balance -= 5
    return self

  def display_account_info(self):
    print(f'Balance: ${self.balance}')

  def yield_interest(self):
    if self.balance > 0:
      self.balance *= (1 + self.int_rate)
    return self

if __name__ == '__main__':
  from faker import Faker
  faker = Faker()
  accounts = []
  for _ in range(3):
    profile = faker.simple_profile()
    accounts.append(BankAccount())
  accounts[0].deposit(100).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()
  accounts[1].deposit(400).deposit(300).withdraw(200).withdraw(100).withdraw(200).withdraw(100).yield_interest().display_account_info()
  