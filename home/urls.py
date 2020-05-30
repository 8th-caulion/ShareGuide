from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('',home.views.main, name = "main"),
    path('signin/',home.views.signin, name = "signin"),
]