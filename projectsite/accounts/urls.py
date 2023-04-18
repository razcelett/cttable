from django.contrib import admin
from django.urls import path, re_path

from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change_password', views.change_password, name="change_password"),
]