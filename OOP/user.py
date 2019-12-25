class User(object):
  def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

  # adding the deposit method
  def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    if amount > 0:
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    else:
      raise Exception('Amount to be deposited should be positive')
    return self

  def make_withdrawal(self, amount): # have this method decrease the user's balance by the amount specified
    if self.account_balance >= amount:
      self.account_balance -= amount
    else:
      raise Exception('Amount to be withdrawed should be less or equal than the balance')
    return self

  def display_user_balance(self): # have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    print(f'User: {self.name}, Balance ${self.account_balance}')

  #BONUS:
  def transfer_money(self, other_user, amount): # have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    self.make_withdrawal(amount)
    other_user.make_deposit(amount)
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
  