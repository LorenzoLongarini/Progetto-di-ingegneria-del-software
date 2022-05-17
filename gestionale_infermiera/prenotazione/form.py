from typing import Text
from django import forms

from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from gestionale_infermiera import settings
from django.core.validators import MaxValueValidator, MinValueValidator

"""def validate_length3(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 3:
        raise ValidationError(
            _('Non è possibile inserire più di 3 caratteri')
        )

def validate_length5(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length > 5:
        raise ValidationError(
            _('Non è possibile inserire più di 5 caratteri')
        )"""

def clean_data(value):
        if str(value) < str(date.today()):
            raise forms.ValidationError("La data non può precedere la data odierna")
        return value


class Prenotazione(forms.Form):

    nome = forms.CharField(max_length=20, label='Nome:')
    cognome = forms.CharField(max_length=20, label='Cognome:')
    citta = forms.CharField(max_length=15, label='Città:')
    via = forms.CharField(max_length=25, label='Via:', required=False)
    num_civico = forms.CharField(widget=forms.NumberInput(attrs={'type':'number'}), max_length=3, label='Numero Civico:', required=False)
    cap = forms.IntegerField( label='Cap:', required=False)
    cod_fiscale = forms.CharField(max_length=16, label='Codice Fiscale:', required=False)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000, label='Richiesta:')
    materiale = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Possiedo il materiale necessario:')
    prescrizione = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Possiedo la prescrizione del medico:')
    orario = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')), label='Orario', required=False)
    data = forms.DateField( widget=forms.DateInput(attrs=dict(type='date')), label='Data', required=False)
    email = forms.EmailField(label='Email')