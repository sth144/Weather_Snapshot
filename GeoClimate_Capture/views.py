import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView

# imports from within application
from .forms import *
from .models import *
from .process import *

# Handle home requests (defunct)
def home(request):

	# render index
    return render(request, 'GeoClimate_Capture/home.html')


# default view for this application
class HomeView(TemplateView):

    # Define template for this views
    template_name = 'GeoClimate_Capture/home.html'

    # Handle HTTP GET requests through this view
    def get(self, request):

        # Define the forms
        #form = HomeForm()

        # serve Google Maps Key (stored in environment)
        MAP_KEY = os.environ.get('MAP_KEY')

        output = WeatherSnapshot.objects.all()

        # Render the page with the form included
        args = {'output': output, 'MAP_KEY': MAP_KEY}
        return render(request, self.template_name, args)

    # Handle HTTP POST requests through this view
    def post(self, request):

        if request.method=='POST' and 'submitButton' in request.POST:
            # Define the form
            form = HomeForm(request.POST)

            # Validate input
            if form.is_valid():

                # Store cleaned input data
                posted = str(form.cleaned_data['post'])
                date = str(form.cleaned_data['date'])

                # Process data
                resultGeo = getGeoFromAddr(posted)
                coord = (resultGeo['results'][0]['geometry']['location']['lat'], resultGeo['results'][0]['geometry']['location']['lng'])
                resultWeather = getWeatherFromCoords(coord, date)

                # Clear text fields
                form = HomeForm()

                # Parse data from JSON object returned from Google Geocode API
                latitude = resultGeo['results'][0]['geometry']['location']['lat']
                longitude = resultGeo['results'][0]['geometry']['location']['lng']

                # Parse data from JSON object returned from Dark Sky API to output result to user
                high_temp = resultWeather['daily']['data'][0]['temperatureHigh']
                low_temp = resultWeather['daily']['data'][0]['temperatureLow']
                precipitation = resultWeather['daily']['data'][0]['precipIntensity']
                summary = resultWeather['daily']['data'][0]['summary']

                # serve Google Maps Key (stored in environment)
                MAP_KEY = os.environ.get('MAP_KEY')

                output = WeatherSnapshot.objects.all()
                print(output)

                # Render the page with form and result database
                args = {
                    'form': form, 'posted': posted, 'date': date, 'latitude': latitude,
                    'longitude': longitude, 'high_temp': high_temp, 'low_temp': low_temp,
                    'precipitation': precipitation, 'summary': summary, 'output': output,
                    'MAP_KEY': MAP_KEY,
                }
                return render(request, self.template_name, args)

        elif request.method=='POST' and 'storeButton' in request.POST:

            # Define form architecture
            form = WeatherSnapshotForm(request.POST)
            print('storing data')

            if form.is_valid():
                print('form is valid')
                _obj = form.save(commit=False)
                _obj.save()
                text = form.cleaned_data['location']
                form = WeatherSnapshotForm()
            #else:
            #    print('problem adding object')
            #    return render(request, self.template_name)

            #output = WeatherSnapshot.objects.all()
            #args = {'output': output}
            return redirect('/')

        elif request.method=='POST' and 'resetButton' in request.POST:
            print('deleting')
            #form = ResetTableForm(request.POST)

            #if form.is_valid():
            WeatherSnapshot.objects.all().delete()
            return redirect('/')
            #else:
            #    print('delete failed')

def about(request):
    return render(request, 'GeoClimate_Capture/about.html')

def contact(request):
    return render(request, 'GeoClimate_Capture/contact.html')

def terms(request):
    return render(request, 'GeoClimate_Capture/terms.html')

def privacy(request):
    return render(request, 'GeoClimate_Capture/privacy.html')
