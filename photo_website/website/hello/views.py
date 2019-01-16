import textwrap
from . import urls
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hello')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'hello/reg_form.html', args)
