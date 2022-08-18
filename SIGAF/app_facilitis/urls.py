from django.urls import path
from . import views

urlpatterns = [
    path("local", views.cadastro_de_local, name="cadastro_de_local"),
]