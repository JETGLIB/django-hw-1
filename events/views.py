from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def events(request):
    return HttpResponse('<h1> This future events page</h1>')