from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import AnonymousUser, User

class ModelTest(models.Model):

    name = models.CharField(max_length=500)

class WeatherSnapshot(models.Model):

    location = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    high_temp = models.CharField(max_length=500)
    low_temp = models.CharField(max_length=500)
    precipitation = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)
