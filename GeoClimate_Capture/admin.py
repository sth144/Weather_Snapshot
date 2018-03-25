from django.contrib import admin
from .models import *

class WSAdmin(admin.ModelAdmin):
    pass

# register models

admin.site.register(ModelTest)
admin.site.register(WeatherSnapshot)
