from os import mkdir
from django.shortcuts import redirect, render, get_list_or_404,get_object_or_404
from .models import Atletas

# from videos.models import Video
# Create your views here.
def cadastrodeAtletas(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        apelido = request.POST['apelido']
        possicao = request.POST['possicao']
        data_nacimento = request.POST['data_nacimento']
        idade = request.POST['idade']
        rg = request.POST['rg']
        cpf = request.POST['cpf']
        perna_dominante = request.POST['perna_dominante']
        matricula_escolar = request.POST['matricula_escolar']
        serie = request.POST['serie']
        naturalidade_uf = request.POST['naturalidade_uf']
        cidade = request.POST['cidade']
        endereco = request.POST['endereco']
        numero_casa = request.POST['numero_casa']
        bairro = request.POST['bairro']
        cep = request.POST['cep']
        telefone = request.POST['telefone']
        whatsapp = request.POST['whatsapp']
        whatsapp2 = request.POST['whatsapp2']
        nome_pai = request.POST['nome_pai']
        nome_mae = request.POST['nome_mae']
        telefone_responsavel = request.POST['telefone_responsavel']
        telefone_responsavel2 = request.POST['telefone_responsavel2']
        peso = request.POST['peso']
        altura = request.POST['altura']
        plano_saude = request.POST['plano_saude']
        alergia = request.POST['alergia']
        image = request.FILES['image']

        if Atletas.objects.filter(rg = rg).exists():
            return redirect('cadastrodeAtletas')

        if Atletas.objects.filter(cpf = cpf).exists():
            return redirect('cadastrodeAtletas')
        atleta = Atletas.objects.create(nome = nome, apelido=apelido, possicao=possicao,data_nacimento=data_nacimento,idade=idade,
        rg=rg,cpf=cpf, perna_dominante=perna_dominante,matricula_escolar=matricula_escolar, serie=serie,naturalidade_uf=naturalidade_uf,
        cidade=cidade,bairro=bairro,cep=cep,endereco=endereco, numero_casa=numero_casa,telefone=telefone,whatsapp=whatsapp,whatsapp2=whatsapp2,nome_pai=nome_pai,nome_mae=nome_mae,
        telefone_responsavel=telefone_responsavel,telefone_responsavel2=telefone_responsavel2,peso=peso,altura=altura,plano_saude=plano_saude,
        alergia=alergia, imagem=image)
        atleta.save()
        return redirect('video')
    return render(request, 'cadastro-atletas.html')

def atleta(request, atleta_id):
    atleta = get_object_or_404(Atletas, pk=atleta_id)
    # if request.method == "POST":
    #     titulos = request.POST['titulo']
    #     video = request.FILES['video']
    #     videoss = Video.objects.create(titulo=titulos,video=video,atleta=atleta, atleta_nome = atleta.nome)
    #     videoss.save()
    # videos = Video.objects.all().filter(atleta = atleta)
    dados = {
        # 'videos':videos,
        'atletas':atleta
    }
    return render(request, 'atleta.html', dados)

# def video(request):
#     videos = Video.objects.all()
#     video = {
#         'videos':videos
#     }

#     return render(request, "video.html", video)

def apagar_atleta(request, atleta_id):
    atleta = get_object_or_404(Atletas, pk=atleta_id)
    atleta.delete()
    return redirect('index')

def editar_atleta(request, atleta_id):
    atleta = get_object_or_404(Atletas, pk=atleta_id)
    atleta_a_editar = {'atleta':atleta}
    return render(request, 'edita_atleta.html', atleta_a_editar)

def atualiza_atleta(request):
    if request.method == 'POST':
        atleta_id = request.POST['atleta_id']
        atleta = Atletas.objects.get(pk=atleta_id)
        if request.POST['cpf'] != atleta.cpf:
            if Atletas.objects.filter(cpf = request.POST['cpf']).exists():
                return redirect(f'editar_atleta/{atleta_id}')
        if request.POST['rg'] != atleta.rg:
            if Atletas.objects.filter(rg = request.POST['rg']).exists():
                return redirect(f'editar_atleta/{atleta_id}')
        atleta.nome = request.POST['nome']
        atleta.apelido = request.POST['apelido']
        atleta.possicao = request.POST['possicao']
        atleta.data_nacimento = request.POST['data_nacimento']
        atleta.idade = request.POST['idade']
        atleta.rg = request.POST['rg']
        atleta.cpf = request.POST['cpf']
        atleta.perna_dominante = request.POST['perna_dominante']
        atleta.matricula_escolar = request.POST['matricula_escolar']
        atleta.serie = request.POST['serie']
        atleta.naturalidade_uf = request.POST['naturalidade_uf']
        atleta.cidade = request.POST['cidade']
        atleta.endereco = request.POST['endereco']
        atleta.numero_casa = request.POST['numero_casa']
        atleta.bairro = request.POST['bairro']
        atleta.cep = request.POST['cep']
        atleta.telefone = request.POST['telefone']
        atleta.whatsapp = request.POST['whatsapp']
        atleta.whatsapp2 = request.POST['whatsapp2']
        atleta.nome_pai = request.POST['nome_pai']
        atleta.nome_mae = request.POST['nome_mae']
        atleta.telefone_responsavel = request.POST['telefone_responsavel']
        atleta.telefone_responsavel2 = request.POST['telefone_responsavel2']
        atleta.peso = request.POST['peso']
        atleta.altura = request.POST['altura']
        atleta.plano_saude = request.POST['plano_saude']
        atleta.alergia = request.POST['alergia']
        if 'image' in request.FILES:
            atleta.image = request.FILES['image']
        atleta.save()
        return redirect('index')