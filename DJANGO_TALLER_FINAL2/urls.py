"""DJANGO_TALLER_FINAL2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from seminarioapp import views




urlpatterns = [
    path('', views.index),
    path('listado/', views.lis_inscripciones),
    path('agregar_inscripcion/', views.cre_inscripciones),
    path('eliminar/<int:id>', views.eli_inscripciones),
    path('actualizar/<int:id>', views.actu_inscripciones),
    path('inscripciones_api/', views.Vista_api),
    path('inscripciones_class/', views.Most_Inscripciones.as_view()),
    path('inscripciones_class/<int:id>', views.Deta_Inscripciones.as_view()),
    path('instituciones_fun/', views.instituciones_lista),
    path('instituciones_fun/<int:id>', views.instituciones_detalle),


    
]
