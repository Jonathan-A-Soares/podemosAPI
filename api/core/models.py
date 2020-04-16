from django.db import models

class Cliente(models.Model):
    nome =models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome =models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True)
    cpf = models.IntegerField(unique=True)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.nome

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    postador = models.CharField(max_length=200)

class Conteudos(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    postador = models.CharField(max_length=200)