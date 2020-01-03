import bcrypt

from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .models import User, UserLevel
from apps.dashboard_messages.models import Message

from apps.utils import get_logged_user, check_admin

@require_GET
def index(request):
  return render(request, 'index.html')

@require_GET
def signin(request):
  return render(request, 'signin.html')

@require_POST
def user_check(request):
  email = request.POST['email_input']
  password = request.POST['password_input']
  user = User.objects.filter(email=email)
  if user and len(user) == 1:
    logged_user = user[0]
    if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
      request.session['userid'] = logged_user.id
      logged_user = get_logged_user(request)

      return redirect('dashboard')
  messages.error(request, 'Invalid username or password')
  return redirect('signin')

@require_GET
def logout(request):
  request.session.clear()
  return redirect('/')

@require_GET
def register(request):
  return render(request, 'register.html')
