
from django.shortcuts import render,get_object_or_404, redirect
from app_funcionario.models import Funcionario, Funcao
from django.contrib.auth.models import User

from app_funcionario.valida import *
from app_usuario.models import Usuario

def cadastroFuncionario(request):
    usuario = request.user.id
    usuario2 = Usuario.objects.get(usuario_id = usuario)
    funcoes = Funcao.objects.order_by('id')
    dados = {
        'funcoes':funcoes,
        'usuario': usuario2
    }
    if request.method == 'POST':
        nome = request.POST ['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        telefone_emergência = request.POST['telefone_emergência']
        cep = request.POST['cep']
        endereco = request.POST ['endereco']
        cidade = request.POST ['cidade']
        bairro = request.POST ['bairro']
        uf = request.POST['uf']
        horario = request.POST['horario']
        funcao = request.POST['funcao']
        admitido = request.POST ['admitido']
        cpf = request.POST['cpf']
        foto_cpf = request.FILES['image_cpf']
        rg = request.POST['rg']
        foto_rg = request.FILES['foto_rg']
        foto_funcionario = request.FILES['foto_funcionario']
        # dados bancarios

        banco =request.POST['banco']
        conta = request.POST['conta']
        pix=request.POST['pix']
        agencia=request.POST['agencia']
        # include('funcionarios.valida') 
        if valida_tudo(request,rg,telefone,telefone_emergência,cep,nome,email,cpf, pix,conta,agencia,banco) == False:
            return redirect('cadastroFuncionario') 

        funcao_v = get_object_or_404(Funcao, nome = funcao)

        expecialista = Funcionario.objects.create(funcao = funcao_v ,nome=nome,telefone=telefone,uf = uf,cep=cep,cpf=cpf,
        foto_cpf=foto_cpf,rg=rg,foto_rg=foto_rg,endereco=endereco,cidade=cidade,bairro=bairro,horario_de_trabalho=horario,
        admitido=admitido,contato_emergencia=telefone_emergência, email=email, foto_funcionario=foto_funcionario,
        banco= banco, conta=conta,pix=pix,agencia=agencia)
        expecialista.save()
        return redirect('index')

    return render(request, 'funcionarios/cadastro_de_funcionario.html', dados) 

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk = funcionario_id)
    funcoes = Funcao.objects.order_by('id')
    funcionario_a_editar = {
        'funcionario':funcionario,
        'funcoes':funcoes
    }
    return render(request, 'funcionarios/edita_funcionario.html', funcionario_a_editar)

def atualiza_funcionario(request):
    if request.method == 'POST':
        funcionario_id = request.POST['id']
        funcionario = get_object_or_404(Funcionario, pk = funcionario_id)

        funcionario.nome = request.POST['nome']
        funcionario.telefone = request.POST['telefone']
        funcionario.contato_emergencia = request.POST['contato_emergencia']
        funcionario.email = request.POST['email']
        funcionario.cep = request.POST['cep']
        funcionario.cpf = request.POST['cpf']
        funcionario.endereco = request.POST['endereco']
        funcionario.bairro = request.POST['bairro']
        funcionario.cpf = request.POST['cpf']
        funcionario.uf = request.POST['uf']
        funcionario.horario_de_trabalho = request.POST['horario']
        funcao = get_object_or_404(Funcao, nome=request.POST['funcao'])
        # funcionario.admitido = request.POST['admitido']
        funcionario.funcao = funcao
        funcionario.ativo = request.POST['estado_funcionario']
        funcionario.save()
        return redirect('index')
