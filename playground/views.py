from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    x = calculate()
    return render(request, "test.html", {"name": "dragon"})


def calculate():
    x = 1 
    y = 2
    x = x+y
    return x