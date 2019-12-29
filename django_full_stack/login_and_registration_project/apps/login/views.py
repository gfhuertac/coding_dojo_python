import bcrypt

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from datetime import datetime

from .models import User

@require_http_methods(['GET'])
def index(request):
  return render(request, 'index.html')

@require_http_methods(['GET'])
def success(request):
  if 'userid' not in request.session:
    return redirect('/')
  context = {
    'type': request.GET['type'],
    'user': User.objects.get(id=request.session['userid'])
  }
  return render(request, 'success.html', context)

@require_http_methods(['POST'])
def login(request):
  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    email = request.POST['email_input']
    password = request.POST['password_input']
    user = User.objects.filter(email=email)
    if user and len(user) == 1:
      logged_user = user[0]
      if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
        request.session['userid'] = logged_user.id
        return redirect('/success?type=login')
  return redirect('/')

@require_http_methods(['POST'])
def register(request):
  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    first_name = request.POST['first_name_input']
    last_name = request.POST['last_name_input']
    email = request.POST['email_input']
    birthdate = datetime.strptime(request.POST['birthdate_input'], '%m/%d/%Y')
    password = request.POST['password_input']
    user = User.objects.filter(email=email)
    if user and len(user) == 1:
      messages.error(request, 'Email is already registered')
    else:
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
      new_user = User.objects.create(first_name=first_name, last_name=last_name, birthdate=birthdate, email=email, password=pw_hash)
      request.session['userid'] = new_user.id
      return redirect('/success?type=register')
  return redirect('/')

@require_http_methods(['GET'])
def logout(request):
  request.session.clear()
  return redirect('/')