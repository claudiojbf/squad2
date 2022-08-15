from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    return render(request, 'usuario/login.html')

def cadastro(request):
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
        if senha == senha2:
            user = User.objects.create_user(username = nome_u, email = email, first_name = nome, password = senha)
            user.save()
            user_id = User.objects.get(email = email)
            user_i = get_object_or_404(User, pk = user_id.id)
            adicional = Usuario.objects.create(usuario = user_i, telefone = telefone, data_n = data, tipo_u = tipo_u)
            adicional.save()
            return redirect('login')
    return render(request, 'usuario/cadastro-de-usuario.html')

def index(request):
    usuario = request.user.id
    tipo = Usuario.objects.filter(usuario_id = usuario)
    dados = {
        "tipo":tipo
    }
    return render(request, "index.html", dados)

def logout(request):
    auth.logout(request)
    return redirect('login')