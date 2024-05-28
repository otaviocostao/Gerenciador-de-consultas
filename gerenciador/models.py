from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100,null=False, blank=False)

    endereco = models.CharField(max_length=100)

    prioridade = models.CharField(max_length=5, null=False, blank=False)

    cpf = models.CharField(max_length=15, null=False, blank=False)

    rg = models.CharField(max_length=15)

    telefone = models.CharField(max_length=20, null=False, blank=False)

    email = models.CharField(max_length=100)