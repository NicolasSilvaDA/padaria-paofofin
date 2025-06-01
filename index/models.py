from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    login_usuario = models.TextField()
    senha_usuario = models.TextField()

class Padaria(models.Model):
    nome = models.CharField(max_length=255)
    login_padaria = models.TextField()
    senha_padaria = models.TextField()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tempo_preparo = models.IntegerField()

class Inscricao_usuario_padaria(models.Model):
    usuario_id = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    padaria_id = models.ForeignKey("Padaria", on_delete=models.CASCADE)

class Padaria_produtos(models.Model):
    padaria_id = models.ForeignKey("Padaria", on_delete=models.CASCADE)
    produto_id = models.ForeignKey("Produto", on_delete=models.CASCADE)