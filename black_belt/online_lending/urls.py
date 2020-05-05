from django.urls import path

from . import views

# urls for the online_lending app
urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('user_create/', views.user_create, name='user_create'),
  path('user_check/', views.user_check, name='user_check'),
  path('borrower/<int:id>', views.borrower, name='borrower'),
  path('lender/<int:id>', views.lender, name='lender'),
  path('lend/', views.lend, name='lend'),
]