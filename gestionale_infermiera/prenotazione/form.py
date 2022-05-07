from django import forms

from datetime import datetime, date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_length3(value):
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
        )

def clean_data(value):
        if value < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return value

class Prenotazione(forms.Form):

    nome = forms.CharField(max_length=20)
    cognome = forms.CharField(max_length=20)
    citta = forms.CharField(max_length=15)
    via = forms.CharField(max_length=25)
    num_civico = forms.IntegerField(validators=[validate_length3])
    cap = forms.IntegerField(validators=[validate_length5])
    cod_fiscale = forms.CharField(max_length=16)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000, label='Richiesta')
    materiale = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    prescrizione = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    orario = forms.TimeField()
    data = forms.DateField(validators=[clean_data])
    email = forms.EmailField()