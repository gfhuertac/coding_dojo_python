from bank_account import BankAccount

class User(object):
  def __init__(self, username, email_address):
    self.name = username			# and we use the values passed in to set the name attribute
    self.email = email_address		# and the email attribute
    self.accounts = {
      'default': BankAccount(int_rate=0.02, balance=0)
    }

  # adding the deposit method
  def make_deposit(self, amount, account='default'):	# takes an argument that is the amount of the deposit
    self.accounts[account].deposit(amount)	# the specific user's account increases by the amount of the value received
    return self

  def make_withdrawal(self, amount, account='default'): # have this method decrease the user's balance by the amount specified
    self.accounts[account].withdraw(amount)
    return self

  def display_user_balance(self, account='default'): # have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    print(f'User: {self.name}')
    self.accounts[account].display_account_info()

  #BONUS:
  def transfer_money(self, other_user, amount): # have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    self.make_withdrawal(amount)
    other_user.make_deposit(amount)
    return self

  # SENSEI BONUS
  def add_account(self, name, account):
    self.accounts[name] = account
    return self

if __name__ == '__main__':
  from faker import Faker
  faker = Faker()
  users = []
  for _ in range(3):
    profile = faker.simple_profile()
    users.append(User(profile['username'], profile['mail']))
  users[0].make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(400).display_user_balance()
  users[1].make_deposit(400).make_deposit(300).make_withdrawal(200).make_withdrawal(100).display_user_balance()
  users[2].make_deposit(400).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()
  users[0].transfer_money(users[1], 100).display_user_balance()
  users[1].display_user_balance()
  