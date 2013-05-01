"""
device.models
-------------
"""
import logging

from django.db import models

from kitchensink.base.models import BaseModel
from kitchensink.device.managers import MakeManager

_log = logging.getLogger('kss.%s' % __name__)


class Make(BaseModel):
    """ Which company made the device (i.e. LG)
    """
    objects = MakeManager()

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    # BaseModel uses it to provide api urls
    resource_name = 'make'

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug


class Device(BaseModel):
    """ What is the model of the device (i.e. make:LG, model:Nexus4)
    """
    #:
    make = models.ForeignKey(Make)
    model = models.CharField(max_length=100)
    # BaseModel uses it to provide api urls
    resource_name = 'device'

    class Meta:
        ordering = ('model',)
        unique_together = ('make', 'model')

    def __unicode__(self):
        return self.make.name + ' ' + self.model
