from dataclasses import fields
from django import forms
from seminarioapp.models import Inscripciones



class Form_inscripciones(forms.ModelForm):
    class Meta:
        model   = Inscripciones
        fields = '__all__'