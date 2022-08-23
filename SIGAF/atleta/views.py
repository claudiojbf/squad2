import email
from hashlib import md5
import hashlib
from django import views
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from .models import Funcionario, Tipofuncionario



# Create your views here.
from atletas.models import Atletas
def cadastroFuncionario(request):
    profissoes = Tipofuncionario.objects.order_by('id')
    dados = {
        'profissoes':profissoes
    }
    if request.method == 'POST':
        nome = request.POST ['nome']
        
        telefone = request.POST ['telefone']
        matricula = request.POST ['matricula']

        email = request.POST ['email']
        profissao = request.POST['profissao']
        senha = request.POST ['senha']
        senha2 = request.POST['senha2']
        cpf = request.POST ['CPF']
        cpf_criptografado = hashlib.md5(cpf.encode('utf-8')).hexdigest()
        print(cpf_criptografado)
        # b =1 
        # a = make_password(b)
        # print(a)
        # print(dados)
        if not nome.strip() or not cpf.strip() or not matricula.strip() or not senha.strip() or not telefone.strip():
            print('nome em branco')
            return redirect('cadastroFuncionario')
        if senha != senha2:
            print('senha esta diferente de confirmação de senha')
            return redirect('cadastroFuncionario')
            
        if Funcionario.objects.filter(email=email).exists():
            return redirect('cadastroFuncionario')
        if Funcionario.objects.filter(matricula=matricula).exists():
            return redirect('cadastroFuncionario')
        if Funcionario.objects.filter(cpf=cpf).exists():
            return redirect('cadastroFuncionario')
        profisional = get_object_or_404(Tipofuncionario, nome = profissao)
        
        user = Funcionario.objects.create(tipo_de_usuario = profisional ,nome = nome, email=email,telefone=telefone, matricula=matricula, cpf=cpf_criptografado, senha=senha)
        user.save()
        # form = ClienteForm(request.POST)
        # if not form.is_valid():
        #     return render(request, 'funcionarios/cliente_form.html', {'form': form})

        # c = form.save(commit=False)
        # c.senha = make_password(c.senha)
        # c.save()
        # return HttpResponseRedirect('/')
        return redirect('index')

    return render(request, 'cadastroFuncionario.html', dados) 
def index(request):
    atleta = Atletas.objects.all()
    funcionarios = Funcionario.objects.all()
    dados = {
        'funcionarios':funcionarios,
        'atletas':atleta
    }
    return render(request, 'index.html', dados)

def atleta(request, atleta_id):
    atleta = get_list_or_404(Atletas, pk=atleta_id)
    dados = {
        'atleta':atleta
    }
    return render(request, 'atleta.html',dados)

def apagar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk = funcionario_id)
    funcionario.delete()
    return redirect('index')
def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk = funcionario_id)
    profissoes = Tipofuncionario.objects.order_by('id')
    funcionario_a_editar = {
        'funcionario':funcionario,
        'profissoes':profissoes
    }
    return render(request, 'editar_funcionario.html', funcionario_a_editar)

def atualiza_funcionario(request):
    if request.method == 'POST':
        funcionario_id = request.POST['id']
        funcionario = get_object_or_404(Funcionario, pk = funcionario_id)

        funcionario.nome = request.POST['nome']
        funcionario.matricula = request.POST['matricula']
        funcionario.cpf = request.POST['cpf']
        funcionario.email = request.POST['email']
        funcionario.telefone = request.POST['telefone']
        funcionario.tipo_de_usuario = request.POST['profissao']
        funcionario.save()
        return redirect('index')