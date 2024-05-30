from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from gerenciador.models import Paciente
from django.urls import reverse_lazy
# Create your views here.

def login(request):
    return render(request, 'gerenciador/login.html')

class HomeTemplateView(TemplateView):
    template_name= "gerenciador/home.html"

class AgendarPaciente(CreateView):
    model=Paciente
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'prioridade', 'data_nascimento']
    template_name='gerenciador/agendar.html'
    def get_success_url(self):
        return reverse_lazy('dados_consulta', kwargs={'pk': self.object.pk})

class ListaPacientes(ListView):
    model=Paciente
    template_name='gerenciador/ver_consultas.html'
    context_object_name = 'pacientes'

class DadosConsulta(DetailView):
    model= Paciente
    template_name= 'gerenciador/dados_consulta.html'
    context_object_name= 'paciente'