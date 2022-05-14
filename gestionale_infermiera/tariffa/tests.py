from django.test import TestCase
from tariffa.models import Tariffa

# Create your tests here.

class TariffaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tariffa.objects.create(nome = 'esempio1', domanda = "domanda1", risposta= "risposta1")

    def test_nome_label(self):
        tariffa = Tariffa.objects.get(id=1)
        field_label = tariffa._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')