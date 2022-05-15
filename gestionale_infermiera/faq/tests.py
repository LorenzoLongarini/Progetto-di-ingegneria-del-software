from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase
from django.urls import reverse
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

    #Fail
    def test_risposta_max_length(self):
        faq = FAQ.objects.get(id=1)
        max_length = faq._meta.get_field('risposta').max_length
        self.assertEqual(max_length, 300)
    
    def test_faqpage(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)