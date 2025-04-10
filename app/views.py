from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from . seriallizers import StudentSeriallizers

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSeriallizers
