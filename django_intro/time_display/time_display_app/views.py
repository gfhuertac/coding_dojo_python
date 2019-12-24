from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime

def index(request):
  return HttpResponseRedirect('/time_display')    

def time_display(request):
  """ Displays the current time

    Parameters:
      request (django.shortcuts.HttpRequest): the request made when accessing the page

    Returns: The rendered time display webpage

  """
  now = datetime.now()
  context = {
    'date': now.strftime('%Y-%m-%d'),
    'time': now.strftime('%H:%M'),
    'ampm': now.strftime('%p').lower(),
  }
  return render(request, 'time_display.html', context)
