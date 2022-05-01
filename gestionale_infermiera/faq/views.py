from django.shortcuts import render
# Create your views here.

class ControllerFaq():

    def faq(request):
        return render(request, 'faq/faq.html')
