from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from app_facilitis.models.local import Local
from app_usuario.models import Usuario

def mostra_local(request):
    local = Local.objects.all()
    dado = {
        'locais': local
    }
    return render(request, 'facilitis/local/mostra_local.html', dado)


"""CRUD LOCAL"""
def cadastro(request):
    usuario = request.user.id
    usuario2 = Usuario.objects.get(usuario_id = usuario)
    dados = {
        "usuario":usuario2,
    }
    if request.method== 'POST':
        nome_do_espaco = request.POST['nome_espaco']
        tipo_de_local = request.POST['tipo_local']
        endereco = request.POST['endereco_local']
        filial = request.POST['nome_filial']
        tamanho_do_espaco = request.POST['tamanho_espaco']
        descrição_do_local = request.POST['descricao_local']
        situaçao = request.POST['situacao']
        nome_responsavel = request.POST['nome_responsavel']
        telefone_contato = request.POST['telefone_contato']

        local = Local.objects.create(nome_do_espaco = nome_do_espaco, tipo_local = tipo_de_local, 
        endereco = endereco, tamanho_do_espaco = tamanho_do_espaco, filial = filial, descrição_do_Local = descrição_do_local, 
        situação = situaçao, nome_responsavel = nome_responsavel, telefone_contato = telefone_contato)

        local.save()
        dados = {
            "usuario":usuario2,
        }
        return render(request,'facilitis/local/cadastro_de_local.html', dados)
    return render(request,'facilitis/local/cadastro_de_local.html', dados)

def deleta_local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)
    local.delete()
    return redirect('mostra_local')

def editar_local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)
    editar_cadastro = {
        'locais': local
    }
    return render(request, 'facilitis/local/editar_local.html', editar_cadastro)

def atualiza_local(request):
    if request.method == 'POST':
        local_id = request.POST['id']
        local = Local.objects.get(pk=local_id)
        local.nome_do_espaco = request.POST['nome']
        local.tamanho_do_espaco = request.POST['tamanho_do_espaco']
        local.Filial = request.POST['Filial']
        local.codigo_do_Local = request.POST['codigo_do_Local']
        local.Descrição_do_Local = request.POST['Descrição_do_Local']
        local.situação = request.POST['Situação']
        local.save()
        return redirect('mostra_local')