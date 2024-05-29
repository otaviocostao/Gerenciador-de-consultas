from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from gerenciador.models import Paciente
# Create your views here.

def login(request):
    return render(request, 'gerenciador/login.html')

class HomeTemplateView(TemplateView):
    template_name= "gerenciador/home.html"

class CadastroPaciente(CreateView):
    model=Paciente
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'prioridade', 'data_nascimento']
    template_name='gerenciador/cadastro.html'

class ListaPacientes(ListView):
    model=Paciente
    template_name='gerenciador/ver_consultas.html'
    context_object_name = 'pacientes'