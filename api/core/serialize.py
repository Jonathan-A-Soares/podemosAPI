from rest_framework import serializers
from .models import Cliente

class ClienterSerialize(serializers.ModelSerializer):
    class Meta:
        model =Cliente
        fields =('id','nome','endereço','idade')