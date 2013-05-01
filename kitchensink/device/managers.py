"""
device.managers
---------------
"""
import logging

from django.db import models

_log = logging.getLogger('kss.%s' % __name__)


class MakeManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)
