from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .models import Message
from apps.dashboard_users.models import User, UserLevel
from apps import utils

@require_POST
def message_create(request):
  logged_user = utils.get_logged_user(request)
  errors = Message.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    user_id = int(request.POST['to_hidden'])
    message_id = int(request.POST.get('reply_to_hidden', 0))
    message = request.POST['message_input']
    to_user = User.objects.get(id=user_id)
    reply = None
    if message_id != 0:
      reply = Message.objects.get(id=message_id)
    
    Message.objects.create(message=message, author=logged_user, to=to_user, reply_to=reply)
  return redirect('user_show', id=to_user.id)

@require_POST
def message_update(request):
  pass

@require_POST
def message_destroy(request):
  pass

