from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, verbose_name="Nome Completo")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
    def __str__(self):
        return self.name

class Grabber(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Grabber")
    grab = models.JSONField(default=dict, verbose_name="Dados do Grab")

    class Meta:
        verbose_name = "Grabber"
        verbose_name_plural = "Grabbers"

    def __str__(self):
        return self.name