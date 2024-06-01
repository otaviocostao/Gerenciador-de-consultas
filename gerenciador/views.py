from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from gerenciador.models import Paciente
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'gerenciador/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            auth_login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return render(request, 'gerenciador/login.html', {'error': 'Usuário ou senha inválidos'})

class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name= "gerenciador/home.html"
    login_url= 'login'
    redirect_field_name= 'redirect_to'

class AgendarPaciente(CreateView):
    model=Paciente
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'data_nascimento', 'prioridade', 'especialidade', 'data_consulta', 'convenio_medico', 'forma_pagamento']
    template_name='gerenciador/agendar.html'
    def get_success_url(self):
        return reverse_lazy('dados_consulta', kwargs={'pk': self.object.pk})

def ver_consultas(request):
    especialidade = request.GET.get('especialidade')
    data_consulta = request.GET.get('data_consulta')
    
    # Filtragem inicial de todos os pacientes
    pacientes = Paciente.objects.all()
    
    # Filtragem por especialidade, se especificada
    if especialidade:
        pacientes = pacientes.filter(especialidade=especialidade)
    
    # Filtragem por dia da semana, se especificada
    if data_consulta:
        pacientes = pacientes.filter(data_consulta=data_consulta)
    
    return render(request, 'gerenciador/ver_consultas.html', {'pacientes': pacientes})

class DadosConsulta(DetailView):
    model= Paciente
    template_name= 'gerenciador/dados_consulta.html'
    context_object_name= 'paciente'

class EditarFicha(UpdateView):
    model=Paciente
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'data_nascimento', 'prioridade', 'especialidade', 'data_consulta', 'convenio_medico', 'forma_pagamento']
    template_name='gerenciador/editar.html'
    def get_success_url(self):
        return reverse_lazy('consultas')
    
def desmarcar_consulta(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('consultas')