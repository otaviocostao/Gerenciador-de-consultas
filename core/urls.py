"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gerenciador.views import HomeTemplateView, AgendarPaciente, DadosConsulta, EditarFicha, Agendar_Fila
from gerenciador import views

# ROTAS URL DO PROJETO
# CADA VIEW CRIADA NO VIEWS.PY PRECISA DE UMA ROTA URL PARA SER ACESSADA
# APÓS CRIAR A VIEW É NECESSÁRIO PASSAR COMO PARAMETRO AQUI NO CAMPO URLPATTERNS
# AQUI É POSSIVEL NOMEAR CADA ROTA DE PAGINA DO SITE NO URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('agendar/', AgendarPaciente.as_view(), name='agendar'),
    path('consultas/', views.ver_consultas, name='consultas'),
    path('dadosConsulta/<int:pk>/', DadosConsulta.as_view(), name='dados_consulta'),
    path('edita/<int:pk>/', EditarFicha.as_view(), name='editar'),
    path('desmarcar/<int:pk>/', views.desmarcar_consulta, name='desmarcar'),
    path('agendar_fila/', Agendar_Fila.as_view(), name='agendar_fila'),
    path('filaespera/', views.ListarFiladeEspera, name='fila_espera'),
]
