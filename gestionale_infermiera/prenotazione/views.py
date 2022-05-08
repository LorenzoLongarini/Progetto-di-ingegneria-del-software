from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .form import Prenotazione
from django.contrib import messages
# Create your views here.

class ControllerPrenotazione():

    def prenotazione(request):
        #return render(request, 'prenotazione/prenotazione.html')
        if request.method == 'POST':
            form = Prenotazione(request.POST)
            if form.is_valid():
                subject = "Website Inquiry" 
                body = {
                'nome': form.cleaned_data['nome'], 
                'cognome': form.cleaned_data['cognome'], 
                'email': form.cleaned_data['email'], 
                'citta': form.cleaned_data['citta'],
                'via': form.cleaned_data['via'],
                'num_civico': form.cleaned_data['num_civico'],
                'cap': form.cleaned_data['cap'],
                'cod_fiscale': form.cleaned_data['cod_fiscale'] ,
                'materiale': form.cleaned_data['materiale'] ,
                'prescrizione': form.cleaned_data['prescrizione'], 
                'orario': form.cleaned_data['orario'], 
                'data': form.cleaned_data['data'] ,
                'message': form.cleaned_data['message'] ,
                }
                message = ''
                for key, value in body.items():
                    message += '\n'+str(key) + ': ' + str(value)
                #message = 'Nome:  ' + str(body['nome']) +'\nCognome:  ' + str(body['cognome']) +'\nEmail:  ' + str(body['email']) +'\nCittà:         ' + str(body['citta']) +'\nVia:           ' + str(body['via']) +'\nN Civico:      ' +str(body['num_civico']) +'\nCap:           ' + str(body['cap']) +'\nCod Fiscale:   ' + str(body['cod_fiscale']) +'\nMateriale:     ' + str(body['materiale']) +'\nPrescrizione:  ' + str(body['prescrizione']) +'\nOrario:        ' + str(body['orario']) +'\nData:          ' + str(body['data']) +'\nMessaggio:     ' + str(body['message'])
                

                try:
                    send_mail(subject, message, body['email'], ['luana.bibini@gmail.com']) 
                    messages.success(request,'Email inviata con successo')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect("contact")
        
        form = Prenotazione()
        return render(request, "prenotazione/prenotazione.html", {'form':form})
                