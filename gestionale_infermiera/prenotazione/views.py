from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .form import Prenotazione
# Create your views here.

class ControllerPrenotazione():

    def prenotazione(request):
        #return render(request, 'prenotazione/prenotazione.html')
        if request.method == 'POST':
            form = Prenotazione(request.POST)
            if form.is_valid():
                subject = "Prenotazione Appuntamento" 
                body = {
                'nome': form.cleaned_data['nome'], 
                'cognome': form.cleaned_data['cognome'], 
                'email': form.cleaned_data['email'], 
                'citta': form.cleaned_data['citta'], 
                'via': form.cleaned_data['via'], 
                'num_civico': form.cleaned_data['num_civico'], 
                'cap': form.cleaned_data['cap'], 
                'cod_fiscale': form.cleaned_data['cod_fiscale'], 
                'materiale': form.cleaned_data['materiale'], 
                'prescrizione': form.cleaned_data['prescrizione'], 
                'orario': form.cleaned_data['orario'], 
                'data': form.cleaned_data['data'], 
                'richiesta':form.cleaned_data['richiesta'], 
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("main:homepage")
        form = Prenotazione()
        return render(request, "prenotazione/contact.hmtl", {'form':form})

