from django.db import models
from django.forms import CharField

class Local(models.Model):
    nome_do_espaco = models.CharField(max_length=200)
    tamanho_do_espaco = models.CharField(max_length=100)
    filial = models.CharField(max_length=100, default='CEFAT')
    codigo_do_Local = models.CharField(max_length=50)
    descrição_do_Local = models.TextField(default='')
    situação = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.nome_do_espaco
