from django.contrib import admin
from .models import Posicao
# Register your models here.
class MostraPosicao(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links=('id','nome')

admin.site.register(Posicao,MostraPosicao)