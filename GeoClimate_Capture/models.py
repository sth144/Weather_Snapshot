from django.db import models

from django.contrib.auth.models import AnonymousUser, User

class ModelTest(models.Model):

    name=models.CharField(max_length=500)
