from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  desc = models.CharField(max_length=255, default='old dojo')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # ninjas <-- referenced field

class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  dojo = models.ForeignKey(to=Dojo, related_name='ninjas', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
