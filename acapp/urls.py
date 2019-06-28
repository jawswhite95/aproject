from django.contrib import admin
from django.urls import path
import acapp.views

urlpatterns = [
    path('accounts/signup/', acapp.views.signup, name='signup'),
    path('accounts/login/', acapp.views.login, name='login'),
    path('accounts/logout/', acapp.views.logout, name='logout'),
]