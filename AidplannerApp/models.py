from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Spot(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_detail_spot', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('update_spot', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('delete_spot', kwargs={'id': self.id})

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    details = models.TextField(null=True)


class Service(models.Model):
    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse('update_service', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('delete_service', kwargs={'id': self.id})

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=640)


class Item(models.Model):
    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse('update_item', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('delete_item', kwargs={'id': self.id})

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=360)


class ItemCollection(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=128)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, through='ItemCollectionItems')


class ItemCollectionItems(models.Model):

    def __str__(self):
        return self.item.name

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemcollection = models.ForeignKey(ItemCollection, on_delete=models.CASCADE)
    number_needed = models.IntegerField(null=True)
    number_delivered = models.IntegerField(null=True)



class ServiceCollection(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=128)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    services = models.ManyToManyField(Service, through='ServiceCollectionServices')


class ServiceCollectionServices(models.Model):

    def __str__(self):
        return self.service.name

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    servicecollection = models.ForeignKey(ServiceCollection, on_delete=models.CASCADE)
    people_needed = models.IntegerField(null=True)
    hours_needed = models.IntegerField(null=True)