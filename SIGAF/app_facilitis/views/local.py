from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from app_facilitis.models.local import Local

def mostra_local(request):
    local = Local.objects.all()
    dado = {
        'locais': local
    }
    return render(request, 'facilitis/local/mostra_local.html', dado)


"""CRUD LOCAL"""
def cadastro(request):
    if request.method== 'POST':
        nome_do_espaco = request.POST['nome']
        tamanho_do_espaco = request.POST['tamanho_do_espaco']
        filial = request.POST['Filial']
        codigo_do_local = request.POST['Código_do_Local']
        descrição_do_local = request.POST['Descrição_do_Local']
        situaçao = request.POST['Situação']

        local = Local.objects.create(nome_do_espaco = nome_do_espaco,tamanho_do_espaco = tamanho_do_espaco,
        filial = filial, codigo_do_Local = codigo_do_local, descrição_do_Local = descrição_do_local, situação = situaçao)

        local.save()
        return render(request,'facilitis/local/cadastro_de_locais.html')
    return render(request,'facilitis/local/cadastro_de_locais.html')

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