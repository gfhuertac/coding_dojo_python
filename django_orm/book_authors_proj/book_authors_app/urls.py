from django.urls import path

from . import views

urlpatterns = [
    path('authors', views.authors, name='authors'),
    path('author/<int:id>', views.author, name='author'),
    path('create_author', views.create_author, name='create_author'),
    path('add_book_to_author', views.add_book_to_author, name='add_book'),
    path('books', views.books, name='books'),
    path('book/<int:id>', views.book, name='book'),
    path('create_book', views.create_book, name='create_book'),
    path('add_author_to_book', views.add_author_to_book, name='add_author'),
]
