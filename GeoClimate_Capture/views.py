from django.shortcuts import render
from django.http import HttpResponse

# Handle home requests

def home(request):

	# render index
    return render(request, 'home.html')
