from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('wykres/', views.wykres, name='wykres'),
    path('api/wykres/', views.api_wykres, name='api_wykres'),
    path('pobierz/', views.pobierz, name='pobierz'),
    path('potwierdzenie/', views.potwierdzenie, name='potwierdzenie'),
    path('zajete/', views.zajete, name='zajete'),
    path('kluby/', views.kluby, name='kluby'),
    path('rezerwacja/', views.rezerwacja, name='rezerwacja'),
    path('cennik/', views.cennik, name='cennik'),
    path('zapisy/<pk_klubu>', views.zapisy, name='zapisy'),
    path('zawodnicy/', views.zawodnicy, name='zawodnicy'),
    path('rezerwacje/', views.rezerwacje, name='rezerwacje'),
    path('klubowi_gracze/<klub_id>', views.klubowi_gracze, name='klubowi-gracze'),
]