from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect # add redirect to import statement

def index(request):
  """ Returns the index page.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with all the blogs 
    """
  return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
  """ Returns a newly created blog page.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A django.shortcuts.HttpResponse with the new blog
    """
  return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
  """ Creates a new blog.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page

    Returns:
        A redirection to the list of blogs
    """
  return redirect('/')

def show(request, number):
  """ Displays the content of a blog.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page
        number (int): The id of the blog to display

    Returns:
        A django.shortcuts.HttpResponse with the requested blog
    """
  return HttpResponse(f'placeholder to display blog number {number}')

def edit(request, number):
  """ Returns the page to edit a blog.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page
        number (int): The id of the blog to display

    Returns:
        A django.shortcuts.HttpResponse with the blog editing page 
    """
  return HttpResponse(f'placeholder to edit blog number {number}')

def destroy(request, number):
  """ Deletes a blog page.

    Parameters:
        request (django.shortcuts.HttpRequest): The request made when accessing the page
        number (int): The id of the blog to display

    Returns:
        A redirection to the list of blogs
    """
  return redirect('/')

