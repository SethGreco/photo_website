import textwrap
from . import urls
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

# Create your views here.	
def index(request):
	return render(request, 'hello/login.html')
	
