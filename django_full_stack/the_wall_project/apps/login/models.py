from django.db import models
from django.core.validators import validate_email

from datetime import datetime

class UserManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    if 'first_name_input' in data:
      first_name = data['first_name_input']
      last_name = data['last_name_input']
      birthdate = datetime.strptime(data['birthdate_input'], '%m/%d/%Y')
      now = datetime.now()
      delta_years = now.year - birthdate.year
      delta_months = now.month - birthdate.month
      delta_days = now.day - birthdate.day

      if birthdate > now:
        errors['birthdate_input'] = 'You cannot be from the future :)'
      elif delta_years < 13 or (
        ( delta_years == 13 and delta_months > 0 ) or
        ( delta_years == 13 and delta_months == 0 and delta_days > 0 )
      ):
        errors['birthdate_input'] = 'You must be older than 13 years to register'

      if len(first_name) < 2:
        errors['first_name_input'] = 'First name should be at least 2 characters long'
      if len(last_name) < 2:
        errors['last_name_input'] = 'Last name should be at least 2 characters long'

    email = data['email_input']
    try:
      validate_email( email )
    except:
      errors['email_input'] = 'Invalid email address'
    password = data['password_input']
    if len(password) < 8:
      errors['password_input'] = 'Password should be at least 8 characters long'
    if 'confirmation_input' in data:
      confirmation = data['confirmation_input']
      if password != confirmation:
        errors['password_input'] = 'Confirmation should match password'
    return errors

class User(models.Model):
  first_name = models.CharField(max_length=32)
  last_name = models.CharField(max_length=32)
  email = models.EmailField()
  password = models.CharField(max_length=512)
  birthdate = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  