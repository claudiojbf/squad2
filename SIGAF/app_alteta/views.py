from django.shortcuts import render,get_object_or_404
from .util import valida_campo_vazio
from django.contrib import messages
from .models import Atletas, SubDivisao, Posicao

