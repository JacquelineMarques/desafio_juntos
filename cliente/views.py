from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from cliente.models import cliente
from cliente.serializer import clienteSerializer

class clienteviewset(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer
