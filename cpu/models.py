from django.db import models
from motherboard.models import Socket

class Cpu(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.IntegerField()
    socket = models.ForeignKey(to=Socket, default=None, null=True)

    def __unicode__(self):
        return self.name