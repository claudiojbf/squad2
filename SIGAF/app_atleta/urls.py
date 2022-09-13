from urllib.request import url2pathname
from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    # path('<int:atleta_id>', views.atleta, name='atleta'),
    path('cadastrodeAtletas', views.cadastrodeAtletas , name='cadastrodeAtletas'),
    path('apagar_atleta/<int:atleta_id>', views.apagar_atleta, name='apagar_atleta'),
    path('editar_atleta/<int:atleta_id>', views.editar_atleta, name='editar_atleta'),
    path('atualiza_atleta', views.atualiza_atleta, name='atualiza_atleta'),  
]