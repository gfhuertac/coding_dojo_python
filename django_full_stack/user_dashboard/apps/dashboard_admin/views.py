import bcrypt

from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from apps.dashboard_users.models import User, UserLevel
from apps.dashboard_messages.models import Message

from apps.utils import get_logged_user, check_admin

@require_GET
def dashboard(request):
  logged_user = get_logged_user(request)
  if logged_user is None:
    return redirect('/')
  users = User.objects.all()
  context = {
    'users': users,
    'is_admin': check_admin(logged_user),
  }
  return render(request, 'dashboard.html',context=context)

@require_GET
def profile(request):
  logged_user = get_logged_user(request)
  context = {
    'user': logged_user,
    'is_admin': check_admin(logged_user),
    'user_level_choices': User._meta.get_field('user_level').choices,
  }
  return render(request, 'profile.html', context=context)

@require_GET
def users_new(request):
  logged_user = get_logged_user(request)
  if not check_admin(logged_user):
    return redirect('/')
  context = {
    'is_admin': check_admin(logged_user),
    'user_level_choices': User._meta.get_field('user_level').choices,
  }
  return render(request, 'user_new.html', context=context)

@require_GET
def user_show(request, id:int):
  logged_user = get_logged_user(request)
  user = User.objects.get(id=id)
  context = {
    'user': user,
    'is_admin': check_admin(logged_user),
  }
  return render(request, 'user_page.html', context=context)

@require_GET
def user_edit(request, id:int):
  logged_user = get_logged_user(request)
  if not check_admin(logged_user):
    return redirect('/')
  user = User.objects.get(id=id)
  context = {
    'user': user,
    'is_admin': check_admin(logged_user),
    'user_level_choices': User._meta.get_field('user_level').choices,
  }
  return render(request, 'profile.html', context=context)

@require_POST
def user_create(request):
  logged_user = get_logged_user(request)

  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    email = request.POST['email_input']
    first_name = request.POST['first_name_input']
    last_name = request.POST['last_name_input']
    password = request.POST['password_input']

    users_count = User.objects.count()
    if users_count == 0:
      user_level = UserLevel.ADMIN.value
    else:
      user_level = UserLevel.NORMAL.value

    if check_admin(logged_user):
      user_level = request.POST.get('user_level_select', user_level)
      print('user should be admin')
    
    user = User.objects.filter(email=email)
    if user and len(user) == 1:
      messages.error(request, 'Email is already registered')
    else:
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
      new_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=pw_hash, user_level=user_level)
      if logged_user is None:
        request.session['userid'] = new_user.id
        logged_user = get_logged_user(request)

      return redirect('dashboard')
  next = request.POST.get('next_hidden', 'register')
  return redirect(next)

@require_POST
def user_update(request, id:int):
  logged_user = get_logged_user(request)
  user = User.objects.get(id=id)
  if not check_admin(logged_user) and user.id != logged_user.id:
    return redirect('/')

  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    email = request.POST.get('email_input', user.email)
    first_name = request.POST.get('first_name_input', user.first_name)
    last_name = request.POST.get('last_name_input', user.last_name)
    description = request.POST.get('description_input', user.description)
    password = request.POST.get('password_input', None)

    user_level = user.user_level
    if check_admin(logged_user):
      user_level = request.POST.get('user_level_select', user_level)
    
    user = User.objects.filter(Q(email=email) & ~Q(id=id))
    if user and len(user) == 1:
      messages.error(request, 'Email is already registered')
    else:
      user = User.objects.get(id=id)
      user.email = email
      user.first_name=first_name
      user.last_name = last_name
      user.description = description
      user.user_level=user_level
      if password is not None:
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user.password = pw_hash      
      user.save()

  next = request.POST.get('next', 'profile')
  try:
    return redirect(next, id=id)
  except:
    return redirect(next)

@require_GET
def user_destroy(request, id:int):
  logged_user = get_logged_user(request)
  if not check_admin(logged_user):
    return redirect('/')

  user = User.objects.get(id=id)
  user.delete()
  return redirect('dashboard')
