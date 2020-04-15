from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serialize import ClienterSerialize

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienterSerialize





