from django.urls import path

from . import views

urlpatterns = [
  path('', views.shows, name='shows'),
  path('new', views.shows_new, name='shows_new'),
  path('create', views.shows_create, name='shows_create'),
  path('<int:id>', views.show, name='show'),
  path('<int:id>/edit', views.show_edit, name='show_edit'),
  path('<int:id>/update', views.show_update, name='show_update'),
  path('<int:id>/destroy', views.show_destroy, name='show_destroy'),
]
