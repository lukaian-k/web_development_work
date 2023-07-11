"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from core import views

from django.urls import path
from core import views

urlpatterns = [
    path('professores/', views.professor_list, name='professor_list'),
    path('professores/<int:pk>/', views.professor_detail, name='professor_detail'),
    path('professores/create/', views.professor_create, name='professor_create'),
    path('salas/', views.sala_list, name='sala_list'),
    path('salas/<int:pk>/', views.sala_detail, name='sala_detail'),
    path('salas/create/', views.sala_create, name='sala_create'),
    path('alocacoes/', views.alocacao_list, name='alocacao_list'),
    path('alocacoes/<int:pk>/', views.alocacao_detail, name='alocacao_detail'),
    path('alocacoes/create/', views.alocacao_create, name='alocacao_create'),
]

