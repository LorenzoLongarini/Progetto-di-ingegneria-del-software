from django.db import models

class Prenotazione():
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    citta = models.CharField(max_length=15)
    via = models.CharField(max_length=25)
    num_civico = models.IntegerField(max_length=999)
    cod_fiscale = models.CharField(max_length=16)
    richiesta = models.CharField(max_length=50)
    materiale = models.BooleanField
    prescrizione = models.BooleanField
    orario = models.DateTimeField()
