from turtle import heading
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def hello(request):
    return HttpResponse('<h1 style="background-color:Black; color:White; text-align: center;">Hello World</h1>')

def homepage(request):
    products = Product.objects.all()
    allproducts = []
    column = []

    for i, p in enumerate(products, start=1):
        if i % 3 == 0:
            column.append(p)
            allproducts.append(column)
            column = []
        else:
            column.append(p)
    if len(column) != 0:
        allproducts.append(column)
    context = {'products':allproducts}

    return render(request, 'changApp/home.html', context)

def about(request):
    return render(request, 'changApp/about.html')

def contact(request):
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        heading = data.get('heading')
        detail = data.get('detail')

        # บันทึกข้อมูลลง model
        newcontact = ContactList()
        newcontact.email = email
        newcontact.head = heading
        print(heading)
        newcontact.detail = detail

        newcontact.save()

    return render(request, 'changApp/contact.html')

