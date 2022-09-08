from django.urls import path
from app_facilitis.views import *

# urlpatterns = [
#     path("local", views.cadastro_de_local, name="cadastro_de_local"),
# ]

urlpatterns = [
    #Local
    path('local/', cadastro , name='Cadastro'),
    path('mostra_local/', mostra_local, name='mostra_local'),
    path('deleta_local/<int:local_id>', deleta_local, name='deleta_local'),
    path('editar_local/<int:local_id>', editar_local, name='editar_local'),
    path('atualiza_local/', atualiza_local, name='atualiza_local'),
    #Ocorrencia
    path('listar_ocorrencias/',  listar_ocorrencias, name='listar_ocorrencias'),
    path('mostra/<int:ocorrencia_id>', mostra_ocorrencia, name='mostra_ocorrencia'),
    path('registrar/',  registrar_ocorrencia, name='registrar_ocorrencia'),
    path('deleta/<int:ocorrencia_id>', deleta_ocorrencia, name='deleta_ocorrencia'),
    path('edita/<int:ocorrencia_id>', edita_ocorrencia, name='edita_ocorrencia'),
    path('atualiza', atualiza_ocorrencia, name='atualiza_ocorrencia'),
]
