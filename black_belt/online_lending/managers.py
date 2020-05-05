from django.db import models

class UserManager(models.Manager):
  """
    Class to validate the creation of a user. We check the input fields, but also if
    the email is already in use
  """
  def basic_validator(self, data):
    """
      Method to validate if a user fulfils all the requirements
      Args:
      - data (dictionary): a dictionary with the data to be used to create/modify a user
      Returns:
      - a dictionary containing the list of errors
    """
    from . import models
    # step 0: create an empty errors dictionary
    errors = {}
    # step 1: check all fields
    first_name = data.get('first_name_input', False)
    last_name = data.get('last_name_input', False)
    email = data.get('email_input', True)
    password = data.get('password_input', True)
    money = data.get('money_input', True)
    need_money_for = data.get('need_money_for_input', False)
    description = data.get('description_input', False)
    user_role = int(data.get('user_role_input', models.UserRole.GUEST))
    if first_name and len(first_name) == 0:
      errors['first_name_input'] = 'First name cannot be empty'
    if last_name and len(last_name) == 0:
      errors['last_name_input'] = 'Last name cannot be empty'
    if email and len(email) == 0:
      errors['email_input'] = 'Email cannot be empty'
    if money:
      try:
        amount = int(money)
        if amount <= 0:
          errors['money_input'] = 'Money should be a positive number'
      except:
        errors['money_input'] = 'Money should be a number'
    if need_money_for and len(need_money_for) == 0:
      errors['need_money_for_input'] = 'Need money for cannot be empty'
    if description and len(description) == 0:
      errors['description_input'] = 'Description cannot be empty'
    if user_role == models.UserRole.GUEST:
      errors['user_role_input'] = 'You must select a valid role'
    # step 2: validate that the email does not exists
    try:
      existing_user = models.User.objects.get(email=email)
      current_role = models.UserRole.role_as_string(existing_user.user_role)
      if existing_user:
        errors['email_input'] = f'Email already registered as {current_role}. Please login, or contact the admin if you want to change roles.'
    except:
      pass
    return errors

class LoanManager(models.Manager):
  """
    Class to validate the creation of a lending between users.
    We need to validate the money requested/borrowed among other stuff.
  """
  def basic_validator(self, data):
    """
      Method to validate if a user fulfils all the requirements
      Args:
      - data (dictionary): a dictionary with the data to be used to create/modify a lending
      Returns:
      - a dictionary containing the list of errors
    """
    from . import models
    # step 0: create an empty errors dictionary
    errors = {}
    # step 1: check all fields
    borrower = data.get('borrower_input', True)
    lender = data.get('lender_input', True)
    amount = data.get('amount_input', True)
    if borrower:
      try:
        if type(borrower) is list:
          borrower = borrower[0]
        borrower = int(borrower)
        borrower = models.User.objects.get(id=borrower)
      except Exception as e:
        errors['borrower_input'] = 'Invalid borrower'
    if lender:
      try:
        lender = int(lender)
        lender = models.User.objects.get(id=lender)
      except Exception as e:
        print(e)
        errors['lender_input'] = 'Invalid lender'
    if amount:
      try:
        if type(amount) is list:
          amount = amount[0]
        amount = int(amount)
        if amount <= 0:
          errors['amount_input'] = 'Amount should be a positive number'
      except:
        errors['amount_input'] = 'Amount should be a number'

    # step 2: validate the amount from request and from lender
    if 'amount_input' not in errors and type(borrower) is models.User and type(lender) is models.User:
      if borrower.money - (borrower.borrowed_amount + amount) < 0:
        errors['amount_input'] = 'Lending amount is greater than requested amount'

      if lender.money - (lender.lent_amount + amount) < 0:
        errors['amount_input'] = 'Lending amount is greater than the total available amount'

    return errors
