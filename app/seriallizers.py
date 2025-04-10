from rest_framework import serializers
from . models import Student,Roll

class StudentSeriallizers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class RollSeriallizers(serializers.ModelSerializer):
    class Meta:
        model=Roll
        fields='__all__'