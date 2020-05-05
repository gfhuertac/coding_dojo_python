from django.db import models
from enum import IntEnum

from . import managers

# we are going to define a user rol. It can be one of lender, borrower
class UserRole(IntEnum):
  GUEST = 0
  BORROWER = 1
  LENDER = 2

  @staticmethod
  def role_as_string(role):
    """
      Method used to transform the enumeration to a string
      Args:
      - role (UserRole): the role to be transformed
      Returns:
      A str containing the label for the role
    """
    existing_role = 'guest'
    if role == UserRole.BORROWER:
      existing_role = 'borrower'
    elif role == UserRole.LENDER:
      existing_role = 'lender'
    return existing_role

class User(models.Model):
  """
    Class to define a user, based on the specified requirements
  """
  first_name = models.CharField(max_length=32)
  last_name = models.CharField(max_length=32)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=512)
  money = models.DecimalField(max_digits=10, decimal_places=2)
  need_money_for = models.CharField(max_length=128)
  description = models.TextField()
  user_role = models.IntegerField(
    choices = [(tag.name, tag.value) for tag in UserRole]
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = managers.UserManager()

  @property
  def borrowed_amount(self):
    """
      A property that computes automatically the amount of money borrowed from the user
    """
    debts = self.debts.all()
    borrowed_amount = sum([debt.amount for debt in debts], 0)
    return borrowed_amount

  @property
  def lent_amount(self):
    """
      A property that computes automatically the amount of money lent by the user
    """
    loans = self.loans.all()
    lent_amount = sum([loan.amount for loan in loans], 0)
    return lent_amount

class Loan(models.Model):
  """
    Class that describes a lending process from a lender to another user
    that requested money
  """
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  lender = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
  borrower = models.ForeignKey(User, related_name='debts', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = managers.LoanManager()
