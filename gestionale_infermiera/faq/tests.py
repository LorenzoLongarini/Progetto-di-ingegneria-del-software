from django.test import TestCase
from faq.models import FAQ

# Create your tests here.

class FAQTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        FAQ.objects.create(nome = 'esempio1', domanda = "domanda1", risposta= "risposta1")

    def test_nome_label(self):
        faq = FAQ.objects.get(id=1)
        field_label = faq._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')