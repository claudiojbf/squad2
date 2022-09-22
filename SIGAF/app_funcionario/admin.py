from django.contrib import admin
from app_funcionario.models import Funcionario, Funcao
# Register your models here.
class MostraProficional(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    
admin.site.register(Funcionario, MostraProficional)

class MostraTipoDeFuncao(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    
admin.site.register(Funcao, MostraTipoDeFuncao)
