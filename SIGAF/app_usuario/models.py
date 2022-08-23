from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    data_n = models.DateField()
    tipo_u = models.CharField(max_length=3)
