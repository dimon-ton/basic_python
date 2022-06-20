from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1 style="background-color:Black; color:White; text-align: center;">Hello World</h1>')

def homepage(request):
    return render(request, 'changApp/home.html')