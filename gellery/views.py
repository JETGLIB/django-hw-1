from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gellery(request):
    return HttpResponse('<h1> This future gellery page</h1>')