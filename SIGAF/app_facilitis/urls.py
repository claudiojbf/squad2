from django.urls import path
from . import views

# urlpatterns = [
#     path("local", views.cadastro_de_local, name="cadastro_de_local"),
# ]

urlpatterns = [
    path('local/', views.cadastro , name='Cadastro'),
    path('mostra_local', views.mostra_local, name='mostra_local'),
    path('deleta_local/<int:local_id>', views.deleta_local, name='deleta_local'),
    path('editar_local/<int:local_id>', views.editar_local, name='editar_local'),
    path('atualiza_local', views.atualiza_local, name='atualiza_local')
]
