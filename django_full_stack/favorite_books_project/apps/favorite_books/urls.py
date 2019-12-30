from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='books'),
  path('new/', views.books_create, name='books_create'),
  path('<int:id>/', views.book, name='book'),
  path('<int:id>/update/', views.book_update, name='book_update'),
  path('<int:id>/favorite/', views.book_favorite, name='book_favorite'),
  path('<int:id>/destroy/', views.book_destroy, name='book_destroy'),
]