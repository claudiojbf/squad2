from django.contrib import admin
from .models import SubDivisao
# Register your models here.
class MostraSubDivisao(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links=('id','nome')

admin.site.register(SubDivisao,MostraSubDivisao)