from django.contrib import admin
from .models import CustomUser, Grabber

# Register your models here.

admin.site.register(CustomUser)

admin.site.register(Grabber)