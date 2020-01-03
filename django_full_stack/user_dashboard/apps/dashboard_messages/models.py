from django.db import models

from apps.dashboard_users.models import User

class MessageManager(models.Manager):
  def basic_validator(self, data):
    errors = {}
    message = data.get('message_input', '')
    if len(message) == 0:
      errors['message_input'] = 'Message cannot be empty'
    return errors

class Message(models.Model):
  message = models.TextField()
  author = models.ForeignKey(User, related_name='written_messages', on_delete=models.CASCADE)
  to = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
  reply_to = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = MessageManager()
