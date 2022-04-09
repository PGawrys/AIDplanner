from django.contrib import admin

from AidplannerApp.models import Spot, Item, Service, ItemCollection, ServiceCollection

admin.site.register(Spot)
admin.site.register(Item)
admin.site.register(Service)
admin.site.register(ItemCollection)
admin.site.register(ServiceCollection)