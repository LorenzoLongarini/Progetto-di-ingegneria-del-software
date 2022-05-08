from dataclasses import dataclass
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_price(value):
        if value < 0 :
            raise ValidationError(
                _('(value) non può essere negativo'),
                params={'value': value},
            )

class Fattura(models.Model):

    nome = models.CharField(max_length=15, default=None, blank=True, null=True)
    cognome = models.CharField(max_length=15, default=None, blank=True, null=True)
    nome_ditta = models.CharField(max_length=20, default=None, blank=True, null=True)
    citta = models.CharField(max_length=15)
    via = models.CharField(max_length=25, default=None)
    num_civico = models.IntegerField( default=None)
    cap = models.BigIntegerField( default=None)
    partita_iva = models.BigIntegerField( default=None, blank=True, null=True)
    cod_fiscale = models.CharField(max_length=16, default=None, blank=True, null=True)
    cod_cliente = models.CharField(max_length=7, blank=True, null=True)
    #tipo_documento = models.CharField() sempre fattura
    numero = models.IntegerField()
    data = models.DateField()
    descrizione_pag = models.TextField(max_length=20, blank=True, null=True)
    banca = models.CharField(max_length=27, blank=True, null=True)

    def __str__(self):
        return str(self.numero)
    
class TariffaFatt(models.Model):
    
    CHOICES = [(i,i) for i in range(11)]
    descrizione_prod = models.TextField(blank=True, null=True)
    quantita = models.IntegerField(choices=CHOICES, blank=True, null=True)
    prezzo = models.FloatField(validators=[validate_price], max_length=6, blank=True, null=True)
    fatt = models.ForeignKey(Fattura, on_delete=models.CASCADE)
