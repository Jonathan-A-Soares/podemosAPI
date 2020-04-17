from rest_framework import serializers

from .models import Aluno
from .models import Noticias
from .models import Cursos





class AlunoSerialize(serializers.ModelSerializer):
    class Meta:
        model =Aluno
        fields =('id','nome','endereço','idade','email','password','username','cpf','datetime')



class NoticiasSerialize(serializers.ModelSerializer):
    class Meta:
        model=Noticias
        fields=('titulo','descricao','imagem','datetime','postador')



class CursosSerialize(serializers.ModelSerializer):
    class Meta:
        model =Cursos
        fields=('nome','descricao','imagem','datetime')

        #def validar_endereço(self, value):
        #qs=Cliente.objects.filter(endereço__iexact=value)
        #if qs.exists():
         #   raise serializers.ValidationError("O Endereço deve ser unico ")
        #return value """