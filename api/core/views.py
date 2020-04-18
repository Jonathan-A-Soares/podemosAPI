from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno
from .models import Noticias
from .models import Cursos
from .models import Extras
from .serialize import AlunoSerialize
from .serialize import NoticiasSerialize
from .serialize import CursosSerialize
from .serialize import ExtraSerialize

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerialize

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class=NoticiasSerialize

class CursoView(viewsets.ModelViewSet):
    queryset=Cursos.objects.all()
    serializer_class=CursosSerialize

class ExtraView(viewsets.ModelViewSet):
    queryset=Extras.objects.all()
    serializer_class=ExtraSerialize





