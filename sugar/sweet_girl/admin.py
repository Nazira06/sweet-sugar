from django.contrib import admin
from .models import Service, Master, Certificates, Feedback, Spot
# Register your models here.

admin.site.register([Service, Master, Certificates, Feedback, Spot])