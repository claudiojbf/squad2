from email.policy import default
from unittest.mock import DEFAULT
from django.db import models
from app_facilitis.models.local import Local

class NivelDeOcorrencia(models.Model):
    sigla = models.CharField(max_length=1)
    descricao = models.CharField(max_length=30)

class Ocorrencia(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    detalhes_ocorrencia = models.TextField()
    descricao_ocorrido = models.TextField()
    nivel_urgencia = models.ForeignKey(NivelDeOcorrencia, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=False, blank=False)
    fase = models.CharField(max_length=2, default = "P")

    