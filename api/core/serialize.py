from rest_framework import serializers
#from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handle
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Usuario
from .models import Aluno
from .models import Noticias
from .models import Cursos
from .models import Extras







class UsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model =Usuario
        fields =('id','nome','endereço','idade','email','password','username','cpf','perfil','datetime')
        
        def create(self,validate_data):
            password=validate_data.pop('password', None)
            instance =self.Meta.model(**validate_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

class AlunoSerialize(serializers.ModelSerializer):
    class Meta:
        model =Aluno
        fields =('id','nome','endereço','idade','email','password','username','cpf','datetime')
        
        def create(self,validate_data):
            password=validate_data.pop('password', None)
            instance =self.Meta.model(**validate_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
    
class NoticiasSerialize(serializers.ModelSerializer):
    class Meta:
        model=Noticias
        fields=('titulo','descricao','imagem','datetime','postador')

        



class CursosSerialize(serializers.ModelSerializer):
    class Meta:
        model =Cursos
        fields=('nome','descricao','imagem','datetime')


class ExtraSerialize(serializers.ModelSerializer):
    class Meta:
        model =Extras
        fields = ('titulo','descricao','imagem','conteudo','datetime','postador')
        

        #def validar_endereço(self, value):
        #qs=Cliente.objects.filter(endereço__iexact=value)
        #if qs.exists():
         #   raise serializers.ValidationError("O Endereço deve ser unico ")
        #return value """