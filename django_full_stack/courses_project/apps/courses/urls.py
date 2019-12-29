from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='courses'),
    path('<int:id>/comments', views.comments, name='course_comments'),
    path('<int:id>/destroy', views.destroy, name='course_destroy'),
]