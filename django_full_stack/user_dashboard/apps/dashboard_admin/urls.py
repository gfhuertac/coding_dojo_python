from django.urls import path

from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('profile/', views.profile, name='profile'),
  path('users/new/', views.users_new, name='users_new'),
  path('users/<int:id>/show/', views.user_show, name='user_show'),
  path('users/<int:id>/edit/', views.user_edit, name='user_edit'),
  path('users/create/', views.user_create, name='user_create'),
  path('users/<int:id>/update/', views.user_update, name='user_update'),
  path('users/<int:id>/destroy/', views.user_destroy, name='user_destroy'),
]