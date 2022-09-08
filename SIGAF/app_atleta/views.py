from django.shortcuts import render,get_object_or_404,redirect
from .util import valida_campo_vazio
from django.contrib import messages
from .models import Atletas, SubDivisao, Posicao, Video

def cadastrodeAtletas(request):
    subdivisao_atleta = SubDivisao.objects.all()
    posicoes = Posicao.objects.all()
    dados = {
        'subdivisoes':subdivisao_atleta,
        'posicoes':posicoes
    }
    if request.method == 'POST':
    
        sub = get_object_or_404(SubDivisao, pk = request.POST['subdivisao'])
        nome = request.POST['nome']
        apelido = request.POST['apelido']

        posicao = get_object_or_404(Posicao, pk=request.POST['posicao'])
        data_nacimento = request.POST['data_nacimento']
        idade = request.POST['idade']
        rg = request.POST['rg']
        cpf = request.POST['cpf']
        perna_dominante = request.POST['perna_dominante']
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
        image = request.FILES['image']
       

        # validações para informações sobre alergia
        if 'semalergia' in request.POST:
            alergia = 'nulo'
        if 'alergia' in request.POST:
            alergia = request.POST['alergia'].lstrip()
            if valida_campo_vazio(alergia):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo alergia. marque Não tenho alergia para caso ele não exista')
                return redirect('cadastrodeAtletas')

        # validações para informações sobre o plamo de saude
        if 'semPlanoSaude' in request.POST:
            plano_saude = 'nulo'
        
        if 'plano_saude' in request.POST:
            plano_saude = request.POST['plano_saude'].lstrip()
            if valida_campo_vazio(plano_saude):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo plano de saude. marque Não tenho plano de saúde para caso ele não existir')
                return redirect('cadastrodeAtletas')
        
        # validações para informações sobre escolaridade
        if 'sem_escolaridade' in request.POST:
            matricula_escolar = 'nulo'
            serie = 'nulo'
            nivel_escolar='nulo'
            
        if 'matricula_escolar' and 'serie' and 'nivel_escolar' in request.POST:
            matricula_escolar = request.POST['matricula_escolar'].lstrip()
            serie = request.POST['serie'].lstrip()
            nivel_escolar =  request.POST['nivel_escolar']
            campos = [request.POST['matricula_escolar'], request.POST['serie']]
            nomes = ['matricula escolar','serie' ]
            iterador = -1
            for campo in campos:
                iterador = iterador+1
                if valida_campo_vazio(campo):
                    messages.error(request, f'O caractere espaço não e considerado no começo do campo {nomes[iterador]} ou marque sem escolaridade')
                    return redirect('cadastrodeAtletas')

        # validações para indentificadores (rg, cpf)
        if Atletas.objects.filter(rg = rg).exists():
            messages.error(request, 'Um atleta com esse RG já foi cadastrado')
            return redirect('cadastrodeAtletas')

        if Atletas.objects.filter(cpf = cpf).exists():
            messages.error(request, 'Um atleta com esse CPF já foi cadastrado')
            return redirect('cadastrodeAtletas')

        campos = [request.POST['nome'], request.POST['apelido'], request.POST['naturalidade_uf'], request.POST['cidade'], 
        request.POST['endereco'],request.POST['cpf'], request.POST['cep'],request.POST['nome_pai'],request.POST['nome_mae'],
        request.POST['bairro'],]
        nomes = ['nome', 'apelido', 'naturalidade','cidade','endereco','CPF', 'CEP','nome do pai','nome da mãe','bairro' ]
        iterador = -1
        for campo in campos:
            iterador = iterador+1
            if valida_campo_vazio(campo):
                messages.error(request, f'preencha os campos coretamente, o caractere espaço não e considerado no começo do campo {nomes[iterador]}')
                return redirect('cadastrodeAtletas')


        atleta = Atletas.objects.create(nome = nome, apelido=apelido, posicao=posicao,data_nacimento=data_nacimento,idade=idade,
        rg=rg,cpf=cpf, perna_dominante=perna_dominante,matricula_escolar=matricula_escolar,nivel_escolar=nivel_escolar, serie=serie,naturalidade_uf=naturalidade_uf,
        cidade=cidade,bairro=bairro,cep=cep,endereco=endereco, numero_casa=numero_casa,telefone=telefone,whatsapp=whatsapp,whatsapp2=whatsapp2,nome_pai=nome_pai,nome_mae=nome_mae,
        telefone_responsavel=telefone_responsavel,telefone_responsavel2=telefone_responsavel2,peso=peso,altura=altura,plano_saude=plano_saude,
        alergia=alergia,subDivisao=sub, imagem=image)


        atleta.save()
        return redirect('index')
    return render(request, 'atletas/cadastro-atletas.html',dados)

# def atleta(request, atleta_id):
#     atleta = get_object_or_404(Atletas, pk=atleta_id)
#     if request.method == "POST":
#         titulos = request.POST['titulo']
#         video = request.FILES['video']
#         videoss = Video.objects.create(titulo=titulos,video=video,atleta=atleta)
#         videoss.save()
#     videos = Video.objects.all().filter(atleta = atleta)
#     dados = {
#         'videos':videos,
#         'atletas':atleta
#     }
#     return render(request, 'atleta.html', dados)

# def video(request):
#     videos = Video.objects.all()
#     video = {
#         'videos':videos
#     }

    # return render(request, "video.html", video)

def apagar_atleta(request, atleta_id):
    atleta = get_object_or_404(Atletas, pk=atleta_id)
    atleta.delete()
    return redirect('index')

def editar_atleta(request, atleta_id):
    subdivisao_atleta = SubDivisao.objects.all()
    posicoes = Posicao.objects.all()

    
    atleta = get_object_or_404(Atletas, pk=atleta_id)
    atleta_a_editar = {
        'atleta':atleta,
        'subdivisoes':subdivisao_atleta,
        'posicoes':posicoes
        }
    return render(request, 'atletas/edita-atletas.html', atleta_a_editar)

def atualiza_atleta(request):
    #nivel escola falta!!
    
    if request.method == 'POST':
        atleta_id = request.POST['atleta_id']
        atleta = Atletas.objects.get(pk=atleta_id)

        # validações para indentificadores (rg, cpf)
        if request.POST['cpf'] != atleta.cpf:
            if Atletas.objects.filter(cpf = request.POST['cpf']).exists():
                messages.error(request, 'Um usuario com esse CPF ja foi cadastrado')
                return redirect(f'editar_atleta/{atleta_id}')
        if request.POST['rg'] != atleta.rg:
            if Atletas.objects.filter(rg = request.POST['rg']).exists():
                messages.error(request, 'Um usuario com esse RG ja foi cadastrado')
                return redirect(f'editar_atleta/{atleta_id}')
              
        # validações para informações sobre alergia
        if 'semalergia' in request.POST:
            atleta.alergia = 'nulo'
        if 'alergia' in request.POST:
            atleta.alergia = request.POST['alergia'].lstrip()
            if valida_campo_vazio(request.POST['alergia']):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo alergia. marque Não tenho alergia para caso ele não exista')
                return redirect('cadastrodeAtletas')

        # validações para informações sobre o plamo de saude
        if 'semPlanoSaude' in request.POST:
            atleta.plano_saude = 'nulo'
        
        if 'plano_saude' in request.POST:
            atleta.plano_saude = request.POST['plano_saude'].lstrip()
            if valida_campo_vazio(request.POST['plano_saude']):
                messages.error(request, 'O caractere espaço não e considerado no começo do campo plano de saude. marque Não tenho plano de saúde para caso ele não existir')
                return redirect('cadastrodeAtletas')
        
        # validações para informações sobre escolaridade
        if 'sem_escolaridade' in request.POST:
            atleta.matricula_escolar = 'nulo'
            atleta.serie = 'nulo'
            atleta.nivel_escolar='nulo'
            
        if 'matricula_escolar' and 'serie' and 'nivel_escolar' in request.POST:
            atleta.matricula_escolar = request.POST['matricula_escolar'].lstrip()
            atleta.serie = request.POST['serie'].lstrip()
            atleta.nivel_escolar =  request.POST['nivel_escolar']
            campos =[request.POST['matricula_escolar'],request.POST['serie']]
            nomes = ['matricula escolar','serie' ]
            iterador = -1
            for campo in campos:
                iterador = iterador+1
                if valida_campo_vazio(campo):
                    messages.error(request, f'O caractere espaço não e considerado no começo do campo {nomes[iterador]}.Marque sem escolaridade caso ela não exista')
                    return redirect('cadastrodeAtletas')

        atleta.nome = request.POST['nome']
        atleta.apelido = request.POST['apelido']
        atleta.data_nacimento = request.POST['data_nacimento']
        atleta.idade = request.POST['idade']
        atleta.rg = request.POST['rg']
        atleta.cpf = request.POST['cpf']
        atleta.perna_dominante = request.POST['perna_dominante']
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
        sub = get_object_or_404(SubDivisao, pk = request.POST['subdivisao'])
        posicao = get_object_or_404(Posicao, pk=request.POST['posicao'])
        atleta.subDivisao = sub
        atleta.posicao = posicao
        if 'image' in request.FILES:
            atleta.image = request.FILES['image']

        campos = [atleta.nome, atleta.apelido, atleta.naturalidade_uf, atleta.cidade, 
        atleta.endereco,atleta.cpf, atleta.cep,atleta.nome_pai,atleta.nome_mae,atleta.bairro,atleta.serie,atleta.matricula_escolar ]
        nomes = ['nome', 'apelido', 'naturalidade','cidade','endereco','CPF', 'CEP','nome do pai','nome da mãe','bairro','serie', 'matricula_escolar']
        iterador = -1
        for campo in campos:
            iterador = iterador +1
            if valida_campo_vazio(campo):
                messages.error(request, f'preencha os campos coretamente, o caractere espaço não e considerado no começo do campo {nomes[iterador]}.')
                return redirect(f'editar_atleta/{atleta.id}' )
                

        atleta.save()
        return redirect('index')
    
