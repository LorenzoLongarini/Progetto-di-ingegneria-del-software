from django import forms

from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Prenotazione():

    def clean_data(value):
        if value < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return value

    nome = forms.CharField(max_length=20)
    cognome = forms.CharField(max_length=20)
    citta = forms.CharField(max_length=15)
    via = forms.CharField(max_length=25)
    num_civico = forms.IntegerField(max_length=3)
    cap = forms.IntegerField(max_length=5)
    cod_fiscale = forms.CharField(max_length=16)
    richiesta = forms.TextField(max_length=50)
    materiale = forms.BooleanField
    prescrizione = forms.BooleanField
    orario = forms.TimeField()
    data = forms.DateField(validators=[clean_data])
    email = forms.EmailField()