from rest_framework import serializers
from .models import Cliente

class ClienterSerialize(serializers.ModelSerializer):
    class Meta:
        model =Cliente
        fields =('id','nome','endereço','idade')


    def validar_endereço(self, value):
        qs=Cliente.objects.filter(endereço__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("O Endereço deve ser unico ")
        return value