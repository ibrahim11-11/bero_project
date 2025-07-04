from django.shortcuts import render
from rest_framework import viewsets 
from django_filters.rest_framework import DjangoFilterBackend 
from.models import Task 
from.serializer import TaskSerializer 

class Tviewset (viewsets.ModelViewSet):
    queryset =Task.objects.all()
    serializer_class =TaskSerializer 
    filter_backends = [DjangoFilterBackend]
    filter_fields= ['completed']
