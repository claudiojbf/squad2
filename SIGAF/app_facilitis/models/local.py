from django.db import models


class Local(models.Model):
    nome_do_espaco = models.CharField(max_length=200)
    tamanho_do_espaco = models.CharField(max_length=100)
    filial = models.CharField(max_length=100, default='CEFAT')
    codigo_do_Local = models.CharField(max_length=50)
    descrição_do_Local = models.TextField(default='')
    situação = models.BooleanField()
    tipo_local = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    nome_responsavel = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=11)
    def __str__(self):
        return self.nome_do_espaco