from django.contrib import admin


from django.contrib import admin
from .models import Trip, Attraction, Place, Expense

admin.site.register(Trip)
admin.site.register(Attraction)
admin.site.register(Place)
admin.site.register(Expense)