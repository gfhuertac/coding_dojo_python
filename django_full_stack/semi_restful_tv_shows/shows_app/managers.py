from django.db import models
from django.db.models import Q

from datetime import datetime

class ShowManager(models.Manager):
  def basic_validator(self, data):
    from .models import Show
    errors = {}
    if len(data['title_input']) < 2:
      errors['title_input'] = 'Title cannot be empty and its minimum length is 2'
    id = int(data['id_hidden'])
    shows = Show.objects.filter(~Q(id=id) & Q(title=data['title_input']))
    if shows is not None and len(shows) != 0:
      errors['title_input'] = 'Title should be unique'
    if len(data['network_input']) < 3:
      errors['network_input'] = 'Network cannot be empty and its minimum length is 3'
    if len(data['description_input']) > 0 and len(data['description_input']) < 10:
      errors['description_input'] = 'Description should be (at least) 10 characters.'
    release_date = datetime.strptime(data['release_date_input'], '%B %d, %Y')
    if  release_date > datetime.now():
      errors['release_date_input'] = 'Invalid date. It must be lower than current date'
    return errors
