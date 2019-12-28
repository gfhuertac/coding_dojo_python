from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect # add redirect to import statement

def index(request):
  """ Returns the index page.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with all the blogs 
    """
  return HttpResponse('placeholder to display all the surveys created')

def new(request):
  """ Returns a form to create a survey.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with the form
    """
  return HttpResponse('placeholder for users to add a new survey')
