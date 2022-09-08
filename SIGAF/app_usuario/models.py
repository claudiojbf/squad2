from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    sigla = models.CharField(max_length=3)
    nome_tipo = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome_tipo

class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    data_n = models.DateField()
    tipo_u = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to = 'foto_usuarios', blank = True)