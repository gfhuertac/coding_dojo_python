from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.blogs),
    path('users', views.index),
    path('users/new', views.new),
    path('register', views.new),
    path('login', views.login),
]
