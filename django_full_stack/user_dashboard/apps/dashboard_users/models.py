from django.db import models
from enum import Enum

class UserLevel(Enum):
  ADMIN = 9
  NORMAL = 1

class UserManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    email = data.get('email_input', False)
    first_name = data.get('first_name_input', False)
    last_name = data.get('last_name_input', False)
    password = data.get('password_input', False)
    confirmation = data.get('confirmation_input', False)
    if email and len(email) == 0:
      errors['email_input'] = 'Email cannot be empty'
    if first_name and len(first_name) == 0:
      errors['first_name_input'] = 'First name cannot be empty'
    if last_name and len(last_name) == 0:
      errors['last_name_input'] = 'Last name cannot be empty'
    if password != confirmation:
      errors['password_input'] = 'Passwords must match!'
    return errors

class User(models.Model):
  email = models.EmailField()
  first_name = models.CharField(max_length=32)
  last_name = models.CharField(max_length=32)
  password = models.CharField(max_length=512)
  description = models.TextField()
  user_level = models.IntegerField(
    choices = [(tag, tag.value) for tag in UserLevel]
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
