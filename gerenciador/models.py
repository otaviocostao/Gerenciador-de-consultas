from django.db import models

# Create your models here.
class Paciente(models.Model):

    ESPECIALIDADE_UM = 'Clinico Geral'
    ESPECIALIDADE_DOIS = 'Oftalmologista'
    ESPECIALIDADE_TRES = 'Dermatologista'

    ESPECIALIDADE_CHOICES = [
        (ESPECIALIDADE_UM, 'Clinico Geral'),
        (ESPECIALIDADE_DOIS, 'Oftalmologista'),
        (ESPECIALIDADE_TRES, 'Dermatologista'),
    ]

    OPTION_SIM = 'Sim'
    OPTION_NAO = 'Não'

    OPTION_CHOICES = [
        (OPTION_SIM, 'Sim'),
        (OPTION_NAO, 'Não'),
    ]

    PAGAMENTO_UM = 'Dinheiro'
    PAGAMENTO_DOIS = 'Cartão de credito'
    PAGAMENTO_TRES = 'Cartão de debito'
    PAGAMENTO_QUATRO = 'Convênio médico'

    PAGAMENTO_CHOICES = [
        (PAGAMENTO_UM, 'Dinheiro'),
        (PAGAMENTO_DOIS, 'Cartão de credito'),
        (PAGAMENTO_TRES, 'Cartão de debito'),
        (PAGAMENTO_QUATRO, 'Convênio médico'),
    ]

    DIA_SEGUNDA = 'Segunda-feira'
    DIA_TERCA = 'Terça-feira'
    DIA_QUARTA = 'Quarta-feira'
    DIA_QUINTA = 'Quinta-feira'
    DIA_SEXTA = 'Sexta-feira'

    DIAS_CHOICES = [
        (DIA_SEGUNDA, 'Segunda-feira'),
        (DIA_TERCA, 'Terça-feira'),
        (DIA_QUARTA, 'Quarta-feira'),
        (DIA_QUINTA, 'Quinta-feira'),
        (DIA_SEXTA, 'Sexta-feira'),
    ]

    nome = models.CharField(max_length=100,null=False, blank=False)

    endereco = models.CharField(max_length=100)

    prioridade = models.CharField(max_length=5, null=False, blank=False, choices=OPTION_CHOICES, default=OPTION_NAO)

    cpf = models.CharField(max_length=15, null=False, blank=False)

    rg = models.CharField(max_length=15)

    telefone = models.CharField(max_length=20, null=False, blank=False)

    email = models.CharField(max_length=100)

    data_nascimento = models.DateField(null=False, blank=False)

    # Dados da consulta:

    especialidade = models.CharField(max_length=50, null=False, blank=False, choices=ESPECIALIDADE_CHOICES, default=ESPECIALIDADE_UM)

    data_consulta = models.CharField(max_length=50, null=False, blank=False, choices=DIAS_CHOICES)

    convenio_medico = models.CharField(max_length=50, null=False, blank=False, choices=OPTION_CHOICES, default=OPTION_NAO)

    forma_pagamento = models.CharField(max_length=50, null=False, blank=False, choices=PAGAMENTO_CHOICES, default=PAGAMENTO_UM)