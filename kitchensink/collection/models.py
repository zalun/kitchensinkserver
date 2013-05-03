"""
collection.models
-----------------
"""
import logging

from django.db import models

from kitchensink.base.models import BaseModel
from kitchensink.phone.models import Phone
from kitchensink.device.models import Device

_log = logging.getLogger('kss.%s' % __name__)


class Result(BaseModel):
    """ Collect results from kitchensink app
    """
    resource_name = 'result'

    #: Unique id of the kitchensink app
    phone = models.ForeignKey(Phone)
    #: Phone model
    device = models.ForeignKey(Device, related_name='results', null=True, blank=True)
    #: version of the kitchecnsink app
    app_version = models.CharField(max_length=10)
    #: value of ``navigator.userAgent``
    user_agent = models.CharField(max_length=255)
    #: results of the tests in JSON form
    test_result = models.TextField()
    #:
    created_at = models.DateTimeField(auto_now_add=True)
