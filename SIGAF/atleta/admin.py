from django.contrib import admin
from .models import Funcionario
# Register your models here.
class MostraProficional(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    
admin.site.register(Funcionario, MostraProficional)