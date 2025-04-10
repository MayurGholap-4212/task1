from django.db import models

# Create your models here.
from django.db import models

from django.db import models

# Create your models here.

class Roll(models.Model):
    usertype = models.CharField(max_length=100,default=True)

    def str(self):
        return self.usertype

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField()
    roll = models.ManyToManyField(Roll)


    def str(self):
        return self.name