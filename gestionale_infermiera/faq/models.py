from django.db import models

class Faq(models.Model):
    domanda = models.CharField(max_length=15)
    risposta = models.CharField(max_length=15)