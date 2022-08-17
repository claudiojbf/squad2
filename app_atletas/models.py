from distutils.command.upload import upload
from select import select
from django.db import models


# Create your models here.
class Atletas(models.Model):
    nome = models.CharField(max_length=100)
    
    apelido = models.CharField(max_length=40)
    possicao = models.CharField(max_length=20)
    data_nacimento = models.DateField()
    idade = models.IntegerField()
    rg = models.CharField(max_length=20,unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    
    perna_dominante = models.CharField(max_length=20)
    matricula_escolar = models.CharField(max_length=100)
    serie = models.CharField(max_length=20)
    naturalidade_uf = models.CharField(max_length=3)
    cidade = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    endereco = models.CharField(max_length=40)
    numero_casa = models.CharField(max_length=40)
    cep =models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    whatsapp2 = models.CharField(max_length=15)
    nome_pai =models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    telefone_responsavel = models.CharField(max_length=15)
    telefone_responsavel2 = models.CharField(max_length=15)
    altura = models.IntegerField()
    peso = models.IntegerField()
    plano_saude = models.CharField(max_length=100, default='')
    alergia = models.CharField(max_length=200, default='')
    
    imagem = models.ImageField(upload_to = 'foto',blank = True)
    def __str__(self):
        return self.nome

