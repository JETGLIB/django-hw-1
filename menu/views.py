from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def menu(request):
    return HttpResponse('<h1> This menu events page</h1>')