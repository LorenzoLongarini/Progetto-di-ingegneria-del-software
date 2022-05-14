from django.test import TestCase
from prenotazione.models import Prenotazione

# Create your tests here.

class PrenotazioneTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Prenotazione.objects.create(nome = 'esempio1', domanda = "domanda1", risposta= "risposta1")

    def test_nome_label(self):
        prenotazione = Prenotazione.objects.get(id=1)
        field_label = prenotazione._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')