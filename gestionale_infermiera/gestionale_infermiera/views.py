from django.http import HttpResponse


def home(*args, **kwargs):
    return HttpResponse("<h1>luzi</h1>")