# Gerenciador de consultas médicas

Sistema web feito em Python com o framework Django

### Criando ambiente virtual:

- python -m venv .venv
- .venv/Scripts/activate

### Instalando o Django:

- pip install django

### Rodando o servidor:

- python manage.py runserver

## Construção do sistema:

### Arquivos base do Django:

Criação do projeto nomeado como 'core' e da 'manage.py':

- django-admin startproject core .

Criação da app nomeada como 'gerenciador':

- django-admin startapp gerenciador

  ### Camada de models:

Após criarmos a nossa classe 'Paciente' no arquivo models.py, é necessario realizar as migrações para o arquivo sqlite3:

Criar migração:

- python manage.py makemigrations

Migrar o conteúdo:

- python manage.py migrate
