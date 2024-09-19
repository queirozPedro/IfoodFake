from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileExample(models.Model):

    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class DiretorProfile(models.Model):

    sala = models.IntegerField()
    departamento = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"