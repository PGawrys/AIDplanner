from django.contrib.auth.models import User
from django.db import models


class Spot(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    details = models.TextField(null=True)


class Service(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=640)
    people_needed = models.IntegerField()
    hours_needed = models.IntegerField()
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)


class Item(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=360)
    number_needed = models.IntegerField()
    number_delivered = models.IntegerField(null=True)

#
# class Item_List(models.Model):
#
#
# class Service_List(models.Model):


