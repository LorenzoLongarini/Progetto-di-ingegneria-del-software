from django.test import TestCase
from fattura.models import Fattura

# Create your tests here.

class FatturaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Fattura.objects.create()

    def test_nome_label(self):
        fattura = Fattura.objects.get(id=1)
        field_label = fattura._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')