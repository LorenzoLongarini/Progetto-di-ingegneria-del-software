from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Prodotto(models.Model):

    def validate_price(value):
            if value < 0 :
                raise ValidationError(
                    _('(value) non può essere negativo'),
                    params={'value': value},
                )

    nome = models.CharField(max_length=10)
    descrizione = models.CharField(max_length=30)
    marca = models.CharField(max_length=15)
    prezzo = models.FloatField(max_length=3, validators=[validate_price])

    def __str__(self):
        return self.nome

    
    
  