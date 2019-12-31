from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='books'),
  path('add/', views.books_add, name='books_add'),
  path('new/', views.books_create, name='books_create'),
  path('<int:id>/', views.book, name='book'),
  path('<int:id>/reviews/', views.review_create, name='review_create'),
  path('<int:id>/reviews/<int:review_id>/destroy/', views.review_destroy, name='review_destroy'),
  path('users/<int:id>/', views.user, name='user'),
]