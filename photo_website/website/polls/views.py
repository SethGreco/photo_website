import textwrap
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

# Create your views here.

def index(request):
	now = datetime.datetime.now()
	display_msg = textwrap.dedent('''\
		<html>
		<head>	
			<title>Hello World</title>
		<head>
		<body>
			<h1>The time is </h1>
			<p>'''+str(now)+''' </p>
		</html>
	''')
	

	return HttpResponse(display_msg )



