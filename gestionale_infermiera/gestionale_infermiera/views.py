from urllib import request
from django.shortcuts import render
# Create your views here.

class ControllerHome():

    def home(request):
        return render(request, 'gestionale_infermiera/home.html')

    def about(request):
        return render(request, 'gestionale_infermiera/about.html' )


