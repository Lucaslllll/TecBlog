from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('artigo/<int:pk>', views.individual, name='individual'),
    path('comentario', views.comment, name='comment'),
    path('resposta', views.recomment, name='recomment'),
    path('registrar', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]