from django.shortcuts import render
# Create your views here.

class ControllerPrenotazione():

    def prenotazione(request):
        return render(request, 'prenotazione/prenotazione.html')
