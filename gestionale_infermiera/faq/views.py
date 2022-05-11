from django.shortcuts import render
from .models import FAQ
# Create your views here.

class ControllerFAQ():

    def faq(request):
        faqs = FAQ.objects.all()
        return render(request, 'faq/faq.html',{'faqs' : faqs})
