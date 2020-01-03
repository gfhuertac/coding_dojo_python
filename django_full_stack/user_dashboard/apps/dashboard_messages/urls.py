from django.urls import path

from . import views

urlpatterns = [
  path('messages/create/', views.message_create, name='message_create'),
  path('messages/<int:id>/update/', views.message_update, name='message_update'),
  path('messages/<int:id>/destroy/', views.message_destroy, name='message_destroy'),
]