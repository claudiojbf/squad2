from django.contrib import admin
from app_atleta.models import Atletas,Posicao,Video,SubDivisao
# Register your models here.
class MostraAtletas(admin.ModelAdmin):
    list_display= ('id','nome')
    list_display_links=('id', 'nome')
    search_fields =('nome',)

admin.site.register(Atletas,MostraAtletas)

class MostraPosicao(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links=('id','nome')

admin.site.register(Posicao,MostraPosicao)

class MostraSubDivisao(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links=('id','nome')

admin.site.register(SubDivisao,MostraSubDivisao)

class MostraVideo(admin.ModelAdmin):
    list_display=('id','titulo', 'atleta')
    list_display_links=('id','titulo')

admin.site.register(Video, MostraVideo)