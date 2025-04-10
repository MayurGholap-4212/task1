from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,Roll
from . seriallizers import StudentSeriallizers,RollSeriallizers

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSeriallizers

class Rollviewset(viewsets.ModelViewSet):
    queryset=Roll.objects.all()
    serializer_class=RollSeriallizers