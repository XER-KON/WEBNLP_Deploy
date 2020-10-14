from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Thema', views.form_Thema1_view, name='form_Thema1'),
]
