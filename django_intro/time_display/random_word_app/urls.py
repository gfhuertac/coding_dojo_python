from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('random_word', views.random_word),
    path('random_word/reset', views.reset),
]
