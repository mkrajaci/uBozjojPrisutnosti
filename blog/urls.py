from django.urls import path
from . import views

'''
 '' označava prazan put jer je to home page,
 views.home je poziv funkcije home iz views.py datoteke
 name je ime puta/rute, dobro je nazivati ga sa prefiksom aplikacije jer može
 biti više aplikacija sa rutom do home page-a
'''
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]