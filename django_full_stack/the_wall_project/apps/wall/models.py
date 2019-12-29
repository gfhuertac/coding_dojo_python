from django.db import models

from apps.login.models import User

class Message(models.Model):
  message = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comments')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
