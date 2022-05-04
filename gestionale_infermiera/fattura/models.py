from django.db import models


class Fattura(models.Model):

    nome = models.CharField(max_length=15, default=None, blank=True, null=True)
    cognome = models.CharField(max_length=15, default=None, blank=True, null=True)
    nome_ditta = models.CharField(max_length=20, default=None, blank=True, null=True)
    via = models.CharField(max_length=25)
    num_civico = models.IntegerField(max_length=999)
    cap = models.BigIntegerField(max_length=99999)
    partita_iva = models.BigIntegerField(max_length=99999999999, default=None, blank=True, null=True)
    cod_fiscale = models.CharField(max_length=16, default=None, blank=True, null=True)

    def __str__(self):
        return self.nome
    
  