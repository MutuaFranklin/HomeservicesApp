from servicesApp.models import Profile
from django.contrib import admin
from .models import Profile, Review, Service

# Register your models here.
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Review)

