from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from gerenciador.models import Paciente
from django.urls import reverse_lazy
# Create your views here.

def login(request):
    return render(request, 'gerenciador/login.html')

class HomeTemplateView(TemplateView):
    template_name= "gerenciador/home.html"

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