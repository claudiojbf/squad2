from django.urls import path
from . import views
urlpatterns = [
    path('cadastroFuncionario', views.cadastroFuncionario, name='cadastroFuncionario'),
    path('editar_funcionario/<int:funcionario_id>', views.editar_funcionario, name='editar_funcionario'),
    path('atualiza_funcionario', views.atualiza_funcionario, name='atualiza_funcionario'),
]