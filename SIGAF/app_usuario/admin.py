from django.contrib import admin
from app_usuario.models import TipoUsuario

class MostrarTipo(admin.ModelAdmin):
    list_display = ('id', 'nome_tipo', 'sigla')
    list_display_links = ('id',)

admin.site.register(TipoUsuario, MostrarTipo)
