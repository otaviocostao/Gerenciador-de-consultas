from django.db import models

# NO ARQUIVO MODELS.PY É POSSIVEL CRIAR AS TABELAS DO BANCO SQLITE3
# CADA TABELA DO BANCO DE DADOS É PASSADA NESSE ARQUIVO COMO UMA CLASSE
# BASTA CRIAR AQUI UMA CLASSE QUE HERDE DE 'MODELS.MODEL'

class Paciente(models.Model):

    # DIAS DA SEMANA PARA FAZER A SELECT BOX NO HTML
    ESPECIALIDADE_UM = 'Clinico Geral' 
    ESPECIALIDADE_DOIS = 'Oftalmologista'
    ESPECIALIDADE_TRES = 'Dermatologista'

    ESPECIALIDADE_CHOICES = [
        (ESPECIALIDADE_UM, 'Clinico Geral'),
        (ESPECIALIDADE_DOIS, 'Oftalmologista'),
        (ESPECIALIDADE_TRES, 'Dermatologista'),
    ]

    # OPCÕES SIM E NAO PARA CRIAÇÃO DE SELECT BOX NO HTML
    OPTION_SIM = 'Sim'
    OPTION_NAO = 'Não'

    OPTION_CHOICES = [
        (OPTION_SIM, 'Sim'),
        (OPTION_NAO, 'Não'),
    ]

    # FORMAS DE PAGAMENTO PARA SELECT BOX NO HTML 

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

    # DIAS DA SEMANA PARA CRIAR SELECT BOX NO HTML

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

    # CAMPOS DO BANCO DE DADOS
    # CADA VARIAVEL ABAIXO RECEBE A TIPAGEM E OS PARAMETROS PARA A CRIAÇÃO DA COLUNA NA DB

    # Dados do paciente:

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

    # APÓS CRIAR SUA CLASSE DA MODEL BASTA GERAR A MIGRAÇÃO NO TERMINAL
    # APÓS CRIAR A MIGRAÇÃO BASTA MIGRAR TAMBEM PELO TERMINAL