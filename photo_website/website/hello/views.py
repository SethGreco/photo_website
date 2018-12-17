import textwrap
from . import urls
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

# Create your views here.	
def index(request):
    name = "Seth Greco"

    var = {'me': name}


    return render(request, 'hello/home.html', var)

def first(request):
    numbers = [1, 2, 3, 4, 5]
    numbers.append(2000)
    name = "Seth Greco"

    var = {'me': name, 'number': numbers}

    return render(request, 'hello/LogSuccess.html', var)