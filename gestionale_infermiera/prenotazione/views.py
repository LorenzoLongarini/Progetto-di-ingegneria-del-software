from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from gestionale_infermiera.prenotazione.form import Prenotazione
# Create your views here.

class ControllerPrenotazione():

    def prenotazione(request):
        #return render(request, 'prenotazione/prenotazione.html')
        if request.method == 'POST':
            form = Prenotazione(request.POST)
            if form.is_valid():
                subject = "Website Inquiry" 
                body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
                'message':form.cleaned_data['message'], 
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("main:homepage")
        form = Prenotazione()
        return render(request, "main/contact.html", {'form':form})