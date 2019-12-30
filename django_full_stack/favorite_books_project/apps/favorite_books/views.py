from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.login.models import User
from .models import Book
from django.contrib import messages

@require_http_methods(['GET'])
def index(request):
  if 'userid' not in request.session:
    redirect('/')
  context = {
    'user': User.objects.get(id=request.session['userid']),
    'books': Book.objects.all()
  }
  return render(request, 'books.html', context)

@require_http_methods(['POST'])
def books_create(request):
  if 'userid' not in request.session:
    return redirect('/')
  errors = Book.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    title = request.POST['title_input']
    description = request.POST['description_input']
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.create(title=title, desc=description, uploaded_by=user)
    book.users_who_like.add(user)
    book.save()
    return redirect('books')
  return redirect('/')

@require_http_methods(['GET'])
def book(request, id:int):
  if 'userid' not in request.session:
    redirect('/')
  context = {
    'user': User.objects.get(id=request.session['userid']),
    'book': Book.objects.get(id=id)
  }
  return render(request, 'book.html', context=context)

@require_http_methods(['POST'])
def book_update(request, id:int):
  if 'userid' not in request.session:
    return redirect('/')
  errors = Book.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
  else:
    title = request.POST['title_input']
    description = request.POST['description_input']
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)
    if book.uploaded_by == user:
      book.title = title
      book.desc = description
      book.save()
    return redirect('book', id=book.id)
  return redirect('/')

@require_http_methods(['POST'])
def book_favorite(request, id:int):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  book = Book.objects.get(id=id)
  action = request.POST['action_hidden']
  if action == 'add':
    book.users_who_like.add(user)
  else:
    book.users_who_like.remove(user)
  book.save()
  next = request.POST.get('next', 'books')
  return redirect(next)

@require_http_methods(['POST'])
def book_destroy(request, id:int):
  if 'userid' not in request.session:
    return redirect('/')
  user = User.objects.get(id=request.session['userid'])
  book = Book.objects.get(id=id)
  if book.uploaded_by == user:
    book.delete()
  return redirect('books')
