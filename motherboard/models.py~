from django.db import models


class Usb(models.Model):
    type = models.CharField(max_length=5)

    def __unicode__(self):
        return self.type


class Socket(models.Model):
    socket = models.CharField(max_length=20)

    def __unicode__(self):
        return self.socket


class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    ram = models.IntegerField()
    connectors_number = models.IntegerField()
    usb = models.OneToOneField(to=Usb)
    socket = models.ManyToManyField(to=Socket)

    def __unicode__(self):
        return self.name