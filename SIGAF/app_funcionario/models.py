from django.db import models
from datetime import datetime

class Funcao(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome =models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20)
    contato_emergencia = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)

    cpf = models.CharField(max_length=11, unique=True)
    foto_cpf = models.FileField(upload_to = 'funcionario/cpf', blank = True)
    rg = models.CharField(max_length=12, unique=True)
    foto_rg = models.FileField(upload_to = 'funcionario/rg', blank = True)

    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=5)
    horario_de_trabalho = models.DecimalField(max_digits=20, decimal_places=2)
    admitido = models.DateTimeField(default=datetime.now)
    ocorencias = models.CharField(max_length=200,blank=True)
    foto_funcionario = models.FileField(upload_to = 'funcionario/funcionario', blank = True)
    ativo = models.BooleanField(default=True)
    #  daddos bancarios
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=100)
    conta = models.CharField(max_length=100)
    pix = models.CharField(max_length=100)
    

