from django.shortcuts import render
from .models import *
from .Serializers import*
from rest_framework import generics
# Create your views here.


class ServiceList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

class ServiceCreate(generics.CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdate(generics.UpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

class ServiceDelete(generics.DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

# List all clients (GET) and Create a new client (POST)
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Retrieve a single client (GET)
class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'  # Use 'pk' for UUID or primary key lookup

# Update a client (PUT or PATCH)
class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

# Delete a client (DELETE)
class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'
