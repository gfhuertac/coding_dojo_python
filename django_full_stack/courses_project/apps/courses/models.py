from django.db import models

class CourseManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    if len(data['name_input']) < 5:
      errors['name_input'] = 'Name cannot be shorter than 5 characters'
    if len(data['name_input']) > 50:
      errors['name_input'] = 'Name cannot be longer than 50 characters'
    if len(data['description_input']) < 15:
      errors['description_input'] = 'Description cannot be shorter than 15 characters'
    return errors

class CommentManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    if len(data['content_input']) < 15:
      errors['content_input'] = 'Comment cannot be shorter than 15 characters'
    return errors

class Description(models.Model):
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  description = models.OneToOneField(Description, on_delete=models.CASCADE)
  objects = CourseManager()

class Comment(models.Model):
  content = models.TextField()
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CommentManager()
