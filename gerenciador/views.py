from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from gerenciador.models import Paciente
# Create your views here.

def login(request):
    return render(request, 'gerenciador/login.html')

class HomeTemplateView(TemplateView):
    template_name= "gerenciador/home.html"

class CadastroPaciente(CreateView):
    model=Paciente
    fields=['nome', 'endereco', 'cpf', 'rg', 'telefone', 'email', 'prioridade']
    template_name='gerenciador/cadastro.html'
