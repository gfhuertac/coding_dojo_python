from django.db import models
from django.core.validators import validate_email

from datetime import datetime

from apps.login.models import User

class BookManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    title = data['title_input']
    desc = data['description_input']
    if len(title) == 0:
      errors['title_input'] = 'Title is required'
    if len(desc) < 5:
      errors['description_input'] = 'Description must be at least 5 characters long'
    return errors

class Book(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  uploaded_by = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
  users_who_like = models.ManyToManyField(User, related_name = 'liked_books')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BookManager()