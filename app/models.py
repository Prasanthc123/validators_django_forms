from django.db import models

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    semail=models.EmailField()
    remail=models.EmailField()

