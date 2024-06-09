from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from gerenciador.models import Paciente, PacienteFilaEspera
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def login(request): # VIEW DA TELA DE LOGIN
    if request.method == "GET": # CASO O LOGIN JA TENHA SIDO FEITO
        return render(request, 'gerenciador/login.html')
    else: # CASO PRECISE FAZER O LOGIN 
        username = request.POST.get('username') # REQUISIÇÃO DO USER NO METODO GET
        senha = request.POST.get('senha') # REQUISIÇÃO DA SENHA NO METODO GET

        user = authenticate(username=username, password=senha) # FUNÇÃO DE AUTENTICAÇÃO

        if user: # CASO O LOGIN SEJA BEM SUCEDIDO
            auth_login(request, user)
            return redirect(reverse_lazy('home'))
        else: # CASO OS DADOS ESTEJAM ERRADOS
            return render(request, 'gerenciador/login.html', {'error': 'Usuário ou senha inválidos'})

class HomeTemplateView(LoginRequiredMixin, TemplateView): # VIEW DA HOMEPAGE
    template_name= "gerenciador/home.html" # PASSAGEM DA TEMPLATE HTML
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

class AgendarPaciente(LoginRequiredMixin, CreateView):
    model = Paciente
    template_name = 'gerenciador/agendar.html'
    fields = [
        'nome', 'endereco', 'cpf', 'rg', 'telefone', 'email',
        'data_nascimento', 'prioridade', 'especialidade',
        'data_consulta', 'convenio_medico', 'forma_pagamento'
    ]
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

    def form_valid(self, form):
        especialidade = form.cleaned_data['especialidade']
        data_consulta = form.cleaned_data['data_consulta']

        # Definindo limites de consultas
        limites = {
            'Clinico Geral': 8,
            'Oftalmologista': 8,
            'Dermatologista': 8
        }

        # Contando consultas já marcadas
        consultas_marcadas = Paciente.objects.filter(especialidade=especialidade, data_consulta=data_consulta).count()

        if consultas_marcadas >= limites[especialidade]:
            return JsonResponse({'limit_reached': True})

        # Salvar o form para criar o paciente
        response = super().form_valid(form)

        # Retorne a URL de redirecionamento
        return JsonResponse({'redirect_url': self.get_success_url()})

    def get_success_url(self):
        return reverse_lazy('dados_consulta', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return super().form_invalid(form)
    
@login_required(login_url=reverse_lazy('login'))
def ver_consultas(request): # VIEW PARA VISUALIZAR AS CONSULTAS MARCADAS
    especialidade = request.GET.get('especialidade') # QUERY DA ESPECIALIDADE NA BASE DE DADOS
    data_consulta = request.GET.get('data_consulta') # QUERY DO DIA NA BASE DE DADOS
    
    pacientes = Paciente.objects.all() # PUXANDO TODOS OS PACIENTES NA BASE DE DADOS
    
    # Filtragem por especialidade, se especificada
    if especialidade: 
        pacientes = pacientes.filter(especialidade=especialidade)
    
    # Filtragem por dia da semana, se especificada
    if data_consulta:
        pacientes = pacientes.filter(data_consulta=data_consulta)
    
    return render(request, 'gerenciador/ver_consultas.html', {'pacientes': pacientes}) # RENDER DA VIEW

class DadosConsulta(LoginRequiredMixin, DetailView): # VIEW DE CONFIRMAÇÃO DA CONSULTA
    model= Paciente # TABELA DA BASE DE DADOS
    template_name= 'gerenciador/dados_consulta.html' # PASSAGEM DA TEMPLATE HTML
    context_object_name= 'paciente' # APELIDO DA TABELA NO TEMPLATE
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

class EditarFicha(LoginRequiredMixin, UpdateView): # VIEW PARA EDITAR A FICHA DO PACIENTE A PARTIR DO SEU ID PRIMARY KEY
    model=Paciente  # TABELA DA BASE DE DADOS
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'data_nascimento',
            'prioridade', 'especialidade', 'data_consulta', 'convenio_medico', 'forma_pagamento'] # CAMPOS DO FORMULARIO HTML
    template_name='gerenciador/editar.html'# PASSAGEM DA TEMPLATE HTML
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

    def get_success_url(self): # URL USADA PARA REDIRECIONAR APÓS SALVAR A ALTERAÇÃO
        return reverse_lazy('consultas')
    
@login_required(login_url=reverse_lazy('login'))
def desmarcar_consulta(request, pk): 
    paciente = get_object_or_404(Paciente, pk=pk) 
    especialidade = paciente.especialidade
    data_consulta = paciente.data_consulta
    paciente.delete()

    # Verifica se há pacientes na fila de espera para a mesma especialidade e data
    paciente_fila = PacienteFilaEspera.objects.filter(especialidade_fila=especialidade, data_consulta_fila=data_consulta).first()

    if paciente_fila:
        # Cria um novo paciente com os dados do paciente da fila de espera
        novo_paciente = Paciente(
            nome=paciente_fila.nome_fila,
            endereco=paciente_fila.endereco_fila,
            cpf=paciente_fila.cpf_fila,
            rg=paciente_fila.rg_fila,
            telefone=paciente_fila.telefone_fila,
            email=paciente_fila.email_fila,
            data_nascimento=paciente_fila.data_nascimento_fila,
            prioridade=paciente_fila.prioridade_fila,
            especialidade=paciente_fila.especialidade_fila,
            data_consulta=paciente_fila.data_consulta_fila,
            convenio_medico=paciente_fila.convenio_medico_fila,
            forma_pagamento=paciente_fila.forma_pagamento_fila
        )
        novo_paciente.save()

        # Remove o paciente da fila de espera
        paciente_fila.delete()

    return redirect('consultas')

class Agendar_Fila(LoginRequiredMixin, CreateView):
    model = PacienteFilaEspera
    template_name = 'gerenciador/agendar_filaespera.html'
    fields = [
        'nome_fila', 'endereco_fila', 'cpf_fila', 'rg_fila', 'telefone_fila', 'email_fila',
        'data_nascimento_fila', 'prioridade_fila', 'especialidade_fila',
        'data_consulta_fila', 'convenio_medico_fila', 'forma_pagamento_fila'
    ]
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('fila_espera')

@login_required(login_url=reverse_lazy('login'))
def ListarFiladeEspera(request):
    especialidade_fila = request.GET.get('especialidade_fila') # QUERY DA ESPECIALIDADE NA BASE DE DADOS
    data_consulta_fila = request.GET.get('data_consulta_fila') # QUERY DO DIA NA BASE DE DADOS
    
    pacientes_fila = PacienteFilaEspera.objects.all() # PUXANDO TODOS OS PACIENTES NA BASE DE DADOS
    
    # Filtragem por especialidade, se especificada
    if especialidade_fila: 
        pacientes_fila = pacientes_fila.filter(especialidade_fila=especialidade_fila)
    
    # Filtragem por dia da semana, se especificada
    if data_consulta_fila:
        pacientes_fila = pacientes_fila.filter(data_consulta_fila=data_consulta_fila)
    
    return render(request, 'gerenciador/ver_fila.html', {'pacientes_fila': pacientes_fila}) # RENDER DA VIEW


class EditarFichaFila(LoginRequiredMixin, UpdateView): # VIEW PARA EDITAR A FICHA DO PACIENTE A PARTIR DO SEU ID PRIMARY KEY
    model=PacienteFilaEspera  # TABELA DA BASE DE DADOS
    fields=['nome_fila', 'endereco_fila', 'cpf_fila', 'rg_fila', 'telefone_fila', 'email_fila', 'data_nascimento_fila',
            'prioridade_fila', 'especialidade_fila', 'data_consulta_fila', 'convenio_medico_fila', 'forma_pagamento_fila'] # CAMPOS DO FORMULARIO HTML
    template_name='gerenciador/editar_fila.html'# PASSAGEM DA TEMPLATE HTML
    login_url= 'login' # REQUISIÇÃO DO LOGIN
    redirect_field_name= 'redirect_to'

    def get_success_url(self): # URL USADA PARA REDIRECIONAR APÓS SALVAR A ALTERAÇÃO
        return reverse_lazy('fila_espera')
