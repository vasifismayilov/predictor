from django.contrib import admin
from django.urls import path,include
from .views import LoginView,HomeView

urlpatterns = [
    path('',LoginView.as_view(),name="index"),
    path('home/',HomeView.as_view(),name="home")
]