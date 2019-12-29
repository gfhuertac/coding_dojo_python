from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='wall'),
  path('messages/create', views.create_message, name='create_message'),
  path('message/<int:id>/delete', views.delete_message, name='delete_message'),
  path('message/<int:message_id>/comments/create', views.create_comment, name='create_comment'),
  path('message/<int:message_idid>/comment/<int:id>/delete', views.delete_comment, name='delete_comment'),
]