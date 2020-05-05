from django.db import models
from datetime import datetime




class Aluno(models.Model):
    nome =models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True)
    cpf = models.CharField(max_length=25, unique=True)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    postador = models.CharField(max_length=200)

class Extras(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    postador = models.CharField(max_length=60)
    tema = models.CharField(max_length=30)

class Cursos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    professor = models.CharField(max_length=60)
    alunos = models.ManyToManyField(Aluno)
    tema = models.CharField(max_length=30)