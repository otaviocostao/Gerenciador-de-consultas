# Gerenciador de consultas médicas

Sistema Web feito em Python com o framework Django para gerenciamento para clínicas médicas de marcação de consultas com fila de espera.
O projeto conta com função para agendar consultas para pacientes armazenando as informações em uma base de dados, o sistema possui um limite de consultas a serem marcadas para cada especialidade e dia, caso seja atingido o limite de consultas, o usuário é redirecionado para o agendamento na fila de espera. Caso algum paciente agendado desmarque, o primeiro da fila de espera é movido para a lista dos agendados. Fora a função de agendamento também existe a função de listar os pacientes e editar o cadastro dos mesmos.


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
