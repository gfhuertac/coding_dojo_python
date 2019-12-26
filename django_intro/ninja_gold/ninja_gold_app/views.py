from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from random import randint, random

# Create your views here.
def index(request):
  """ Renders the main page

    Parameters:
      request (django.shortcuts.HttpRequest): the request made when accessing the page

    Returns: the rendered page

  """
  if not 'gold' in request.session:
    request.session['gold'] = 0
  if not 'activities' in request.session:
    request.session['activities'] = ''
  return render(request, 'index.html')

def process_money(request):
  """ Process the money according to the building

    Parameters:
      request (django.shortcuts.HttpRequest): the request made when accessing the page

    Returns: a redirect to the index page

  """
  building = request.POST['building']
  min = int(request.POST['min'])
  max = int(request.POST['max'])
  color = 'green'
  now = datetime.now().strftime('%Y/%m/%d %H:%M %p')
  sign = 1
  if building == 'casino':
    sign = -1 if random() < 0.5 else 1
    
  amount = randint(min, max)
  request.session['gold'] += sign * amount
  if sign == 1:
    message = f'<div style="color:{color};">Earned {amount} golds from the {building} ({now})'
  else:
    color = 'red'
    message = f'<div style="color:{color};">Entered a {building} and lost {amount} golds ... Ouch ... ({now})'
  request.session['activities'] = message + request.session['activities']
  return HttpResponseRedirect('/')    

def reset(request):
  request.session.clear()
  return HttpResponseRedirect('/')