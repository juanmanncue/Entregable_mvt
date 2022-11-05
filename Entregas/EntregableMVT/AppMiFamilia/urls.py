from django.contrib import admin
from django.urls import path
from .views import mostrar_info

urlpatterns = [
    path('mostrar_info/', mostrar_info),
]