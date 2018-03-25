from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView

# imports from within application
from .forms import HomeForm
from .models import *
from .process import *

# Handle home requests
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
        form = HomeForm()

        # Render the page with the form included
        args = {'form': form,}
        return render(request, self.template_name, args)

    # Handle HTTP POST requests through this view
    def post(self, request):

        # Define the form
        form = HomeForm(request.POST)

        # Validate input
        if form.is_valid():

            # Store cleaned input data
            posted = form.cleaned_data['post']
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

            # Parse data from JSON object returned from Dark Sky API
            tempHigh = resultWeather['daily']['data'][0]['temperatureHigh']
            tempLow = resultWeather['daily']['data'][0]['temperatureLow']
            precip = resultWeather['daily']['data'][0]['precipIntensity']
            summary = resultWeather['daily']['data'][0]['summary']

            output = ModelTest.objects.all()
            print(output)

            # Render the page with form and result database
            args = {
                'form': form, 'posted': posted, 'date': date, 'latitude': latitude,
                'longitude': longitude, 'tempHigh': tempHigh, 'tempLow': tempLow,
                'precip': precip, 'summary': summary, 'output': output
            }
            return render(request, self.template_name, args)
