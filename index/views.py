from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpRequest
from .models import (
    Padaria_usuario, 
    Pessoa_usuario, 
    Inscricao_usuario_padaria, 
    Fornada, Produto, 
    Notificacao,
)

# Create your views here.


def index_view(request):
    return render(
        request,
        'index/index.html',
    )


def padarias_view(request):
    padarias = Padaria_usuario.objects.all()
    return render(
        request,
        'index/padarias.html',
        {'padarias': padarias},
    )


def inscrever_padaria(request, padaria_id):
    usuario = Pessoa_usuario.objects.first()
    padaria = get_object_or_404(Padaria_usuario, id=padaria_id)

    Inscricao_usuario_padaria.objects.get_or_create(
        usuario_id=usuario, 
        padaria_id=padaria,
    )

    return redirect('padarias')


def fornadas_view(request):
    fornadas = Fornada.objects.all().order_by('horario_previsto')

    return render(
        request,
        'index/fornadas.html',
        {'fornadas': fornadas},
    )


def cadastrar_fornada(request):
    if request.method == 'POST':
        padaria_id = request.POST['padaria_id']
        produto_id = request.POST['produto_id']
        quantidade = request.POST['quantidade']

        padaria_usuario = Padaria_usuario.objects.get(id=padaria_id)
        produto = Produto.objects.get(id=produto_id)

        horario_inicial = datetime.now()
        
        horario_previsto = horario_inicial + timedelta(minutes=produto.tempo_preparo)

        fornada = Fornada.objects.create(
            padaria=padaria_usuario,
            produto=produto,
            horario_previsto=horario_previsto,
            quantidade=quantidade,
        )

        notif_inscritos = Inscricao_usuario_padaria.objects.filter(padaria_id=padaria_usuario)

        msg = f'Nova fornada de {produto.nome} estará pronta às {horario_previsto.strftime("%H:%M")} na padaria {padaria_usuario.padaria.nome}'

        for inscrito in notif_inscritos:
            Notificacao.objects.create(
                pessoa_usuario=inscrito.pessoa_usuario,
                fornada=fornada,
                msg=msg
            )

        return redirect('fornadas')
    
    padarias = Padaria_usuario.objects.all()
    produtos = Produto.objects.all()

    return render(
        request,
        'index/cadastrar_fornada.html',
        {
            'padarias': padarias,
            'produtos': produtos,
        }
    )

def notificacoes_view(request):
    pessoa_usuario = Pessoa_usuario.objects.first()

    notificacoes = Notificacao.objects.filter(pessoa_usuario=pessoa_usuario).order_by('-data_envio')
    
    return render(
        request,
        'index/notificacoes.html',
        {'notificacoes': notificacoes}
    )