from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signin/', views.signin, name='signin'),
  path('logout/', views.logout, name='logout'),
  path('register/', views.register, name='register'),
  path('users/check', views.user_check, name='user_check'),
]