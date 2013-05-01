"""
device.admin
------------
"""
from django.contrib import admin
from kitchensink.device.models import Make, Device

admin.site.register(Make)
admin.site.register(Device)
