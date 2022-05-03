from django.shortcuts import render
# Create your views here.

class ControllerTariffa():

    def tariffa(request):
        return render(request, 'tariffa/tariffa.html')
