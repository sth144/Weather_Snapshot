from django import forms
from django.forms import ModelForm
import datetime
from .models import *

# Default form for location submission

class HomeForm(forms.Form):

    #input field for this forms
    post = forms.CharField()    # location
    date = forms.DateField(initial=datetime.date.today)

class ModelTest_Form(ModelForm):

    class Meta:
        model = ModelTest
        fields = '__all__'

class WeatherSnapshotForm(forms.ModelForm):

    #location = forms.CharField(widget=forms.HiddenInput())
    #date = forms.CharField(widget=forms.HiddenInput())
    #high_temp = forms.CharField(widget=forms.HiddenInput())
    #low_temp = forms.CharField(widget=forms.HiddenInput())
    ##precipitation = forms.IntegerField(widget=forms.HiddenInput())
    #summary = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = WeatherSnapshot
        fields = ('location', 'date', 'high_temp', 'low_temp', 'precipitation', 'summary',)
        widgets = {
            'location': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            'high_temp': forms.HiddenInput(),
            'low_temp': forms.HiddenInput(),
            'precipitation': forms.HiddenInput(),
            'summary': forms.HiddenInput()
        }

#class ResetTableForm(forms.ModelForm):

#    class Meta:
#        model = WeatherSnapshotForm
#        fields = '__all__'
