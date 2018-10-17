from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home,),
]

#TODO: https://youtu.be/a48xeeo5Vnk?t=399