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
