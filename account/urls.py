from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('loginpage/', views.loginPage, name='loginPage'),
    path('logoutpage/', views.logoutPage, name='logoutPage'),

    path('account/', views.userAccount, name='account'),
    path('edit_account/', views.editAccount, name='edit'),

]