"""
phone.models
------------
"""

import logging

from django.db import models

from kitchensink.base.models import BaseModel

_log = logging.getLogger('kss.%s' % __name__)


class Phone(BaseModel):
    """Provides a unique identification of the KitchenSinkApp
    """
    #:
    created_at = models.DateTimeField(auto_now_add=True)
    # BaseModel uses it to provide api urls
    resource_name = 'phone'
