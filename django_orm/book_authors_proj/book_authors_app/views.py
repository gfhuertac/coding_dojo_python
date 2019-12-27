from django.shortcuts import render, HttpResponseRedirect, resolve_url
from django.views.decorators.http import require_http_methods

from book_authors_app.models import *

@require_http_methods(['GET'])
def authors(request):
  context = { 'authors': Author.objects.all() }
  return render(request, 'authors.html', context)

@require_http_methods(['POST'])
def create_author(request):
  first_name = request.POST['first_name_input']
  last_name = request.POST['last_name_input']
  notes = request.POST['notes_input']
  Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
  return HttpResponseRedirect('authors')

@require_http_methods(['GET'])
def author(request, id):
  author = Author.objects.get(id=id)
  context = { 'author': author, 'books': Book.objects.exclude(authors=author) }
  return render(request, 'author.html', context)

@require_http_methods(['POST'])
def add_book_to_author(request):
  author = Author.objects.get(id=request.POST['author_hidden'])
  book = Book.objects.get(id=request.POST['books_select'])
  author.books.add(book)
  author.save()
  return HttpResponseRedirect(resolve_url('author', id=author.id))

@require_http_methods(['GET'])
def books(request):
  context = { 'books': Book.objects.all() }
  return render(request, 'books.html', context)

@require_http_methods(['POST'])
def create_book(request):
  title = request.POST['title_input']
  description = request.POST['description_input']
  Book.objects.create(title=title, desc=description)
  return HttpResponseRedirect('books')

@require_http_methods(['GET'])
def book(request, id):
  book = Book.objects.get(id=id)
  context = { 'book': book, 'authors': Author.objects.exclude(books=book)}
  return render(request, 'book.html', context)

@require_http_methods(['POST'])
def add_author_to_book(request):
  author = Author.objects.get(id=request.POST['authors_select'])
  book = Book.objects.get(id=request.POST['book_hidden'])
  author.books.add(book)
  author.save()
  return HttpResponseRedirect(resolve_url('book', id=book.id))
