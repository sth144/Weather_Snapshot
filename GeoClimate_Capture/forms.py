from django import forms
import datetime
from .models import *

# Default form for location submission

class HomeForm(forms.Form):

    #input field for this forms
    post = forms.CharField()
    date = forms.DateField(initial=datetime.date.today)
