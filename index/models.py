from django.db import models

# Create your models here.


class Pessoa_usuario(models.Model):
    pessoa_cpf = models.ForeignKey("index.Pessoa", on_delete=models.CASCADE)
    login_usuario = models.TextField()
    senha_usuario = models.TextField()

    def __str__(self):
        return f'Usuário(Pessoa)'


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome


class Padaria_usuario(models.Model):
    padaria_id = models.ForeignKey("index.Padaria", on_delete=models.CASCADE)
    login_padaria = models.TextField()
    senha_padaria = models.TextField()

    def __str__(self):
        return f'Usuário(Padaria)'


class Padaria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tempo_preparo = models.IntegerField()

    def __str__(self):
        return f'Produto: {self.nome} \n Tempo de preparo: {self.tempo_preparo}'


class Fornada(models.Model):
    produto_id = models.ForeignKey("index.Produto", on_delete=models.CASCADE)
    padaria_id = models.ForeignKey("index.Padaria", on_delete=models.CASCADE)
    horario_previsto = models.DateTimeField()

    def __str__(self):
        return f'Fornada de {self.produto_id.nome} às {self.horario_previsto}'


class Notificacao(models.Model):
    usuario_id = models.ForeignKey("index.Pessoa_usuario", on_delete=models.CASCADE)
    fornada_id = models.ForeignKey("index.Fornada", on_delete=models.CASCADE)
    msg = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notificação para {self.usuario_id.login_usuario} sobre a fornada {self.fornada_id.id}'


class Inscricao_usuario_padaria(models.Model):
    usuario_id = models.ForeignKey("index.Pessoa_usuario", on_delete=models.CASCADE)
    padaria_id = models.ForeignKey("index.Padaria_usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario_id.nome} inscrito em {self.padaria_id.nome}'


class Padaria_produtos(models.Model):
    padaria_id = models.ForeignKey("index.Padaria_usuario", on_delete=models.CASCADE)
    produto_id = models.ForeignKey("index.Produto", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.padaria_id.nome}({self.padaria_id.id}) - {self.produto_id.nome}({self.produto_id.id})'
