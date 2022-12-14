from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('index', views.index, name = 'index'),
    path('logout', views.logout, name='logout'),
    path('perfil', views.perfil, name='perfil'),
]