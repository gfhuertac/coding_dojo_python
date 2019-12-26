from django.shortcuts import render, HttpResponseRedirect

from users_app.models import *

def index(request):
  """

  """  
  users = User.objects.all()
  context = {
      'users': users
  }
  return render(request, 'index.html', context)

def process(request):
  """

  """
  first_name = request.POST['first_name_input']
  last_name = request.POST['last_name_input']
  email = request.POST['email_input']
  age = request.POST['age_input']
  User.objects.create(first_name=first_name, last_name=last_name, email_address=email, age=age)
  return HttpResponseRedirect('/')
