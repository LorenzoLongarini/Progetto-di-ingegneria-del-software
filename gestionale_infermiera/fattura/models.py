from dataclasses import dataclass
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


def validate_price(value):
        if value < 0 :
            raise ValidationError(
                _('questo campo non può essere negativo'),
                params={'value': value},
            )

class Fattura(models.Model):

    nome = models.CharField(max_length=15, default=None, blank=True, null=True)
    cognome = models.CharField(max_length=15, default=None, blank=True, null=True)
    nome_ditta = models.CharField(max_length=20, default=None, blank=True, null=True)
    citta = models.CharField(max_length=15)
    via = models.CharField(max_length=25, default=None)
    num_civico = models.IntegerField( default=None, validators=[validate_price, MaxValueValidator(999)])
    cap = models.BigIntegerField( default=None, validators=[MinValueValidator(0), MaxValueValidator(99999)])
    partita_iva = models.BigIntegerField( validators=[MinValueValidator(0), MaxValueValidator(99999999999), validate_price],default=None, blank=True, null=True)
    cod_fiscale = models.CharField(max_length=16, default=None, blank=True, null=True)
    cod_cliente = models.CharField(max_length=7, blank=True, null=True)
    #tipo_documento = models.CharField() sempre fattura
    numero = models.IntegerField(validators=[validate_price])
    data = models.DateField()
    descrizione_pag = models.TextField(max_length=20, blank=True, null=True)
    banca = models.CharField(max_length=27, blank=True, null=True)

    def __str__(self):
        return str(self.numero)
    
    class Meta:
        verbose_name = u'Fattura'
        verbose_name_plural = u'Fatture' 


class TariffaFatt(models.Model):
    
    CHOICES = [(i,i) for i in range(11)]
    descrizione_prod = models.TextField(blank=True, null=True)
    quantita = models.IntegerField(choices=CHOICES, blank=True, null=True, validators=[validate_price])
    prezzo = models.FloatField( validators=[validate_price], blank=True, null=True)
    fatt = models.ForeignKey(Fattura, on_delete=models.CASCADE)
