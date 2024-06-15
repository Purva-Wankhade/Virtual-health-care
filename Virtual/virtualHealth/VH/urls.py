from django.contrib import admin
from django.urls import path
from VH import views

urlpatterns = [
    path('', views.index, name='home'),
    path('diseaseDia', views.diseaseDia, name='diseaseDia'),
]
