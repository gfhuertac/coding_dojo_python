from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
  """ Displays a random word using get_random_string

    Parameters:
      - request (django.shortcuts.HttpRequest): the request made to the page

    Returns: a rendered page showing a random word
  """
  try:
      request.session['attempt'] += 1
  except:
      request.session['attempt'] = 1
  context = {
      'random_word': get_random_string(length=14),
      'attempt': request.session['attempt'],
  }
  return render(request, 'random_word.html', context)

def reset(request):
  """ Resets the number of attemtps

    Parameters:
      - request (django.shortcuts.HttpRequest): the request made to the page

    Returns: redirects to the random word
  """
  request.session['attempt'] = 0
  return redirect('/random_word')