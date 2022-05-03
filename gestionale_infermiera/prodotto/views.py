from django.shortcuts import render
# Create your views here.

class ControllerProdotto():

    def prodotto(request):
        return render(request, 'prodotto/prodotto.html')
