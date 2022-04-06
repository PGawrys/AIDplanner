from django.contrib import admin

from AidplannerApp.models import Spot, User, Item, Service, ItemList, ServiceList

# Register your models here.

admin.site.register(Spot)
admin.site.register(Item)
admin.site.register(Service)
admin.site.register(ItemList)
admin.site.register(ServiceList)