from django.contrib import admin

from AidplannerApp.models import Spot, User, Item, Service
# Register your models here.

admin.site.register(Spot)
admin.site.register(Item)
admin.site.register(Service)
