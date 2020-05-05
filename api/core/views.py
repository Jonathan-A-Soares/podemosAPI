from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Usuario
from .models import Aluno
from .models import Noticias
from .models import Cursos
from .models import Extras
from .serialize import UsuarioSerialize
from .serialize import AlunoSerialize
from .serialize import NoticiasSerialize
from .serialize import CursosSerialize
from .serialize import ExtraSerialize
import requests


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerialize

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









