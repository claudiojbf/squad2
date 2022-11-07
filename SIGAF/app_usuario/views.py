from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, TipoUsuario
from django.contrib import auth
from django.contrib.auth.models import User
from .util import validar_campo_senha, validar_campo_vazio, validar_nome_de_usuario, validar_email, validar_tipo_usuario
from django.contrib import messages
from app_atleta.models import Atletas
from django.contrib.auth.decorators import login_required
from app_facilitis.models.ocorencias import Ocorrencia

def login(request):
    """Campo para autenticar o usuario"""
    if request.method == 'POST':
        user_n = request.POST.get('user_n')
        senha = request.POST.get('senha')
        if User.objects.filter(username = user_n).exists():
            user = auth.authenticate(request, username = user_n, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Senha invalida!!!")
        else:
            messages.error(request, "Email invalido!!!")
    return render(request, 'usuario/login.html')

@login_required(login_url='login')
def cadastro(request):
    """Campo para cadastrar um novo usuario"""
    tipos_usuarios = TipoUsuario.objects.all()
    usuario = request.user.id
    usuario2 = Usuario.objects.get(usuario_id = usuario)

    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        data_n = request.POST['data_n']
        data = datetime.strptime(data_n, '%Y-%m-%d').date()
        nome_u = request.POST['user_name']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        tipo_u = request.POST['tipo_u']
        tipo_f = get_object_or_404(TipoUsuario, pk=tipo_u)
        foto = request.FILES['foto_usuario']
        campos = [nome,nome_u,senha,senha2]
        for campo in campos:
            if validar_campo_vazio(campo):
                messages.error(request, "Preencha todos os campos corretamente")
                return redirect('cadastro')
            elif validar_nome_de_usuario(nome_u):
                messages.error(request, "Login já existente")
                return redirect('cadastro')
            elif validar_email(email):
                messages.error(request, "Email já cadastrado")
                return redirect('cadastro')
            elif validar_campo_senha(senha, senha2):
                messages.error(request, "Confirmação de Senha não batem")
                return redirect('cadastro')
            elif validar_tipo_usuario(tipo_u):
                messages.error(request, "Selecione o seu nivel de usuario")
                return redirect('cadastro')
            else:
                user = User.objects.create_user(username = nome_u, email = email, first_name = nome, password = senha)
                user.save()
                user_id = User.objects.get(email = email)
                user_i = get_object_or_404(User, pk = user_id.id)
                adicional = Usuario.objects.create(usuario = user_i, telefone = telefone, data_n = data, tipo_u = tipo_f, imagem = foto)
                adicional.save()
                return redirect('login')
    dados = {
        "tipos_usuarios" : tipos_usuarios,
        "usuario" :usuario2
    }
    return render(request, 'usuario/cadastro-de-usuario.html', dados)

@login_required(login_url='login')
def index(request):
    """campo para redirecionar um usuario para a tela principal"""
    atletas = Atletas.objects.all()
    usuario = request.user.id
    usuario2 = Usuario.objects.get(usuario_id = usuario)
    dados = {
        "usuario":usuario2,
        "atletas":atletas
    }
    if usuario2.tipo_u.sigla == "GES":
        return render(request, "gestor/index.html", dados)
    elif usuario2.tipo_u.sigla == "FAC":
        ocorrencias = Ocorrencia.objects.all()
        ocorrencia_p = Ocorrencia.objects.filter(fase = "P").count()
        ocorrencia_ep = Ocorrencia.objects.filter(fase = "EP").count()
        ocorrencia_r = Ocorrencia.objects.filter(fase = "R").count()
        dados["ocorrencias"] = ocorrencias
        dados["op"] = ocorrencia_p
        dados["ep"] = ocorrencia_ep
        dados["r"] = ocorrencia_r
        return render(request, "facilitis/ocorrencia/ocorrencia.html",dados)
    elif usuario2.tipo_u.sigla == "PRF":
        return render(request, "proficional/index.html", dados)

def logout(request):
    """Campo para desconectar um usuario"""
    auth.logout(request)
    return redirect('login')

def perfil(request):
    usuario = request.user.id
    user = get_object_or_404(User, pk = usuario)
    user_t = get_object_or_404(Usuario, usuario = user)
    dados = {
        "usuario" : user_t
    }
    return render(request, 'usuario/perfil.html', dados)
