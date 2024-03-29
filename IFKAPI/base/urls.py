from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name= "advocates"),
    path('advocates/<str:username>', views.advocate_details),
]
