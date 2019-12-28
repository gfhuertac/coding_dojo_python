from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect # add redirect to import statement

def blogs(request):
  """ Redirects to the blog page

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A rdirects to the page with all the blogs 
    """
  return redirect('/blogs')

def index(request):
  """ Returns the index page.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with all the users 
    """
  return HttpResponse('placeholder to later display all the list of users')

def new(request):
  """ Returns a form to create a new user.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with the form
    """
  return HttpResponse('placeholder for users to create a new user record')

def login(request):
  """ Login form

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with the form
    """
  return HttpResponse('placeholder for users to log in')
