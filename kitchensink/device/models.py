"""
device.models
-------------
"""
import logging

from django.db import models

from kitchensink.base.models import BaseModel

_log = logging.getLogger('kss.%s' % __name__)


class Make(BaseModel):
    """ Which company made the device (i.e. LG)
    """
    name = models.CharField(max_length=100)
    # BaseModel uses it to provide api urls
    resource_name = 'make'

    def __unicode__(self):
        return self.name


class Device(BaseModel):
    """ What is the model of the device (i.e. make:LG, model:Nexus4)
    """
    #:
    make = models.ForeignKey(Make)
    model = models.CharField(max_length=100)
    # BaseModel uses it to provide api urls
    resource_name = 'device'

    def __unicode__(self):
        return self.make.name + ' ' + self.model
