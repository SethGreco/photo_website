import textwrap
from django.shortcuts import render
from django.http import HttpResponse

import datetime


# Create your views here.

def index(request):
    list = ['san antonio', 'austin']
    now = datetime.datetime.now()
    display_msg = textwrap.dedent('''\
		<html>
		<head>	
			<title>Hello World</title>
		<head>
		<body style="background-color:powderblue;">
			<h1 style="background-color:white;">The current time in  ''' + list[0] + ''' 
			is ''' + now.strftime("%H:%M") + ''' </h1>
			<p> This is a webpage set up with Django framework
				I am attempting to learn some html tags in order to format
				simple text additions 
			</p>
			
			<p style="font-size:160%;">New paragraph and sizing I hope ? </p>
		</html>
	''')

    return HttpResponse(display_msg)
