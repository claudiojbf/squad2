from django.shortcuts import render, get_object_or_404, redirect
from app_facilitis.models.local import Local
from app_facilitis.models.ocorencias import Ocorrencia,NivelDeOcorrencia
from app_usuario.models import Usuario

def listar_ocorrencias(request):

    ocorrencias = Ocorrencia.objects.all()

    dados = {
        'ocorrencias': ocorrencias
    }
    return render(request, 'facilitis/ocorrencia/lista_de_ocorrencias.html', dados)

def mostra_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
        
    dados_ocorrencia = {
            'ocorrencia': ocorrencia
        }
    return render (request, 'facilitis/ocorrencia/mostra_ocorrencia.html', dados_ocorrencia)

#CRUD OCORRENCIAS
def registrar_ocorrencia(request):
    usuario = request.user.id
    usuario2 = Usuario.objects.get(usuario_id = usuario)
    local_ocorrencia = Local.objects.all()
    
    dados_local_exibir = {
        'usuario' : usuario2,
        'local_ocorrencia': local_ocorrencia,
    }
    if request.method == 'POST':

        #local = request.POST['sala']
        local_id = request.POST.get('local')
        local = Local.objects.get(id=local_id)
        detalhes_ocorrencia = request.POST.get('detalhes_ocorrencia')
        email = request.POST.get('email')
        descricao_ocorrido = request.POST.get('descricao_ocorrido')
        nivel_urgencia = request.POST.get('nivel')
        nivel_u_i = get_object_or_404(NivelDeOcorrencia, sigla = nivel_urgencia)

        ocorrencia = Ocorrencia.objects.create(local = local, 
        detalhes_ocorrencia = detalhes_ocorrencia, email=email, descricao_ocorrido = descricao_ocorrido, 
        nivel_urgencia=nivel_u_i)

        ocorrencia.save()

        return redirect('listar_ocorrencias')
    return render(request, 'facilitis/ocorrencia/form_ocorrencia.html', dados_local_exibir)

def deleta_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    ocorrencia.delete()

    return redirect('listar_ocorrencias')

def edita_ocorrencia(request, ocorrencia_id):

    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    dados_  = {
    'ocorrencia': ocorrencia
    }
    return render  (request, 'facilitis/ocorrencia/edita_ocorrencia.html', dados_)

def atualiza_ocorrencia (request):
    if request.method == 'POST':
        ocorrencia_id  = request.POST.get('ocorrencia_id')
        ocorrencia = Ocorrencia.objects.get(id=ocorrencia_id)
        ocorrencia.detalhes_ocorrencia = request.POST.get('detalhes_ocorrencia')
        ocorrencia.email = request.POST.get('email')
        ocorrencia.descricao_ocorrido = request.POST.get('descricao_ocorrido')
        nivel = request.POST.get('nivel')
        print(nivel)
        ocorrencia.nivel_urgencia = get_object_or_404(NivelDeOcorrencia, sigla = nivel)
        
        ocorrencia.save()

        return redirect ('listar_ocorrencias')