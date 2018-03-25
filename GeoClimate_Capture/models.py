from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import AnonymousUser, User

class ModelTest(models.Model):

    name=models.CharField(max_length=500)

class ModelTest_Form(ModelForm):

    class Meta:
        model = ModelTest
        fields = '__all__'
