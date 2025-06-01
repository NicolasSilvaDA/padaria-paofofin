from django.db import models

# Create your models here.


class Pessoa_usuario(models.Model):
    pessoa_cpf = models.ForeignKey("index.Pessoa", on_delete=models.CASCADE)
    login_usuario = models.TextField()
    senha_usuario = models.TextField()

class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()

class Padaria_usuario(models.Model):
    padaria_id = models.ForeignKey("index.Padaria", on_delete=models.CASCADE)
    login_padaria = models.TextField()
    senha_padaria = models.TextField()

class Padaria(models.Model):
    nome = models.CharField(max_length=255)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tempo_preparo = models.IntegerField()

class Inscricao_usuario_padaria(models.Model):
    usuario_id = models.ForeignKey("index.Pessoa_usuario", on_delete=models.CASCADE)
    padaria_id = models.ForeignKey("index.Padaria_usuario", on_delete=models.CASCADE)

class Padaria_produtos(models.Model):
    padaria_id = models.ForeignKey("index.Padaria_usuario", on_delete=models.CASCADE)
    produto_id = models.ForeignKey("index.Produto", on_delete=models.CASCADE)