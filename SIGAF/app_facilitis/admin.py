from django.contrib import admin
from app_facilitis.models.ocorencias import NivelDeOcorrencia

class MostrNivelDeUrgencia(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'sigla')
    list_display_links = ('id',)

admin.site.register(NivelDeOcorrencia, MostrNivelDeUrgencia)
