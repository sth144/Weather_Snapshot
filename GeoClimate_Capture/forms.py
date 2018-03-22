from django import forms
from .models import *

# Default form for location submission

class HomeForm(forms.Form):

    #input field for this forms
    post = forms.CharField()
