from dataclasses import dataclass
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class TariffaFatt(models.Model):

    CHOICES = [(i,i) for i in range(11)]

    def validate_price(value):
        if value < 0 :
            raise ValidationError(
                _('(value) non può essere negativo'),
                params={'value': value},
            ) 

    descrizione_prod = models.TextField()
    quantita = models.IntegerField(choices=CHOICES)
    prezzo = models.FloatField(validators=[validate_price], max_length=6)

class Fattura(models.Model):

    nome = models.CharField(max_length=15, default=None, blank=True, null=True)
    cognome = models.CharField(max_length=15, default=None, blank=True, null=True)
    nome_ditta = models.CharField(max_length=20, default=None, blank=True, null=True)
    citta = models.CharField(max_length=15)
    via = models.CharField(max_length=25, default=None, blank=True, null=True)
    num_civico = models.IntegerField(max_length=3, default=None, blank=True, null=True)
    cap = models.BigIntegerField(max_length=5, default=None, blank=True, null=True)
    partita_iva = models.BigIntegerField(max_length=11, default=None, blank=True, null=True)
    cod_fiscale = models.CharField(max_length=16, default=None, blank=True, null=True)
    cod_cliente = models.CharField(max_length=7)
    #tipo_documento = models.CharField() sempre fattura
    numero = models.IntegerField()
    data = models.DateField()
    descrizione_pag = models.TextField(max_length=20)
    banca = models.CharField(max_length=27)
    prod_fatt = models.ForeignKey(TariffaFatt, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
    
