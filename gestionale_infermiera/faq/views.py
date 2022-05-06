from django.shortcuts import render
from .models import Faq
# Create your views here.

class ControllerFaq():

    def faq(request):
        faqs = Faq.objects.all()
        return render(request, 'faq/faq.html',{'faqs' : faqs})
