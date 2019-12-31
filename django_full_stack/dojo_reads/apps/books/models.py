from django.db import models
from django.core.validators import validate_email

from datetime import datetime

from apps.login.models import User

class AuthorManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    selected = int(data['author_select'])
    name = data['author_input']
    if selected == 0 and len(name) < 5:
      errors['author_input'] = 'Author is required and its length should be at least 5'
    return errors

class Author(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = AuthorManager()

class BookManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    title = data['title_input']
    if len(title) == 0:
      errors['title_input'] = 'Title is required'
    return errors

class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
  uploaded_by = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BookManager()

class ReviewManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    review = data['review_input']
    if len(review) < 15:
      errors['review_input'] = 'Review should be at least 15 characters long'
    return errors

class Review(models.Model):
  review = models.TextField()
  rating = models.IntegerField(choices=[(i+1,i+1) for i in range(5)])
  book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
  posted_by = models.ForeignKey(User, related_name = 'reviews', on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ReviewManager()
